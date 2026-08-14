# LitLightingModel

**Framework**: RealityKit  
**Kind**: struct

Configuration for RealityKit’s physically based lighting model.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct LitLightingModel
```

## Topics

### Configuring shading models
- [var diffuseModel: LitLightingModel.DiffuseModel](litlightingmodel/diffusemodel-swift.property.md)
  The diffuse algorithm to use.
- [LitLightingModel.DiffuseModel](litlightingmodel/diffusemodel-swift.enum.md)
  The diffuse lighting algorithm used in a [`LitLightingModel`](litlightingmodel.md).
- [var specularModel: LitLightingModel.SpecularModel](litlightingmodel/specularmodel-swift.property.md)
  The specular algorithm to use.
- [LitLightingModel.SpecularModel](litlightingmodel/specularmodel-swift.enum.md)
  The specular lighting algorithm used in a [`LitLightingModel`](litlightingmodel.md).
### Enabling lighting features
- [var isSubsurfaceScatteringEnabled: Bool](litlightingmodel/issubsurfacescatteringenabled.md)
  Whether to include subsurface scattering in the lighting calculation.
- [var isClearcoatEnabled: Bool](litlightingmodel/isclearcoatenabled.md)
  Whether to include a clearcoat layer in the lighting calculation.
- [var isMultiscatteringEnabled: Bool](litlightingmodel/ismultiscatteringenabled.md)
  Whether to account for multiple scattering between microfacets.
- [var isBentNormalEnabled: Bool](litlightingmodel/isbentnormalenabled.md)
  Whether to apply bent normal maps to improve ambient occlusion accuracy.
### Initializers
- [init()](litlightingmodel/init.md)

## Relationships

### Conforms To
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [enum LightingModel](lightingmodel.md)
  The lighting model used by a [`ShaderGraphMaterial.Program`](shadergraphmaterial/program-swift.struct.md).
- [struct UnlitLightingModel](unlitlightingmodel.md)
  Configuration for an unlit lighting model, which renders without any light interaction.
- [struct HairLightingModel](hairlightingmodel.md)
  Configuration for RealityKit’s hair lighting model.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/litlightingmodel)*