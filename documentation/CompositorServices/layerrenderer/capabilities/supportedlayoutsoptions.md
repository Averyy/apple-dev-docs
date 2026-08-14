# LayerRenderer.Capabilities.SupportedLayoutsOptions

**Framework**: Compositor Services  
**Kind**: struct

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
- [static let foveationEnabled: LayerRenderer.Capabilities.SupportedLayoutsOptions](layerrenderer/capabilities/supportedlayoutsoptions/foveationenabled.md)
  An option to request a layout that supports foveated rendering.
### Type Properties
- [static let progressiveImmersionEnabled: LayerRenderer.Capabilities.SupportedLayoutsOptions](layerrenderer/capabilities/supportedlayoutsoptions/progressiveimmersionenabled.md)

## Relationships

### Conforms To
- [Equatable](../swift/equatable.md)
- [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md)
- [OptionSet](../swift/optionset.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [SetAlgebra](../swift/setalgebra.md)

## See Also

- [func supportedLayouts(options: LayerRenderer.Capabilities.SupportedLayoutsOptions) -> [LayerRenderer.Layout]](layerrenderer/capabilities/supportedlayouts(options:).md)
  Returns an array of texture layouts that the layer supports.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/layerrenderer/capabilities/supportedlayoutsoptions)*