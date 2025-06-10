# ambientOcclusion

**Framework**: RealityKit  
**Kind**: property

The ambient occlusion values for a material.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+ (Beta)
- visionOS ?+

## Declaration

```swift
var ambientOcclusion: PhysicallyBasedMaterial.AmbientOcclusion { get set }
```

#### Discussion

Ambient occlusion represents the entity’s exposure to ambient light.

Specify ambient occlusion using a UV-mapped image called an . A value of black (`0.0`) represents parts of the model that receive less ambient light because that part of the model is a crevice, dent, or recessed area, or because another part of the same entity is preventing ambient light from reaching it. Ambient occlusion values of white (`1.0`) represent flat portions of the model that receive full ambient light. You generate ambient occlusion maps using a 3D software package.

The following code loads an ambient occlusion map:

```swift if let aoResource = try? TextureResource.load(named:
"entity_ao") {
    let aoMap = MaterialParameters.Texture(aoResource)
    material.emissiveColor = .init(texture: aoMap)
} ```
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
- [var specular: PhysicallyBasedMaterial.Specular](physicallybasedmaterial/specular-swift.property.md)
  The specular highlight applied to the entity.
- [var clearcoat: PhysicallyBasedMaterial.Clearcoat](physicallybasedmaterial/clearcoat-swift.property.md)
  The transparent highlights that simulate a clear, shiny coating on an entity.
- [var clearcoatRoughness: PhysicallyBasedMaterial.ClearcoatRoughness](physicallybasedmaterial/clearcoatroughness-swift.property.md)
  The degree to which an entity’s clear, shiny coating scatters light to create soft highlights.
- [var clearcoatNormal: PhysicallyBasedMaterial.ClearcoatNormal](physicallybasedmaterial/clearcoatnormal-swift.property.md)
  Waviness and imperfections for the top clearcoat.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/physicallybasedmaterial/ambientocclusion-swift.property)*