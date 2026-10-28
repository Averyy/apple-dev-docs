# cp_layer_renderer_capabilities_supported_tracking_areas_format

**Framework**: Compositor Services  
**Kind**: func  
**Role**: Function

Returns the tracking areas format at the specified index in the layer capabilities.

**Availability**:
- macOS 26.0+
- visionOS 26.0+

## Declaration

```c
MTLPixelFormat cp_layer_renderer_capabilities_supported_tracking_areas_format(cp_layer_renderer_capabilities_t layer_capabilities, size_t index);
```

## Return Value

The pixel format at the specified index.

## Discussion

Use this function to determine what tracking areas texture formats the layer supports.

## Parameters

- `layer_capabilities`: The layer capabilities to query.
- `index`: A zero-based index into the list of index formats.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/cp_layer_renderer_capabilities_supported_tracking_areas_format)*