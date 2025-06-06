# position

**Framework**: Core Animation  
**Kind**: property

The layer’s position in its superlayer’s coordinate space. Animatable.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var position: CGPoint { get set }
```

#### Discussion

The value of this property is specified in points and is always specified relative to the value in the [`anchorPoint`](calayer/anchorpoint.md) property. For new standalone layers, the default position is set to (0.0, 0.0). Changing the [`frame`](calayer/frame.md) property also updates the value in this property.

For more information about the relationship between the [`frame`](calayer/frame.md), [`bounds`](calayer/bounds.md), [`anchorPoint`](calayer/anchorpoint.md) and [`position`](calayer/position.md) properties, see [`Core Animation Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CoreAnimation_guide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40004514).

## See Also

- [var frame: CGRect](calayer/frame.md)
  The layer’s frame rectangle.
- [var bounds: CGRect](calayer/bounds.md)
  The layer’s bounds rectangle. Animatable.
- [var zPosition: CGFloat](calayer/zposition.md)
  The layer’s position on the z axis. Animatable.
- [var anchorPointZ: CGFloat](calayer/anchorpointz.md)
  The anchor point for the layer’s position along the z axis. Animatable.
- [var anchorPoint: CGPoint](calayer/anchorpoint.md)
  Defines the anchor point of the layer’s bounds rectangle. Animatable.
- [var contentsScale: CGFloat](calayer/contentsscale.md)
  The scale factor applied to the layer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/calayer/position)*