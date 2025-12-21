# drawMaskOnStencilAttachment(commandEncoder:value:)

**Framework**: Compositor Services  
**Kind**: method

Store the value parameter in the stencil texture in the pixels that the compositor will display onscreen.

**Availability**:
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
func drawMaskOnStencilAttachment(commandEncoder command_encoder: any MTLRenderCommandEncoder, value: UInt8)
```

#### Discussion

In full and mixed immersion styles, [`drawMaskOnStencilAttachment(commandEncoder:value:)`](layerrenderer/drawable/rendercontext/drawmaskonstencilattachment(commandencoder:value:)-65i67.md) stores the full texture. The command encoder used in the render context has the following constraints:

- The stencil texture has the same pixel format as [`cp_layer_renderer_configuration_get_drawable_render_context_stencil_format`](cp_layer_renderer_configuration_get_drawable_render_context_stencil_format.md).
- The [`renderTargetArrayLength`](https://developer.apple.com/documentation/Metal/MTLRenderPassDescriptor/renderTargetArrayLength) is the same as the number of views in the layer renderer drawable.
- The [`rasterizationRateMap`](https://developer.apple.com/documentation/Metal/MTLRenderPassDescriptor/rasterizationRateMap) matches the one provided by the layer renderer drawable.
- The API doesn’t support dedicated or shared layouts.

If the render encoder has multiple color attachments, set [`supportColorAttachmentMapping`](https://developer.apple.com/documentation/Metal/MTL4RenderPassDescriptor/supportColorAttachmentMapping) to `true` to avoid Metal API validation errors.

For testing performance of this method, always test your app on-device rather than in Simulator. However, if you need to iterate on your code in development, you can disable API validation in Xcode, or separate the rendering into multiple render encoders for other color attachments.

This function modifies the depth stencil state, viewports, vertex amplification count, and some of the texture bindings in the render command encoder passed to the function. Make sure to set those values again to those expected in your app.

## Parameters

- `value`: The value to use when updating the stencil texture in the  .

## See Also

- [func endEncoding(commandEncoder: any MTLRenderCommandEncoder)](layerrenderer/drawable/rendercontext/endencoding(commandencoder:)-4hx0m.md)
  Finish encoding the render context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/layerrenderer/drawable/rendercontext/drawmaskonstencilattachment(commandencoder:value:)-65i67)*