# LightingModel

**Framework**: RealityKit  
**Kind**: enum  
**Role**: Enumeration

The lighting model used by a [`ShaderGraphMaterial.Program`](./shadergraphmaterial/program-swift.struct.md).

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
enum LightingModel
```

#### Overview

This must match the type of the surface output node in the [`ShaderGraph`](./shadergraph.md). For example, a graph whose surface node is a PBR surface shader requires `.lit`.

## Topics

### Creating a lit model
- [static func lit(diffuseModel: LitLightingModel.DiffuseModel, specularModel: LitLightingModel.SpecularModel, isSubsurfaceScatteringEnabled: Bool, isMultiscatteringEnabled: Bool, isBentNormalEnabled: Bool, isClearcoatEnabled: Bool) -> LightingModel](./lightingmodel/lit%28diffusemodel,specularmodel,issubsurfacescatteringenabled,ismultiscatteringenabled,isbentnormalenabled,isclearcoatenabled%29.md)
- [case lit(LitLightingModel)](./lightingmodel/lit%28_%29.md)
### Creating an unlit model
- [static func unlit(isTonemappingEnabled: Bool) -> LightingModel](./lightingmodel/unlit%28istonemappingenabled%29.md)
- [case unlit(UnlitLightingModel)](./lightingmodel/unlit%28_%29.md)
### Creating a hair model
- [static func hair() -> LightingModel](./lightingmodel/hair%28%29.md)
- [case hair(HairLightingModel)](./lightingmodel/hair%28_%29.md)

## Relationships

### Conforms To
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Lighting models
- [struct LitLightingModel](./litlightingmodel.md)
  Configuration for RealityKit’s physically based lighting model.
- [struct UnlitLightingModel](./unlitlightingmodel.md)
  Configuration for an unlit lighting model, which renders without any light interaction.
- [struct HairLightingModel](./hairlightingmodel.md)
  Configuration for RealityKit’s hair lighting model.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lightingmodel)*