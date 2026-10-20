# MDLMaterialTextureWrapMode

**Framework**: Model I/O  
**Kind**: enum  
**Role**: Enumeration

Modes for sampling textures at coordinates outside the texture bounds, used by the [`sWrapMode`](./mdltexturefilter/swrapmode.md), [`tWrapMode`](./mdltexturefilter/twrapmode.md), and [`rWrapMode`](./mdltexturefilter/rwrapmode.md) properties.

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

```c
enum MDLMaterialTextureWrapMode : NSUInteger;
```

## Topics

### Constants
- [MDLMaterialTextureWrapMode.clamp](./mdlmaterialtexturewrapmode/clamp.md)
  Sampling at any texture coordinate outside the `0.0` to `1.0` range returns the texel color from the nearest edge.
- [MDLMaterialTextureWrapMode.repeat](./mdlmaterialtexturewrapmode/repeat.md)
  Sampling at texture coordinates outside the `0.0` to `1.0` range results in a repeated tiling effect.
- [MDLMaterialTextureWrapMode.mirror](./mdlmaterialtexturewrapmode/mirror.md)
  Sampling at texture coordinates outside the `0.0` to `1.0` range results in a mirrored tiling effect.
### Initializers
- [init?(rawValue: UInt)](./mdlmaterialtexturewrapmode/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Constants
- [enum MDLMaterialTextureFilterMode](./mdlmaterialtexturefiltermode.md)
  Modes for sampling textures at coordinates between texels, used by the [`minFilter`](./mdltexturefilter/minfilter.md) and [`magFilter`](./mdltexturefilter/magfilter.md) properties.
- [enum MDLMaterialMipMapFilterMode](./mdlmaterialmipmapfiltermode.md)
  Modes for sampling textures at sizes between mipmap levels, used by the [`mipFilter`](./mdltexturefilter/mipfilter.md) property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlmaterialtexturewrapmode)*