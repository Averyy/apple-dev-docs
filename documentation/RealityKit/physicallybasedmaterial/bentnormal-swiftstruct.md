# PhysicallyBasedMaterial.BentNormal

**Framework**: RealityKit  
**Kind**: struct

The bent normal map for the entity.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct BentNormal
```

#### Overview

*Bent normal mapping* describes the average direction of least occlusion at each surface point. This is used to modulate lighting intensity and direction of the material. Use with ambient occlusion to improve the accuracy of indirect diffuse lighting. You can generate bent normals maps from a 3D software package.

## Topics

### Accessing the texture key
- [static let textureKey: String](physicallybasedmaterial/bentnormal-swift.struct/texturekey.md)
### Initializers
- [init(texture: PhysicallyBasedMaterial.Texture?)](physicallybasedmaterial/bentnormal-swift.struct/init(texture:).md)
### Instance Properties
- [var texture: PhysicallyBasedMaterial.Texture?](physicallybasedmaterial/bentnormal-swift.struct/texture.md)
### Type Properties
- [static let textureSemantic: TextureResource.Semantic](physicallybasedmaterial/bentnormal-swift.struct/texturesemantic.md)

## See Also

- [var bentNormal: PhysicallyBasedMaterial.BentNormal](physicallybasedmaterial/bentnormal-swift.property.md)
  The bent normal map for the entity.
- [var enableSpecularOcclusion: Bool](physicallybasedmaterial/enablespecularocclusion.md)
  Enables specular occlusion computations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/physicallybasedmaterial/bentnormal-swift.struct)*