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
- visionOS 1.0+

## Declaration

```objc
@property (nonatomic, strong, nullable) UIImage * image;
```

## Discussion

This property contains the image displayed in the view’s background. If this property is set to `nil`, the view displays no background image.

Changing the image in this property doesn’t change the size of the view automatically. You can use the background configuration’s [`imageContentMode`](./imagecontentmode.md) to specify how to lay out the image when its size differs from the size in the view’s bounds.

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
- [- resolvedBackgroundColorForTintColor:](./resolvedbackgroundcolorfortintcolor_.md)
  Generates the resolved background color for the specified tint color, using the background color and color transformer.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibackgroundconfiguration-c.class/image)*