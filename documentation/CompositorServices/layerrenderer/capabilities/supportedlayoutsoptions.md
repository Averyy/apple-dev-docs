# LayerRenderer.Capabilities.SupportedLayoutsOptions

**Framework**: Compositor Services  
**Kind**: struct  
**Role**: Structure

Options you can use to filter the supported layouts for a layer.

**Availability**:
- macOS 26.0+
- visionOS 1.0+

## Declaration

```swift
struct SupportedLayoutsOptions
```

## Topics

### Getting the options
- [static let foveationEnabled: LayerRenderer.Capabilities.SupportedLayoutsOptions](./supportedlayoutsoptions/foveationenabled.md)
  An option to request a layout that supports foveated rendering.
### Type Properties
- [static let progressiveImmersionEnabled: LayerRenderer.Capabilities.SupportedLayoutsOptions](./supportedlayoutsoptions/progressiveimmersionenabled.md)

## Relationships

### Conforms To
- [Equatable](../../../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../../../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../../../Swift/optionset.md)
- [RawRepresentable](../../../Swift/rawrepresentable.md)
- [SetAlgebra](../../../Swift/setalgebra.md)

## See Also

### Getting the supported layouts
- [func supportedLayouts(options: LayerRenderer.Capabilities.SupportedLayoutsOptions) -> [LayerRenderer.Layout]](./supportedlayouts%28options%29.md)
  Returns an array of texture layouts that the layer supports.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/layerrenderer/capabilities/supportedlayoutsoptions)*