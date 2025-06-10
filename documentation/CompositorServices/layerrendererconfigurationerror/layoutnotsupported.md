# LayerRendererConfigurationError.layoutNotSupported

**Framework**: Compositor Services  
**Kind**: case

An error that indicates the configuration’s current layout value is invalid.

**Availability**:
- macOS 26.0+ (Beta)
- visionOS 1.0+

## Declaration

```swift
case layoutNotSupported
```

#### Discussion

Specify a supported layout value using the [`layout`](layerrenderer/configuration-swift.struct/layout.md) property. Get a list of supported layouts from the [`supportedLayouts(options:)`](layerrenderer/capabilities/supportedlayouts(options:).md) function.

## See Also

- [LayerRendererConfigurationError.missingConfiguration](layerrendererconfigurationerror/missingconfiguration.md)
  An error that indicates the system didn’t find a default layer configuration.
- [LayerRendererConfigurationError.notEnoughFramesRequested](layerrendererconfigurationerror/notenoughframesrequested.md)
  An error that indicates not enough frames are available for rendering.
- [LayerRendererConfigurationError.temporalAntiAliasingNotSupported](layerrendererconfigurationerror/temporalantialiasingnotsupported.md)
  An error that occurs when you try to enable temporal anti-aliasing but the current configuration parameters don’t support it.
- [LayerRendererConfigurationError.tooManyFramesRequested](layerrendererconfigurationerror/toomanyframesrequested.md)
  An error that indicates your app requested too many frames for rendering.
- [LayerRendererConfigurationError.unsupportedForwardDepthRange](layerrendererconfigurationerror/unsupportedforwarddepthrange.md)
  An error that indicates the depth range values aren’t in reverse-z order.
- [LayerRendererConfigurationError.unsupportedNearPlaneDistance](layerrendererconfigurationerror/unsupportednearplanedistance.md)
  An error that indicates the near plane of the client is closer than the minimum supported distance.
- [LayerRendererConfigurationError.variableRasterizationRateIsNotSupported](layerrendererconfigurationerror/variablerasterizationrateisnotsupported.md)
  An error that indicates foveation is enabled but not supported.
- [LayerRendererConfigurationError.unsupportedColorFormat](layerrendererconfigurationerror/unsupportedcolorformat.md)
  An error that indicates the system doesn’t support the specified color format choice.
- [LayerRendererConfigurationError.unsupportedColorUsage](layerrendererconfigurationerror/unsupportedcolorusage.md)
  An error that indicates the system doesn’t support the specified color usage option.
- [LayerRendererConfigurationError.unsupportedDepthFormat](layerrendererconfigurationerror/unsupporteddepthformat.md)
  An error that indicates the system doesn’t support the specified depth format choice.
- [LayerRendererConfigurationError.unsupportedDepthUsage](layerrendererconfigurationerror/unsupporteddepthusage.md)
  An error that indicates the system doesn’t support the specified depth usage choice.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/layerrendererconfigurationerror/layoutnotsupported)*