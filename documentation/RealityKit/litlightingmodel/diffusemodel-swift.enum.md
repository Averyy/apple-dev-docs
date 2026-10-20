# LitLightingModel.DiffuseModel

**Framework**: RealityKit  
**Kind**: enum  
**Role**: Enumeration

The diffuse lighting algorithm used in a [`LitLightingModel`](../litlightingmodel.md).

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
- [LitLightingModel.DiffuseModel.lambertian](./diffusemodel-swift.enum/lambertian.md)
  Lambertian diffuse, a simple and performant constant-factor model.
- [LitLightingModel.DiffuseModel.orenNayar](./diffusemodel-swift.enum/orennayar.md)
  Oren-Nayar diffuse, a roughness-aware model suited to matte surfaces.
- [LitLightingModel.DiffuseModel.hammon](./diffusemodel-swift.enum/hammon.md)
  Hammon diffuse, a physically based model that accounts for roughness.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Configuring shading models
- [var diffuseModel: LitLightingModel.DiffuseModel](./diffusemodel-swift.property.md)
  The diffuse algorithm to use.
- [var specularModel: LitLightingModel.SpecularModel](./specularmodel-swift.property.md)
  The specular algorithm to use.
- [LitLightingModel.SpecularModel](./specularmodel-swift.enum.md)
  The specular lighting algorithm used in a [`LitLightingModel`](../litlightingmodel.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/litlightingmodel/diffusemodel-swift.enum)*