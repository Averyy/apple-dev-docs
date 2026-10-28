# cp_layer_renderer_configuration_error_code_unsupported_drawable_render_context_stencil_format

**Framework**: Compositor Services  
**Kind**: case  
**Role**: Enumeration Case

An error that indicates the layer doesn’t support the current pixel format for stencil texture.

**Availability**:
- macOS 26.0+
- visionOS 26.0+

## Declaration

```c
cp_layer_renderer_configuration_error_code_unsupported_drawable_render_context_stencil_format
```

## Discussion

Compare the value the [`cp_layer_renderer_configuration_get_drawable_render_context_stencil_format`](../cp_layer_renderer_configuration_get_drawable_render_context_stencil_format.md) function returns and make sure it matches one of the values the [`cp_layer_renderer_capabilities_drawable_render_context_supported_stencil_format`](../cp_layer_renderer_capabilities_drawable_render_context_supported_stencil_format.md) function returns.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/cp_layer_renderer_configuration_error_code/cp_layer_renderer_configuration_error_code_unsupported_drawable_render_context_stencil_format)*