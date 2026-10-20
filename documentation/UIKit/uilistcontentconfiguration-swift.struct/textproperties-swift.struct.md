# UIListContentConfiguration.TextProperties

**Framework**: UIKit  
**Kind**: struct  
**Role**: Structure

Properties that affect the list content configuration’s text.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- tvOS 14.0+
- visionOS

## Declaration

```swift
struct TextProperties
```

## Topics

### Configuring text properties
- [var font: UIFont](./textproperties-swift.struct/font.md)
  The font for the text.
- [var color: UIColor](./textproperties-swift.struct/color.md)
  The color of the text.
- [var colorTransformer: UIConfigurationColorTransformer?](./textproperties-swift.struct/colortransformer.md)
  The color transformer for resolving the text color.
- [func resolvedColor() -> UIColor](./textproperties-swift.struct/resolvedcolor%28%29.md)
  Generates the resolved color for the specified color, using the text color and color transformer.
- [var alignment: UIListContentConfiguration.TextProperties.TextAlignment](./textproperties-swift.struct/alignment.md)
  The alignment for the text.
- [var lineBreakMode: NSLineBreakMode](./textproperties-swift.struct/linebreakmode.md)
  The line break mode to use for the text.
- [var numberOfLines: Int](./textproperties-swift.struct/numberoflines.md)
  The maximum number of lines for the text.
- [var adjustsFontSizeToFitWidth: Bool](./textproperties-swift.struct/adjustsfontsizetofitwidth.md)
  A Boolean value that determines whether the configuration automatically adjusts the font size of the text when necessary to fit in the available width.
- [var minimumScaleFactor: CGFloat](./textproperties-swift.struct/minimumscalefactor.md)
  The smallest multiplier for the font size that the configuration uses to make the text fit.
- [var allowsDefaultTighteningForTruncation: Bool](./textproperties-swift.struct/allowsdefaulttighteningfortruncation.md)
  A Boolean value that determines whether the configuration tightens the text before truncating.
- [var adjustsFontForContentSizeCategory: Bool](./textproperties-swift.struct/adjustsfontforcontentsizecategory.md)
  A Boolean value that determines whether the configuration automatically updates the font when the content size category changes.
- [UIListContentConfiguration.TextProperties.TextAlignment](./textproperties-swift.struct/textalignment.md)
  Constants that specify the visual alignment of the text.
- [var transform: UIListContentConfiguration.TextProperties.TextTransform](./textproperties-swift.struct/transform.md)
  The transform to apply to the text.
- [UIListContentConfiguration.TextProperties.TextTransform](./textproperties-swift.struct/texttransform.md)
  Constants that specify the transform to apply to the text.
- [var showsExpansionTextWhenTruncated: Bool](./textproperties-swift.struct/showsexpansiontextwhentruncated.md)
  A Boolean value that determines whether the full text displays when the pointer hovers over the truncated text.

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
- [UIListContentConfiguration.ImageProperties](./imageproperties-swift.struct.md)
  Properties that affect the list content configuration’s image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uilistcontentconfiguration-swift.struct/textproperties-swift.struct)*