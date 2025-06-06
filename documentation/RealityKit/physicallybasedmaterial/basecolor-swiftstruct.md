# PhysicallyBasedMaterial.BaseColor

**Framework**: RealityKit  
**Kind**: struct

An object that defines an entity’s base color.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS ?+

## Declaration

```swift
struct BaseColor
```

#### Overview

Use this struct to specify an entity’s base color, which defines the entity’s appearance before RealityKit calculates the effect of lighting or material properties such as [`roughness`](physicallybasedmaterial/roughness-swift.property.md) or [`metallic`](physicallybasedmaterial/metallic-swift.property.md). For more information, see [`baseColor`](physicallybasedmaterial/basecolor-swift.property.md).

## Topics

### Creating a base color object
- [init(tint: UIColor, texture: MaterialParameters.Texture?)](physicallybasedmaterial/basecolor-swift.struct/init(tint:texture:)-2wriz.md)
  Creates a base color object from a color or texture on macOS.
- [init(tint: NSColor, texture: MaterialParameters.Texture?)](physicallybasedmaterial/basecolor-swift.struct/init(tint:texture:)-5jeqr.md)
  Creates a base color object from a color or texture on macOS.
- [init(CustomMaterial.BaseColor)](physicallybasedmaterial/basecolor-swift.struct/init(_:).md)
  Creates a base color object from a custom material’s base color property.
### Accessing texture data
- [var texture: PhysicallyBasedMaterial.Texture?](physicallybasedmaterial/basecolor-swift.struct/texture.md)
  The base color as a UV Image map.
- [static let textureSemantic: TextureResource.Semantic](physicallybasedmaterial/basecolor-swift.struct/texturesemantic.md)
  The intended use of this object’s texture property.
### Instance Properties
- [var tint: UIColor](physicallybasedmaterial/basecolor-swift.struct/tint-2znu0.md)
- [var tint: NSColor](physicallybasedmaterial/basecolor-swift.struct/tint-6heih.md)

## See Also

- [Applying realistic material and lighting effects to entities](applying-realistic-material-and-lighting-effects-to-entities.md)
  Enhance the appearance of objects in a RealityKit scene with Physically Based Rendering (PBR).
- [struct PhysicallyBasedMaterial](physicallybasedmaterial.md)
  A material that simulates the appearance of real-world objects.
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
- [PhysicallyBasedMaterial.AnisotropyLevel](physicallybasedmaterial/anisotropylevel-swift.struct.md)
  An object that defines the degree to which an entity reflects light to create stretched or oblong highlights.
- [PhysicallyBasedMaterial.AnisotropyAngle](physicallybasedmaterial/anisotropyangle-swift.struct.md)
  An object used to define a material’s anisotropy angle.
- [PhysicallyBasedMaterial.EmissiveColor](physicallybasedmaterial/emissivecolor-swift.struct.md)
  An object that defines the color of the light an entity emits.
- [PhysicallyBasedMaterial.TextureCoordinateTransform](physicallybasedmaterial/texturecoordinatetransform-swift.typealias.md)
  An alias for the texture coordinate transform that’s appropriate for this material class.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/physicallybasedmaterial/basecolor-swift.struct)*