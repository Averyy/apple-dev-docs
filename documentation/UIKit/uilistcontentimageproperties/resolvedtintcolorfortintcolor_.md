# resolvedTintColorForTintColor:

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Generates the resolved tint color for the specified tint color, using the tint color and color transformer.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```objc
- (UIColor *) resolvedTintColorForTintColor:(UIColor *) tintColor;
```

#### Discussion

The resulting color depends on [`tintColor`](./tintcolor.md) and [`tintColorTransformer`](./tintcolortransformer.md).

## See Also

### Configuring image properties
- [preferredSymbolConfiguration](./preferredsymbolconfiguration.md)
  The symbol configuration to use.
- [tintColor](./tintcolor.md)
  The tint color to apply to the image view.
- [tintColorTransformer](./tintcolortransformer.md)
  The color transformer for resolving the tint color.
- [cornerRadius](./cornerradius.md)
  The preferred corner radius, using a continuous corner curve, for the image.
- [maximumSize](./maximumsize.md)
  The maximum size for the image.
- [reservedLayoutSize](./reservedlayoutsize.md)
  The layout size that the system reserves for the image, and then centers the image within.
- [UIListContentImageStandardDimension](../uilistcontentimagestandarddimension.md)
  The system standard layout dimension for reserved layout size.
- [accessibilityIgnoresInvertColors](./accessibilityignoresinvertcolors.md)
  A Boolean value that determines whether the image inverts its colors when the user turns on the Invert Colors accessibility setting.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uilistcontentimageproperties/resolvedtintcolorfortintcolor:)*