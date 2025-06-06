# anisotropyLevel

**Framework**: RealityKit  
**Kind**: property

The degree to which an entity reflects light to create stretched or oblong highlights.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS ?+

## Declaration

```swift
var anisotropyLevel: PhysicallyBasedMaterial.AnisotropyLevel { get set }
```

## Mentions

- [Applying realistic material and lighting effects to entities](applying-realistic-material-and-lighting-effects-to-entities.md)

#### Discussion

By default, PBR materials are isotropic; in other words, an entity that uses [`PhysicallyBasedMaterial`](physicallybasedmaterial.md) reflects light uniformly in all directions, mimicking the behavior of most real-world objects. Some objects, including those with many small parallel striations such as vinyl records, CDs, or straight hair, reflect light more in some directions than others, resulting in stretched or oblong specular highlights, as shown in the following figure.

![An illustration showing 11 metallic spheres in a horizontal row. The](https://docs-assets.developer.apple.com/published/2eecb2feb22234ad8501e669131a2d52/PhysicallyBasedMaterial-anisotropyLevel-swift-property-1%402x.png)

This property controls the amount of anisotropy. It works together with [`anisotropyAngle`](physicallybasedmaterial/anisotropyangle-swift.property.md), which defines the angle of elongation for the specular highlights.

The following example specifies `anisotropyLevel` using single values for the entire material:

```swift
material.anisotropyLevel = .AnisotropyLevel(floatLiteral: 0.5)
```

This example specifies `anisotropyLevel` using a UV-mapped image texture.

```swift
if let anisoLevelResource = try? TextureResource.load(named:
"entity_aniso_level") {
    let anisoLevelMap = MaterialParameters.Texture(sheenResource)
    material.anisotropyLevel = .init(texture: anisoLevelMap)
}
```

## See Also

- [var anisotropyAngle: PhysicallyBasedMaterial.AnisotropyAngle](physicallybasedmaterial/anisotropyangle-swift.property.md)
  The angle at which the anisotropic direction of the material is oriented, influencing the reflection and appearance of surface highlights.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/physicallybasedmaterial/anisotropylevel-swift.property)*