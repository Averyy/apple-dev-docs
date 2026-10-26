# cp_layer_renderer_capabilities_supported_tracking_areas_formats_count

**Framework**: Compositor Services  
**Kind**: func  
**Role**: Function

Returns the number of tracking areas formats the specified layer supports.

**Availability**:
- macOS 26.0+
- visionOS 26.0+

## Declaration

```c
size_t cp_layer_renderer_capabilities_supported_tracking_areas_formats_count(cp_layer_renderer_capabilities_t layer_capabilities);
```

#### Return Value

The number of tracking areas formats the layer supports.

#### Discussion

To iterate over the index formats, use the [`cp_layer_renderer_capabilities_supported_tracking_areas_format`](./cp_layer_renderer_capabilities_supported_tracking_areas_format.md) function.

## Parameters

- `layer_capabilities`: The layer capabilities to query.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/cp_layer_renderer_capabilities_supported_tracking_areas_formats_count)*