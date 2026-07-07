# preferSmallTextureFiles(quality:)

**Framework**: RealityKit  
**Kind**: method

Reduce textures’ file size while preserving its dimensions.

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

The returned option instructs RealityKit to encode textures using smaller file representations. RealityKit selects the best strategy for each texture based on context, which may include lossy image encoding, preserving the original source image, or regenerating mipmaps.

> ⚠️ **Warning**: While writing smaller texture files reduces the size of reality files on disk, loading those textures can increase memory usage and load times compared to the default compressed format. Larger memory region can also consume more power during rendering due to increased cache pressure.

> **Note**: RealityKit ignores this option for textures created with [`none`](textureresource/compression/none.md).

## See Also

- [static var preferFastExport: Entity.WriteOptions](entity/writeoptions/preferfastexport.md)
  Expedite the reality file export when possible.
- [Entity.WriteOptions.TextureQuality](entity/writeoptions/texturequality.md)
  A texture quality level.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/entity/writeoptions/prefersmalltexturefiles(quality:))*