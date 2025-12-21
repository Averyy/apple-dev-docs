# specular

**Framework**: RealityKit  
**Kind**: property

The specular highlight applied to the entity.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+
- visionOS ?+

## Declaration

```swift
var specular: PhysicallyBasedMaterial.Specular { get set }
```

## Mentions

- [Applying realistic material and lighting effects to entities](applying-realistic-material-and-lighting-effects-to-entities.md)

#### Discussion

In Physically Based Rendering (PBR), specular highlights primarily come from the object’s [`roughness`](physicallybasedmaterial/roughness-swift.property.md) value. RealityKit automatically renders materials that have a low roughness value with specular highlights based on the environment lighting and the shape of the entity. As a result, for most materials, you won’t need to specify a `specular` value when using [`PhysicallyBasedMaterial`](physicallybasedmaterial.md).

For some types of dielectric (nonmetallic) materials, like facet-cut glass or gems, PBR algorithms don’t create bright enough specular highlights using just roughness. To accurately simulate those types of materials, use the [`specular`](physicallybasedmaterial/specular-swift.property.md) property to specify additional specular for the entity.

The following example demonstrates how to specify specular using a single value for the entire material:

```swift
material.specular = .init(floatLiteral: 0.8)
```

This example shows how to specify specular using a UV-mapped image texture:

```swift
if let specularResource = try? TextureResource.load(named:"entity_specular") {
    let specularMap = MaterialParameters.Texture(specularResource)
    material.specular = .init(texture: specularMap)
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
- [var clearcoat: PhysicallyBasedMaterial.Clearcoat](physicallybasedmaterial/clearcoat-swift.property.md)
  The transparent highlights that simulate a clear, shiny coating on an entity.
- [var clearcoatRoughness: PhysicallyBasedMaterial.ClearcoatRoughness](physicallybasedmaterial/clearcoatroughness-swift.property.md)
  The degree to which an entity’s clear, shiny coating scatters light to create soft highlights.
- [var clearcoatNormal: PhysicallyBasedMaterial.ClearcoatNormal](physicallybasedmaterial/clearcoatnormal-swift.property.md)
  Waviness and imperfections for the top clearcoat.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/physicallybasedmaterial/specular-swift.property)*