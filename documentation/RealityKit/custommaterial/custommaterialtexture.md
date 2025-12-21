# CustomMaterial.CustomMaterialTexture

**Framework**: RealityKit  
**Kind**: struct

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
- [init(TextureResource)](custommaterial/custommaterialtexture/init(_:)-1i8wq.md)
  Creates a custom texture from a texture resource.
- [init(MaterialParameters.Texture)](custommaterial/custommaterialtexture/init(_:)-71hfh.md)
  Creates a custom texture by copying values from a material parameters texture.
### Accessing texture resources
- [var resource: TextureResource](custommaterial/custommaterialtexture/resource.md)
  The texture resource you use to create a custom texture.
### Initializers
- [init(_:)](custommaterial/custommaterialtexture/init(_:).md)
  Creates a custom texture from a texture resource.
- [init(TextureResource, MTLTextureSwizzleChannels)](custommaterial/custommaterialtexture/init(_:_:).md)
  Creates a custom texture from a texture resource.
### Instance Properties
- [var swizzle: MTLTextureSwizzleChannels](custommaterial/custommaterialtexture/swizzle.md)

## See Also

- [CustomMaterial.Custom](custommaterial/custom-swift.struct.md)
  An object that defines the custom properties for the material.
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

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/custommaterial/custommaterialtexture)*