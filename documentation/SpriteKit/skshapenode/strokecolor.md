# strokeColor

**Framework**: SpriteKit  
**Kind**: property  
**Role**: Instance Property

The color used to stroke the shape.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```swift
var strokeColor: UIColor { get set }
```

*macOS*

```swift
var strokeColor: NSColor { get set }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, retain) UIColor * strokeColor;
```

*macOS*

```objc
@property (nonatomic, retain) NSColor * strokeColor;
```

## Mentions

- [Getting Started with Shape Nodes](../getting-started-with-shape-nodes.md)

#### Discussion

The default stroke color is `[SKColor whiteColor]`. If you do not want to stroke the shape, use `[SKColor clearColor].`

## See Also

### Stroking a Shape
- [var lineWidth: CGFloat](./linewidth.md)
  The width used to stroke the path.
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

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skshapenode/strokecolor)*