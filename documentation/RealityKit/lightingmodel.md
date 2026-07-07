# LightingModel

**Framework**: RealityKit  
**Kind**: enum

The lighting model used by a [`ShaderGraphMaterial.Program`](shadergraphmaterial/program-swift.struct.md).

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
enum LightingModel
```

#### Overview

This must match the type of the surface output node in the [`ShaderGraph`](shadergraph.md). For example, a graph whose surface node is a PBR surface shader requires `.lit`.

## Topics

### Creating a lit model
- [static func lit(diffuseModel: LitLightingModel.DiffuseModel, specularModel: LitLightingModel.SpecularModel, isSubsurfaceScatteringEnabled: Bool, isMultiscatteringEnabled: Bool, isBentNormalEnabled: Bool, isClearcoatEnabled: Bool) -> LightingModel](lightingmodel/lit(diffusemodel:specularmodel:issubsurfacescatteringenabled:ismultiscatteringenabled:isbentnormalenabled:isclearcoatenabled:).md)
- [case lit(LitLightingModel)](lightingmodel/lit(_:).md)
### Creating an unlit model
- [static func unlit(isTonemappingEnabled: Bool) -> LightingModel](lightingmodel/unlit(istonemappingenabled:).md)
- [case unlit(UnlitLightingModel)](lightingmodel/unlit(_:).md)
### Creating a hair model
- [static func hair() -> LightingModel](lightingmodel/hair.md)
- [case hair(HairLightingModel)](lightingmodel/hair(_:).md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct LitLightingModel](litlightingmodel.md)
  Configuration for RealityKit’s physically based lighting model.
- [struct UnlitLightingModel](unlitlightingmodel.md)
  Configuration for an unlit lighting model, which renders without any light interaction.
- [struct HairLightingModel](hairlightingmodel.md)
  Configuration for RealityKit’s hair lighting model.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lightingmodel)*