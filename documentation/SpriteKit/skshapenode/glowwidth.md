# glowWidth

**Framework**: SpriteKit  
**Kind**: property

A glow that extends outward from the stroked line.

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
var glowWidth: CGFloat { get set }
```

## Mentions

- [Getting Started with Shape Nodes](getting-started-with-shape-nodes.md)

#### Discussion

The default value is `0.0`, which means no glow is added. The glow color is determined by [`strokeColor`](skshapenode/strokecolor.md).

## See Also

- [var lineWidth: CGFloat](skshapenode/linewidth.md)
  The width used to stroke the path.
- [var strokeColor: UIColor](skshapenode/strokecolor.md)
  The color used to stroke the shape.
- [var strokeTexture: SKTexture?](skshapenode/stroketexture.md)
  The texture used to stroke the shape.
- [var lineCap: CGLineCap](skshapenode/linecap.md)
  The style used to render the endpoints of the stroked portion of the shape node.
- [var lineJoin: CGLineJoin](skshapenode/linejoin.md)
  The junction type used when the stroked portion of the shape node is rendered.
- [var miterLimit: CGFloat](skshapenode/miterlimit.md)
  The miter limit to use when the line is stroked using a miter join style.
- [var isAntialiased: Bool](skshapenode/isantialiased.md)
  A Boolean value that determines whether the stroked path is smoothed when drawn.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skshapenode/glowwidth)*