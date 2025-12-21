# clearcoatRoughness

**Framework**: RealityKit  
**Kind**: property

The degree to which an entity’s clear, shiny coating scatters light to create soft highlights.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+
- visionOS ?+

## Declaration

```swift
var clearcoatRoughness: PhysicallyBasedMaterial.ClearcoatRoughness { get set }
```

#### Discussion

When you enable clearcoat rendering for a material, RealityKit renders the clearcoat as a separate layer just above the surface of the entity. You can specify a clearcoat roughness value for the clearcoat to indicate how much the clearcoat scatters light that bounces off of it, which softens and spreads out the highlights.

You can specify a single value that applies to the entire material, or you can supply a UV-mapped image texture containing different roughness values for different parts of the entity.

The following example sets the `clearcoatRoughness` using a single value:

```swift
material.clearcoatRoughness = .init(floatLiteral: 0.5)
```

This example shows how to set the `clearcoatRoughness` using a UV-mapped image:

```swift
if let clearcoatRoughnessResource = try?
TextureResource.load(named: "entity_cc_roughness") {
    let ccRoughnessMap = MaterialParameters.Texture(clearcoatRoughnessResource)
    material.clearcoat = .init(texture: ccRoughnessMap)
}
```

## See Also

- [var baseColor: PhysicallyBasedMaterial.BaseColor](physicallybasedmaterial/basecolor-swift.property.md)
  The color of an entity unmodified by lighting.
- [var roughness: PhysicallyBasedMaterial.Roughness](physicallybasedmaterial/roughness-swift.property.md)
  The amount the surface of the 3D object scatters reflected light.
- [var metallic: PhysicallyBasedMaterial.Metallic](physicallybasedmaterial/metallic-swift.property.md)
  The reflectiveness of an entity.
- [var normal: PhysicallyBasedMaterial.Normal](physicallybasedmaterial/normal-swift.property.md)
  The normal map for the entity.
- [var ambientOcclusion: PhysicallyBasedMaterial.AmbientOcclusion](physicallybasedmaterial/ambientocclusion-swift.property.md)
  The ambient occlusion values for a material.
- [var specular: PhysicallyBasedMaterial.Specular](physicallybasedmaterial/specular-swift.property.md)
  The specular highlight applied to the entity.
- [var clearcoat: PhysicallyBasedMaterial.Clearcoat](physicallybasedmaterial/clearcoat-swift.property.md)
  The transparent highlights that simulate a clear, shiny coating on an entity.
- [var clearcoatNormal: PhysicallyBasedMaterial.ClearcoatNormal](physicallybasedmaterial/clearcoatnormal-swift.property.md)
  Waviness and imperfections for the top clearcoat.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/physicallybasedmaterial/clearcoatroughness-swift.property)*