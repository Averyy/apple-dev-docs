# frame

**Framework**: Quartzcore  
**Kind**: property

The layer’s frame rectangle.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var frame: CGRect { get set }
```

#### Discussion

The frame rectangle is position and size of the layer specified in the superlayer’s coordinate space. For layers, the frame rectangle is a computed property that is derived from the values in the[`bounds`](calayer/bounds.md), [`anchorPoint`](calayer/anchorpoint.md) and [`position`](calayer/position.md) properties. When you assign a new value to this property, the layer changes its [`position`](calayer/position.md) and [`bounds`](calayer/bounds.md) properties to match the rectangle you specified. The values of each coordinate in the rectangle are measured in points.

Do not set the frame if the [`transform`](calayer/transform.md) property applies a rotation transform that is not a multiple of 90 degrees.

For more information about the relationship between the [`frame`](calayer/frame.md), [`bounds`](calayer/bounds.md), [`anchorPoint`](calayer/anchorpoint.md) and [`position`](calayer/position.md) properties, see [`Core Animation Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CoreAnimation_guide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40004514).

> **Note**:  The `frame` property is not directly animatable. Instead you should animate the appropriate combination of the [`bounds`](calayer/bounds.md), [`anchorPoint`](calayer/anchorpoint.md) and [`position`](calayer/position.md) properties to achieve the desired result.

## See Also

- [var bounds: CGRect](calayer/bounds.md)
  The layer’s bounds rectangle. Animatable.
- [var position: CGPoint](calayer/position.md)
  The layer’s position in its superlayer’s coordinate space. Animatable.
- [var zPosition: CGFloat](calayer/zposition.md)
  The layer’s position on the z axis. Animatable.
- [var anchorPointZ: CGFloat](calayer/anchorpointz.md)
  The anchor point for the layer’s position along the z axis. Animatable.
- [var anchorPoint: CGPoint](calayer/anchorpoint.md)
  Defines the anchor point of the layer’s bounds rectangle. Animatable.
- [var contentsScale: CGFloat](calayer/contentsscale.md)
  The scale factor applied to the layer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/QuartzCore/calayer/frame)*