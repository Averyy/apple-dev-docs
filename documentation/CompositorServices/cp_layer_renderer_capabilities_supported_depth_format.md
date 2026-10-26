# cp_layer_renderer_capabilities_supported_depth_format

**Framework**: Compositor Services  
**Kind**: func  
**Role**: Function

Returns the depth format at the specified index in the layer capabilities.

**Availability**:
- macOS 26.0+
- visionOS 1.0+

## Declaration

```c
MTLPixelFormat cp_layer_renderer_capabilities_supported_depth_format(cp_layer_renderer_capabilities_t layer_capabilities, size_t index);
```

#### Return Value

The depth format at the specified index.

#### Discussion

This function tells you which pixel arrangements and characteristics the layer supports for its depth textures.

## Parameters

- `layer_capabilities`: The layer capabilities to query.
- `index`: A zero-based index into the list of supported depth formats. This index must be less than the value the [`cp_layer_renderer_capabilities_supported_depth_formats_count`](./cp_layer_renderer_capabilities_supported_depth_formats_count.md) function returns.

## See Also

### Getting the supported depth formats
- [cp_layer_renderer_capabilities_supported_depth_formats_count](./cp_layer_renderer_capabilities_supported_depth_formats_count.md)
  Returns the number of depth formats the layer supports.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/cp_layer_renderer_capabilities_supported_depth_format)*