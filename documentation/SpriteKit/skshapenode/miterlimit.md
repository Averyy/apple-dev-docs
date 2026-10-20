# miterLimit

**Framework**: SpriteKit  
**Kind**: property  
**Role**: Instance Property

The miter limit to use when the line is stroked using a miter join style.

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
var miterLimit: CGFloat { get set }
```

```objc
@property (nonatomic) CGFloat miterLimit;
```

#### Discussion

If the line join style is set to [`CGLineJoin.miter`](../../CoreGraphics/cglinejoin/miter.md), SpriteKit uses the miter limit to determine whether the lines should be joined with a bevel instead of a miter. SpriteKit divides the length of the miter by the line width. If the result is greater than the miter limit, SpriteKit converts the style to a bevel.

## See Also

### Stroking a Shape
- [var lineWidth: CGFloat](./linewidth.md)
  The width used to stroke the path.
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
- [var isAntialiased: Bool](./isantialiased.md)
  A Boolean value that determines whether the stroked path is smoothed when drawn.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skshapenode/miterlimit)*