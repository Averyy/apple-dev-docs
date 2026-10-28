# MPSGraphExecutable

**Framework**: Metal Performance Shaders Graph  
**Kind**: class  
**Role**: Class

The compiled representation of a compute graph executable.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
class MPSGraphExecutable
```

```objc
@interface MPSGraphExecutable : MPSGraphObject
```

## Overview

An `MPSGraphExecutable` is a compiled graph for specific feeds for specific target tensors and target operations.

## Topics

### Initializers
- [init(MPSGraphPackageAtURL: URL, compilationDescriptor: MPSGraphCompilationDescriptor?)](./mpsgraphexecutable/init%28mpsgraphpackageaturl,compilationdescriptor%29.md)
- [init(coreMLPackageAtURL: URL, compilationDescriptor: MPSGraphCompilationDescriptor?)](./mpsgraphexecutable/init%28coremlpackageaturl,compilationdescriptor%29.md)
- [init(coreMLPackageAtURL: URL, descriptor: MPSGraphCompilationDescriptor?)](./mpsgraphexecutable/init%28coremlpackageaturl,descriptor%29.md)
  Initialize the executable with the Core ML model package at the provided URL.
- [init(package: URL, descriptor: MPSGraphCompilationDescriptor?)](./mpsgraphexecutable/init%28package,descriptor%29.md)
  Initialize the executable with the Metal Performance Shaders Graph package at the provided URL.
### Instance Properties
- [var feedTensors: [MPSGraphTensor]?](./mpsgraphexecutable/feedtensors.md)
  Tensors fed to the graph, can be used to order the inputs when executable is created with a graph.
- [var options: MPSGraphOptions](./mpsgraphexecutable/options.md)
  Options for the graph executable.
- [var targetTensors: [MPSGraphTensor]?](./mpsgraphexecutable/targettensors.md)
  Tensors targeted by the graph, can be used to order the outputs when executable was created with a graph.
### Instance Methods
- [func encode(to: MPSCommandBuffer, inputs: [MPSGraphTensorData], results: [MPSGraphTensorData]?, executionDescriptor: MPSGraphExecutableExecutionDescriptor?) -> [MPSGraphTensorData]](./mpsgraphexecutable/encode%28to,inputs,results,executiondescriptor%29.md)
  Runs the graph for the given feeds and returns the target tensor values, ensuring all target operations also executed. This call is asynchronous and will return immediately after finishing encoding.
- [func getOutputTypes(with: MPSGraphDevice?, inputTypes: [MPSGraphType], compilationDescriptor: MPSGraphCompilationDescriptor?) -> [MPSGraphShapedType]?](./mpsgraphexecutable/getoutputtypes%28with,inputtypes,compilationdescriptor%29.md)
  Get output shapes for a specialized executable.
- [func run(on: any MTL4CommandQueue, inputs: [MPSGraphTensorData], results: [MPSGraphTensorData]?, executionDescriptor: MPSGraphExecutableExecutionDescriptor?) -> [MPSGraphTensorData]](./mpsgraphexecutable/run%28on,inputs,results,executiondescriptor%29.md)
  Runs the graph for the given feeds and returns the target tensor values, ensuring all target operations also executed.
- [func run(with: any MTLCommandQueue, inputs: [MPSGraphTensorData], results: [MPSGraphTensorData]?, executionDescriptor: MPSGraphExecutableExecutionDescriptor?) -> [MPSGraphTensorData]](./mpsgraphexecutable/run%28with,inputs,results,executiondescriptor%29.md)
  Runs the graph for the given feeds and returns the target tensor values, ensuring all target operations also executed.
- [func runAsync(on: any MTL4CommandQueue, inputs: [MPSGraphTensorData], results: [MPSGraphTensorData]?, executionDescriptor: MPSGraphExecutableExecutionDescriptor?) -> [MPSGraphTensorData]](./mpsgraphexecutable/runasync%28on,inputs,results,executiondescriptor%29.md)
  Runs the graph for the given feeds and returns the target tensor values, ensuring all target operations also executed. This call is asynchronous and will return immediately.
- [func runAsync(with: any MTLCommandQueue, inputs: [MPSGraphTensorData], results: [MPSGraphTensorData]?, executionDescriptor: MPSGraphExecutableExecutionDescriptor?) -> [MPSGraphTensorData]](./mpsgraphexecutable/runasync%28with,inputs,results,executiondescriptor%29.md)
  Runs the graph for the given feeds and returns the target tensor values, ensuring all target operations also executed. This call is asynchronous and will return immediately.
- [func serialize(package: URL, descriptor: MPSGraphExecutableSerializationDescriptor?)](./mpsgraphexecutable/serialize%28package,descriptor%29.md)
  Serialize the MPSGraph executable at the provided url.
- [func specialize(with: MPSGraphDevice?, inputTypes: [MPSGraphType], compilationDescriptor: MPSGraphCompilationDescriptor?)](./mpsgraphexecutable/specialize%28with,inputtypes,compilationdescriptor%29.md)
  Specialize the executable and optimize it.

## Relationships

### Inherits From
- [MPSGraphObject](./mpsgraphobject.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Classes
- [class MPSGraph](./mpsgraph.md)
  The optimized representation of a compute graph of operations and tensors.
- [class MPSGraphCompilationDescriptor](./mpsgraphcompilationdescriptor.md)
  A class that consists of all the levers for compiling graphs.
- [class MPSGraphConvolution2DOpDescriptor](./mpsgraphconvolution2dopdescriptor.md)
  A class that describes the properties of a 2D-convolution operator.
- [class MPSGraphConvolution3DOpDescriptor](./mpsgraphconvolution3dopdescriptor.md)
  A class that describes the properties of a 3D-convolution operator.
- [class MPSGraphCreateSparseOpDescriptor](./mpsgraphcreatesparseopdescriptor.md)
  A class that describes the properties of a create sparse operation.
- [class MPSGraphDepthwiseConvolution2DOpDescriptor](./mpsgraphdepthwiseconvolution2dopdescriptor.md)
  A class that defines the parameters for  a 2D-depthwise convolution operation.
- [class MPSGraphDepthwiseConvolution3DOpDescriptor](./mpsgraphdepthwiseconvolution3dopdescriptor.md)
  The class that defines the parameters for a 3D-depthwise convolution operation.
- [class MPSGraphDevice](./mpsgraphdevice.md)
  A class that describes the compute device.
- [class MPSGraphExecutableExecutionDescriptor](./mpsgraphexecutableexecutiondescriptor.md)
  A class that consists of all the levers  to synchronize and schedule executable execution.
- [class MPSGraphExecutableSerializationDescriptor](./mpsgraphexecutableserializationdescriptor.md)
  A class that consists of all the levers  to serialize an executable.
- [class MPSGraphExecutionDescriptor](./mpsgraphexecutiondescriptor.md)
  A class that consists of all the levers  to synchronize and schedule graph execution.
- [class MPSGraphFFTDescriptor](./mpsgraphfftdescriptor.md)
  The class that defines the parameters for a fast Fourier transform (FFT) operation.
- [class MPSGraphGRUDescriptor](./mpsgraphgrudescriptor.md)
  The class that defines the parameters for a gated recurrent unit (GRU) operation.
- [class MPSGraphImToColOpDescriptor](./mpsgraphimtocolopdescriptor.md)
  The class that defines the parameters for an image to column or column to image operation.
- [class MPSGraphLSTMDescriptor](./mpsgraphlstmdescriptor.md)
  The class that defines the parameters for a long short-term memory (LSTM) operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraphexecutable)*