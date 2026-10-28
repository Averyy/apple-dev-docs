# shadowRadius

**Framework**: Core Animation  
**Kind**: property  
**Role**: Instance Property

The blur radius (in points) used to render the layer’s shadow. Animatable.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var shadowRadius: CGFloat { get set }
```

```objc
@property CGFloat shadowRadius;
```

## Discussion

You specify the radius The default value of this property is 3.0.

## See Also

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
- [var shadowOffset: CGSize](./shadowoffset.md)
  The offset (in points) of the layer’s shadow. Animatable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/calayer/shadowradius)*