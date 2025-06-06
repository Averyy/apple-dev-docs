# PhysicallyBasedMaterial.Clearcoat

**Framework**: RealityKit  
**Kind**: struct

An object that defines the intensity of an entity’s clear, shiny coating.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS ?+

## Declaration

```swift
struct Clearcoat
```

#### Overview

A clearcoat is a separate layer of transparent specular highlights used to simulate a clear coating, like on a car or the surface of lacquered objects.

## Topics

### Creating a clearcoat object
- [init(floatLiteral: Float)](physicallybasedmaterial/clearcoat-swift.struct/init(floatliteral:).md)
  Creates a clearcoat object using a single value.
- [init(scale: Float, texture: PhysicallyBasedMaterial.Texture?)](physicallybasedmaterial/clearcoat-swift.struct/init(scale:texture:).md)
  Creates a clearcoat object using a single value or a texture.
- [init(CustomMaterial.Clearcoat)](physicallybasedmaterial/clearcoat-swift.struct/init(_:).md)
  Creates a clearcoat object from a custom material’s clearcoat property.
### Accessing clearcoat values
- [var texture: PhysicallyBasedMaterial.Texture?](physicallybasedmaterial/clearcoat-swift.struct/texture.md)
  The clearcoat intensity specified using a UV-mapped image.
- [static let textureSemantic: TextureResource.Semantic](physicallybasedmaterial/clearcoat-swift.struct/texturesemantic.md)
  The intended use of the object’s texture property.
- [var scale: Float](physicallybasedmaterial/clearcoat-swift.struct/scale.md)
  The clearcoat intensity specified as a single value.
- [PhysicallyBasedMaterial.Clearcoat.FloatLiteralType](physicallybasedmaterial/clearcoat-swift.struct/floatliteraltype.md)
  A type that represents a floating-point literal.

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

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/physicallybasedmaterial/clearcoat-swift.struct)*