# CustomMaterial.Metallic

**Framework**: RealityKit  
**Kind**: struct  
**Role**: Structure

An object that defines an entity’s reflectiveness.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+

## Declaration

```swift
struct Metallic
```

## Overview

In physically based rendering, the `metallic` property represents the reflectiveness of an entity. Use this object to specify whether an entity displays metallic qualities and reflects the surrounding environment.

For more information on using metallic values in a custom material, see [`metallic`](./metallic-swift.property.md).

## Topics

### Creating a metallic object
- [init(floatLiteral: Float)](./metallic-swift.struct/init%28floatliteral%29.md)
  Creates an object from a single value.
- [init(scale: Float, texture: CustomMaterial.Texture?)](./metallic-swift.struct/init%28scale,texture%29.md)
  Creates an object from a color or texture.
- [init(PhysicallyBasedMaterial.Metallic)](./metallic-swift.struct/init%28_%29.md)
  Creates a metallic object from a physically based material’s metallic property.
### Accessing metallic data
- [var scale: Float](./metallic-swift.struct/scale.md)
  The reflectiveness value for the entire entity or a multiplier for the metallic texture.
- [var texture: CustomMaterial.Texture?](./metallic-swift.struct/texture.md)
  The reflectiveness as a UV-mapped image texture.

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

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/custommaterial/metallic-swift.struct)*