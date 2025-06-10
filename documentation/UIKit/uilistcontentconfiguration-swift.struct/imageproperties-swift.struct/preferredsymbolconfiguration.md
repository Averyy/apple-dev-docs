# preferredSymbolConfiguration

**Framework**: UIKit  
**Kind**: property

The symbol configuration to use.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst ?+
- tvOS 14.0+
- visionOS ?+

## Declaration

```swift
var preferredSymbolConfiguration: UIImage.SymbolConfiguration? { get set }
```

## See Also

- [var tintColor: UIColor?](uilistcontentconfiguration-swift.struct/imageproperties-swift.struct/tintcolor.md)
  The tint color to apply to the image view.
- [var tintColorTransformer: UIConfigurationColorTransformer?](uilistcontentconfiguration-swift.struct/imageproperties-swift.struct/tintcolortransformer.md)
  The color transformer for resolving the tint color.
- [func resolvedTintColor(for: UIColor) -> UIColor](uilistcontentconfiguration-swift.struct/imageproperties-swift.struct/resolvedtintcolor(for:).md)
  Generates the resolved tint color for the specified tint color, using the tint color and color transformer.
- [var cornerRadius: CGFloat](uilistcontentconfiguration-swift.struct/imageproperties-swift.struct/cornerradius.md)
  The preferred corner radius, using a continuous corner curve, for the image.
- [var maximumSize: CGSize](uilistcontentconfiguration-swift.struct/imageproperties-swift.struct/maximumsize.md)
  The maximum size for the image.
- [var reservedLayoutSize: CGSize](uilistcontentconfiguration-swift.struct/imageproperties-swift.struct/reservedlayoutsize.md)
  The layout size that the system reserves for the image, and then centers the image within.
- [static let standardDimension: CGFloat](uilistcontentconfiguration-swift.struct/imageproperties-swift.struct/standarddimension.md)
  The system standard layout dimension for reserved layout size.
- [var accessibilityIgnoresInvertColors: Bool](uilistcontentconfiguration-swift.struct/imageproperties-swift.struct/accessibilityignoresinvertcolors.md)
  A Boolean value that determines whether the image inverts its colors when the user turns on the Invert Colors accessibility setting.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uilistcontentconfiguration-swift.struct/imageproperties-swift.struct/preferredsymbolconfiguration)*