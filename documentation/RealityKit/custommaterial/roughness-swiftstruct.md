# CustomMaterial.Roughness

**Framework**: RealityKit  
**Kind**: struct

An object that defines how the surface of an entity scatters the light it reflects.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+

## Declaration

```swift
struct Roughness
```

#### Overview

In physically based rendering, the `roughness` property represents how much the surface of an entity scatters the light it reflects. A material with a high roughness has a matte appearance, whereas one with a low roughness has a shiny appearance.

For more information on using roughness values in a custom material, see [`roughness`](custommaterial/roughness-swift.property.md).

## Topics

### Creating a roughness object
- [init(floatLiteral: Float)](custommaterial/roughness-swift.struct/init(floatliteral:).md)
  Creates an object to specify the amount of roughness, using a single value that applies to the entire material.
- [init(scale: Float, texture: CustomMaterial.Texture?)](custommaterial/roughness-swift.struct/init(scale:texture:).md)
  Creates a roughness object from a color or texture.
- [init(PhysicallyBasedMaterial.Roughness)](custommaterial/roughness-swift.struct/init(_:).md)
  Creates a roughness object from a physically based material’s roughness property.
### Accessing roughness values
- [var scale: Float](custommaterial/roughness-swift.struct/scale.md)
  The roughness value for the entire entity or a multiplier for its texture.
- [var texture: CustomMaterial.Texture?](custommaterial/roughness-swift.struct/texture.md)
  The roughness values as a UV-mapped image texture.

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
- [CustomMaterial.Specular](custommaterial/specular-swift.struct.md)
  An object that defines the specular highlights of an entity.
- [CustomMaterial.Clearcoat](custommaterial/clearcoat-swift.struct.md)
  An object that defines the intensity of an entity’s clear, shiny coating.
- [CustomMaterial.ClearcoatNormal](custommaterial/clearcoatnormal-swift.struct.md)
  An object that defines the clearcoat normal map texture.
- [CustomMaterial.ResourceStorage](custommaterial/resourcestorage.md)
  A container for resources that will be encoded into a CustomMaterial’s custom uniforms argument buffer.
- [CustomMaterial.TextureCoordinateTransform](custommaterial/texturecoordinatetransform-swift.typealias.md)
  The object type that custom material use to hold UV texture coordinates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/custommaterial/roughness-swift.struct)*