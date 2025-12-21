# contentsGravity

**Framework**: Core Animation  
**Kind**: property

A constant that specifies how the layer’s contents are positioned or scaled within its bounds.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var contentsGravity: CALayerContentsGravity { get set }
```

#### Discussion

The possible values for this property are listed in [`Contents Gravity Values`](contents-gravity-values.md).

The default value of this property is [`resize`](calayercontentsgravity/resize.md).

> ❗ **Important**:  The naming of contents gravity constants is based on the direction of the vertical axis.  If you are using gravity constants with a vertical component, e.g. [`top`](calayercontentsgravity/top.md), you should also check the layer’s [`contentsAreFlipped()`](calayer/contentsareflipped().md). When this is [`true`](https://developer.apple.com/documentation/Swift/true), [`top`](calayercontentsgravity/top.md) aligns contents to the bottom of the layer and [`bottom`](calayercontentsgravity/bottom.md) aligns content to the top of the layer. The default coordinate system for views in macOS and iOS differ in the orientation of the vertical axis: in macOS, the default coordinate system has its origin at the lower left of the drawing area and positive values extend up from it, and in iOS the default coordinate system has its origin at the upper left of the drawing area and positive values extend down from it. For more information, see [`Coordinate system`](https://developer.apple.comhttps://developer.apple.com/library/content/documentation/General/Conceptual/Devpedia-CocoaApp/CoordinateSystem.html).

[`Figure 1`](calayer/1410872-contentsgravity#2851774.md) shows four examples of the effect of setting different values for a layer’s [`contentsGravity`](calayer/contentsgravity.md) property.

![Different effects of setting a layer’s contents gravity](https://docs-assets.developer.apple.com/published/55a0f37cf74b8a24023604ae6c89ade1/media-2851774%402x.png)

1. Contents gravity is [`resize`](calayercontentsgravity/resize.md) - the default
2. Contents gravity is [`center`](calayercontentsgravity/center.md)
3. Contents gravity is [`contentsAreFlipped()`](calayer/contentsareflipped().md) `?` [`top`](calayercontentsgravity/top.md) : [`bottom`](calayercontentsgravity/bottom.md)
4. Contents gravity is [`contentsAreFlipped()`](calayer/contentsareflipped().md) `?` [`bottomLeft`](calayercontentsgravity/bottomleft.md) : [`topLeft`](calayercontentsgravity/topleft.md)

## See Also

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
- [var shadowOffset: CGSize](calayer/shadowoffset.md)
  The offset (in points) of the layer’s shadow. Animatable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/calayer/contentsgravity)*