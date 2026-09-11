# preferFastExport

**Framework**: RealityKit  
**Kind**: property

Expedite the reality file export when possible.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
static var preferFastExport: Entity.WriteOptions { get }
```

#### Discussion

This option may disable archival compression during the export process. This reduces the time required to write a reality file but produces a larger file on disk. Use this option when rapid iteration is more important than file size, such as during development in a content authoring tool.

## See Also

- [static func preferSmallTextureFiles(quality: Entity.WriteOptions.TextureQuality) -> Entity.WriteOptions](entity/writeoptions/prefersmalltexturefiles(quality:).md)
  Reduce textures’ file size while preserving its dimensions.
- [Entity.WriteOptions.TextureQuality](entity/writeoptions/texturequality.md)
  A texture quality level.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/entity/writeoptions/preferfastexport)*