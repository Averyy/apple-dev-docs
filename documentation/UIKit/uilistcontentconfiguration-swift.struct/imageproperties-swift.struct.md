# UIListContentConfiguration.ImageProperties

**Framework**: UIKit  
**Kind**: struct  
**Role**: Structure

Properties that affect the list content configuration’s image.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- tvOS 14.0+
- visionOS

## Declaration

```swift
struct ImageProperties
```

## Topics

### Configuring image properties
- [var preferredSymbolConfiguration: UIImage.SymbolConfiguration?](./imageproperties-swift.struct/preferredsymbolconfiguration.md)
  The symbol configuration to use.
- [var tintColor: UIColor?](./imageproperties-swift.struct/tintcolor.md)
  The tint color to apply to the image view.
- [var tintColorTransformer: UIConfigurationColorTransformer?](./imageproperties-swift.struct/tintcolortransformer.md)
  The color transformer for resolving the tint color.
- [func resolvedTintColor(for: UIColor) -> UIColor](./imageproperties-swift.struct/resolvedtintcolor%28for%29.md)
  Generates the resolved tint color for the specified tint color, using the tint color and color transformer.
- [var cornerRadius: CGFloat](./imageproperties-swift.struct/cornerradius.md)
  The preferred corner radius, using a continuous corner curve, for the image.
- [var maximumSize: CGSize](./imageproperties-swift.struct/maximumsize.md)
  The maximum size for the image.
- [var reservedLayoutSize: CGSize](./imageproperties-swift.struct/reservedlayoutsize.md)
  The layout size that the system reserves for the image, and then centers the image within.
- [static let standardDimension: CGFloat](./imageproperties-swift.struct/standarddimension.md)
  The system standard layout dimension for reserved layout size.
- [var accessibilityIgnoresInvertColors: Bool](./imageproperties-swift.struct/accessibilityignoresinvertcolors.md)
  A Boolean value that determines whether the image inverts its colors when the user turns on the Invert Colors accessibility setting.
### Instance Properties
- [var strokeColor: UIColor?](./imageproperties-swift.struct/strokecolor.md)
- [var strokeColorTransformer: UIConfigurationColorTransformer?](./imageproperties-swift.struct/strokecolortransformer.md)
- [var strokeWidth: CGFloat](./imageproperties-swift.struct/strokewidth.md)
### Instance Methods
- [func resolvedStrokeColor(for: UIColor) -> UIColor](./imageproperties-swift.struct/resolvedstrokecolor%28for%29.md)

## Relationships

### Conforms To
- [Copyable](../../Swift/copyable.md)
- [CustomDebugStringConvertible](../../Swift/customdebugstringconvertible.md)
- [CustomReflectable](../../Swift/customreflectable.md)
- [CustomStringConvertible](../../Swift/customstringconvertible.md)
- [Equatable](../../Swift/equatable.md)
- [Escapable](../../Swift/escapable.md)
- [Hashable](../../Swift/hashable.md)

## See Also

### Customizing appearance
- [var imageProperties: UIListContentConfiguration.ImageProperties](./imageproperties-swift.property.md)
  Properties for configuring the image.
- [var textProperties: UIListContentConfiguration.TextProperties](./textproperties-swift.property.md)
  Properties for configuring the primary text.
- [var secondaryTextProperties: UIListContentConfiguration.TextProperties](./secondarytextproperties.md)
  Properties for configuring the secondary text.
- [UIListContentConfiguration.TextProperties](./textproperties-swift.struct.md)
  Properties that affect the list content configuration’s text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uilistcontentconfiguration-swift.struct/imageproperties-swift.struct)*