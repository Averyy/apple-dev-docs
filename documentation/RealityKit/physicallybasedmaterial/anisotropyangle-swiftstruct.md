# PhysicallyBasedMaterial.AnisotropyAngle

**Framework**: RealityKit  
**Kind**: struct

An object used to define a material’s anisotropy angle.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+
- visionOS ?+

## Declaration

```swift
struct AnisotropyAngle
```

## Topics

### Creating an anisotropy angle object
- [init(floatLiteral: Float)](physicallybasedmaterial/anisotropyangle-swift.struct/init(floatliteral:).md)
  Creates an anisotropy angle object from a single value.
- [init(scale: Float, texture: PhysicallyBasedMaterial.Texture?)](physicallybasedmaterial/anisotropyangle-swift.struct/init(scale:texture:).md)
  Creates an anisotropy angle object using a single value or a texture.
### Accessing anisotropy angle values
- [var texture: PhysicallyBasedMaterial.Texture?](physicallybasedmaterial/anisotropyangle-swift.struct/texture.md)
  The anisotropy angle values specified using a UV-mapped image.
- [static let textureSemantic: TextureResource.Semantic](physicallybasedmaterial/anisotropyangle-swift.struct/texturesemantic.md)
  The intended use of the object’s texture property.
- [var scale: Float](physicallybasedmaterial/anisotropyangle-swift.struct/scale.md)
  The anistropy angle specified as a single value.

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
- [PhysicallyBasedMaterial.AnisotropyLevel](physicallybasedmaterial/anisotropylevel-swift.struct.md)
  An object that defines the degree to which an entity reflects light to create stretched or oblong highlights.
- [PhysicallyBasedMaterial.EmissiveColor](physicallybasedmaterial/emissivecolor-swift.struct.md)
  An object that defines the color of the light an entity emits.
- [PhysicallyBasedMaterial.TextureCoordinateTransform](physicallybasedmaterial/texturecoordinatetransform-swift.typealias.md)
  An alias for the texture coordinate transform that’s appropriate for this material class.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/physicallybasedmaterial/anisotropyangle-swift.struct)*