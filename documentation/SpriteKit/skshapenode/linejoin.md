# lineJoin

**Framework**: SpriteKit  
**Kind**: property  
**Role**: Instance Property

The junction type used when the stroked portion of the shape node is rendered.

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
var lineJoin: CGLineJoin { get set }
```

```objc
@property (nonatomic) CGLineJoin lineJoin;
```

#### Discussion

The default value is [`CGLineJoin.bevel`](../../CoreGraphics/cglinejoin/bevel.md). See [`CGLineJoin`](../../CoreGraphics/cglinejoin.md).

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
- [var miterLimit: CGFloat](./miterlimit.md)
  The miter limit to use when the line is stroked using a miter join style.
- [var isAntialiased: Bool](./isantialiased.md)
  A Boolean value that determines whether the stroked path is smoothed when drawn.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skshapenode/linejoin)*