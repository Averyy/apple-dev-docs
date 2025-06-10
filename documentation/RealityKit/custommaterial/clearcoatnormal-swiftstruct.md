# CustomMaterial.ClearcoatNormal

**Framework**: RealityKit  
**Kind**: struct

An object that defines the clearcoat normal map texture.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+ (Beta)

## Declaration

```swift
struct ClearcoatNormal
```

#### Overview

An entity in RealityKit can display a clearcoat, which is a separate layer of transparent specular highlights used to simulate a clear coating, like on a car or the surface of lacquered objects. Use this object to specify a clearcoat normal and vary the normal used to calculate the clearcoat. This can be used to add imperfections and waviness to the clearcoat layer.

For information, see [`clearcoatNormal`](custommaterial/clearcoatnormal-swift.property.md).

## Topics

### Initializers
- [init(PhysicallyBasedMaterial.ClearcoatNormal)](custommaterial/clearcoatnormal-swift.struct/init(_:).md)
  Construct a `CustomMaterial.ClearcoatNormal` object from a `PhysicallyBasedMaterial.ClearcoatNormal`
- [init(texture: CustomMaterial.Texture?)](custommaterial/clearcoatnormal-swift.struct/init(texture:).md)
  Construct a `CustomMaterial.ClearcoatNormal` object from a texture.
### Instance Properties
- [var texture: CustomMaterial.Texture?](custommaterial/clearcoatnormal-swift.struct/texture.md)
  The material’s clearcoat normal map.

## See Also

- [CustomMaterial.Custom](custommaterial/custom-swift.struct.md)
  An object that defines the custom properties for the material.
- [CustomMaterial.CustomMaterialTexture](custommaterial/custommaterialtexture.md)
  A texture object that you use to create custom materials.
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
- [CustomMaterial.ResourceStorage](custommaterial/resourcestorage.md)
  A container for resources that will be encoded into a CustomMaterial’s custom uniforms argument buffer.
- [CustomMaterial.TextureCoordinateTransform](custommaterial/texturecoordinatetransform-swift.typealias.md)
  The object type that custom material use to hold UV texture coordinates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/custommaterial/clearcoatnormal-swift.struct)*