# filteringMode

**Framework**: SpriteKit  
**Kind**: property

The filtering mode used when the size of a sprite drawn with the texture is not drawn at the texture’s native size.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
var filteringMode: SKTextureFilteringMode { get set }
```

#### Discussion

The possible values for this property are listed in [`SKTextureFilteringMode`](sktexturefilteringmode.md). The default value is [`SKTextureFilteringMode.linear`](sktexturefilteringmode/linear.md) where each pixel is drawn by using a linear filter of multiple texels in the texture. The other option is [`SKTextureFilteringMode.nearest`](sktexturefilteringmode/nearest.md) where each pixel is drawn using the nearest point in the texture.

The figure below shows the effect of different filtering modes. The rabbit texture (original on left) has been scaled up five times. Node 1 has been scaled using [`SKTextureFilteringMode.nearest`](sktexturefilteringmode/nearest.md) and node 2 has been scaled with [`SKTextureFilteringMode.linear`](sktexturefilteringmode/linear.md).

![The effect of filtering modes on a scaled texture](https://docs-assets.developer.apple.com/published/e83b4c005376dbf55f125ba9e52b414c/media-2668828%402x.png)

## See Also

- [enum SKTextureFilteringMode](sktexturefilteringmode.md)
  Texture filtering modes to use when the texture is drawn in a size other than its native size.
- [var usesMipmaps: Bool](sktexture/usesmipmaps.md)
  A Boolean value that indicates whether the texture attempts to generate mipmaps.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/sktexture/filteringmode)*