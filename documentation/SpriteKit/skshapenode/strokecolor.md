# strokeColor

**Framework**: SpriteKit  
**Kind**: property

The color used to stroke the shape.

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
var strokeColor: UIColor { get set }
```

## Mentions

- [Getting Started with Shape Nodes](getting-started-with-shape-nodes.md)

#### Discussion

The default stroke color is `[SKColor whiteColor]`. If you do not want to stroke the shape, use `[SKColor clearColor].`

## See Also

- [var lineWidth: CGFloat](skshapenode/linewidth.md)
  The width used to stroke the path.
- [var strokeTexture: SKTexture?](skshapenode/stroketexture.md)
  The texture used to stroke the shape.
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

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skshapenode/strokecolor)*