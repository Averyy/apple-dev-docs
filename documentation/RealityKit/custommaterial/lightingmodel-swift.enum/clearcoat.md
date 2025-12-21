# CustomMaterial.LightingModel.clearcoat

**Framework**: RealityKit  
**Kind**: case

The entity renders using physically based rendering techniques with a clearcoat.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+

## Declaration

```swift
case clearcoat
```

#### Discussion

A custom material using the [`CustomMaterial.LightingModel.clearcoat`](custommaterial/lightingmodel-swift.enum/clearcoat.md) lighting model uses physically based rendering, including a clearcoat if the material’s surface shader calls `params.surface().set_clearcoat()`.

## See Also

- [CustomMaterial.LightingModel.lit](custommaterial/lightingmodel-swift.enum/lit.md)
  The entity renders using physically based rendering techniques without a clearcoat.
- [CustomMaterial.LightingModel.unlit](custommaterial/lightingmodel-swift.enum/unlit.md)
  The entity renders with no light or shadow calculations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/custommaterial/lightingmodel-swift.enum/clearcoat)*