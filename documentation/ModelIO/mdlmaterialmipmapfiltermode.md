# MDLMaterialMipMapFilterMode

**Framework**: Model I/O  
**Kind**: enum  
**Role**: Enumeration

Modes for sampling textures at sizes between mipmap levels, used by the [`mipFilter`](./mdltexturefilter/mipfilter.md) property.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.0+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
enum MDLMaterialMipMapFilterMode
```

```c
enum MDLMaterialMipMapFilterMode : NSUInteger;
```

## Topics

### Constants
- [MDLMaterialMipMapFilterMode.nearest](./mdlmaterialmipmapfiltermode/nearest.md)
  Sampling a texture at a size between mipmap levels should return a texel value from the nearest mipmap level.
- [MDLMaterialMipMapFilterMode.linear](./mdlmaterialmipmapfiltermode/linear.md)
  Sampling a texture at a size between mipmap levels should linearly interpolate between mipmap levels.
### Initializers
- [init?(rawValue: UInt)](./mdlmaterialmipmapfiltermode/init%28rawvalue%29.md)

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
- [enum MDLMaterialTextureWrapMode](./mdlmaterialtexturewrapmode.md)
  Modes for sampling textures at coordinates outside the texture bounds, used by the [`sWrapMode`](./mdltexturefilter/swrapmode.md), [`tWrapMode`](./mdltexturefilter/twrapmode.md), and [`rWrapMode`](./mdltexturefilter/rwrapmode.md) properties.
- [enum MDLMaterialTextureFilterMode](./mdlmaterialtexturefiltermode.md)
  Modes for sampling textures at coordinates between texels, used by the [`minFilter`](./mdltexturefilter/minfilter.md) and [`magFilter`](./mdltexturefilter/magfilter.md) properties.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlmaterialmipmapfiltermode)*