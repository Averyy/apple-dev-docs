# cp_layer_renderer_capabilities_supported_color_format

**Framework**: Compositor Services  
**Kind**: func  
**Role**: Function

Returns the color format at the specified index in the layer capabilities.

**Availability**:
- visionOS 1.0+

## Declaration

```c
MTLPixelFormat cp_layer_renderer_capabilities_supported_color_format(cp_layer_renderer_capabilities_t layer_capabilities, size_t index);
```

## Return Value

The color format at the specified index.

## Discussion

This function tells you which pixel arrangements and characteristics the layer supports for its color textures.

## Parameters

- `layer_capabilities`: The layer capabilities to query.
- `index`: A zero-based index into the list of supported color formats. This index must be less than the value returned by the [`cp_layer_renderer_capabilities_supported_color_formats_count`](./cp_layer_renderer_capabilities_supported_color_formats_count.md) function.

## See Also

### Getting the supported color formats
- [cp_layer_renderer_capabilities_supported_color_formats_count](./cp_layer_renderer_capabilities_supported_color_formats_count.md)
  Returns the number of color formats the layer supports.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/cp_layer_renderer_capabilities_supported_color_format)*