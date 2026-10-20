# fillColor

**Framework**: SpriteKit  
**Kind**: property  
**Role**: Instance Property

The color used to fill the shape.

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
var fillColor: UIColor { get set }
```

*macOS*

```swift
var fillColor: NSColor { get set }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, retain) UIColor * fillColor;
```

*macOS*

```objc
@property (nonatomic, retain) NSColor * fillColor;
```

## Mentions

- [Controlling Shape Drawing with Shaders](../controlling-shape-drawing-with-shaders.md)
- [Getting Started with Shape Nodes](../getting-started-with-shape-nodes.md)

#### Discussion

The default fill color is `[SKColor clearColor]`, which means the shape is not filled.

## See Also

### Filling a Shape
- [var fillTexture: SKTexture?](./filltexture.md)
  The texture used to fill the shape.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skshapenode/fillcolor)*