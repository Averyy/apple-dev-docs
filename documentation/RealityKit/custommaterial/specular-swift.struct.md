# CustomMaterial.Specular

**Framework**: RealityKit  
**Kind**: struct  
**Role**: Structure

An object that defines the specular highlights of an entity.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+

## Declaration

```swift
struct Specular
```

## Overview

In physically based rendering (PBR), specular highlights primarily come from the object’s [`roughness`](../physicallybasedmaterial/roughness-swift.property.md) value. RealityKit renders materials that have a low roughness value with specular highlights based on the environment, lighting, and shape of the entity.

For more information on using specular values in a custom material, see [`specular`](./specular-swift.property.md).

## Topics

### Creating a specular object
- [init(floatLiteral: Float)](./specular-swift.struct/init%28floatliteral%29.md)
  Creates an object from a single value.
- [init(scale: Float, texture: CustomMaterial.Texture?)](./specular-swift.struct/init%28scale,texture%29.md)
  Creates an object from a single value, a UV-mapped texture, or both.
- [init(PhysicallyBasedMaterial.Specular)](./specular-swift.struct/init%28_%29.md)
  Creates an object from a physically based material’s specular property.
### Accessing specular values
- [var scale: Float](./specular-swift.struct/scale.md)
  The specular value for the entire entity or a multiplier for values sampled from the material’s texture.
- [var texture: CustomMaterial.Texture?](./specular-swift.struct/texture.md)
  The specular value as a UV-mapped image texture.

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
- [CustomMaterial.Roughness](./roughness-swift.struct.md)
  An object that defines how the surface of an entity scatters the light it reflects.
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
- [CustomMaterial.Clearcoat](./clearcoat-swift.struct.md)
  An object that defines the intensity of an entity’s clear, shiny coating.
- [CustomMaterial.ClearcoatNormal](./clearcoatnormal-swift.struct.md)
  An object that defines the clearcoat normal map texture.
- [CustomMaterial.ResourceStorage](./resourcestorage.md)
  A container for resources that will be encoded into a CustomMaterial’s custom uniforms argument buffer.
- [CustomMaterial.TextureCoordinateTransform](./texturecoordinatetransform-swift.typealias.md)
  The object type that custom material use to hold UV texture coordinates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/custommaterial/specular-swift.struct)*