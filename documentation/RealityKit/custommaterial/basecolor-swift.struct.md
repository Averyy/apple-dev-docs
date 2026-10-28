# CustomMaterial.BaseColor

**Framework**: RealityKit  
**Kind**: struct  
**Role**: Structure

An object that defines an entity’s base color.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+

## Declaration

```swift
struct BaseColor
```

## Mentions

- [Modifying RealityKit rendering using custom materials](../modifying-realitykit-rendering-using-custom-materials.md)

## Overview

For more information on using base color values in a custom material, see [`baseColor`](./basecolor-swift.property.md).

## Topics

### Creating a base color object
- [init(tint: UIColor, texture: CustomMaterial.Texture?)](./basecolor-swift.struct/init%28tint,texture%29-5c2fr.md)
  Creates a base color object from a color or texture on macOS.
- [init(tint: NSColor, texture: CustomMaterial.Texture?)](./basecolor-swift.struct/init%28tint,texture%29-71h0i.md)
  Creates a base color object from a color or texture on macOS.
- [init(PhysicallyBasedMaterial.BaseColor)](./basecolor-swift.struct/init%28_%29.md)
  Creates a custom base color object from an existing physically based material’s base color object.
### Accessing base color data
- [var texture: CustomMaterial.Texture?](./basecolor-swift.struct/texture.md)
  The base color as a UV-mapped image.
- [var tint: UIColor](./basecolor-swift.struct/tint-4xg2a.md)
- [var tint: NSColor](./basecolor-swift.struct/tint-99g.md)
### Initializers
- [init(tint:texture:)](./basecolor-swift.struct/init%28tint,texture%29.md)
  Creates a base color object from a color or texture on macOS.

## See Also

### Custom material types
- [CustomMaterial.Custom](./custom-swift.struct.md)
  An object that defines the custom properties for the material.
- [CustomMaterial.CustomMaterialTexture](./custommaterialtexture.md)
  A texture object that you use to create custom materials.
- [CustomMaterial.LightingModel](./lightingmodel-swift.enum.md)
  An object that defines how the framework renders a custom material.
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

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/custommaterial/basecolor-swift.struct)*