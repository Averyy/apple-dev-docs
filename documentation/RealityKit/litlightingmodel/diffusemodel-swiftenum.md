# LitLightingModel.DiffuseModel

**Framework**: RealityKit  
**Kind**: enum

The diffuse lighting algorithm used in a [`LitLightingModel`](litlightingmodel.md).

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
enum DiffuseModel
```

## Topics

### Choosing a diffuse model
- [LitLightingModel.DiffuseModel.lambertian](litlightingmodel/diffusemodel-swift.enum/lambertian.md)
  Lambertian diffuse, a simple and performant constant-factor model.
- [LitLightingModel.DiffuseModel.orenNayar](litlightingmodel/diffusemodel-swift.enum/orennayar.md)
  Oren-Nayar diffuse, a roughness-aware model suited to matte surfaces.
- [LitLightingModel.DiffuseModel.hammon](litlightingmodel/diffusemodel-swift.enum/hammon.md)
  Hammon diffuse, a physically based model that accounts for roughness.

## Relationships

### Conforms To
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [var diffuseModel: LitLightingModel.DiffuseModel](litlightingmodel/diffusemodel-swift.property.md)
  The diffuse algorithm to use.
- [var specularModel: LitLightingModel.SpecularModel](litlightingmodel/specularmodel-swift.property.md)
  The specular algorithm to use.
- [LitLightingModel.SpecularModel](litlightingmodel/specularmodel-swift.enum.md)
  The specular lighting algorithm used in a [`LitLightingModel`](litlightingmodel.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/litlightingmodel/diffusemodel-swift.enum)*