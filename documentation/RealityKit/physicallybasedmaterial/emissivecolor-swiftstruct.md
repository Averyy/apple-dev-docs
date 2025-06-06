# PhysicallyBasedMaterial.EmissiveColor

**Framework**: RealityKit  
**Kind**: struct

An object that defines the color of the light an entity emits.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS ?+

## Declaration

```swift
struct EmissiveColor
```

#### Overview

With physically based rendering (PBR), you can give entities in RealityKit the appearance of emitting light. Define the color of the light the entity emits by using this object.

## Topics

### Creating an emissive color object
- [init(color: UIColor, texture: MaterialParameters.Texture?)](physicallybasedmaterial/emissivecolor-swift.struct/init(color:texture:)-3dtam.md)
  Creates a color of emitted light in iOS.
- [init(color: NSColor, texture: MaterialParameters.Texture?)](physicallybasedmaterial/emissivecolor-swift.struct/init(color:texture:)-5hl9i.md)
  Creates a color of emitted light in iOS.
- [init(CustomMaterial.EmissiveColor)](physicallybasedmaterial/emissivecolor-swift.struct/init(_:).md)
  Creates a color of emitted light from a custom material’s emissive color property.
### Accessing texture data
- [var texture: PhysicallyBasedMaterial.Texture?](physicallybasedmaterial/emissivecolor-swift.struct/texture.md)
  An optional image texture that defines the color of light emission.
- [static let textureSemantic: TextureResource.Semantic](physicallybasedmaterial/emissivecolor-swift.struct/texturesemantic.md)
  The intended use of the object’s texture property.
### Instance Properties
- [var color: UIColor](physicallybasedmaterial/emissivecolor-swift.struct/color-6l8ly.md)
- [var color: NSColor](physicallybasedmaterial/emissivecolor-swift.struct/color-9ktf.md)

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
- [PhysicallyBasedMaterial.AnisotropyAngle](physicallybasedmaterial/anisotropyangle-swift.struct.md)
  An object used to define a material’s anisotropy angle.
- [PhysicallyBasedMaterial.TextureCoordinateTransform](physicallybasedmaterial/texturecoordinatetransform-swift.typealias.md)
  An alias for the texture coordinate transform that’s appropriate for this material class.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/physicallybasedmaterial/emissivecolor-swift.struct)*