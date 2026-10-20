# CustomMaterial.AmbientOcclusion

**Framework**: RealityKit  
**Kind**: struct  
**Role**: Structure

An object that defines an entity’s exposure to ambient light.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+

## Declaration

```swift
struct AmbientOcclusion
```

## Topics

### Creating an ambient occlusion object
- [init(texture: CustomMaterial.Texture?)](./ambientocclusion-swift.struct/init%28texture%29.md)
  Creates an object from an image texture.
- [init(PhysicallyBasedMaterial.AmbientOcclusion)](./ambientocclusion-swift.struct/init%28_%29.md)
  Creates an object from a physically based material’s ambient occlusion property.
### Accessing ambient occlusion values
- [var texture: CustomMaterial.Texture?](./ambientocclusion-swift.struct/texture.md)
  The entity’s exposure to ambient light specified using a UV-mapped image.

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

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/custommaterial/ambientocclusion-swift.struct)*