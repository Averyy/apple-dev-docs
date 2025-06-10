# CustomMaterial.LightingModel.lit

**Framework**: RealityKit  
**Kind**: case

The entity renders using physically based rendering techniques without a clearcoat.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+ (Beta)

## Declaration

```swift
case lit
```

#### Discussion

A custom material using the [`CustomMaterial.LightingModel.lit`](custommaterial/lightingmodel-swift.enum/lit.md) lighting model uses physically based rendering techniques, but doesn’t render a clearcoat. If a [`CustomMaterial.LightingModel.lit`](custommaterial/lightingmodel-swift.enum/lit.md) material’s surface shader calls `params.surface().set_clearcoat()` or `params.surface().set_clearcoat_roughness(),` ReallityKit ignores it.

## See Also

- [CustomMaterial.LightingModel.clearcoat](custommaterial/lightingmodel-swift.enum/clearcoat.md)
  The entity renders using physically based rendering techniques with a clearcoat.
- [CustomMaterial.LightingModel.unlit](custommaterial/lightingmodel-swift.enum/unlit.md)
  The entity renders with no light or shadow calculations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/custommaterial/lightingmodel-swift.enum/lit)*