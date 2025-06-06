# fillTexture

**Framework**: SpriteKit  
**Kind**: property

The texture used to fill the shape.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
var fillTexture: SKTexture? { get set }
```

## Mentions

- [Controlling Shape Drawing with Shaders](controlling-shape-drawing-with-shaders.md)

#### Discussion

The default value is `nil`. If a fill texture is specified, the shape node is rendered using that texture blended with the [`fillColor`](skshapenode/fillcolor.md).

> ❗ **Important**:  The default fill color of a [`SKShapeNode`](skshapenode.md) is `SKColor.clear`. Since the fill texture is blended with the fill color, [`fillColor`](skshapenode/fillcolor.md) needs to be set to a non-clear color for it to display. For example, to display the texture without any color blend effects, set [`fillColor`](skshapenode/fillcolor.md) to `SKColor.white`.

 The default fill color of a [`SKShapeNode`](skshapenode.md) is `SKColor.clear`. Since the fill texture is blended with the fill color, [`fillColor`](skshapenode/fillcolor.md) needs to be set to a non-clear color for it to display. For example, to display the texture without any color blend effects, set [`fillColor`](skshapenode/fillcolor.md) to `SKColor.white`.

## See Also

- [var fillColor: UIColor](skshapenode/fillcolor.md)
  The color used to fill the shape.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skshapenode/filltexture)*