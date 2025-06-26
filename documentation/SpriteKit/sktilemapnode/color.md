# color

**Framework**: SpriteKit  
**Kind**: property

The base color for the tile map. The influence of the color over the tile map node’s textures is controlled by [`colorBlendFactor`](sktilemapnode/colorblendfactor.md).

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
@MainActor
var color: UIColor { get set }
```

## See Also

- [var colorBlendFactor: CGFloat](sktilemapnode/colorblendfactor.md)
  Controls the blending between the texture and the tile map object’s [`color`](sktilemapnode/color.md). Values are clamped between zero and one where zero has no color blending and one has the maximum color blending.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/sktilemapnode/color)*