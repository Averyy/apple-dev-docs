# MTL4RenderPipelineColorAttachmentDescriptor

**Framework**: Metal  
**Kind**: class

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
class MTL4RenderPipelineColorAttachmentDescriptor
```

## Topics

### Instance Properties
- [var alphaBlendOperation: MTLBlendOperation](mtl4renderpipelinecolorattachmentdescriptor/alphablendoperation.md)
  Configures the alpha blending operation.
- [var blendingState: MTL4BlendState](mtl4renderpipelinecolorattachmentdescriptor/blendingstate.md)
  Enables blending.
- [var destinationAlphaBlendFactor: MTLBlendFactor](mtl4renderpipelinecolorattachmentdescriptor/destinationalphablendfactor.md)
  Configures the destination-alpha blend factor.
- [var destinationRGBBlendFactor: MTLBlendFactor](mtl4renderpipelinecolorattachmentdescriptor/destinationrgbblendfactor.md)
  Configures the destination RGB blend factor.
- [var pixelFormat: MTLPixelFormat](mtl4renderpipelinecolorattachmentdescriptor/pixelformat.md)
  Configures the pixel format.
- [var rgbBlendOperation: MTLBlendOperation](mtl4renderpipelinecolorattachmentdescriptor/rgbblendoperation.md)
  Configures the RGB blend operation.
- [var sourceAlphaBlendFactor: MTLBlendFactor](mtl4renderpipelinecolorattachmentdescriptor/sourcealphablendfactor.md)
  Configures the source-alpha blend factor.
- [var sourceRGBBlendFactor: MTLBlendFactor](mtl4renderpipelinecolorattachmentdescriptor/sourcergbblendfactor.md)
  Configures the source RGB blend factor.
- [var writeMask: MTLColorWriteMask](mtl4renderpipelinecolorattachmentdescriptor/writemask.md)
  Configures the color write mask.
### Instance Methods
- [func reset()](mtl4renderpipelinecolorattachmentdescriptor/reset.md)
  Resets this descriptor to its default state.

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
- [class MTL4RenderPipelineBinaryFunctionsDescriptor](mtl4renderpipelinebinaryfunctionsdescriptor.md)
  Allows you to specify additional binary functions to link to each stage of a render pipeline.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4renderpipelinecolorattachmentdescriptor)*