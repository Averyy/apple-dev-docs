# preferSmallTextureFiles(quality:)

**Framework**: RealityKit  
**Kind**: method

Reduce textures’ file size.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
static func preferSmallTextureFiles(quality: Entity.WriteOptions.TextureQuality) -> Entity.WriteOptions
```

#### Discussion

RealityKit reduces the file size while preserving its dimensions. RealityKit can use various strategies to reduce the file size including lossy encoding the texture as an image or storing the original source image. Mipmaps can also be regenerated.

Writing smaller texture files can increase memory usage and load time. Without this option, textures can be written to a compressed pixel format, resulting in larger file sizes but smaller memory usage and load time.

> **Note**: RealityKit ignores this option for textures created with [`none`](textureresource/compression/none.md).

## See Also

- [static var preferFastExport: Entity.WriteOptions](entity/writeoptions/preferfastexport.md)
  Expedite the reality file export when possible. This may disable reality file compression, resulting in larger file size.
- [Entity.WriteOptions.TextureQuality](entity/writeoptions/texturequality.md)
  A texture quality level.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/entity/writeoptions/prefersmalltexturefiles(quality:))*