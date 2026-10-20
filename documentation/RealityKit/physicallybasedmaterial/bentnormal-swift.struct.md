# PhysicallyBasedMaterial.BentNormal

**Framework**: RealityKit  
**Kind**: struct  
**Role**: Structure

The bent normal map for the entity.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
struct BentNormal
```

#### Overview

*Bent normal mapping* describes the average direction of least occlusion at each surface point. This is used to modulate lighting intensity and direction of the material. Use with ambient occlusion to improve the accuracy of indirect diffuse lighting. You can generate bent normals maps from a 3D software package.

## Topics

### Accessing the texture key
- [static let textureKey: String](./bentnormal-swift.struct/texturekey.md)
### Initializers
- [init(texture: PhysicallyBasedMaterial.Texture?)](./bentnormal-swift.struct/init%28texture%29.md)
### Instance Properties
- [var texture: PhysicallyBasedMaterial.Texture?](./bentnormal-swift.struct/texture.md)
### Type Properties
- [static let textureSemantic: TextureResource.Semantic](./bentnormal-swift.struct/texturesemantic.md)

## See Also

### Configuring occlusion shading
- [var bentNormal: PhysicallyBasedMaterial.BentNormal](./bentnormal-swift.property.md)
  The bent normal map for the entity.
- [var enableSpecularOcclusion: Bool](./enablespecularocclusion.md)
  Enables specular occlusion computations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/physicallybasedmaterial/bentnormal-swift.struct)*