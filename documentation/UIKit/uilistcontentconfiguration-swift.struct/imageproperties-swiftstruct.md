# UIListContentConfiguration.ImageProperties

**Framework**: UIKit  
**Kind**: struct

Properties that affect the list content configuration’s image.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst ?+
- tvOS 14.0+
- visionOS ?+

## Declaration

```swift
struct ImageProperties
```

## Topics

### Configuring image properties
- [var preferredSymbolConfiguration: UIImage.SymbolConfiguration?](uilistcontentconfiguration-swift.struct/imageproperties-swift.struct/preferredsymbolconfiguration.md)
  The symbol configuration to use.
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
### Instance Properties
- [var strokeColor: UIColor?](uilistcontentconfiguration-swift.struct/imageproperties-swift.struct/strokecolor.md)
- [var strokeColorTransformer: UIConfigurationColorTransformer?](uilistcontentconfiguration-swift.struct/imageproperties-swift.struct/strokecolortransformer.md)
- [var strokeWidth: CGFloat](uilistcontentconfiguration-swift.struct/imageproperties-swift.struct/strokewidth.md)
### Instance Methods
- [func resolvedStrokeColor(for: UIColor) -> UIColor](uilistcontentconfiguration-swift.struct/imageproperties-swift.struct/resolvedstrokecolor(for:).md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomReflectable](../Swift/CustomReflectable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)

## See Also

- [var imageProperties: UIListContentConfiguration.ImageProperties](uilistcontentconfiguration-swift.struct/imageproperties-swift.property.md)
  Properties for configuring the image.
- [var textProperties: UIListContentConfiguration.TextProperties](uilistcontentconfiguration-swift.struct/textproperties-swift.property.md)
  Properties for configuring the primary text.
- [var secondaryTextProperties: UIListContentConfiguration.TextProperties](uilistcontentconfiguration-swift.struct/secondarytextproperties.md)
  Properties for configuring the secondary text.
- [UIListContentConfiguration.TextProperties](uilistcontentconfiguration-swift.struct/textproperties-swift.struct.md)
  Properties that affect the list content configuration’s text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uilistcontentconfiguration-swift.struct/imageproperties-swift.struct)*