# Entity.WriteOptions.TextureQuality

**Framework**: RealityKit  
**Kind**: struct

A texture quality level.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct TextureQuality
```

## Topics

### Choosing a quality level
- [static var medium: Entity.WriteOptions.TextureQuality](entity/writeoptions/texturequality/medium.md)
  Reduces more the texture file size. RealityKit might not preserve fine details to reach a small file size.
- [static var low: Entity.WriteOptions.TextureQuality](entity/writeoptions/texturequality/low.md)
  Aggressively reduces the texture file size. RealityKit can suppress some visual details to reach the smallest file size.
### Type Properties
- [static var standard: Entity.WriteOptions.TextureQuality](entity/writeoptions/texturequality/standard.md)
  Reduces the texture file size while preserving most details.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [static var preferFastExport: Entity.WriteOptions](entity/writeoptions/preferfastexport.md)
  Expedite the reality file export when possible. This may disable reality file compression, resulting in larger file size.
- [static func preferSmallTextureFiles(quality: Entity.WriteOptions.TextureQuality) -> Entity.WriteOptions](entity/writeoptions/prefersmalltexturefiles(quality:).md)
  Reduce textures’ file size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/entity/writeoptions/texturequality)*