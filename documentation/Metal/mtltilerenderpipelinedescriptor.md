# MTLTileRenderPipelineDescriptor

**Framework**: Metal  
**Kind**: class

An object that configures new render pipeline state objects for tile shading.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.5+
- visionOS 1.0+

## Declaration

```swift
class MTLTileRenderPipelineDescriptor
```

## Topics

### Identifying the Render Pipeline
- [var label: String?](mtltilerenderpipelinedescriptor/label.md)
  A string that identifies the tile pipeline descriptor.
### Specifying Graphics Functions and Associated Data
- [var tileFunction: any MTLFunction](mtltilerenderpipelinedescriptor/tilefunction.md)
  The compute kernel or fragment function the pipeline calls.
- [var tileBuffers: MTLPipelineBufferDescriptorArray](mtltilerenderpipelinedescriptor/tilebuffers.md)
  An array that contains the buffer mutability options for a render pipeline’s tile function.
- [var maxCallStackDepth: Int](mtltilerenderpipelinedescriptor/maxcallstackdepth.md)
  The maximum function call depth from the top-most shader function.
### Specifying Rasterization and Visibility State
- [var threadgroupSizeMatchesTileSize: Bool](mtltilerenderpipelinedescriptor/threadgroupsizematchestilesize.md)
  A Boolean value that indicates whether all threadgroups for this pipeline completely cover tiles.
- [var rasterSampleCount: Int](mtltilerenderpipelinedescriptor/rastersamplecount.md)
  The number of samples in each fragment.
### Specifying Rendering Pipeline State
- [func reset()](mtltilerenderpipelinedescriptor/reset.md)
  Specifies the default rendering pipeline state values for the descriptor.
- [var colorAttachments: MTLTileRenderPipelineColorAttachmentDescriptorArray](mtltilerenderpipelinedescriptor/colorattachments.md)
  An array of attachments that store color data.
### Specifying Threads per Threadgroup
- [var maxTotalThreadsPerThreadgroup: Int](mtltilerenderpipelinedescriptor/maxtotalthreadsperthreadgroup.md)
  The maximum number of threads in a threadgroup when dispatching a command using the pipeline.
### Specifying Precompiled Shader Binaries
- [var supportAddingBinaryFunctions: Bool](mtltilerenderpipelinedescriptor/supportaddingbinaryfunctions.md)
  A Boolean value that indicates whether you can use the pipeline to create new pipelines by adding binary functions to its callable functions list.
- [var binaryArchives: [any MTLBinaryArchive]?](mtltilerenderpipelinedescriptor/binaryarchives.md)
  An array of binary archives to search for precompiled versions of the shader.
### Specifying Callable Functions for the Pipeline
- [var linkedFunctions: MTLLinkedFunctions!](mtltilerenderpipelinedescriptor/linkedfunctions.md)
  Functions that you can specify as function arguments for the tile shader when encoding commands that use the pipeline.
### Specifying Shader Validation
- [var shaderValidation: MTLShaderValidation](mtltilerenderpipelinedescriptor/shadervalidation.md)
  A value that enables or disables shader validation for the pipeline.
### Instance Properties
- [var preloadedLibraries: [any MTLDynamicLibrary]](mtltilerenderpipelinedescriptor/preloadedlibraries.md)
- [var requiredThreadsPerThreadgroup: MTLSize](mtltilerenderpipelinedescriptor/requiredthreadsperthreadgroup.md)

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

- [protocol MTLRenderPipelineState](mtlrenderpipelinestate.md)
  An interface that represents a graphics pipeline configuration for a render pass, which the pass applies to the draw commands you encode.
- [class MTL4RenderPipelineDescriptor](mtl4renderpipelinedescriptor.md)
  Groups together properties to create a render pipeline state object.
- [class MTLRenderPipelineDescriptor](mtlrenderpipelinedescriptor.md)
  An argument of options you pass to a GPU device to get a render pipeline state.
- [class MTLRenderPipelineFunctionsDescriptor](mtlrenderpipelinefunctionsdescriptor.md)
  A collection of functions for updating a render pipeline.
- [class MTL4MeshRenderPipelineDescriptor](mtl4meshrenderpipelinedescriptor.md)
  Groups together properties you use to create a mesh render pipeline state object.
- [class MTLMeshRenderPipelineDescriptor](mtlmeshrenderpipelinedescriptor.md)
  An object that configures new render pipeline state objects for mesh shading.
- [class MTLPipelineBufferDescriptor](mtlpipelinebufferdescriptor.md)
  The mutability options for a buffer that a render or compute pipeline uses.
- [class MTLPipelineBufferDescriptorArray](mtlpipelinebufferdescriptorarray.md)
  An array of pipeline buffer descriptors.
- [class MTL4RenderPipelineColorAttachmentDescriptor](mtl4renderpipelinecolorattachmentdescriptor.md)
- [class MTLRenderPipelineColorAttachmentDescriptor](mtlrenderpipelinecolorattachmentdescriptor.md)
  A color render target that specifies the color configuration and color operations for a render pipeline.
- [class MTLRenderPipelineColorAttachmentDescriptorArray](mtlrenderpipelinecolorattachmentdescriptorarray.md)
  An array of render pipeline color attachment descriptor objects.
- [class MTL4TileRenderPipelineDescriptor](mtl4tilerenderpipelinedescriptor.md)
  Groups together properties you use to create a tile render pipeline state object.
- [class MTLTileRenderPipelineColorAttachmentDescriptor](mtltilerenderpipelinecolorattachmentdescriptor.md)
  A description of a tile-shading render pipeline’s color render target.
- [struct MTLPipelineOption](mtlpipelineoption.md)
  Options that determine how Metal prepares the pipeline.
- [class MTL4RenderPipelineBinaryFunctionsDescriptor](mtl4renderpipelinebinaryfunctionsdescriptor.md)
  Allows you to specify additional binary functions to link to each stage of a render pipeline.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtltilerenderpipelinedescriptor)*