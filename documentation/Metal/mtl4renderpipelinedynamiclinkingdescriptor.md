# MTL4RenderPipelineDynamicLinkingDescriptor

**Framework**: Metal  
**Kind**: class

Groups together properties that provide linking properties for render pipelines.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
class MTL4RenderPipelineDynamicLinkingDescriptor
```

## Topics

### Instance Properties
- [var fragmentLinkingDescriptor: MTL4PipelineStageDynamicLinkingDescriptor](mtl4renderpipelinedynamiclinkingdescriptor/fragmentlinkingdescriptor.md)
  Controls properties for linking the fragment stage of the render pipeline.
- [var meshLinkingDescriptor: MTL4PipelineStageDynamicLinkingDescriptor](mtl4renderpipelinedynamiclinkingdescriptor/meshlinkingdescriptor.md)
  Controls properties for linking the mesh stage of the render pipeline.
- [var objectLinkingDescriptor: MTL4PipelineStageDynamicLinkingDescriptor](mtl4renderpipelinedynamiclinkingdescriptor/objectlinkingdescriptor.md)
  Controls properties for link the object stage of the render pipeline.
- [var tileLinkingDescriptor: MTL4PipelineStageDynamicLinkingDescriptor](mtl4renderpipelinedynamiclinkingdescriptor/tilelinkingdescriptor.md)
  Controls properties for linking the tile stage of the render pipeline.
- [var vertexLinkingDescriptor: MTL4PipelineStageDynamicLinkingDescriptor](mtl4renderpipelinedynamiclinkingdescriptor/vertexlinkingdescriptor.md)
  Controls properties for linking the vertex stage of the render pipeline.

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
- [class MTLTileRenderPipelineDescriptor](mtltilerenderpipelinedescriptor.md)
  An object that configures new render pipeline state objects for tile shading.
- [class MTLTileRenderPipelineColorAttachmentDescriptor](mtltilerenderpipelinecolorattachmentdescriptor.md)
  A description of a tile-shading render pipeline’s color render target.
- [struct MTLPipelineOption](mtlpipelineoption.md)
  Options that determine how Metal prepares the pipeline.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4renderpipelinedynamiclinkingdescriptor)*