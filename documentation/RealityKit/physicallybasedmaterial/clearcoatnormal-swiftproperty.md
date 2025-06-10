# clearcoatNormal

**Framework**: RealityKit  
**Kind**: property

Waviness and imperfections for the top clearcoat.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS ?+
- visionOS 2.0+

## Declaration

```swift
var clearcoatNormal: PhysicallyBasedMaterial.ClearcoatNormal { get set }
```

#### Discussion

An entity in RealityKit can display a clearcoat, which is a separate layer of transparent specular highlights used to simulate a clear coating, like on a car or the surface of lacquered objects. This property allows you to specify a clearcoat normal and add waviness and imperfections to the top clearcoat.

To use clearcoat rendering, set `clearcoat` to a value greater than `0.0`.

This example shows how to set the `clearcoatNormal` using a UV-mapped image:

```swift
if let clearcoatNormalTextureResource = try?
TextureResource.load(named: "entity_cc_normalMap") {
    let ccNormalMap = MaterialParameters.Texture(clearcoatNormalTextureResource)
    material.clearcoatNormal = .init(texture: ccNormalMap)
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
- [var clearcoatRoughness: PhysicallyBasedMaterial.ClearcoatRoughness](physicallybasedmaterial/clearcoatroughness-swift.property.md)
  The degree to which an entity’s clear, shiny coating scatters light to create soft highlights.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/physicallybasedmaterial/clearcoatnormal-swift.property)*