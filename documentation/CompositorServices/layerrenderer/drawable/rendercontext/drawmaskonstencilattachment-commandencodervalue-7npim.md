# drawMaskOnStencilAttachment(commandEncoder:value:)

**Framework**: Compositor Services  
**Kind**: method

Store the `value` parameter in the stencil texture in the pixels that Compositor will display on the screen.

**Availability**:
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
func drawMaskOnStencilAttachment(commandEncoder command_encoder: any MTL4RenderCommandEncoder, value: UInt8)
```

#### Discussion

> **Note**: In Full and Mixed immersion style, this will be the full texture.

> **Note**: The command encoder used in the render context has the following constraints: - stencil texture: should have the same pixel format as [`cp_layer_renderer_configuration_get_drawable_render_context_stencil_format`](cp_layer_renderer_configuration_get_drawable_render_context_stencil_format.md)
- renderTargetArrayLength: should be the same as the number of views in the drawable.
- rasterizationRateMap: should be the one provided by the drawable.
- layer renderer layout: Dedicated and Shared layout is not supported.
- supportColorAttachmentMapping: The render pass descriptor used to create the render encoder should have `supportColorAttachmentMapping` set to true.

> **Note**: This function will modify the depth stencil state, the viewports, the vertex amplification count and some of the texture bindings in the render command encoder passed to the function. Make sure to set those values again to the ones expected in your application.

## Parameters

- `command_encoder`: The command encoder to use to render the Compositor effects   and present the drawable.
- `value`: The value to use when updating the stencil texture in the command_encoder.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/layerrenderer/drawable/rendercontext/drawmaskonstencilattachment(commandencoder:value:)-7npim)*