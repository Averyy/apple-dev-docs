# TextureSamplingQuality

**Framework**: RealityKit  
**Kind**: enum

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
enum TextureSamplingQuality
```

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
  An object for generating based light textures. Computes an image based light’s diffuse and specular textures from a skybox texture.
- [class SkyboxGenerator](skyboxgenerator.md)
  An object for generating skybox textures.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/texturesamplingquality)*