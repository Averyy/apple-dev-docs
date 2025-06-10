# CustomMaterial.ResourceStorage

**Framework**: RealityKit  
**Kind**: struct

A container for resources that will be encoded into a CustomMaterial’s custom uniforms argument buffer.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+ (Beta)

## Declaration

```swift
struct ResourceStorage<UniformsType>
```

#### Overview

An object of this type is passed to you in the callback closure passed to [`withMutableUniforms(ofType:stage:_:)`](custommaterial/withmutableuniforms(oftype:stage:_:).md) and allows you to set [`TextureResource`](textureresource.md) values within your custom uniforms argument buffer.

## Topics

### Subscripts
- [subscript<BufferType>(buffer _: KeyPath<UniformsType, UnsafeMutablePointer<BufferType>?>) -> LowLevelBuffer?](custommaterial/resourcestorage/subscript(buffer:).md)
- [subscript(textureResource _: KeyPath<UniformsType, UInt64>) -> TextureResource](custommaterial/resourcestorage/subscript(textureresource:).md)

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
- [CustomMaterial.ClearcoatNormal](custommaterial/clearcoatnormal-swift.struct.md)
  An object that defines the clearcoat normal map texture.
- [CustomMaterial.TextureCoordinateTransform](custommaterial/texturecoordinatetransform-swift.typealias.md)
  The object type that custom material use to hold UV texture coordinates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/custommaterial/resourcestorage)*