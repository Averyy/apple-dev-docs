# image

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The image displayed in the view’s background.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- tvOS 15.0+
- visionOS

## Declaration

```swift
var image: UIImage? { get set }
```

## Discussion

This property contains the image displayed in the view’s background. If this property is set to `nil`, the view displays no background image.

Changing the image in this property doesn’t change the size of the view automatically. You can use the background configuration’s [`imageContentMode`](./imagecontentmode.md) to specify how to lay out the image when its size differs from the size in the view’s bounds.

## See Also

### Customizing the background
- [var customView: UIView?](./customview.md)
  A custom view for the background.
- [var cornerRadius: CGFloat](./cornerradius.md)
  The preferred corner radius, using a continuous corner curve, for the background and stroke.
- [var backgroundInsets: NSDirectionalEdgeInsets](./backgroundinsets.md)
  The insets (or outsets, if negative) for the background and stroke, relative to the edges of the containing view.
- [var edgesAddingLayoutMarginsToBackgroundInsets: NSDirectionalRectEdge](./edgesaddinglayoutmarginstobackgroundinsets.md)
  The edges on which the configuration adds the containing view’s layout margins to the background insets.
- [var backgroundColor: UIColor?](./backgroundcolor.md)
  The color of the background.
- [var backgroundColorTransformer: UIConfigurationColorTransformer?](./backgroundcolortransformer.md)
  The color transformer for resolving the background color.
- [func resolvedBackgroundColor(for: UIColor) -> UIColor](./resolvedbackgroundcolor%28for%29.md)
  Generates the resolved background color for the specified tint color, using the background color and color transformer.
- [var visualEffect: UIVisualEffect?](./visualeffect.md)
  The visual effect that the configuration applies to the background.
- [var shadowProperties: UIShadowProperties](./shadowproperties.md)
- [struct UIShadowProperties](../uishadowproperties-swift.struct.md)
- [var strokeColor: UIColor?](./strokecolor.md)
  The color of the stroke.
- [var strokeColorTransformer: UIConfigurationColorTransformer?](./strokecolortransformer.md)
  The color transformer for resolving the stroke color.
- [func resolvedStrokeColor(for: UIColor) -> UIColor](./resolvedstrokecolor%28for%29.md)
  Generates the resolved stroke color for the specified tint color, using the stroke color and color transformer.
- [var strokeWidth: CGFloat](./strokewidth.md)
  The width of the stroke.
- [var strokeOutset: CGFloat](./strokeoutset.md)
  The outset (or inset, if negative) for the stroke.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibackgroundconfiguration-swift.struct/image)*