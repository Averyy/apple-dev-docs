# LayerRendererConfigurationError.unsupportedDrawableRenderContextStencilFormat

**Framework**: Compositor Services  
**Kind**: case

An error that indicates the layer doesn’t support the current pixel format for the stencil texture.

**Availability**:
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
case unsupportedDrawableRenderContextStencilFormat
```

#### Discussion

Compare the value that the [`cp_layer_renderer_configuration_get_drawable_render_context_stencil_format`](cp_layer_renderer_configuration_get_drawable_render_context_stencil_format.md) function returns and make sure it matches one of the values that the [`cp_layer_renderer_capabilities_drawable_render_context_supported_stencil_format`](cp_layer_renderer_capabilities_drawable_render_context_supported_stencil_format.md) function returns.

## See Also

- [LayerRendererConfigurationError.layoutNotSupported](layerrendererconfigurationerror/layoutnotsupported.md)
  An error that indicates the configuration’s current layout value is invalid.
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
- [LayerRendererConfigurationError.unsupportedRenderQuality](layerrendererconfigurationerror/unsupportedrenderquality.md)
  An error that indicates the configuration’s render quality is unsupported. This could be because foveation is disabled or the quality is outside of the valid range of [0, 1], the error `userInfo` will contain additional information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/layerrendererconfigurationerror/unsupporteddrawablerendercontextstencilformat)*