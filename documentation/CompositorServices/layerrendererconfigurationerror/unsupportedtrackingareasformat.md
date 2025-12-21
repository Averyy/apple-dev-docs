# LayerRendererConfigurationError.unsupportedTrackingAreasFormat

**Framework**: Compositor Services  
**Kind**: case

An error that indicates the layer doesn’t support the current pixel format for tracking areas textures.

**Availability**:
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
case unsupportedTrackingAreasFormat
```

#### Discussion

Compare the value the [`cp_layer_renderer_configuration_get_tracking_areas_format`](cp_layer_renderer_configuration_get_tracking_areas_format.md) function returns and make sure it matches one of the values the [`cp_layer_renderer_capabilities_supported_tracking_areas_format`](cp_layer_renderer_capabilities_supported_tracking_areas_format.md) function returns.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/layerrendererconfigurationerror/unsupportedtrackingareasformat)*