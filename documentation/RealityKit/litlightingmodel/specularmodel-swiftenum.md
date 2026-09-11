# LitLightingModel.SpecularModel

**Framework**: RealityKit  
**Kind**: enum

The specular lighting algorithm used in a [`LitLightingModel`](litlightingmodel.md).

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
enum SpecularModel
```

## Topics

### Choosing a specular model
- [LitLightingModel.SpecularModel.ggx](litlightingmodel/specularmodel-swift.enum/ggx.md)
  GGX (Trowbridge-Reitz) specular, a physically based microfacet model.
- [LitLightingModel.SpecularModel.anisotropicGGX](litlightingmodel/specularmodel-swift.enum/anisotropicggx.md)
  Anisotropic GGX specular, for surfaces with directional highlight variation such as brushed metal.
- [LitLightingModel.SpecularModel.blinnPhong](litlightingmodel/specularmodel-swift.enum/blinnphong.md)
  Blinn-Phong specular, a simple and performant approximation.
- [LitLightingModel.SpecularModel.sheen](litlightingmodel/specularmodel-swift.enum/sheen.md)
  Sheen specular, designed for cloth and fabric surfaces.

## Relationships

### Conforms To
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [var diffuseModel: LitLightingModel.DiffuseModel](litlightingmodel/diffusemodel-swift.property.md)
  The diffuse algorithm to use.
- [LitLightingModel.DiffuseModel](litlightingmodel/diffusemodel-swift.enum.md)
  The diffuse lighting algorithm used in a [`LitLightingModel`](litlightingmodel.md).
- [var specularModel: LitLightingModel.SpecularModel](litlightingmodel/specularmodel-swift.property.md)
  The specular algorithm to use.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/litlightingmodel/specularmodel-swift.enum)*