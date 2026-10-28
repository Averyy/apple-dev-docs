# cp_layer_renderer_capabilities_supported_color_format_with_options

**Framework**: Compositor Services  
**Kind**: func  
**Role**: Function

Returns the color format at the specified index in the layer capabilities.

**Availability**:
- macOS 26.0+
- visionOS 26.0+

## Declaration

```c
MTLPixelFormat cp_layer_renderer_capabilities_supported_color_format_with_options(cp_layer_renderer_capabilities_t layer_capabilities, cp_supported_color_formats_options options, size_t index);
```

## Return Value

The color format at the specified index.

## Discussion

Use this function to determine the pixel arrangements and characteristics you can apply to the layer.

## Parameters

- `layer_capabilities`: The layer capabilities to query.
- `options`: The options to consider when creating the list of supported color formats.
- `index`: A zero-based index into the list of color formats.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/cp_layer_renderer_capabilities_supported_color_format_with_options)*