# CustomMaterial.CustomMaterialTexture

**Framework**: RealityKit  
**Kind**: struct  
**Role**: Structure

A texture object that you use to create custom materials.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+

## Declaration

```swift
struct CustomMaterialTexture
```

## Topics

### Creating a custom texture
- [init(TextureResource)](./custommaterialtexture/init%28_%29-1i8wq.md)
  Creates a custom texture from a texture resource.
- [init(MaterialParameters.Texture)](./custommaterialtexture/init%28_%29-71hfh.md)
  Creates a custom texture by copying values from a material parameters texture.
### Accessing texture resources
- [var resource: TextureResource](./custommaterialtexture/resource.md)
  The texture resource you use to create a custom texture.
### Initializers
- [init(_:)](./custommaterialtexture/init%28_%29.md)
  Creates a custom texture from a texture resource.
- [init(TextureResource, MTLTextureSwizzleChannels)](./custommaterialtexture/init%28_,_%29.md)
  Creates a custom texture from a texture resource.
### Instance Properties
- [var swizzle: MTLTextureSwizzleChannels](./custommaterialtexture/swizzle.md)

## See Also

### Custom material types
- [CustomMaterial.Custom](./custom-swift.struct.md)
  An object that defines the custom properties for the material.
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

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/custommaterial/custommaterialtexture)*