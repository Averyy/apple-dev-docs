# colorBlendFactor

**Framework**: SpriteKit  
**Kind**: property  
**Role**: Instance Property

Controls the blending between the texture and the tile map object’s [`color`](./color.md). Values are clamped between zero and one where zero has no color blending and one has the maximum color blending.

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
var colorBlendFactor: CGFloat { get set }
```

```objc
@property (nonatomic) CGFloat colorBlendFactor;
```

## See Also

### Tinting a Tile Map
- [var color: UIColor](./color.md)
  The base color for the tile map. The influence of the color over the tile map node’s textures is controlled by [`colorBlendFactor`](./colorblendfactor.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/sktilemapnode/colorblendfactor)*