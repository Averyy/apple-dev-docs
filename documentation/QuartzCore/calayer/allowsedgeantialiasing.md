# allowsEdgeAntialiasing

**Framework**: Core Animation  
**Kind**: property  
**Role**: Instance Property

A Boolean indicating whether the layer is allowed to perform edge antialiasing.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var allowsEdgeAntialiasing: Bool { get set }
```

```objc
@property BOOL allowsEdgeAntialiasing;
```

## Discussion

When the value is [`true`](../../Swift/true.md), the layer is allowed to antialias its edges, as requested by the value in the layer’s [`edgeAntialiasingMask`](./edgeantialiasingmask.md) property. The default value is read from the boolean `UIViewEdgeAntialiasing` property in the main bundle’s `Info.plist` file. If no value is found, the default value is [`false`](../../Swift/false.md).

## See Also

### Related Documentation
- [var edgeAntialiasingMask: CAEdgeAntialiasingMask](./edgeantialiasingmask.md)
  A bitmask defining how the edges of the receiver are rasterized.
### Modifying the layer’s appearance
- [var contentsGravity: CALayerContentsGravity](./contentsgravity.md)
  A constant that specifies how the layer’s contents are positioned or scaled within its bounds.
- [Contents Gravity Values](../contents-gravity-values.md)
  The contents gravity constants specify the position of the content object when the layer bounds is larger than the bounds of the content object. They are used by the [`contentsGravity`](./contentsgravity.md) property.
- [var opacity: Float](./opacity.md)
  The opacity of the receiver. Animatable.
- [var isHidden: Bool](./ishidden.md)
  A Boolean indicating whether the layer is displayed. Animatable.
- [var masksToBounds: Bool](./maskstobounds.md)
  A Boolean indicating whether sublayers are clipped to the layer’s bounds. Animatable.
- [var mask: CALayer?](./mask.md)
  An optional layer whose alpha channel is used to mask the layer’s content.
- [var isDoubleSided: Bool](./isdoublesided.md)
  A Boolean indicating whether the layer displays its content when facing away from the viewer. Animatable.
- [var cornerRadius: CGFloat](./cornerradius.md)
  The radius to use when drawing rounded corners for the layer’s background. Animatable.
- [var maskedCorners: CACornerMask](./maskedcorners.md)
- [struct CACornerMask](../cacornermask.md)
- [var borderWidth: CGFloat](./borderwidth.md)
  The width of the layer’s border. Animatable.
- [var borderColor: CGColor?](./bordercolor.md)
  The color of the layer’s border. Animatable.
- [var backgroundColor: CGColor?](./backgroundcolor.md)
  The background color of the receiver. Animatable.
- [var shadowOpacity: Float](./shadowopacity.md)
  The opacity of the layer’s shadow. Animatable.
- [var shadowRadius: CGFloat](./shadowradius.md)
  The blur radius (in points) used to render the layer’s shadow. Animatable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/calayer/allowsedgeantialiasing)*