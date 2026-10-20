# Entity.WriteOptions.TextureQuality

**Framework**: RealityKit  
**Kind**: struct  
**Role**: Structure

A texture quality level.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+

## Declaration

```swift
struct TextureQuality
```

## Topics

### Choosing a quality level
- [static var medium: Entity.WriteOptions.TextureQuality](./texturequality/medium.md)
  Reduces more the texture file size. RealityKit might not preserve fine details to reach a small file size.
- [static var low: Entity.WriteOptions.TextureQuality](./texturequality/low.md)
  Aggressively reduces the texture file size. RealityKit can suppress some visual details to reach the smallest file size.
### Type Properties
- [static var standard: Entity.WriteOptions.TextureQuality](./texturequality/standard.md)
  Reduces the texture file size while preserving most details.

## Relationships

### Conforms To
- [Equatable](../../../Swift/equatable.md)
- [Hashable](../../../Swift/hashable.md)
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)

## See Also

### Configuring export options
- [static var preferFastExport: Entity.WriteOptions](./preferfastexport.md)
  Expedite the reality file export when possible.
- [static func preferSmallTextureFiles(quality: Entity.WriteOptions.TextureQuality) -> Entity.WriteOptions](./prefersmalltexturefiles%28quality%29.md)
  Reduce textures’ file size while preserving its dimensions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/entity/writeoptions/texturequality)*