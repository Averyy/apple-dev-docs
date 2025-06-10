# PhysicallyBasedMaterial.Normal

**Framework**: RealityKit  
**Kind**: struct

An object that specifies an entity’s normal map.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+ (Beta)
- visionOS ?+

## Declaration

```swift
struct Normal
```

#### Overview

The `normal` property of a RealityKit entity holds an optional , which stores fine details about the entity’s surface, using a texture rather than increasing the number of polygons in the model. If you provide a normal map, RealityKit uses the vectors from that normal map when rendering the entity, resulting in greater detail and more accurate highlights, shadows, and reflections.

## Topics

### Creating a normal object
- [init(texture: PhysicallyBasedMaterial.Texture?)](physicallybasedmaterial/normal-swift.struct/init(texture:).md)
  Creates an object from a specified texture.
- [init(CustomMaterial.Normal)](physicallybasedmaterial/normal-swift.struct/init(_:).md)
  Creates a normal object from a custom material’s normal property.
### Accessing the normal map
- [var texture: PhysicallyBasedMaterial.Texture?](physicallybasedmaterial/normal-swift.struct/texture.md)
  The material’s normal map.
- [static let textureSemantic: TextureResource.Semantic](physicallybasedmaterial/normal-swift.struct/texturesemantic.md)
  The intended use of the object’s texture property.

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

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/physicallybasedmaterial/normal-swift.struct)*