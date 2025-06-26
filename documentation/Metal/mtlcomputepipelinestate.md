# MTLComputePipelineState

**Framework**: Metal  
**Kind**: protocol

An interface that represents a GPU pipeline configuration for running kernels in a compute pass.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
protocol MTLComputePipelineState : MTLAllocation, Sendable
```

## Mentions

- [Improving CPU Performance by Using Argument Buffers](improving-cpu-performance-by-using-argument-buffers.md)
- [Calculating Threadgroup and Grid Sizes](calculating-threadgroup-and-grid-sizes.md)

#### Overview

The [`MTLComputePipelineState`](mtlcomputepipelinestate.md) protocol is an interface that represents a specific configuration for the GPU pipeline for a compute pass. Use a pipeline state instance to configure a compute pass by calling the [`setComputePipelineState(_:)`](mtlcomputecommandencoder/setcomputepipelinestate(_:).md) method of an [`MTLComputeCommandEncoder`](mtlcomputecommandencoder.md) instance.

To create a pipeline state, call the appropriate [`MTLDevice`](mtldevice.md) method (see [`Pipeline State Creation`](pipeline-state-creation.md)). You typically make pipeline state instances at a noncritical time, like when your app first launches. This is because graphics drivers may need time to evaluate and build each pipeline state. However, you can quickly use and reuse each pipeline state throughout your app’s lifetime.

## Topics

### Identifying a Pipeline State
- [var device: any MTLDevice](mtlcomputepipelinestate/device.md)
  The device instance that created the pipeline state.
- [var gpuResourceID: MTLResourceID](mtlcomputepipelinestate/gpuresourceid.md)
  An unique identifier that represents the pipeline state, which you can add to an argument buffer.
- [var label: String?](mtlcomputepipelinestate/label.md)
  A string that helps you identify the compute pipeline state during debugging.
### Checking Threadgroup Attributes
- [var maxTotalThreadsPerThreadgroup: Int](mtlcomputepipelinestate/maxtotalthreadsperthreadgroup.md)
  The maximum number of threads in a threadgroup that you can dispatch to the pipeline.
- [var threadExecutionWidth: Int](mtlcomputepipelinestate/threadexecutionwidth.md)
  The number of threads that the GPU executes simultaneously.
- [var staticThreadgroupMemoryLength: Int](mtlcomputepipelinestate/staticthreadgroupmemorylength.md)
  The length, in bytes, of statically allocated threadgroup memory.
### Checking Imageblock Attributes
- [func imageblockMemoryLength(forDimensions: MTLSize) -> Int](mtlcomputepipelinestate/imageblockmemorylength(fordimensions:).md)
  Returns the length of reserved memory for an imageblock of a given size.
### Checking Indirect Command Buffer Support
- [var supportIndirectCommandBuffers: Bool](mtlcomputepipelinestate/supportindirectcommandbuffers.md)
  A Boolean value that indicates whether the compute pipeline supports indirect command buffers.
### Checking Shader Validation
- [var shaderValidation: MTLShaderValidation](mtlcomputepipelinestate/shadervalidation.md)
  The current state of shader validation for the pipeline.
### Creating Function Handles
- [func functionHandle(function: any MTLFunction) -> (any MTLFunctionHandle)?](mtlcomputepipelinestate/functionhandle(function:)-7d523.md)
  Creates a function handle for a visible function.
### Adding Visible Functions
- [func makeComputePipelineStateWithAdditionalBinaryFunctions(functions: [any MTLFunction]) throws -> any MTLComputePipelineState](mtlcomputepipelinestate/makecomputepipelinestatewithadditionalbinaryfunctions(functions:).md)
  Creates a new pipeline state object with additional callable functions.
### Creating Function Tables
- [func makeVisibleFunctionTable(descriptor: MTLVisibleFunctionTableDescriptor) -> (any MTLVisibleFunctionTable)?](mtlcomputepipelinestate/makevisiblefunctiontable(descriptor:).md)
  Creates a new visible function table.
- [func makeIntersectionFunctionTable(descriptor: MTLIntersectionFunctionTableDescriptor) -> (any MTLIntersectionFunctionTable)?](mtlcomputepipelinestate/makeintersectionfunctiontable(descriptor:).md)
  Creates a new intersection function table.
### Instance Properties
- [var reflection: MTLComputePipelineReflection?](mtlcomputepipelinestate/reflection.md)
  Provides access to this compute pipeline’s reflection.
- [var requiredThreadsPerThreadgroup: MTLSize](mtlcomputepipelinestate/requiredthreadsperthreadgroup.md)
### Instance Methods
- [func functionHandle(function: any MTL4BinaryFunction) -> (any MTLFunctionHandle)?](mtlcomputepipelinestate/functionhandle(function:)-8spaa.md)
  Gets the function handle for a function this pipeline links at the binary level.
- [func functionHandle(withName: String) -> (any MTLFunctionHandle)?](mtlcomputepipelinestate/functionhandle(withname:).md)
  Gets the function handle for a function this pipeline links at the Metal IR level by name.
- [func makeComputePipelineState(additionalBinaryFunctions: [any MTL4BinaryFunction]) throws -> any MTLComputePipelineState](mtlcomputepipelinestate/makecomputepipelinestate(additionalbinaryfunctions:).md)
  Allocates a new compute pipeline state by adding binary functions to this pipeline state.

## Relationships

### Inherits From
- [MTLAllocation](mtlallocation.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class MTL4ComputePipelineDescriptor](mtl4computepipelinedescriptor.md)
  Describes a compute pipeline state.
- [class MTLComputePipelineDescriptor](mtlcomputepipelinedescriptor.md)
  An instance describing the desired GPU state for a kernel call in a compute pass.
- [class MTLStageInputOutputDescriptor](mtlstageinputoutputdescriptor.md)
  A description of the input and output data of a function.
- [class MTLPipelineBufferDescriptor](mtlpipelinebufferdescriptor.md)
  The mutability options for a buffer that a render or compute pipeline uses.
- [class MTLPipelineBufferDescriptorArray](mtlpipelinebufferdescriptorarray.md)
  An array of pipeline buffer descriptors.
- [struct MTLPipelineOption](mtlpipelineoption.md)
  Options that determine how Metal prepares the pipeline.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcomputepipelinestate)*