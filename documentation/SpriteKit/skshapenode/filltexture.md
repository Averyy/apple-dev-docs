# fillTexture

**Framework**: SpriteKit  
**Kind**: property  
**Role**: Instance Property

The texture used to fill the shape.

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
var fillTexture: SKTexture? { get set }
```

```objc
@property (nonatomic, retain, nullable) SKTexture * fillTexture;
```

## Mentions

- [Controlling Shape Drawing with Shaders](../controlling-shape-drawing-with-shaders.md)

#### Discussion

The default value is `nil`. If a fill texture is specified, the shape node is rendered using that texture blended with the [`fillColor`](./fillcolor.md).

> ❗ **Important**:  The default fill color of a [`SKShapeNode`](../skshapenode.md) is `SKColor.clear`. Since the fill texture is blended with the fill color, [`fillColor`](./fillcolor.md) needs to be set to a non-clear color for it to display. For example, to display the texture without any color blend effects, set [`fillColor`](./fillcolor.md) to `SKColor.white`.

## See Also

### Filling a Shape
- [var fillColor: UIColor](./fillcolor.md)
  The color used to fill the shape.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skshapenode/filltexture)*