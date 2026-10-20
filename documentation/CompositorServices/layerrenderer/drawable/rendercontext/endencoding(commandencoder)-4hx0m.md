# endEncoding(commandEncoder:)

**Framework**: Compositor Services  
**Kind**: method  
**Role**: Instance Method

Finish encoding the render context.

**Availability**:
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
func endEncoding(commandEncoder command_encoder: any MTLRenderCommandEncoder)
```

```c
void cp_drawable_render_context_end_encoding(cp_drawable_render_context_t render_context, id<MTLRenderCommandEncoder>command_encoder);
```

#### Discussion

`endEncoding(commandEncoder:)` passes the ownership of the command encoder to the drawable render context and calls [`endEncoding()`](../../../../Metal/mtlcommandencoder/endencoding%28%29.md) on the command encoder. The command encoder used in the render context has the following constraints:

- The `colorAttachment[0]` contains the color texture provided by the layer renderer drawable.
- The [`depthAttachment`](../../../../Metal/mtlrenderpassdescriptor/depthattachment.md) contains the depth texture provided by the layer renderer drawable.
- The [`renderTargetArrayLength`](../../../../Metal/mtlrenderpassdescriptor/rendertargetarraylength.md) is the same as the number of views in the layer renderer drawable.
- The [`rasterizationRateMap`](../../../../Metal/mtlrenderpassdescriptor/rasterizationratemap.md) matches the one provided by the layer renderer drawable.
- The API doesn’t support dedicated and shared layouts.

If the render encoder has multiple color attachments, set [`supportColorAttachmentMapping`](../../../../Metal/mtl4renderpassdescriptor/supportcolorattachmentmapping.md) to `true` to avoid Metal API validation errors.

For testing performance of this method, always test your app on-device rather than in Simulator. However, if you need to iterate on your code in development, you can disable API validation in Xcode, or separate the rendering into multiple render encoders for other color attachments.

## Parameters

- `command_encoder`: The command encoder to use to render the Compositor effects and present the layer renderer drawable.

## See Also

### Rendering with Metal
- [func drawMaskOnStencilAttachment(commandEncoder: any MTLRenderCommandEncoder, value: UInt8)](./drawmaskonstencilattachment%28commandencoder,value%29-65i67.md)
  Store the value parameter in the stencil texture in the pixels that the compositor will display onscreen.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/layerrenderer/drawable/rendercontext/endencoding(commandencoder:)-4hx0m)*