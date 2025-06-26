# MTL4ComputePipelineDescriptor

**Framework**: Metal  
**Kind**: class

Describes a compute pipeline state.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
class MTL4ComputePipelineDescriptor
```

## Topics

### Instance Properties
- [var computeFunctionDescriptor: MTL4FunctionDescriptor?](mtl4computepipelinedescriptor/computefunctiondescriptor.md)
  A descriptor representing the compute pipeline’s function.
- [var maxTotalThreadsPerThreadgroup: Int](mtl4computepipelinedescriptor/maxtotalthreadsperthreadgroup.md)
  The maximum total number of threads that can be executing in a single threadgroup for the compute function.
- [var requiredThreadsPerThreadgroup: MTLSize](mtl4computepipelinedescriptor/requiredthreadsperthreadgroup.md)
  The required number of threads per threadgroup for compute dispatches.
- [var staticLinkingDescriptor: MTL4StaticLinkingDescriptor?](mtl4computepipelinedescriptor/staticlinkingdescriptor.md)
  An object that contains information about functions to link to the compute pipeline.
- [var supportBinaryLinking: Bool](mtl4computepipelinedescriptor/supportbinarylinking.md)
  A boolean value indicating whether the compute pipeline supports linking binary functions.
- [var supportIndirectCommandBuffers: MTL4IndirectCommandBufferSupportState](mtl4computepipelinedescriptor/supportindirectcommandbuffers.md)
  A value indicating whether the pipeline supports Metal indirect command buffers.
- [var threadGroupSizeIsMultipleOfThreadExecutionWidth: Bool](mtl4computepipelinedescriptor/threadgroupsizeismultipleofthreadexecutionwidth.md)
  A boolean value indicating whether each dimension of the threadgroup size is a multiple of its corresponding thread execution width.
### Instance Methods
- [func reset()](mtl4computepipelinedescriptor/reset.md)
  Resets the descriptor to the default values.

## Relationships

### Inherits From
- [MTL4PipelineDescriptor](mtl4pipelinedescriptor.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class MTLComputePipelineDescriptor](mtlcomputepipelinedescriptor.md)
  An instance describing the desired GPU state for a kernel call in a compute pass.
- [protocol MTLComputePipelineState](mtlcomputepipelinestate.md)
  An interface that represents a GPU pipeline configuration for running kernels in a compute pass.
- [class MTLStageInputOutputDescriptor](mtlstageinputoutputdescriptor.md)
  A description of the input and output data of a function.
- [class MTLPipelineBufferDescriptor](mtlpipelinebufferdescriptor.md)
  The mutability options for a buffer that a render or compute pipeline uses.
- [class MTLPipelineBufferDescriptorArray](mtlpipelinebufferdescriptorarray.md)
  An array of pipeline buffer descriptors.
- [struct MTLPipelineOption](mtlpipelineoption.md)
  Options that determine how Metal prepares the pipeline.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4computepipelinedescriptor)*