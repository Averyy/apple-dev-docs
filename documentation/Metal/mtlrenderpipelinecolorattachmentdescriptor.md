# MTLRenderPipelineColorAttachmentDescriptor

**Framework**: Metal  
**Kind**: class

A color render target that specifies the color configuration and color operations for a render pipeline.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
class MTLRenderPipelineColorAttachmentDescriptor
```

#### Overview

An [`MTLRenderPipelineColorAttachmentDescriptor`](mtlrenderpipelinecolorattachmentdescriptor.md) instance defines the configuration of a color attachment associated with a rendering pipeline.

The [`pixelFormat`](mtlrenderpipelinecolorattachmentdescriptor/pixelformat.md) property needs to be specified for the rendering pipeline state at the color attachment.

Blend operations determine how a source fragment is combined with a destination value in a color attachment to determine the pixel value to be written. The following properties define whether and how blending is performed:

- The [`isBlendingEnabled`](mtlrenderpipelinecolorattachmentdescriptor/isblendingenabled.md) property enables blending. The default value is [`false`](https://developer.apple.com/documentation/Swift/false).
- The [`writeMask`](mtlrenderpipelinecolorattachmentdescriptor/writemask.md) property identifies which color channels are blended. The default value is [`all`](mtlcolorwritemask/all.md), which allows all color channels to be blended.
- The [`rgbBlendOperation`](mtlrenderpipelinecolorattachmentdescriptor/rgbblendoperation.md) and [`alphaBlendOperation`](mtlrenderpipelinecolorattachmentdescriptor/alphablendoperation.md) properties assign the blend operations for RGB and alpha pixel data. The default value for both properties is [`MTLBlendOperation.add`](mtlblendoperation/add.md).
- The [`sourceRGBBlendFactor`](mtlrenderpipelinecolorattachmentdescriptor/sourcergbblendfactor.md), [`sourceAlphaBlendFactor`](mtlrenderpipelinecolorattachmentdescriptor/sourcealphablendfactor.md), [`destinationRGBBlendFactor`](mtlrenderpipelinecolorattachmentdescriptor/destinationrgbblendfactor.md), and [`destinationAlphaBlendFactor`](mtlrenderpipelinecolorattachmentdescriptor/destinationalphablendfactor.md) properties assign the source and destination blend factors. The default value for [`sourceRGBBlendFactor`](mtlrenderpipelinecolorattachmentdescriptor/sourcergbblendfactor.md) and [`sourceAlphaBlendFactor`](mtlrenderpipelinecolorattachmentdescriptor/sourcealphablendfactor.md) is [`MTLBlendFactor.one`](mtlblendfactor/one.md). The default value for [`destinationRGBBlendFactor`](mtlrenderpipelinecolorattachmentdescriptor/destinationrgbblendfactor.md) and [`destinationAlphaBlendFactor`](mtlrenderpipelinecolorattachmentdescriptor/destinationalphablendfactor.md) is [`MTLBlendFactor.zero`](mtlblendfactor/zero.md).

## Topics

### Configuring render pipeline states
- [var pixelFormat: MTLPixelFormat](mtlrenderpipelinecolorattachmentdescriptor/pixelformat.md)
  The pixel format of the color attachment’s texture.
- [var writeMask: MTLColorWriteMask](mtlrenderpipelinecolorattachmentdescriptor/writemask.md)
  A bitmask that restricts which color channels are written into the texture.
- [struct MTLColorWriteMask](mtlcolorwritemask.md)
  Values used to specify a mask to permit or restrict writing to color channels of a color value.
### Controlling blend operations
- [var isBlendingEnabled: Bool](mtlrenderpipelinecolorattachmentdescriptor/isblendingenabled.md)
  A Boolean value that determines whether blending is enabled.
- [var alphaBlendOperation: MTLBlendOperation](mtlrenderpipelinecolorattachmentdescriptor/alphablendoperation.md)
  The blend operation assigned for the alpha data.
- [var rgbBlendOperation: MTLBlendOperation](mtlrenderpipelinecolorattachmentdescriptor/rgbblendoperation.md)
  The blend operation assigned for the RGB data.
- [enum MTLBlendOperation](mtlblendoperation.md)
  For every pixel, `MTLBlendOperation` determines how to combine and weight the source fragment values with the destination values. Some blend operations multiply the source values by a source blend factor (SBF), multiply the destination values by a destination blend factor (DBF), and then combine the results using addition or subtraction. Other blend operations use either a minimum or maximum function to determine the result.
### Configuring blend factors
- [var destinationAlphaBlendFactor: MTLBlendFactor](mtlrenderpipelinecolorattachmentdescriptor/destinationalphablendfactor.md)
  The destination blend factor (DBF) used by the alpha blend operation.
- [var destinationRGBBlendFactor: MTLBlendFactor](mtlrenderpipelinecolorattachmentdescriptor/destinationrgbblendfactor.md)
  The destination blend factor (DBF) used by the RGB blend operation.
- [var sourceAlphaBlendFactor: MTLBlendFactor](mtlrenderpipelinecolorattachmentdescriptor/sourcealphablendfactor.md)
  The source blend factor (SBF) used by the alpha blend operation.
- [var sourceRGBBlendFactor: MTLBlendFactor](mtlrenderpipelinecolorattachmentdescriptor/sourcergbblendfactor.md)
  The source blend factor (SBF) used by the RGB blend operation.
- [enum MTLBlendFactor](mtlblendfactor.md)
  The source and destination blend factors are often needed to complete specification of a blend operation. In most cases, the blend factor for both RGB values () and alpha values () are similar to one another, but in some cases, such as `MTLBlendFactorSourceAlphaSaturated`, the blend factor is slightly different. Four blend factors (`MTLBlendFactorBlendColor`, `MTLBlendFactorOneMinusBlendColor`, `MTLBlendFactorBlendAlpha`, and `MTLBlendFactorOneMinusBlendAlpha`) refer to a constant blend color value that is set by the [`setBlendColor(red:green:blue:alpha:)`](mtlrendercommandencoder/setblendcolor(red:green:blue:alpha:).md) method of `MTLRenderCommandEncoder`.

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
  The mutability options for a buffer that a render or compute pipeline uses.
- [class MTLPipelineBufferDescriptorArray](mtlpipelinebufferdescriptorarray.md)
  An array of pipeline buffer descriptors.
- [class MTL4RenderPipelineColorAttachmentDescriptor](mtl4renderpipelinecolorattachmentdescriptor.md)
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

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrenderpipelinecolorattachmentdescriptor)*