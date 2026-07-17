# Running a machine learning model on the GPU timeline

**Framework**: Metal

Dispatch model inference commands with a machine learning pass in a Metal 4 command buffer.

**Availability**:
- macOS 26.0+
- Xcode 26.2+

#### Overview

This sample demonstrates how to encode commands that run a machine learning model with the Metal 4 API. Each machine learning inference pass runs alongside other tasks on a Metal device and typically requires less time and overhead than running a model from the CPU and passing its outputs to a Metal workload.

You encode a machine learning pass into a command buffer with the [`MTL4MachineLearningCommandEncoder`](mtl4machinelearningcommandencoder.md) protocol. When the Metal device finishes running the pass, other passes can immediately work with the inference results.

The app multiplies two matrices on both the CPU and the Metal device, then reports whether the results are the same. It does the matrix multiplication on the Metal device by running a machine learning pass with a model that does matrix multiplication.

Metal apps can apply model files from [`Core ML`](https://developer.apple.com/documentation/CoreML) by converting each into a Metal package:

```shell
    
% xcrun metal-package-builder -ml ./path/to/model.mlpackage -o ./output/path/to/ml-model.mtlpackage

```

Metal packages provide an entry point to the model within it that a Metal device can run. The Metal package file in this sample’s app is a relatively simple network that multiplies two matrices, a task which most apps can run more efficiently with the CPU or GPU shader code. For an example of multiplying matrices directly in a GPU kernel function with inline tensor operations, see [`Running inline ML operations in a shader with Metal 4`](running-inline-ml-operations-in-a-shader-with-metal-4.md).

When you run the app, it:

1. Creates Metal resources, most of which are reusable
2. Compiles a machine learning pipeline state from the model in the Metal package
3. Extracts tensor bindings from pipeline reflection
4. Creates tensors that match the binding requirements
5. Fills the input tensors with matrix data
6. Binds tensors to an argument table
7. Creates a heap for the machine learning encoder’s temporary allocations
8. Encodes and runs the machine learning pass
9. Compares the GPU result against the CPU result

The app reports whether the results match and exits.

#### Create a Compiler

The app creates an [`MTL4Compiler`](mtl4compiler.md) along with other reusable resources like the device, command queue, and command buffer.

```objective-c
compiler = [device newCompilerWithDescriptor:[MTL4CompilerDescriptor new]
                                       error:nil];
```

The app creates these resources one time so long-running apps avoid repeating setup costs.

The app’s compiler builds the machine learning model into a pipeline state that runs on the GPU.

#### Compile the Pipeline State

The app creates a pipeline state based on the model by passing the compiler instance and a library that represents the model to the app’s `createPipelineStateWithCompiler:fromLibrary:forMatrices:` method. The method starts by retrieving the reflection information for the library’s `main` function:

```objective-c
- (nullable id<MTL4MachineLearningPipelineState>)
createPipelineStateWithCompiler:(id<MTL4Compiler>)compiler
                    fromLibrary:(id<MTLLibrary>)library
                    forMatrices:(NSArray<Matrix *> *)matrices {
    MTLFunctionReflection *functionReflection =
    [library reflectionForFunctionWithName:@"main"];
```

Function reflection provides information about the network’s inputs and outputs. Metal packages for ML models designate a `main` function as the entry point for running model inference.

Next, the method creates a function descriptor that tells the compiler which function to compile from a library:

```objective-c
MTL4LibraryFunctionDescriptor *functionDescriptor =
[MTL4LibraryFunctionDescriptor new];
functionDescriptor.name = @"main";
functionDescriptor.library = library;
```

The method then creates a pipeline descriptor and turns on reflection:

```objective-c
MTL4MachineLearningPipelineDescriptor *pipelineDescriptor;
pipelineDescriptor = [MTL4MachineLearningPipelineDescriptor new];
pipelineDescriptor.machineLearningFunctionDescriptor = functionDescriptor;

// Enable reflection to get binding information after compilation.
MTL4PipelineOptions *options = [MTL4PipelineOptions new];
options.shaderReflection = MTL4ShaderReflectionBindingInfo;
pipelineDescriptor.options = options;
```

The [`bindingInfo`](mtl4shaderreflection/bindinginfo.md) option tells the compiler to include tensor binding information the app can later inspect.

The method configures the input dimensions for the model’s two inputs by gathering the input bindings from the function reflection of the main function, sorting them by name, and setting the dimensions to the corresponding matrix’s size.

```objective-c
// Set the input dimensions for each tensor binding from the matrices.
for (NSInteger index = 0; index < inputBindings.count; index++) {
    id<MTLTensorBinding> tensorBinding = inputBindings[index];
    Matrix *matrix = matrices[index];

    NSInteger dimensions[] = {matrix.columns, matrix.rows};
    MTLTensorExtents *extents = [[MTLTensorExtents alloc] initWithRank:2
                                                                values:dimensions];

    [pipelineDescriptor setInputDimensions:extents
                             atBufferIndex:tensorBinding.index];
}
```

Each [`MTLTensorExtents`](mtltensorextents.md) instance defines the rank and dimension sizes for a tensor, with the innermost dimension first. Sorting the bindings by name maps the first matrix to `inputA` and the second to `inputB`.

The method concludes by compiling the pipeline state with the descriptor:

```objective-c
id<MTL4MachineLearningPipelineState> state =
[compiler newMachineLearningPipelineStateWithDescriptor:pipelineDescriptor
                                                  error:&error];
```

The model has inputs with a dynamic shape, which means the app needs to select specific dimensions for those inputs when building a pipeline state.

> **Note**: Apps need to create a pipeline state for each unique combination of dimensions for model inputs that have dynamic shapes.

#### Extract Tensor Bindings From Pipeline Reflection

The `extractTensorBindingsFromPipelineState:` method retrieves tensor bindings from the pipeline state.

```objective-c
- (nullable TensorBindingsByName *)
extractTensorBindingsFromPipelineState:(id<MTL4MachineLearningPipelineState>)pipelineState {
    NSMutableDictionary<NSString *, id<MTLTensorBinding>> *bindingsByName;
    bindingsByName = [NSMutableDictionary new];

    for (id<MTLBinding> binding in pipelineState.reflection.bindings) {
        if (binding.type != MTLBindingTypeTensor) {
            continue;
        }

        bindingsByName[binding.name] = (id<MTLTensorBinding>)binding;
    }

    return bindingsByName;
}
```

The app matches bindings by name because the bindings in a pipeline state reflection can be in any order. Pipeline reflection provides information about each binding, including its name, index, dimensions, and data type.

#### Create Tensors for the Bindings

The `createTensorsForBindings:withDevice:` method creates tensors that match the dimensions and data types from the pipeline bindings.

```objective-c
- (nullable TensorsByName *)createTensorsForBindings:(TensorBindingsByName *)bindings
                                          withDevice:(id<MTLDevice>)device {
    NSMutableDictionary<NSString *, id<MTLTensor>> *tensorsByName;
    tensorsByName = [NSMutableDictionary new];

    MTLTensorDescriptor *tensorDescriptor = [MTLTensorDescriptor new];
    tensorDescriptor.usage = MTLTensorUsageMachineLearning;

    for (NSString *name in bindings) {
        id<MTLTensorBinding> binding = bindings[name];
        MTLTensorExtents *dimensions = binding.dimensions;
        MTLTensorDataType dataType = binding.tensorDataType;
```

The [`machineLearning`](mtltensorusage/machinelearning.md) usage flag indicates that the tensor participates in ML passes.

For each binding, the method validates that it doesn’t have dynamic shapes:

```objective-c
        /// A sentinel value that indicates a dimension has a dynamic shape.
        const NSUInteger sentinelValueForVariableDimensions = -1;

        // Return early if any dimension has a dynamic shape.
        for (NSUInteger index = 0; index < dimensions.rank; index++) {
            if ([dimensions extentAtDimensionIndex:index] == sentinelValueForVariableDimensions) {
                NSLog(@"The app doesn't support dynamic tensor shapes.");
                return nil;
            }
        }
```

The method creates a tensor for each binding by configuring the descriptor with the binding’s shape and type:

```objective-c
        tensorDescriptor.dimensions = dimensions;
        tensorDescriptor.dataType = dataType;

        NSError *error = nil;
        id<MTLTensor> tensor = [device newTensorWithDescriptor:tensorDescriptor
                                                         error:&error];

        tensorsByName[name] = tensor;
    }

    return tensorsByName;
}
```

Each tensor stores multidimensional data on the GPU for machine learning operations.

#### Fill Input Tensors with Matrix Data

The app copies each matrix’s data from regular memory into the corresponding tensor by calling the `copyDataToTensor:` method:

```objective-c
- (void)copyDataToTensor:(id<MTLTensor>)tensor {
    if (tensor.dimensions.rank != 2) {
        NSLog(@"Tensor rank isn't 2, which means it's not a 2D matrix.");
        return;
    }

    MTLTensorExtents *dimensions = tensor.dimensions;
    MTLTensorExtents *zeroExtents = [Matrix tensorSliceOriginForRank:dimensions.rank];

    MTLTensorExtents *strides = [Matrix tensorStridesForDimensions:dimensions];

    [tensor replaceSliceOrigin:zeroExtents
               sliceDimensions:dimensions
                     withBytes:self.data.bytes
                       strides:strides];
}
```

The [`replace(sliceOrigin:sliceDimensions:withBytes:strides:)`](mtltensor/replace(sliceorigin:slicedimensions:withbytes:strides:).md) method copies data from CPU memory into a tensor slice. The slice origin argument tells the tensor where to start writing within its data. The method tells the tensor to start with its first element by passing `zeroExtents`, an [`MTLTensorExtents`](mtltensorextents.md) instance with all zero values, to the `replaceSliceOrigin` parameter.

> **Note**: The sample includes helper methods in the `Matrix+TensorUtilities` category that create default arguments for the origin and stride parameters.

#### Add Each Tensor to an Argument Table Entry

The app provides machine learning pass access to the input and output tensors by binding each tensor to an entry in an argument table:

```objective-c
for (NSString *tensorName in bindingsByName) {
    id<MTLTensorBinding> binding = bindingsByName[tensorName];
    id<MTLTensor> tensor = tensorsByName[tensorName];

    [argumentTable setResource:tensor.gpuResourceID
                 atBufferIndex:binding.index];
}
```

Each argument table entry has a unique index, and refers to each tensor by the value of its [`gpuResourceID`](mtltensor/gpuresourceid.md) property.

#### Create an Intermediates Heap

A machine learning encoder sometimes needs a temporary pool of memory as it encodes a pass. The app creates a heap for the encoder based on the value of the pipeline state’s [`intermediatesHeapSize`](mtl4machinelearningpipelinestate/intermediatesheapsize.md) property:

```objective-c
MTLHeapDescriptor *heapDescriptor = [MTLHeapDescriptor new];
heapDescriptor.type = MTLHeapTypePlacement;
heapDescriptor.size = pipelineState.intermediatesHeapSize;

intermediatesHeap = [device newHeapWithDescriptor:heapDescriptor];
if (intermediatesHeap == nil) {
    NSLog(@"Can't create heap for intermediates.");
    return NO;
}
```

Each machine learning encoder needs a heap that supports the [`MTLHeapType.placement`](mtlheaptype/placement.md) option. An encoder creates the intermediate resources it needs from this heap as it encodes a machine learning pass to a command buffer.

#### Encode the Machine Learning Pass

To run a model inference on the Metal device, the app encodes a machine learning dispatch pass into its command buffer.

The app starts the command buffer with a command allocator that provides memory for encoding. It then creates an [`MTL4MachineLearningCommandEncoder`](mtl4machinelearningcommandencoder.md) from the command buffer and configures it with an argument table and the pipeline state.

```objective-c
[commandBuffer beginCommandBufferWithAllocator:commandAllocator];

id<MTL4MachineLearningCommandEncoder> encoder;
encoder = [commandBuffer machineLearningCommandEncoder];

[encoder setArgumentTable:argumentTable];
[encoder setPipelineState:pipelineState];
```

It adds a machine learning pass to the command buffer by calling the encoder’s [`dispatchNetwork(intermediatesHeap:)`](mtl4machinelearningcommandencoder/dispatchnetwork(intermediatesheap:).md) method:

```objective-c
[encoder dispatchNetworkWithIntermediatesHeap:intermediatesHeap];
[encoder endEncoding];

[commandBuffer endCommandBuffer];
```

#### Run the Machine Learning Pass

The app submits the machine learning pass to the Metal device by committing the command buffer to a queue:

```objective-c
[commandQueue commit:&commandBuffer count:1];
```

It may take the Metal device some time to run the contents of a command buffer, which depends on the number of passes the command buffer has and the workload in each pass.

> 💡 **Tip**: You can reuse an [`MTL4CommandBuffer`](mtl4commandbuffer.md) instance immediately after committing it to a queue.

#### Wait for Machine Learning Pass to Finish

The app detects when the device has finished running the pass by adding a signal command that updates an [`MTLSharedEvent`](mtlsharedevent.md) instance to the queue:

```objective-c
// Add a command to the queue that increments the shared event's value.
uint64_t signalValue = sharedEvent.signaledValue + 1;
[commandQueue signalEvent:sharedEvent value:signalValue];
```

The queue runs this command after it finishes running all previous tasks the app submits to it.

Before the app can retrieve the model’s output, it waits for the queue to update the shared event by calling the event’s [`wait(untilSignaledValue:timeoutMS:)`](mtlsharedevent/wait(untilsignaledvalue:timeoutms:).md) method:

```objective-c
const uint64_t kMLPassTimeoutMilliseconds = 100;

// Wait for the GPU to complete the work.
BOOL success = [sharedEvent waitUntilSignaledValue:signalValue
                                         timeoutMS:kMLPassTimeoutMilliseconds];
if (!success) {
    NSLog(@"The machine learning pass timed out.");
}
```

The timeout value is large enough to give the GPU enough time to run the command buffer’s single pass, and small enough that the app can report potential problems, such as stalls or an error state.

#### Retrieve the Results From the Machine Learning Pass

The app copies the data from the output tensor into a new matrix instance with an initializer:

```objective-c
Matrix *product = [[Matrix alloc] initFromTensor:[multiplier productTensor]];
```

The initializer copies data from the Metal tensor by:

1. Retrieving the tensor’s dimensions
2. Creating an [`MTLTensorExtents`](mtltensorextents.md) instance that defines the memory layout of the destination
3. Creating another [`MTLTensorExtents`](mtltensorextents.md) instance that defines the starting point within the source tensor
4. Copying the entire tensor with its [`getBytes(_:strides:sliceOrigin:sliceDimensions:)`](mtltensor/getbytes(_:strides:sliceorigin:slicedimensions:).md) method

```objective-c
// Metal tensors define their dimensions with the innermost dimension first.
MTLTensorExtents *dimensions = tensor.dimensions;
NSInteger columns = [dimensions extentAtDimensionIndex:0];
NSInteger rows = [dimensions extentAtDimensionIndex:1];

NSInteger elementCount = [Matrix totalElementsForDimensions:dimensions];
NSInteger dataLength = elementCount * sizeof(Float32);
NSMutableData *matrixData = [NSMutableData dataWithLength:dataLength];

// Copy data from the tensor.
MTLTensorExtents *zeroExtents = [Matrix tensorSliceOriginForRank:dimensions.rank];
MTLTensorExtents *strides = [Matrix tensorStridesForDimensions:dimensions];

[tensor getBytes:matrixData.mutableBytes
         strides:strides
 fromSliceOrigin:zeroExtents
 sliceDimensions:dimensions];
```

The method assumes the tensor only has two dimensions and retrieves:

- The number of rows from the tensor’s dimension at index `1`
- The number of columns from the tensor’s dimension at index `0`

The two helper methods — `tensorStridesForDimensions:` and `tensorSliceOriginForRank:` — create the `strides` and `zeroExtents` local instances, respectively. The `strides` instance defines the memory layout of the destination memory, `matrixData.mutableBytes`. The `zeroExtents` instance defines the tensor’s first element as the copy operation’s starting point.

## See Also

- [protocol MTL4MachineLearningCommandEncoder](mtl4machinelearningcommandencoder.md)
  Encodes machine learning model inference commands for a single pass.
- [protocol MTL4MachineLearningPipelineState](mtl4machinelearningpipelinestate.md)
  A pipeline state that you can use with machine-learning encoder instances.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/running-a-machine-learning-model-on-the-gpu-timeline)*