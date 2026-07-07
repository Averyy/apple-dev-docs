# TextureSamplingQuality

**Framework**: RealityKit  
**Kind**: enum

A discrete trade-off between generation time and texture quality, used by [`SkyboxGenerator`](skyboxgenerator.md) and [`ImageBasedLightTextureGenerator`](imagebasedlighttexturegenerator.md).

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
enum TextureSamplingQuality
```

#### Overview

Higher quality reduces noise and banding at the cost of proportionally more GPU work.

## Topics

### Specifying the sampling quality
- [TextureSamplingQuality.low](texturesamplingquality/low.md)
  Low sampling rates can result in higher noise in high-frequency areas and banding in low-frequency gradients.
- [TextureSamplingQuality.normal](texturesamplingquality/normal.md)
  Computes with regular sampling rates.
- [TextureSamplingQuality.high](texturesamplingquality/high.md)
  Computes with high sampling rates, reducing texture noise in high-frequency areas.
- [TextureSamplingQuality.veryHigh](texturesamplingquality/veryhigh.md)
  Computes with very high sampling rates.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class ImageBasedLightTextureGenerator](imagebasedlighttexturegenerator.md)
  An object that generates image-based-lighting diffuse and specular cube textures from a skybox.
- [class SkyboxGenerator](skyboxgenerator.md)
  An object that generates a skybox cube texture from an equirectangular source.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/texturesamplingquality)*