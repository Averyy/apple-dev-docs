# cp_layer_renderer_capabilities_supported_color_formats_count_with_options

**Framework**: Compositor Services  
**Kind**: func  
**Role**: Function

Returns the number of color formats the specified layer supports.

**Availability**:
- macOS 26.0+
- visionOS 26.0+

## Declaration

```c
size_t cp_layer_renderer_capabilities_supported_color_formats_count_with_options(cp_layer_renderer_capabilities_t layer_capabilities, cp_supported_color_formats_options options);
```

#### Return Value

The number of color formats the layer supports.

#### Discussion

To iterate over the color formats, use the [`cp_layer_renderer_capabilities_supported_color_format`](./cp_layer_renderer_capabilities_supported_color_format.md) function.

## Parameters

- `layer_capabilities`: The layer capabilities to query.
- `options`: The options to consider when creating the list of supported color formats.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/cp_layer_renderer_capabilities_supported_color_formats_count_with_options)*