# lineCap

**Framework**: SpriteKit  
**Kind**: property

The style used to render the endpoints of the stroked portion of the shape node.

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
var lineCap: CGLineCap { get set }
```

#### Discussion

The default value is [`CGLineCap.butt`](https://developer.apple.com/documentation/CoreGraphics/CGLineCap/butt). See [`CGLineCap`](https://developer.apple.com/documentation/CoreGraphics/CGLineCap).

## See Also

- [var lineWidth: CGFloat](skshapenode/linewidth.md)
  The width used to stroke the path.
- [var strokeColor: UIColor](skshapenode/strokecolor.md)
  The color used to stroke the shape.
- [var strokeTexture: SKTexture?](skshapenode/stroketexture.md)
  The texture used to stroke the shape.
- [var glowWidth: CGFloat](skshapenode/glowwidth.md)
  A glow that extends outward from the stroked line.
- [var lineJoin: CGLineJoin](skshapenode/linejoin.md)
  The junction type used when the stroked portion of the shape node is rendered.
- [var miterLimit: CGFloat](skshapenode/miterlimit.md)
  The miter limit to use when the line is stroked using a miter join style.
- [var isAntialiased: Bool](skshapenode/isantialiased.md)
  A Boolean value that determines whether the stroked path is smoothed when drawn.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skshapenode/linecap)*