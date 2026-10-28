# resolvedBackgroundColorForTintColor:

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Generates the resolved background color for the specified tint color, using the background color and color transformer.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```objc
- (UIColor *) resolvedBackgroundColorForTintColor:(UIColor *) tintColor;
```

## Discussion

The resulting color depends on `backgroundColor` and `backgroundColorTransformer`.

## See Also

### Customizing the background
- [customView](./customview.md)
  A custom view for the background.
- [cornerRadius](./cornerradius.md)
  The preferred corner radius, using a continuous corner curve, for the background and stroke.
- [backgroundInsets](./backgroundinsets.md)
  The insets (or outsets, if negative) for the background and stroke, relative to the edges of the containing view.
- [edgesAddingLayoutMarginsToBackgroundInsets](./edgesaddinglayoutmarginstobackgroundinsets.md)
  The edges on which the configuration adds the containing view’s layout margins to the background insets.
- [backgroundColor](./backgroundcolor.md)
  The color of the background.
- [backgroundColorTransformer](./backgroundcolortransformer.md)
  The color transformer for resolving the background color.
- [visualEffect](./visualeffect.md)
  The visual effect that the configuration applies to the background.
- [shadowProperties](./shadowproperties.md)
  Describes a shadow applied by the background. Defaults to no shadow (i.e. a shadow with an opacity of 0.0).
- [UIShadowProperties](../uishadowproperties-c.class.md)
- [strokeColor](./strokecolor.md)
  The color of the stroke.
- [strokeColorTransformer](./strokecolortransformer.md)
  The color transformer for resolving the stroke color.
- [- resolvedStrokeColorForTintColor:](./resolvedstrokecolorfortintcolor_.md)
  Generates the resolved stroke color for the specified tint color, using the stroke color and color transformer.
- [strokeWidth](./strokewidth.md)
  The width of the stroke.
- [strokeOutset](./strokeoutset.md)
  The outset (or inset, if negative) for the stroke.
- [image](./image.md)
  The image displayed in the view’s background.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibackgroundconfiguration-c.class/resolvedbackgroundcolorfortintcolor:)*