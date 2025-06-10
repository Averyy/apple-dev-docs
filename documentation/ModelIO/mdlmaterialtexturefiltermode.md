# MDLMaterialTextureFilterMode

**Framework**: Model I/O  
**Kind**: enum

Modes for sampling textures at coordinates between texels, used by the [`minFilter`](mdltexturefilter/minfilter.md) and [`magFilter`](mdltexturefilter/magfilter.md) properties.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.0+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
enum MDLMaterialTextureFilterMode
```

## Topics

### Constants
- [MDLMaterialTextureFilterMode.nearest](mdlmaterialtexturefiltermode/nearest.md)
  Sampling at texture coordinates between texels should return the value of the nearest texel.
- [MDLMaterialTextureFilterMode.linear](mdlmaterialtexturefiltermode/linear.md)
  Sampling at texture coordinates between texels should linearly interpolate between texel values.
### Initializers
- [init?(rawValue: UInt)](mdlmaterialtexturefiltermode/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [enum MDLMaterialTextureWrapMode](mdlmaterialtexturewrapmode.md)
  Modes for sampling textures at coordinates outside the texture bounds, used by the [`sWrapMode`](mdltexturefilter/swrapmode.md), [`tWrapMode`](mdltexturefilter/twrapmode.md), and [`rWrapMode`](mdltexturefilter/rwrapmode.md) properties.
- [enum MDLMaterialMipMapFilterMode](mdlmaterialmipmapfiltermode.md)
  Modes for sampling textures at sizes between mipmap levels, used by the [`mipFilter`](mdltexturefilter/mipfilter.md) property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlmaterialtexturefiltermode)*