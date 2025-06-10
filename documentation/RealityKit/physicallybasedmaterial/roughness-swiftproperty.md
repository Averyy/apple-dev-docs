# roughness

**Framework**: RealityKit  
**Kind**: property

The amount the surface of the 3D object scatters reflected light.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+ (Beta)
- visionOS ?+

## Declaration

```swift
var roughness: PhysicallyBasedMaterial.Roughness { get set }
```

## Mentions

- [Applying realistic material and lighting effects to entities](applying-realistic-material-and-lighting-effects-to-entities.md)

#### Discussion

The `roughness` property represents how much the surface of the entity scatters light it reflects. A material with a high roughness has a matte appearance, while one with a low roughness has a shiny appearance.

![An illustration showing three spheres with different amounts of](https://docs-assets.developer.apple.com/published/6dccdd9884a6e12444a9f61c265d8644/PhysicallyBasedMaterial-roughness-swift-property-1%402x.png)

Specify this property using a [`Float`](https://developer.apple.com/documentation/Swift/Float) to represent a uniform `roughness` for the entire entity, or a UV-mapped grayscale image that uses shades of gray to represent the roughness of different parts of the entity. When using an image, black pixels represent areas that have a low roughness and appear shiny, while white represents areas that have a high roughness and display a matte finish.

If you initialize this property with a color image rather than a grayscale image, RealityKit only uses the intensity of the image’s red channel.

The following example uses a single value to specify roughness:

```swift
material.roughness = PhysicallyBasedMaterial.Roughness(floatLiteral: 0.0)
```

The following example uses an image to specify roughness:

```swift
if let roughnessResource = try? TextureResource.load(named:
"entity_roughness") {
    let roughness = MaterialParameters.Texture(roughnessResource)
    material.roughness = PhysicallyBasedMaterial.Roughness(texture:roughness)
}
```

## See Also

- [var baseColor: PhysicallyBasedMaterial.BaseColor](physicallybasedmaterial/basecolor-swift.property.md)
  The color of an entity unmodified by lighting.
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
- [var clearcoatNormal: PhysicallyBasedMaterial.ClearcoatNormal](physicallybasedmaterial/clearcoatnormal-swift.property.md)
  Waviness and imperfections for the top clearcoat.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/physicallybasedmaterial/roughness-swift.property)*