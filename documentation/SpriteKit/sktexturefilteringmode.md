# SKTextureFilteringMode

**Framework**: SpriteKit  
**Kind**: enum  
**Role**: Enumeration

Texture filtering modes to use when the texture is drawn in a size other than its native size.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
enum SKTextureFilteringMode
```

```c
enum SKTextureFilteringMode : NSInteger;
```

## Topics

### Constants
- [SKTextureFilteringMode.nearest](./sktexturefilteringmode/nearest.md)
  Each pixel is drawn using the nearest point in the texture. This mode is faster, but the results are often pixelated.
- [SKTextureFilteringMode.linear](./sktexturefilteringmode/linear.md)
  Each pixel is drawn by using a linear filter of multiple texels in the texture. This mode produces higher quality results but may be slower.
### Initializers
- [init?(rawValue: Int)](./sktexturefilteringmode/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Configuring a Texture’s Behavior for Scaling
- [var filteringMode: SKTextureFilteringMode](./sktexture/filteringmode.md)
  The filtering mode used when the size of a sprite drawn with the texture is not drawn at the texture’s native size.
- [var usesMipmaps: Bool](./sktexture/usesmipmaps.md)
  A Boolean value that indicates whether the texture attempts to generate mipmaps.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/sktexturefilteringmode)*