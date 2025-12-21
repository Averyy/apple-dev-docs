# allowsGroupOpacity

**Framework**: Core Animation  
**Kind**: property

A Boolean indicating whether the layer is allowed to composite itself as a group separate from its parent.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var allowsGroupOpacity: Bool { get set }
```

#### Discussion

When the value is [`true`](https://developer.apple.com/documentation/Swift/true) and the layer’s opacity property value is less than `1.0`, the layer is allowed to composite itself as a group separate from its parent. This gives correct results when the layer contains multiple opaque components, but may reduce performance.

The default value is read from the boolean `UIViewGroupOpacity` property in the main bundle’s `Info.plist` file. If no value is found, the default value is [`true`](https://developer.apple.com/documentation/Swift/true) for apps linked against the iOS 7 SDK or later and [`false`](https://developer.apple.com/documentation/Swift/false) for apps linked against an earlier SDK.

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/calayer/allowsgroupopacity)*