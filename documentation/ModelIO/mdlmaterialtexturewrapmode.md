# MDLMaterialTextureWrapMode

**Framework**: Model I/O  
**Kind**: enum

Modes for sampling textures at coordinates outside the texture bounds, used by the [`sWrapMode`](mdltexturefilter/swrapmode.md), [`tWrapMode`](mdltexturefilter/twrapmode.md), and [`rWrapMode`](mdltexturefilter/rwrapmode.md) properties.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.0+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
enum MDLMaterialTextureWrapMode
```

## Topics

### Constants
- [MDLMaterialTextureWrapMode.clamp](mdlmaterialtexturewrapmode/clamp.md)
  Sampling at any texture coordinate outside the `0.0` to `1.0` range returns the texel color from the nearest edge.
- [MDLMaterialTextureWrapMode.repeat](mdlmaterialtexturewrapmode/repeat.md)
  Sampling at texture coordinates outside the `0.0` to `1.0` range results in a repeated tiling effect.
- [MDLMaterialTextureWrapMode.mirror](mdlmaterialtexturewrapmode/mirror.md)
  Sampling at texture coordinates outside the `0.0` to `1.0` range results in a mirrored tiling effect.
### Initializers
- [init?(rawValue: UInt)](mdlmaterialtexturewrapmode/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [enum MDLMaterialTextureFilterMode](mdlmaterialtexturefiltermode.md)
  Modes for sampling textures at coordinates between texels, used by the [`minFilter`](mdltexturefilter/minfilter.md) and [`magFilter`](mdltexturefilter/magfilter.md) properties.
- [enum MDLMaterialMipMapFilterMode](mdlmaterialmipmapfiltermode.md)
  Modes for sampling textures at sizes between mipmap levels, used by the [`mipFilter`](mdltexturefilter/mipfilter.md) property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlmaterialtexturewrapmode)*