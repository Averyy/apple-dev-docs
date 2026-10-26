# cp_layer_renderer_capabilities_drawable_render_context_supported_stencil_formats_count

**Framework**: Compositor Services  
**Kind**: func  
**Role**: Function

Returns the number of stencil formats the specified layer supports.

**Availability**:
- macOS 26.0+
- visionOS 26.0+

## Declaration

```c
size_t cp_layer_renderer_capabilities_drawable_render_context_supported_stencil_formats_count(cp_layer_renderer_capabilities_t layer_capabilities);
```

#### Return Value

The number of stencil formats the layer supports.

#### Discussion

To iterate over the stencil formats, use the [`cp_layer_renderer_capabilities_drawable_render_context_supported_stencil_format`](./cp_layer_renderer_capabilities_drawable_render_context_supported_stencil_format.md) function.

## Parameters

- `layer_capabilities`: The layer capabilities to query.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/cp_layer_renderer_capabilities_drawable_render_context_supported_stencil_formats_count)*