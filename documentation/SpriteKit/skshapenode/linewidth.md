# lineWidth

**Framework**: SpriteKit  
**Kind**: property  
**Role**: Instance Property

The width used to stroke the path.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
var lineWidth: CGFloat { get set }
```

```objc
@property (nonatomic) CGFloat lineWidth;
```

## Mentions

- [Getting Started with Shape Nodes](../getting-started-with-shape-nodes.md)

## Discussion

A line width larger than `2.0` may cause rendering artifacts in the final rendered image. The default value is `1.0`.

## See Also

### Stroking a Shape
- [var strokeColor: UIColor](./strokecolor.md)
  The color used to stroke the shape.
- [var strokeTexture: SKTexture?](./stroketexture.md)
  The texture used to stroke the shape.
- [var glowWidth: CGFloat](./glowwidth.md)
  A glow that extends outward from the stroked line.
- [var lineCap: CGLineCap](./linecap.md)
  The style used to render the endpoints of the stroked portion of the shape node.
- [var lineJoin: CGLineJoin](./linejoin.md)
  The junction type used when the stroked portion of the shape node is rendered.
- [var miterLimit: CGFloat](./miterlimit.md)
  The miter limit to use when the line is stroked using a miter join style.
- [var isAntialiased: Bool](./isantialiased.md)
  A Boolean value that determines whether the stroked path is smoothed when drawn.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skshapenode/linewidth)*