# cp_layer_renderer_capabilities_supported_depth_formats_count

**Framework**: Compositor Services  
**Kind**: func  
**Role**: Function

Returns the number of depth formats the layer supports.

**Availability**:
- macOS 26.0+
- visionOS 1.0+

## Declaration

```c
size_t cp_layer_renderer_capabilities_supported_depth_formats_count(cp_layer_renderer_capabilities_t layer_capabilities);
```

#### Return Value

The number of depth formats the layer supports.

#### Discussion

To iterate over the depth formats, use the [`cp_layer_renderer_capabilities_supported_depth_format`](./cp_layer_renderer_capabilities_supported_depth_format.md) function.

## Parameters

- `layer_capabilities`: The layer capabilities to query.

## See Also

### Getting the supported depth formats
- [cp_layer_renderer_capabilities_supported_depth_format](./cp_layer_renderer_capabilities_supported_depth_format.md)
  Returns the depth format at the specified index in the layer capabilities.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/cp_layer_renderer_capabilities_supported_depth_formats_count)*