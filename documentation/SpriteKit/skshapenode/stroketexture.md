# strokeTexture

**Framework**: SpriteKit  
**Kind**: property

The texture used to stroke the shape.

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
@MainActor
var strokeTexture: SKTexture? { get set }
```

#### Discussion

The default value is `nil`. If a stroke texture is specified, the [`strokeColor`](skshapenode/strokecolor.md) property is ignored and the stroked portion of the shape node is rendered using the texture instead.

## See Also

- [var lineWidth: CGFloat](skshapenode/linewidth.md)
  The width used to stroke the path.
- [var strokeColor: UIColor](skshapenode/strokecolor.md)
  The color used to stroke the shape.
- [var glowWidth: CGFloat](skshapenode/glowwidth.md)
  A glow that extends outward from the stroked line.
- [var lineCap: CGLineCap](skshapenode/linecap.md)
  The style used to render the endpoints of the stroked portion of the shape node.
- [var lineJoin: CGLineJoin](skshapenode/linejoin.md)
  The junction type used when the stroked portion of the shape node is rendered.
- [var miterLimit: CGFloat](skshapenode/miterlimit.md)
  The miter limit to use when the line is stroked using a miter join style.
- [var isAntialiased: Bool](skshapenode/isantialiased.md)
  A Boolean value that determines whether the stroked path is smoothed when drawn.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skshapenode/stroketexture)*