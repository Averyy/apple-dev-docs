# customView

**Framework**: UIKit  
**Kind**: property

A custom view for the background.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst ?+
- tvOS 14.0+
- visionOS ?+

## Declaration

```swift
var customView: UIView? { get set }
```

#### Discussion

The custom view must have [`translatesAutoresizingMaskIntoConstraints`](uiview/translatesautoresizingmaskintoconstraints.md) set to [`true`](https://developer.apple.com/documentation/Swift/true), but it can use Auto Layout constraints internally for layout of its subviews.

## See Also

- [var cornerRadius: CGFloat](uibackgroundconfiguration-swift.struct/cornerradius.md)
  The preferred corner radius, using a continuous corner curve, for the background and stroke.
- [var backgroundInsets: NSDirectionalEdgeInsets](uibackgroundconfiguration-swift.struct/backgroundinsets.md)
  The insets (or outsets, if negative) for the background and stroke, relative to the edges of the containing view.
- [var edgesAddingLayoutMarginsToBackgroundInsets: NSDirectionalRectEdge](uibackgroundconfiguration-swift.struct/edgesaddinglayoutmarginstobackgroundinsets.md)
  The edges on which the configuration adds the containing view’s layout margins to the background insets.
- [var backgroundColor: UIColor?](uibackgroundconfiguration-swift.struct/backgroundcolor.md)
  The color of the background.
- [var backgroundColorTransformer: UIConfigurationColorTransformer?](uibackgroundconfiguration-swift.struct/backgroundcolortransformer.md)
  The color transformer for resolving the background color.
- [func resolvedBackgroundColor(for: UIColor) -> UIColor](uibackgroundconfiguration-swift.struct/resolvedbackgroundcolor(for:).md)
  Generates the resolved background color for the specified tint color, using the background color and color transformer.
- [var visualEffect: UIVisualEffect?](uibackgroundconfiguration-swift.struct/visualeffect.md)
  The visual effect that the configuration applies to the background.
- [var shadowProperties: UIShadowProperties](uibackgroundconfiguration-swift.struct/shadowproperties.md)
- [struct UIShadowProperties](uishadowproperties-swift.struct.md)
- [var strokeColor: UIColor?](uibackgroundconfiguration-swift.struct/strokecolor.md)
  The color of the stroke.
- [var strokeColorTransformer: UIConfigurationColorTransformer?](uibackgroundconfiguration-swift.struct/strokecolortransformer.md)
  The color transformer for resolving the stroke color.
- [func resolvedStrokeColor(for: UIColor) -> UIColor](uibackgroundconfiguration-swift.struct/resolvedstrokecolor(for:).md)
  Generates the resolved stroke color for the specified tint color, using the stroke color and color transformer.
- [var strokeWidth: CGFloat](uibackgroundconfiguration-swift.struct/strokewidth.md)
  The width of the stroke.
- [var strokeOutset: CGFloat](uibackgroundconfiguration-swift.struct/strokeoutset.md)
  The outset (or inset, if negative) for the stroke.
- [var image: UIImage?](uibackgroundconfiguration-swift.struct/image.md)
  The image displayed in the view’s background.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibackgroundconfiguration-swift.struct/customview)*