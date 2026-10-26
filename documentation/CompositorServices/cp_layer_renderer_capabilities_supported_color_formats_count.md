# cp_layer_renderer_capabilities_supported_color_formats_count

**Framework**: Compositor Services  
**Kind**: func  
**Role**: Function

Returns the number of color formats the layer supports.

**Availability**:
- visionOS 1.0+

## Declaration

```c
size_t cp_layer_renderer_capabilities_supported_color_formats_count(cp_layer_renderer_capabilities_t layer_capabilities);
```

#### Return Value

The number of color formats the layer supports.

#### Discussion

To iterate over the color formats, use the [`cp_layer_renderer_capabilities_supported_color_format`](./cp_layer_renderer_capabilities_supported_color_format.md) function.

## Parameters

- `layer_capabilities`: The layer capabilities to query.

## See Also

### Getting the supported color formats
- [cp_layer_renderer_capabilities_supported_color_format](./cp_layer_renderer_capabilities_supported_color_format.md)
  Returns the color format at the specified index in the layer capabilities.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/cp_layer_renderer_capabilities_supported_color_formats_count)*