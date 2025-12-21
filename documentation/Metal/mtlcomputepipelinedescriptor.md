# MTLComputePipelineDescriptor

**Framework**: Metal  
**Kind**: class

An instance describing the desired GPU state for a kernel call in a compute pass.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class MTLComputePipelineDescriptor
```

## Mentions

- [Compiling and linking Metal dynamic libraries](compiling-and-linking-metal-dynamic-libraries.md)

#### Overview

> ❗ **Important**:  Before creating a pipeline state, set the [`computeFunction`](mtlcomputepipelinedescriptor/computefunction.md) property on your descriptor instance. This property tells the GPU which kernel to run.

A pipeline descriptor provides information necessary for creating an [`MTLComputePipelineState`](mtlcomputepipelinestate.md) instance.

## Topics

### Configuring the compute execution environment
- [var computeFunction: (any MTLFunction)?](mtlcomputepipelinedescriptor/computefunction.md)
  The compute kernel the pipeline calls.
- [var threadGroupSizeIsMultipleOfThreadExecutionWidth: Bool](mtlcomputepipelinedescriptor/threadgroupsizeismultipleofthreadexecutionwidth.md)
  A Boolean value that indicates whether the threadgroup size is always a multiple of the thread execution width.
- [var maxTotalThreadsPerThreadgroup: Int](mtlcomputepipelinedescriptor/maxtotalthreadsperthreadgroup.md)
  A property that limits the number of threads you can dispatch in a threadgroup for the compute function.
- [var maxCallStackDepth: Int](mtlcomputepipelinedescriptor/maxcallstackdepth.md)
  The maximum call stack depth for indirect function calls in compute shaders.
### Configuring compute pass inputs
- [var stageInputDescriptor: MTLStageInputOutputDescriptor?](mtlcomputepipelinedescriptor/stageinputdescriptor.md)
  The organization of input and output data for the next kernel call.
- [class MTLAttributeDescriptor](mtlattributedescriptor.md)
  A descriptor of an argument’s format and where its data is in memory.
- [class MTLAttributeDescriptorArray](mtlattributedescriptorarray.md)
  An array of attribute descriptor objects.
- [class MTLBufferLayoutDescriptor](mtlbufferlayoutdescriptor.md)
  A description of how a compute function fetches input data for an attribute.
- [class MTLBufferLayoutDescriptorArray](mtlbufferlayoutdescriptorarray.md)
  An array of buffer layout descriptor objects.
### Configuring buffer mutability
- [var buffers: MTLPipelineBufferDescriptorArray](mtlcomputepipelinedescriptor/buffers.md)
  The buffer mutability options to apply to the next kernel call.
### Identifying the pipeline state object
- [var label: String?](mtlcomputepipelinedescriptor/label.md)
  A string that identifies the instance.
### Configuring indirect command buffers
- [var supportIndirectCommandBuffers: Bool](mtlcomputepipelinedescriptor/supportindirectcommandbuffers.md)
  A Boolean value that indicates whether you can encode commands that reference the pipeline state object into an indirect command buffer.
### Configuring shader validation
- [var shaderValidation: MTLShaderValidation](mtlcomputepipelinedescriptor/shadervalidation.md)
  A value that enables or disables shader validation for the pipeline.
### Reset to defaults
- [func reset()](mtlcomputepipelinedescriptor/reset.md)
  Resets all compute pipeline descriptor properties to their default values.
### Loading dynamic libraries to link at runtime
- [var preloadedLibraries: [any MTLDynamicLibrary]](mtlcomputepipelinedescriptor/preloadedlibraries.md)
  The dynamic libraries that contain precompiled shader functions you want to link.
- [var insertLibraries: [any MTLDynamicLibrary]?](mtlcomputepipelinedescriptor/insertlibraries.md)
  The dynamic libraries that contain precompiled shader functions you want to link.
### Setting callable functions
- [var linkedFunctions: MTLLinkedFunctions?](mtlcomputepipelinedescriptor/linkedfunctions.md)
  The functions with available function pointers for the next kernel call.
### Loading binary archives
- [var supportAddingBinaryFunctions: Bool](mtlcomputepipelinedescriptor/supportaddingbinaryfunctions.md)
  A Boolean value that indicates whether you can use the pipeline to create new pipelines by adding binary functions to its callable functions list.
- [var binaryArchives: [any MTLBinaryArchive]?](mtlcomputepipelinedescriptor/binaryarchives.md)
  The binary archives that contain any precompiled shader functions to link.
### Instance Properties
- [var requiredThreadsPerThreadgroup: MTLSize](mtlcomputepipelinedescriptor/requiredthreadsperthreadgroup.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class MTL4ComputePipelineDescriptor](mtl4computepipelinedescriptor.md)
  Describes a compute pipeline state.
- [protocol MTLComputePipelineState](mtlcomputepipelinestate.md)
  An interface that represents a GPU pipeline configuration for running kernels in a compute pass.
- [class MTLStageInputOutputDescriptor](mtlstageinputoutputdescriptor.md)
  A description of the input and output data of a function.
- [class MTLPipelineBufferDescriptor](mtlpipelinebufferdescriptor.md)
  The mutability options for a buffer that a render or compute pipeline uses.
- [class MTLPipelineBufferDescriptorArray](mtlpipelinebufferdescriptorarray.md)
  An array of pipeline buffer descriptors.
- [struct MTLPipelineOption](mtlpipelineoption.md)
  Options that determine how Metal prepares the pipeline.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcomputepipelinedescriptor)*