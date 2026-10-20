# bounds

**Framework**: Core Animation  
**Kind**: property  
**Role**: Instance Property

The layer’s bounds rectangle. Animatable.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var bounds: CGRect { get set }
```

```objc
@property CGRect bounds;
```

#### Discussion

The bounds rectangle is the origin and size of the layer in its own coordinate space. When you create a new standalone layer, the default value for this property is an empty rectangle, which you must change before using the layer. The values of each coordinate in the rectangle are measured in points.

For more information about the relationship between the [`frame`](./frame.md), [`bounds`](./bounds.md), [`anchorPoint`](./anchorpoint.md) and [`position`](./position.md) properties, see [Core Animation Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CoreAnimation_guide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40004514).

## See Also

### Modifying the layer geometry
- [var frame: CGRect](./frame.md)
  The layer’s frame rectangle.
- [var position: CGPoint](./position.md)
  The layer’s position in its superlayer’s coordinate space. Animatable.
- [var zPosition: CGFloat](./zposition.md)
  The layer’s position on the z axis. Animatable.
- [var anchorPointZ: CGFloat](./anchorpointz.md)
  The anchor point for the layer’s position along the z axis. Animatable.
- [var anchorPoint: CGPoint](./anchorpoint.md)
  Defines the anchor point of the layer’s bounds rectangle. Animatable.
- [var contentsScale: CGFloat](./contentsscale.md)
  The scale factor applied to the layer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/calayer/bounds)*