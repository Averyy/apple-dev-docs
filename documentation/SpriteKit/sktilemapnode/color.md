# color

**Framework**: SpriteKit  
**Kind**: property  
**Role**: Instance Property

The base color for the tile map. The influence of the color over the tile map node’s textures is controlled by [`colorBlendFactor`](./colorblendfactor.md).

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```swift
var color: UIColor { get set }
```

*macOS*

```swift
var color: NSColor { get set }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, retain) UIColor * color;
```

*macOS*

```objc
@property (nonatomic, retain) NSColor * color;
```

## See Also

### Tinting a Tile Map
- [var colorBlendFactor: CGFloat](./colorblendfactor.md)
  Controls the blending between the texture and the tile map object’s [`color`](./color.md). Values are clamped between zero and one where zero has no color blending and one has the maximum color blending.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/sktilemapnode/color)*