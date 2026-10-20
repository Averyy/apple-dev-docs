# drawMaskOnStencilAttachment(commandEncoder:value:)

**Framework**: Compositor Services  
**Kind**: method  
**Role**: Instance Method

Store the value parameter in the stencil texture in the pixels that the Compositor displays onscreen.

**Availability**:
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
func drawMaskOnStencilAttachment(commandEncoder command_encoder: any MTL4RenderCommandEncoder, value: UInt8)
```

```c
void cp_drawable_render_context_mtl4_draw_mask_on_stencil_attachment(cp_drawable_render_context_t render_context, id<MTL4RenderCommandEncoder>command_encoder, uint8_t value);
```

#### Discussion

In full and mixed immersion styles, [`drawMaskOnStencilAttachment(commandEncoder:value:)`](./drawmaskonstencilattachment%28commandencoder,value%29-65i67.md) stores the full texture. The command encoder used in the render context has the following constraints:

- The stencil texture has the same pixel format as [`cp_layer_renderer_configuration_get_drawable_render_context_stencil_format`](../../../cp_layer_renderer_configuration_get_drawable_render_context_stencil_format.md).
- The [`renderTargetArrayLength`](../../../../Metal/mtlrenderpassdescriptor/rendertargetarraylength.md) is the same as the number of views in the layer renderer drawable.
- The [`rasterizationRateMap`](../../../../Metal/mtlrenderpassdescriptor/rasterizationratemap.md) matches the one provided by the layer renderer drawable.
- The API doesn’t support dedicated or shared layouts.

If the render encoder has multiple color attachments, set [`supportColorAttachmentMapping`](../../../../Metal/mtl4renderpassdescriptor/supportcolorattachmentmapping.md) to `true` to avoid Metal API validation errors.

For testing performance of this method, always test your app on-device rather than in Simulator. However, if you need to iterate on your code in development, you can disable API validation in Xcode, or separate the rendering into multiple render encoders for other color attachments.

This function modifies the depth stencil state, viewports, vertex amplification count, and some of the texture bindings in the render command encoder passed to the function. Make sure to set those values again to those expected in your app.

## Parameters

- `value`: The value to use when updating the stencil texture in the [`MTLRenderCommandEncoder`](../../../../Metal/mtlrendercommandencoder.md).

## See Also

### Rendering with Metal 4
- [func endEncoding(commandEncoder: any MTL4RenderCommandEncoder)](./endencoding%28commandencoder%29-2l6lk.md)
  Finish encoding the render context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/layerrenderer/drawable/rendercontext/drawmaskonstencilattachment(commandencoder:value:)-7npim)*