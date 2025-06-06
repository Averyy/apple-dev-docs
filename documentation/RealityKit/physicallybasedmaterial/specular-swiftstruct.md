# PhysicallyBasedMaterial.Specular

**Framework**: RealityKit  
**Kind**: struct

An object that defines the specular highlights of an entity.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS ?+

## Declaration

```swift
struct Specular
```

#### Overview

RealityKit automatically draws  for physically based materials, using the values of various properties, primarily [`roughness`](physicallybasedmaterial/roughness-swift.property.md) and [`metallic`](physicallybasedmaterial/metallic-swift.property.md). Specular highlights are bright spots of reflected light that appear on shiny objects.

![An illustration showing a sphere and a cube with rounded corners. Both](https://docs-assets.developer.apple.com/published/0b83dd2d5721a30ef708e7bf6420620b/PhysicallyBasedMaterial-Specular-swift-struct-1%402x.png)

Although many real-world objects can be accurately and realistically simulated with just the core physically based rendering (PBR) properties, you can create additional realistic effects by augmenting the specular highlights.

Use this object to specify the amount of [`specular`](physicallybasedmaterial/specular-swift.property.md) for a [`PhysicallyBasedMaterial`](physicallybasedmaterial.md).

## Topics

### Creating a specular object
- [init(floatLiteral: Float)](physicallybasedmaterial/specular-swift.struct/init(floatliteral:).md)
  Creates an object from single value.
- [init(scale: Float, texture: PhysicallyBasedMaterial.Texture?)](physicallybasedmaterial/specular-swift.struct/init(scale:texture:).md)
  Creates an object from a single value or a texture.
- [init(CustomMaterial.Specular)](physicallybasedmaterial/specular-swift.struct/init(_:).md)
  Creates an object from a custom material’s specular property.
### Accessing specular values
- [var texture: PhysicallyBasedMaterial.Texture?](physicallybasedmaterial/specular-swift.struct/texture.md)
  The amount of specular as a UV-mapped image texture.
- [static let textureSemantic: TextureResource.Semantic](physicallybasedmaterial/specular-swift.struct/texturesemantic.md)
  The intended use of the object’s texture property.
- [var scale: Float](physicallybasedmaterial/specular-swift.struct/scale.md)
  The amount of specular for the entire entity.
- [PhysicallyBasedMaterial.Specular.FloatLiteralType](physicallybasedmaterial/specular-swift.struct/floatliteraltype.md)
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

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/physicallybasedmaterial/specular-swift.struct)*