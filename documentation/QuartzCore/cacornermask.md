# CACornerMask

**Framework**: Core Animation  
**Kind**: struct

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
struct CACornerMask
```

## Topics

### Constants
- [init(rawValue: UInt)](cacornermask/init(rawvalue:).md)
- [static var layerMaxXMaxYCorner: CACornerMask](cacornermask/layermaxxmaxycorner.md)
- [static var layerMaxXMinYCorner: CACornerMask](cacornermask/layermaxxminycorner.md)
- [static var layerMinXMaxYCorner: CACornerMask](cacornermask/layerminxmaxycorner.md)
- [static var layerMinXMinYCorner: CACornerMask](cacornermask/layerminxminycorner.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

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
- [var cornerRadius: CGFloat](calayer/cornerradius.md)
  The radius to use when drawing rounded corners for the layer’s background. Animatable.
- [var maskedCorners: CACornerMask](calayer/maskedcorners.md)
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

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/cacornermask)*