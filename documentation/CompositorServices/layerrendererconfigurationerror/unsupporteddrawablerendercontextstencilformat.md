# LayerRendererConfigurationError.unsupportedDrawableRenderContextStencilFormat

**Framework**: Compositor Services  
**Kind**: case

An error that indicates the layer doesn’t support the current pixel format for stencil texture.

**Availability**:
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
case unsupportedDrawableRenderContextStencilFormat
```

#### Discussion

Compare the value the [`cp_layer_renderer_configuration_get_drawable_render_context_stencil_format`](cp_layer_renderer_configuration_get_drawable_render_context_stencil_format.md) function returns and make sure it matches one of the values the [`cp_layer_renderer_capabilities_drawable_render_context_supported_stencil_format`](cp_layer_renderer_capabilities_drawable_render_context_supported_stencil_format.md) function returns.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/layerrendererconfigurationerror/unsupporteddrawablerendercontextstencilformat)*