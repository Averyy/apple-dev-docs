# UIListContentImageStandardDimension

**Framework**: UIKit  
**Kind**: var  
**Role**: Global Variable

The system standard layout dimension for reserved layout size.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```c
extern const CGFloat UIListContentImageStandardDimension;
```

#### Discussion

Setting the [`reservedLayoutSize`](./uilistcontentimageproperties/reservedlayoutsize.md) width or height to this constant results in using the system standard value for a symbol image for that dimension, even when the image is not a symbol image.

## See Also

### Configuring image properties
- [preferredSymbolConfiguration](./uilistcontentimageproperties/preferredsymbolconfiguration.md)
  The symbol configuration to use.
- [tintColor](./uilistcontentimageproperties/tintcolor.md)
  The tint color to apply to the image view.
- [tintColorTransformer](./uilistcontentimageproperties/tintcolortransformer.md)
  The color transformer for resolving the tint color.
- [- resolvedTintColorForTintColor:](./uilistcontentimageproperties/resolvedtintcolorfortintcolor_.md)
  Generates the resolved tint color for the specified tint color, using the tint color and color transformer.
- [cornerRadius](./uilistcontentimageproperties/cornerradius.md)
  The preferred corner radius, using a continuous corner curve, for the image.
- [maximumSize](./uilistcontentimageproperties/maximumsize.md)
  The maximum size for the image.
- [reservedLayoutSize](./uilistcontentimageproperties/reservedlayoutsize.md)
  The layout size that the system reserves for the image, and then centers the image within.
- [accessibilityIgnoresInvertColors](./uilistcontentimageproperties/accessibilityignoresinvertcolors.md)
  A Boolean value that determines whether the image inverts its colors when the user turns on the Invert Colors accessibility setting.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uilistcontentimagestandarddimension)*