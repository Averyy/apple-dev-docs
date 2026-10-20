# LayerRendererConfigurationError.variableRasterizationRateIsNotSupported

**Framework**: Compositor Services  
**Kind**: case  
**Role**: Case

An error that indicates foveation is enabled but not supported.

**Availability**:
- macOS 26.0+
- visionOS 1.0+

## Declaration

```swift
case variableRasterizationRateIsNotSupported
```

#### Discussion

Disable foveation in your layer’s configuration.

## See Also

### Getting the configuration errors
- [LayerRendererConfigurationError.layoutNotSupported](./layoutnotsupported.md)
  An error that indicates the configuration’s current layout value is invalid.
- [LayerRendererConfigurationError.missingConfiguration](./missingconfiguration.md)
  An error that indicates the system didn’t find a default layer configuration.
- [LayerRendererConfigurationError.notEnoughFramesRequested](./notenoughframesrequested.md)
  An error that indicates not enough frames are available for rendering.
- [LayerRendererConfigurationError.temporalAntiAliasingNotSupported](./temporalantialiasingnotsupported.md)
  An error that occurs when you try to enable temporal anti-aliasing but the current configuration parameters don’t support it.
- [LayerRendererConfigurationError.tooManyFramesRequested](./toomanyframesrequested.md)
  An error that indicates your app requested too many frames for rendering.
- [LayerRendererConfigurationError.unsupportedForwardDepthRange](./unsupportedforwarddepthrange.md)
  An error that indicates the depth range values aren’t in reverse-z order.
- [LayerRendererConfigurationError.unsupportedNearPlaneDistance](./unsupportednearplanedistance.md)
  An error that indicates the near plane of the client is closer than the minimum supported distance.
- [LayerRendererConfigurationError.unsupportedColorFormat](./unsupportedcolorformat.md)
  An error that indicates the system doesn’t support the specified color format choice.
- [LayerRendererConfigurationError.unsupportedColorUsage](./unsupportedcolorusage.md)
  An error that indicates the system doesn’t support the specified color usage option.
- [LayerRendererConfigurationError.unsupportedDepthFormat](./unsupporteddepthformat.md)
  An error that indicates the system doesn’t support the specified depth format choice.
- [LayerRendererConfigurationError.unsupportedDepthUsage](./unsupporteddepthusage.md)
  An error that indicates the system doesn’t support the specified depth usage choice.
- [LayerRendererConfigurationError.unsupportedDrawableRenderContextStencilFormat](./unsupporteddrawablerendercontextstencilformat.md)
  An error that indicates the layer doesn’t support the current pixel format for the stencil texture.
- [LayerRendererConfigurationError.unsupportedRenderQuality](./unsupportedrenderquality.md)
  An error that indicates the configuration’s render quality is unsupported. This could be because foveation is disabled or the quality is outside of the valid range of [0, 1], the error `userInfo` will contain additional information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/layerrendererconfigurationerror/variablerasterizationrateisnotsupported)*