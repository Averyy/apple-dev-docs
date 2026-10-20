# CustomMaterial.Opacity

**Framework**: RealityKit  
**Kind**: struct  
**Role**: Structure

An object that defines the transparency options for a custom material.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+

## Declaration

```swift
struct Opacity
```

## Topics

### Creating an opacity object
- [init(floatLiteral: Float)](./opacity/init%28floatliteral%29.md)
  Creates an opacity object from a single value.
- [init(scale: Float, texture: CustomMaterial.Texture?)](./opacity/init%28scale,texture%29.md)
  Creates an object that defines the opacity of an entity using a single value, a UV-mapped image texture, or both.
- [init(PhysicallyBasedMaterial.Opacity)](./opacity/init%28_%29.md)
  Creates an object from the opacity property of an existing physically based material.
### Accessing opacity data
- [var scale: Float](./opacity/scale.md)
  The amount of opacity specified as a single value.
- [var texture: CustomMaterial.Texture?](./opacity/texture.md)
  The amount of opacity specified using a UV-mapped image.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [ExpressibleByFloatLiteral](../../Swift/expressiblebyfloatliteral.md)
- [Hashable](../../Swift/hashable.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/custommaterial/opacity)*