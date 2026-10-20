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
- visionOS

## Declaration

```swift
var maximumSize: CGSize { get set }
```

#### Discussion

The default value is [`CGSizeZero`](../../../CoreGraphics/cgsizezero.md). A width or height of zero means that the system doesn’t constrain the size for that dimension.

If the image exceeds this size on either dimension, the system reduces the size proportionately, maintaining the aspect ratio.

## See Also

### Configuring image properties
- [var preferredSymbolConfiguration: UIImage.SymbolConfiguration?](./preferredsymbolconfiguration.md)
  The symbol configuration to use.
- [var tintColor: UIColor?](./tintcolor.md)
  The tint color to apply to the image view.
- [var tintColorTransformer: UIConfigurationColorTransformer?](./tintcolortransformer.md)
  The color transformer for resolving the tint color.
- [func resolvedTintColor(for: UIColor) -> UIColor](./resolvedtintcolor%28for%29.md)
  Generates the resolved tint color for the specified tint color, using the tint color and color transformer.
- [var cornerRadius: CGFloat](./cornerradius.md)
  The preferred corner radius, using a continuous corner curve, for the image.
- [var reservedLayoutSize: CGSize](./reservedlayoutsize.md)
  The layout size that the system reserves for the image, and then centers the image within.
- [static let standardDimension: CGFloat](./standarddimension.md)
  The system standard layout dimension for reserved layout size.
- [var accessibilityIgnoresInvertColors: Bool](./accessibilityignoresinvertcolors.md)
  A Boolean value that determines whether the image inverts its colors when the user turns on the Invert Colors accessibility setting.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uilistcontentconfiguration-swift.struct/imageproperties-swift.struct/maximumsize)*