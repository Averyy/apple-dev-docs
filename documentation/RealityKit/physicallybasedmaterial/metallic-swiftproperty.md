# metallic

**Framework**: RealityKit  
**Kind**: property

The reflectiveness of an entity.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS ?+

## Declaration

```swift
var metallic: PhysicallyBasedMaterial.Metallic { get set }
```

## Mentions

- [Applying realistic material and lighting effects to entities](applying-realistic-material-and-lighting-effects-to-entities.md)

#### Discussion

The `metallic` property represents the reflectiveness of an entity. Use this property to specify whether the entity displays metallic qualities and reflects the surrounding environment, or displays dielectric qualities and doesn’t reflect the environment.

![An illustration showing two spheres rendered in RealityKit. The sphere](https://docs-assets.developer.apple.com/published/905cfc9b323ae0c410a550342e2dc378/PhysicallyBasedMaterial-metallic-swift-property-1%402x.png)

Specify this property using a [`Float`](https://developer.apple.com/documentation/Swift/Float) to represent a uniform reflectiveness for the entire entity. You an also use a UV-mapped grayscale image to represent the reflectiveness of different parts of the entity. When using an image, black pixels represent areas that are dielectric, while white pixels represents areas that are completely metallic and reflective.

If you initialize this property with a color image, rather than a grayscale image, RealityKit only uses the intensity of the image’s red channel.

The following example specifies the metallic qualities of an entity using a single float value:

```swift
material.metallic = 1.0
```

The following example specifies the metallic qualities of an entity using a UV-mapped image:

```swift
// Load a texture resource from a file.
let metalResource = try TextureResource.load(named: "entity_metallic")

// Set the texture to the metallic property.
let metallic = MaterialParameters.Texture(metalResource)
material.metallic = PhysicallyBasedMaterial.Metallic(texture: metallic)
```

## See Also

- [var baseColor: PhysicallyBasedMaterial.BaseColor](physicallybasedmaterial/basecolor-swift.property.md)
  The color of an entity unmodified by lighting.
- [var roughness: PhysicallyBasedMaterial.Roughness](physicallybasedmaterial/roughness-swift.property.md)
  The amount the surface of the 3D object scatters reflected light.
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

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/physicallybasedmaterial/metallic-swift.property)*