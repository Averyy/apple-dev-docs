# visualEffect

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The visual effect that the configuration applies to the background.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- tvOS 14.0+
- visionOS

## Declaration

```swift
var visualEffect: UIVisualEffect? { get set }
```

#### Discussion

The default value is `nil`.

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
- [var image: UIImage?](./image.md)
  The image displayed in the view’s background.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibackgroundconfiguration-swift.struct/visualeffect)*