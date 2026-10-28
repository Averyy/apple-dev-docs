# cp_layer_renderer_capabilities_drawable_render_context_supported_stencil_format

**Framework**: Compositor Services  
**Kind**: func  
**Role**: Function

Returns the stencil format at the specified index in the layer capabilities.

**Availability**:
- macOS 26.0+
- visionOS 26.0+

## Declaration

```c
MTLPixelFormat cp_layer_renderer_capabilities_drawable_render_context_supported_stencil_format(cp_layer_renderer_capabilities_t layer_capabilities, size_t index);
```

## Return Value

The stencil format at the specified index.

## Discussion

Use this function to determine the pixel arrangements and characteristics you can apply to the layer.

## Parameters

- `layer_capabilities`: The layer capabilities to query.
- `index`: A zero-based index into the list of stencil formats.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/cp_layer_renderer_capabilities_drawable_render_context_supported_stencil_format)*