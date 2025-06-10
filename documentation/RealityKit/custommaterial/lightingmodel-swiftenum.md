# CustomMaterial.LightingModel

**Framework**: RealityKit  
**Kind**: enum

An object that defines how the framework renders a custom material.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+ (Beta)

## Declaration

```swift
enum LightingModel
```

## Topics

### Specifying the lighting model
- [CustomMaterial.LightingModel.lit](custommaterial/lightingmodel-swift.enum/lit.md)
  The entity renders using physically based rendering techniques without a clearcoat.
- [CustomMaterial.LightingModel.clearcoat](custommaterial/lightingmodel-swift.enum/clearcoat.md)
  The entity renders using physically based rendering techniques with a clearcoat.
- [CustomMaterial.LightingModel.unlit](custommaterial/lightingmodel-swift.enum/unlit.md)
  The entity renders with no light or shadow calculations.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [CustomMaterial.Custom](custommaterial/custom-swift.struct.md)
  An object that defines the custom properties for the material.
- [CustomMaterial.CustomMaterialTexture](custommaterial/custommaterialtexture.md)
  A texture object that you use to create custom materials.
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

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/custommaterial/lightingmodel-swift.enum)*