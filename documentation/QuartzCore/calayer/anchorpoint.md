# anchorPoint

**Framework**: Core Animation  
**Kind**: property  
**Role**: Instance Property

Defines the anchor point of the layer’s bounds rectangle. Animatable.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var anchorPoint: CGPoint { get set }
```

```objc
@property CGPoint anchorPoint;
```

#### Discussion

You specify the value for this property using the unit coordinate space. The default value of this property is (0.5, 0.5), which represents the center of the layer’s bounds rectangle. All geometric manipulations to the view occur about the specified point. For example, applying a rotation transform to a layer with the default anchor point causes the layer to rotate around its center. Changing the anchor point to a different location would cause the layer to rotate around that new point.

For more information about the relationship between the [`frame`](./frame.md), [`bounds`](./bounds.md), [`anchorPoint`](./anchorpoint.md) and [`position`](./position.md) properties, see [Core Animation Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CoreAnimation_guide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40004514).

## See Also

### Modifying the layer geometry
- [var frame: CGRect](./frame.md)
  The layer’s frame rectangle.
- [var bounds: CGRect](./bounds.md)
  The layer’s bounds rectangle. Animatable.
- [var position: CGPoint](./position.md)
  The layer’s position in its superlayer’s coordinate space. Animatable.
- [var zPosition: CGFloat](./zposition.md)
  The layer’s position on the z axis. Animatable.
- [var anchorPointZ: CGFloat](./anchorpointz.md)
  The anchor point for the layer’s position along the z axis. Animatable.
- [var contentsScale: CGFloat](./contentsscale.md)
  The scale factor applied to the layer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/calayer/anchorpoint)*