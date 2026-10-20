# CustomMaterial.Roughness

**Framework**: RealityKit  
**Kind**: struct  
**Role**: Structure

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

For more information on using roughness values in a custom material, see [`roughness`](./roughness-swift.property.md).

## Topics

### Creating a roughness object
- [init(floatLiteral: Float)](./roughness-swift.struct/init%28floatliteral%29.md)
  Creates an object to specify the amount of roughness, using a single value that applies to the entire material.
- [init(scale: Float, texture: CustomMaterial.Texture?)](./roughness-swift.struct/init%28scale,texture%29.md)
  Creates a roughness object from a color or texture.
- [init(PhysicallyBasedMaterial.Roughness)](./roughness-swift.struct/init%28_%29.md)
  Creates a roughness object from a physically based material’s roughness property.
### Accessing roughness values
- [var scale: Float](./roughness-swift.struct/scale.md)
  The roughness value for the entire entity or a multiplier for its texture.
- [var texture: CustomMaterial.Texture?](./roughness-swift.struct/texture.md)
  The roughness values as a UV-mapped image texture.

## Relationships

### Conforms To
- [ExpressibleByFloatLiteral](../../Swift/expressiblebyfloatliteral.md)

## See Also

### Custom material types
- [CustomMaterial.Custom](./custom-swift.struct.md)
  An object that defines the custom properties for the material.
- [CustomMaterial.CustomMaterialTexture](./custommaterialtexture.md)
  A texture object that you use to create custom materials.
- [CustomMaterial.LightingModel](./lightingmodel-swift.enum.md)
  An object that defines how the framework renders a custom material.
- [CustomMaterial.BaseColor](./basecolor-swift.struct.md)
  An object that defines an entity’s base color.
- [CustomMaterial.Metallic](./metallic-swift.struct.md)
  An object that defines an entity’s reflectiveness.
- [CustomMaterial.Normal](./normal-swift.struct.md)
  An object that stores fine surface details for an entity in an image texture.
- [CustomMaterial.EmissiveColor](./emissivecolor-swift.struct.md)
  An object that defines the color of the light an entity emits.
- [CustomMaterial.Blending](./blending-swift.enum.md)
  An object that specifies the transparency of an entity.
- [CustomMaterial.Opacity](./opacity.md)
  An object that defines the transparency options for a custom material.
- [CustomMaterial.AmbientOcclusion](./ambientocclusion-swift.struct.md)
  An object that defines an entity’s exposure to ambient light.
- [CustomMaterial.Specular](./specular-swift.struct.md)
  An object that defines the specular highlights of an entity.
- [CustomMaterial.Clearcoat](./clearcoat-swift.struct.md)
  An object that defines the intensity of an entity’s clear, shiny coating.
- [CustomMaterial.ClearcoatNormal](./clearcoatnormal-swift.struct.md)
  An object that defines the clearcoat normal map texture.
- [CustomMaterial.ResourceStorage](./resourcestorage.md)
  A container for resources that will be encoded into a CustomMaterial’s custom uniforms argument buffer.
- [CustomMaterial.TextureCoordinateTransform](./texturecoordinatetransform-swift.typealias.md)
  The object type that custom material use to hold UV texture coordinates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/custommaterial/roughness-swift.struct)*