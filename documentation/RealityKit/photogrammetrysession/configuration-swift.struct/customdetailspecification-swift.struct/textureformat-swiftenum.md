# PhotogrammetrySession.Configuration.CustomDetailSpecification.TextureFormat

**Framework**: RealityKit  
**Kind**: enum

The output format to use for all textures.

**Availability**:
- Mac Catalyst 17.0+
- macOS 14.0+

## Declaration

```swift
enum TextureFormat
```

## Topics

### Enumeration Cases
- [PhotogrammetrySession.Configuration.CustomDetailSpecification.TextureFormat.jpeg(compressionQuality:)](photogrammetrysession/configuration-swift.struct/customdetailspecification-swift.struct/textureformat-swift.enum/jpeg(compressionquality:).md)
  Textures will be output in JPG format with the given `compressionQuality` in the range of [0, 1], where 1.0 is highest quality (least compression, larger size) and 0.0 is the lowest quality (most compression, smallest size).
- [PhotogrammetrySession.Configuration.CustomDetailSpecification.TextureFormat.png](photogrammetrysession/configuration-swift.struct/customdetailspecification-swift.struct/textureformat-swift.enum/png.md)
  Textures will be output in (uncompressed) PNG format.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/photogrammetrysession/configuration-swift.struct/customdetailspecification-swift.struct/textureformat-swift.enum)*