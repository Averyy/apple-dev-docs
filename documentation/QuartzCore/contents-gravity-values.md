# Contents Gravity Values

**Framework**: Core Animation

The contents gravity constants specify the position of the content object when the layer bounds is larger than the bounds of the content object. They are used by the [`contentsGravity`](calayer/contentsgravity.md) property.

## Topics

### Constants
- [static let center: CALayerContentsGravity](calayercontentsgravity/center.md)
  The content is horizontally and vertically centered in the bounds rectangle.
- [static let top: CALayerContentsGravity](calayercontentsgravity/top.md)
  The content is horizontally centered at the top-edge of the bounds rectangle.
- [static let bottom: CALayerContentsGravity](calayercontentsgravity/bottom.md)
  The content is horizontally centered at the bottom-edge of the bounds rectangle.
- [static let left: CALayerContentsGravity](calayercontentsgravity/left.md)
  The content is vertically centered at the left-edge of the bounds rectangle.
- [static let right: CALayerContentsGravity](calayercontentsgravity/right.md)
  The content is vertically centered at the right-edge of the bounds rectangle.
- [static let topLeft: CALayerContentsGravity](calayercontentsgravity/topleft.md)
  The content is positioned in the top-left corner of the bounds rectangle.
- [static let topRight: CALayerContentsGravity](calayercontentsgravity/topright.md)
  The content is positioned in the top-right corner of the bounds rectangle.
- [static let bottomLeft: CALayerContentsGravity](calayercontentsgravity/bottomleft.md)
  The content is positioned in the bottom-left corner of the bounds rectangle.
- [static let bottomRight: CALayerContentsGravity](calayercontentsgravity/bottomright.md)
  The content is positioned in the bottom-right corner of the bounds rectangle.
- [static let resize: CALayerContentsGravity](calayercontentsgravity/resize.md)
  The content is resized to fit the entire bounds rectangle.
- [static let resizeAspect: CALayerContentsGravity](calayercontentsgravity/resizeaspect.md)
  The content is resized to fit the bounds rectangle, preserving the aspect of the content. If the content does not completely fill the bounds rectangle, the content is centered in the partial axis.
- [static let resizeAspectFill: CALayerContentsGravity](calayercontentsgravity/resizeaspectfill.md)
  The content is resized to completely fill the bounds rectangle, while still preserving the aspect of the content. The content is centered in the axis it exceeds.

## See Also

- [var contentsGravity: CALayerContentsGravity](calayer/contentsgravity.md)
  A constant that specifies how the layer’s contents are positioned or scaled within its bounds.
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

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/contents-gravity-values)*