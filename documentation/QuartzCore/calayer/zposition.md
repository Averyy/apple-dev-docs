# zPosition

**Framework**: Core Animation  
**Kind**: property  
**Role**: Instance Property

The layer’s position on the z axis. Animatable.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var zPosition: CGFloat { get set }
```

```objc
@property CGFloat zPosition;
```

#### Discussion

The default value of this property is `0`. Changing the value of this property changes the front-to-back ordering of layers onscreen. Higher values place this layer visually closer to the viewer than layers with lower values. This can affect the visibility of layers whose frame rectangles overlap.

The value of this property is measured in points. The range of this property is single-precision, floating-point `-`[`greatestFiniteMagnitude`](../../Swift/float/greatestfinitemagnitude.md) to [`greatestFiniteMagnitude`](../../Swift/float/greatestfinitemagnitude.md).

## See Also

### Modifying the layer geometry
- [var frame: CGRect](./frame.md)
  The layer’s frame rectangle.
- [var bounds: CGRect](./bounds.md)
  The layer’s bounds rectangle. Animatable.
- [var position: CGPoint](./position.md)
  The layer’s position in its superlayer’s coordinate space. Animatable.
- [var anchorPointZ: CGFloat](./anchorpointz.md)
  The anchor point for the layer’s position along the z axis. Animatable.
- [var anchorPoint: CGPoint](./anchorpoint.md)
  Defines the anchor point of the layer’s bounds rectangle. Animatable.
- [var contentsScale: CGFloat](./contentsscale.md)
  The scale factor applied to the layer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/calayer/zposition)*