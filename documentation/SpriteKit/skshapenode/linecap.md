# lineCap

**Framework**: SpriteKit  
**Kind**: property  
**Role**: Instance Property

The style used to render the endpoints of the stroked portion of the shape node.

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
var lineCap: CGLineCap { get set }
```

```objc
@property (nonatomic) CGLineCap lineCap;
```

#### Discussion

The default value is [`CGLineCap.butt`](../../CoreGraphics/cglinecap/butt.md). See [`CGLineCap`](../../CoreGraphics/cglinecap.md).

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
- [var lineJoin: CGLineJoin](./linejoin.md)
  The junction type used when the stroked portion of the shape node is rendered.
- [var miterLimit: CGFloat](./miterlimit.md)
  The miter limit to use when the line is stroked using a miter join style.
- [var isAntialiased: Bool](./isantialiased.md)
  A Boolean value that determines whether the stroked path is smoothed when drawn.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skshapenode/linecap)*