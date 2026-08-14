# cornerRadius

**Framework**: Core Animation  
**Kind**: property

The radius to use when drawing rounded corners for the layer’s background. Animatable.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var cornerRadius: CGFloat { get set }
```

#### Discussion

Setting the radius to a value greater than `0.0` causes the layer to begin drawing rounded corners on its background. By default, the corner radius does not apply to the image in the layer’s [`contents`](calayer/contents.md) property; it applies only to the background color and border of the layer. However, setting the [`masksToBounds`](calayer/maskstobounds.md) property to [`true`](https://developer.apple.com/documentation/swift/true) causes the content to be clipped to the rounded corners.

The default value of this property is `0.0`.

## See Also

- [var contentsGravity: CALayerContentsGravity](calayer/contentsgravity.md)
  A constant that specifies how the layer’s contents are positioned or scaled within its bounds.
- [Contents Gravity Values](contents-gravity-values.md)
  The contents gravity constants specify the position of the content object when the layer bounds is larger than the bounds of the content object. They are used by the [`contentsGravity`](calayer/contentsgravity.md) property.
- [var opacity: Float](calayer/opacity.md)
  The opacity of the receiver. Animatable.
- [var isHidden: Bool](calayer/ishidden.md)
  A Boolean indicating whether the layer is displayed. Animatable.
- [var masksToBounds: Bool](calayer/maskstobounds.md)
  A Boolean indicating whether sublayers are clipped to the layer’s bounds. Animatable.
- [var mask: CALayer?](calayer/mask.md)
  An optional layer whose alpha channel is used to mask the layer’s content.
- [var isDoubleSided: Bool](calayer/isdoublesided.md)
  A Boolean indicating whether the layer displays its content when facing away from the viewer. Animatable.
- [var maskedCorners: CACornerMask](calayer/maskedcorners.md)
- [struct CACornerMask](cacornermask.md)
- [var borderWidth: CGFloat](calayer/borderwidth.md)
  The width of the layer’s border. Animatable.
- [var borderColor: CGColor?](calayer/bordercolor.md)
  The color of the layer’s border. Animatable.
- [var backgroundColor: CGColor?](calayer/backgroundcolor.md)
  The background color of the receiver. Animatable.
- [var shadowOpacity: Float](calayer/shadowopacity.md)
  The opacity of the layer’s shadow. Animatable.
- [var shadowRadius: CGFloat](calayer/shadowradius.md)
  The blur radius (in points) used to render the layer’s shadow. Animatable.
- [var shadowOffset: CGSize](calayer/shadowoffset.md)
  The offset (in points) of the layer’s shadow. Animatable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/calayer/cornerradius)*