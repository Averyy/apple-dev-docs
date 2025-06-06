# CustomMaterial.BaseColor

**Framework**: RealityKit  
**Kind**: struct

An object that defines an entity’s base color.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+

## Declaration

```swift
struct BaseColor
```

## Mentions

- [Modifying RealityKit rendering using custom materials](modifying-realitykit-rendering-using-custom-materials.md)

#### Overview

For more information on using base color values in a custom material, see [`baseColor`](custommaterial/basecolor-swift.property.md).

## Topics

### Creating a base color object
- [init(tint: UIColor, texture: CustomMaterial.Texture?)](custommaterial/basecolor-swift.struct/init(tint:texture:)-5c2fr.md)
  Creates a base color object from a color or texture on macOS.
- [init(tint: NSColor, texture: CustomMaterial.Texture?)](custommaterial/basecolor-swift.struct/init(tint:texture:)-71h0i.md)
  Creates a base color object from a color or texture on macOS.
- [init(PhysicallyBasedMaterial.BaseColor)](custommaterial/basecolor-swift.struct/init(_:).md)
  Creates a custom base color object from an existing physically based material’s base color object.
### Accessing base color data
- [var texture: CustomMaterial.Texture?](custommaterial/basecolor-swift.struct/texture.md)
  The base color as a UV-mapped image.
- [var tint: UIColor](custommaterial/basecolor-swift.struct/tint-4xg2a.md)
- [var tint: NSColor](custommaterial/basecolor-swift.struct/tint-99g.md)

## See Also

- [CustomMaterial.Custom](custommaterial/custom-swift.struct.md)
  An object that defines the custom properties for the material.
- [CustomMaterial.CustomMaterialTexture](custommaterial/custommaterialtexture.md)
  A texture object that you use to create custom materials.
- [CustomMaterial.LightingModel](custommaterial/lightingmodel-swift.enum.md)
  An object that defines how the framework renders a custom material.
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

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/custommaterial/basecolor-swift.struct)*