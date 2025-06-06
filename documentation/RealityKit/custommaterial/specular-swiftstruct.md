# CustomMaterial.Specular

**Framework**: RealityKit  
**Kind**: struct

An object that defines the specular highlights of an entity.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+

## Declaration

```swift
struct Specular
```

#### Overview

In physically based rendering (PBR), specular highlights primarily come from the object’s [`roughness`](physicallybasedmaterial/roughness-swift.property.md) value. RealityKit renders materials that have a low roughness value with specular highlights based on the environment, lighting, and shape of the entity.

For more information on using specular values in a custom material, see [`specular`](custommaterial/specular-swift.property.md).

## Topics

### Creating a specular object
- [init(floatLiteral: Float)](custommaterial/specular-swift.struct/init(floatliteral:).md)
  Creates an object from a single value.
- [init(scale: Float, texture: CustomMaterial.Texture?)](custommaterial/specular-swift.struct/init(scale:texture:).md)
  Creates an object from a single value, a UV-mapped texture, or both.
- [init(PhysicallyBasedMaterial.Specular)](custommaterial/specular-swift.struct/init(_:).md)
  Creates an object from a physically based material’s specular property.
### Accessing specular values
- [var scale: Float](custommaterial/specular-swift.struct/scale.md)
  The specular value for the entire entity or a multiplier for values sampled from the material’s texture.
- [var texture: CustomMaterial.Texture?](custommaterial/specular-swift.struct/texture.md)
  The specular value as a UV-mapped image texture.
- [CustomMaterial.Specular.FloatLiteralType](custommaterial/specular-swift.struct/floatliteraltype.md)
  A type that represents a floating-point literal.

## Relationships

### Conforms To
- [ExpressibleByFloatLiteral](../Swift/ExpressibleByFloatLiteral.md)

## See Also

- [CustomMaterial.Custom](custommaterial/custom-swift.struct.md)
  An object that defines the custom properties for the material.
- [CustomMaterial.CustomMaterialTexture](custommaterial/custommaterialtexture.md)
  A texture object that you use to create custom materials.
- [CustomMaterial.LightingModel](custommaterial/lightingmodel-swift.enum.md)
  An object that defines how the framework renders a custom material.
- [CustomMaterial.BaseColor](custommaterial/basecolor-swift.struct.md)
  An object that defines an entity’s base color.
- [CustomMaterial.Roughness](custommaterial/roughness-swift.struct.md)
  An object that defines how the surface of an entity scatters the light it reflects.
- [CustomMaterial.Metallic](custommaterial/metallic-swift.struct.md)
  An object that defines an entity’s reflectiveness.
- [CustomMaterial.Normal](custommaterial/normal-swift.struct.md)
  An object that stores fine surface details for an entity in an image texture.
- [CustomMaterial.EmissiveColor](custommaterial/emissivecolor-swift.struct.md)
  An object that defines the color of the light an entity emits.
- [CustomMaterial.Blending](custommaterial/blending-swift.enum.md)
  An object that specifies the transparency of an entity.
- [CustomMaterial.Opacity](custommaterial/opacity.md)
  An object that defines the transparency options for a custom material.
- [CustomMaterial.AmbientOcclusion](custommaterial/ambientocclusion-swift.struct.md)
  An object that defines an entity’s exposure to ambient light.
- [CustomMaterial.Clearcoat](custommaterial/clearcoat-swift.struct.md)
  An object that defines the intensity of an entity’s clear, shiny coating.
- [CustomMaterial.ClearcoatNormal](custommaterial/clearcoatnormal-swift.struct.md)
  An object that defines the clearcoat normal map texture.
- [CustomMaterial.ResourceStorage](custommaterial/resourcestorage.md)
  A container for resources that will be encoded into a CustomMaterial’s custom uniforms argument buffer.
- [CustomMaterial.TextureCoordinateTransform](custommaterial/texturecoordinatetransform-swift.typealias.md)
  The object type that custom material use to hold UV texture coordinates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/custommaterial/specular-swift.struct)*