# maximumSize

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The maximum size for the image.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```objc
@property (nonatomic) CGSize maximumSize;
```

## Discussion

The default value is [`CGSizeZero`](../../CoreGraphics/cgsizezero.md). A width or height of zero means that the system doesn’t constrain the size for that dimension.

If the image exceeds this size on either dimension, the system reduces the size proportionately, maintaining the aspect ratio.

## See Also

### Configuring image properties
- [preferredSymbolConfiguration](./preferredsymbolconfiguration.md)
  The symbol configuration to use.
- [tintColor](./tintcolor.md)
  The tint color to apply to the image view.
- [tintColorTransformer](./tintcolortransformer.md)
  The color transformer for resolving the tint color.
- [- resolvedTintColorForTintColor:](./resolvedtintcolorfortintcolor_.md)
  Generates the resolved tint color for the specified tint color, using the tint color and color transformer.
- [cornerRadius](./cornerradius.md)
  The preferred corner radius, using a continuous corner curve, for the image.
- [reservedLayoutSize](./reservedlayoutsize.md)
  The layout size that the system reserves for the image, and then centers the image within.
- [UIListContentImageStandardDimension](../uilistcontentimagestandarddimension.md)
  The system standard layout dimension for reserved layout size.
- [accessibilityIgnoresInvertColors](./accessibilityignoresinvertcolors.md)
  A Boolean value that determines whether the image inverts its colors when the user turns on the Invert Colors accessibility setting.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uilistcontentimageproperties/maximumsize)*