# LayerRendererConfigurationError.unsupportedTrackingAreasUsage

**Framework**: Compositor Services  
**Kind**: case

An error that indicates the layer doesn’t support the current texture usage for tracking areas textures.

**Availability**:
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
case unsupportedTrackingAreasUsage
```

#### Discussion

Compare the value the [`cp_layer_renderer_configuration_get_tracking_areas_usage`](cp_layer_renderer_configuration_get_tracking_areas_usage.md) function returns and make sure it has at least `MTLTextureUsageShaderRead` and does not contain `MTLTextureUsageShaderAtomic`


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/layerrendererconfigurationerror/unsupportedtrackingareasusage)*