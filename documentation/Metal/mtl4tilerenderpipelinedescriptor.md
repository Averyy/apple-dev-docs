# MTL4TileRenderPipelineDescriptor

**Framework**: Metal  
**Kind**: class

Groups together properties you use to create a tile render pipeline state object.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
class MTL4TileRenderPipelineDescriptor
```

## Topics

### Instance Properties
- [var colorAttachments: MTLTileRenderPipelineColorAttachmentDescriptorArray](mtl4tilerenderpipelinedescriptor/colorattachments.md)
  Access an array of descriptors that configure the properties of each color attachment in the tile render pipeline.
- [var maxTotalThreadsPerThreadgroup: Int](mtl4tilerenderpipelinedescriptor/maxtotalthreadsperthreadgroup.md)
  Sets the maximum number of threads that the GPU can execute simultaneously within a single threadgroup in the tile render pipeline.
- [var rasterSampleCount: Int](mtl4tilerenderpipelinedescriptor/rastersamplecount.md)
  Configures the number of samples per pixel used for multisampling.
- [var requiredThreadsPerThreadgroup: MTLSize](mtl4tilerenderpipelinedescriptor/requiredthreadsperthreadgroup.md)
  Sets the required number of threads per threadgroup for tile dispatches.
- [var staticLinkingDescriptor: MTL4StaticLinkingDescriptor!](mtl4tilerenderpipelinedescriptor/staticlinkingdescriptor.md)
  Configures an object that contains information about functions to link to the tile render pipeline when Metal builds it.
- [var supportBinaryLinking: Bool](mtl4tilerenderpipelinedescriptor/supportbinarylinking.md)
  Indicates whether the pipeline supports linking binary functions.
- [var threadgroupSizeMatchesTileSize: Bool](mtl4tilerenderpipelinedescriptor/threadgroupsizematchestilesize.md)
  Indicating whether the size of the threadgroup matches the size of a tile in the render pipeline.
- [var tileFunctionDescriptor: MTL4FunctionDescriptor?](mtl4tilerenderpipelinedescriptor/tilefunctiondescriptor.md)
  Configures the tile function that the render pipeline executes for each tile in the tile shader stage.
### Instance Methods
- [func reset()](mtl4tilerenderpipelinedescriptor/reset.md)
  Resets the descriptor to the default state.

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
- [class MTLTileRenderPipelineDescriptor](mtltilerenderpipelinedescriptor.md)
  An object that configures new render pipeline state objects for tile shading.
- [class MTLTileRenderPipelineColorAttachmentDescriptor](mtltilerenderpipelinecolorattachmentdescriptor.md)
  A description of a tile-shading render pipeline’s color render target.
- [struct MTLPipelineOption](mtlpipelineoption.md)
  Options that determine how Metal prepares the pipeline.
- [class MTL4RenderPipelineBinaryFunctionsDescriptor](mtl4renderpipelinebinaryfunctionsdescriptor.md)
  Allows you to specify additional binary functions to link to each stage of a render pipeline.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4tilerenderpipelinedescriptor)*