# baseColor

**Framework**: RealityKit  
**Kind**: property

The color of an entity unmodified by lighting.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS ?+

## Declaration

```swift
var baseColor: PhysicallyBasedMaterial.BaseColor { get set }
```

## Mentions

- [Applying realistic material and lighting effects to entities](applying-realistic-material-and-lighting-effects-to-entities.md)

#### Discussion

The base color of an entity is either a solid color or a UV-mapped image texture. This property represents the color of the entity before RealityKit applies any lighting or rendering calculations.

To determine the appearance of the entity, RealityKit modifies the entity’s base color using its material properties and the light sources in the scene.

You can define an entity’s base color using a `CGColor`, a UV-mapped image texture, or both. If you only provide a color, RealityKit uses that as the base color for the entire entity. If you specify only an image texture, it applies that texture as the base color of the entity. If you provide both a color and a texture, RealityKit tints the image texture using the color.

Here’s an example of using a single color to specify base color:

```swift
var material = PhysicallyBasedMaterial()
material.baseColor = PhysicallyBasedMaterial.BaseColor(tint:.red)
```

The following example demonstrates how to use an image to specify base color:

```swift
var material = PhysicallyBasedMaterial()

    // Load entity_basecolor.png from the app's bundle.
    if let baseResource = try? TextureResource.load(named: "entity_basecolor") {
        // Create a material parameter and assign it.
        let baseColor = MaterialParameters.Texture(baseResource)
        material.baseColor = PhysicallyBasedMaterial.BaseColor(texture:baseColor)
    }
```

## See Also

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
- [var clearcoatNormal: PhysicallyBasedMaterial.ClearcoatNormal](physicallybasedmaterial/clearcoatnormal-swift.property.md)
  Waviness and imperfections for the top clearcoat.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/physicallybasedmaterial/basecolor-swift.property)*