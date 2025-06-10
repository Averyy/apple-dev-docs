# PhysicallyBasedMaterial.AnisotropyLevel

**Framework**: RealityKit  
**Kind**: struct

An object that defines the degree to which an entity reflects light to create stretched or oblong highlights.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+ (Beta)
- visionOS ?+

## Declaration

```swift
struct AnisotropyLevel
```

#### Overview

By default, PBR materials are isotropic; in other words, an entity that uses [`PhysicallyBasedMaterial`](physicallybasedmaterial.md) reflects light uniformly in all directions, mimicking the behavior of most real-world objects. Some objects, including those with many small parallel striations such as vinyl records, CDs, or straight hair, reflect light more in some directions than others, resulting in stretched or oblong specular highlights, as shown in the following figure.

![An illustration showing 11 metallic spheres in a horizontal row. The](https://docs-assets.developer.apple.com/published/2eecb2feb22234ad8501e669131a2d52/PhysicallyBasedMaterial-AnisotropyLevel-swift-struct-1%402x.png)

Use this object to specify the [`anisotropyLevel`](physicallybasedmaterial/anisotropylevel-swift.property.md) for a material.

## Topics

### Creating an anisotropy level object
- [init(floatLiteral: Float)](physicallybasedmaterial/anisotropylevel-swift.struct/init(floatliteral:).md)
  Creates an anisotropy level object from a single value.
- [init(scale: Float, texture: PhysicallyBasedMaterial.Texture?)](physicallybasedmaterial/anisotropylevel-swift.struct/init(scale:texture:).md)
  Creates an anisotropy level object using a single value or a texture.
### Accessing anisotropy level values
- [var texture: PhysicallyBasedMaterial.Texture?](physicallybasedmaterial/anisotropylevel-swift.struct/texture.md)
  The anisotropy level values specified using a UV-mapped image.
- [static let textureSemantic: TextureResource.Semantic](physicallybasedmaterial/anisotropylevel-swift.struct/texturesemantic.md)
  The intended use of the object’s texture property.
- [var scale: Float](physicallybasedmaterial/anisotropylevel-swift.struct/scale.md)
  The anistropy level specified as a single value.

## Relationships

### Conforms To
- [ExpressibleByFloatLiteral](../Swift/ExpressibleByFloatLiteral.md)

## See Also

- [Applying realistic material and lighting effects to entities](applying-realistic-material-and-lighting-effects-to-entities.md)
  Enhance the appearance of objects in a RealityKit scene with Physically Based Rendering (PBR).
- [struct PhysicallyBasedMaterial](physicallybasedmaterial.md)
  A material that simulates the appearance of real-world objects.
- [PhysicallyBasedMaterial.BaseColor](physicallybasedmaterial/basecolor-swift.struct.md)
  An object that defines an entity’s base color.
- [PhysicallyBasedMaterial.Roughness](physicallybasedmaterial/roughness-swift.struct.md)
  An object that defines the roughness of an entity’s surface.
- [PhysicallyBasedMaterial.Metallic](physicallybasedmaterial/metallic-swift.struct.md)
  An object that defines the reflectiveness of an entity.
- [PhysicallyBasedMaterial.Normal](physicallybasedmaterial/normal-swift.struct.md)
  An object that specifies an entity’s normal map.
- [PhysicallyBasedMaterial.Blending](physicallybasedmaterial/blending-swift.enum.md)
  The object that defines the transparency of an entity.
- [PhysicallyBasedMaterial.AmbientOcclusion](physicallybasedmaterial/ambientocclusion-swift.struct.md)
  An object that defines the ambient occlusion of an entity’s surface.
- [PhysicallyBasedMaterial.Specular](physicallybasedmaterial/specular-swift.struct.md)
  An object that defines the specular highlights of an entity.
- [PhysicallyBasedMaterial.SheenColor](physicallybasedmaterial/sheencolor.md)
  An object that defines the color of an entity’s sheen.
- [PhysicallyBasedMaterial.Clearcoat](physicallybasedmaterial/clearcoat-swift.struct.md)
  An object that defines the intensity of an entity’s clear, shiny coating.
- [PhysicallyBasedMaterial.ClearcoatRoughness](physicallybasedmaterial/clearcoatroughness-swift.struct.md)
  An object that defines the degree to which an entity’s clear, shiny coating scatters light to create soft highlights.
- [PhysicallyBasedMaterial.AnisotropyAngle](physicallybasedmaterial/anisotropyangle-swift.struct.md)
  An object used to define a material’s anisotropy angle.
- [PhysicallyBasedMaterial.EmissiveColor](physicallybasedmaterial/emissivecolor-swift.struct.md)
  An object that defines the color of the light an entity emits.
- [PhysicallyBasedMaterial.TextureCoordinateTransform](physicallybasedmaterial/texturecoordinatetransform-swift.typealias.md)
  An alias for the texture coordinate transform that’s appropriate for this material class.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/physicallybasedmaterial/anisotropylevel-swift.struct)*