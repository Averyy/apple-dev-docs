# UIListContentConfiguration.TextProperties.TextAlignment

**Framework**: UIKit  
**Kind**: enum

Constants that specify the visual alignment of the text.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst ?+
- tvOS 14.0+
- visionOS ?+

## Declaration

```swift
enum TextAlignment
```

## Topics

### Text alignment
- [UIListContentConfiguration.TextProperties.TextAlignment.center](uilistcontentconfiguration-swift.struct/textproperties-swift.struct/textalignment/center.md)
  The text has centered alignment.
- [UIListContentConfiguration.TextProperties.TextAlignment.justified](uilistcontentconfiguration-swift.struct/textproperties-swift.struct/textalignment/justified.md)
  The text has justified alignment.
- [UIListContentConfiguration.TextProperties.TextAlignment.natural](uilistcontentconfiguration-swift.struct/textproperties-swift.struct/textalignment/natural.md)
  The text uses the default alignment that the system associates with the current localization of the app.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)

## See Also

- [var font: UIFont](uilistcontentconfiguration-swift.struct/textproperties-swift.struct/font.md)
  The font for the text.
- [var color: UIColor](uilistcontentconfiguration-swift.struct/textproperties-swift.struct/color.md)
  The color of the text.
- [var colorTransformer: UIConfigurationColorTransformer?](uilistcontentconfiguration-swift.struct/textproperties-swift.struct/colortransformer.md)
  The color transformer for resolving the text color.
- [func resolvedColor() -> UIColor](uilistcontentconfiguration-swift.struct/textproperties-swift.struct/resolvedcolor.md)
  Generates the resolved color for the specified color, using the text color and color transformer.
- [var alignment: UIListContentConfiguration.TextProperties.TextAlignment](uilistcontentconfiguration-swift.struct/textproperties-swift.struct/alignment.md)
  The alignment for the text.
- [var lineBreakMode: NSLineBreakMode](uilistcontentconfiguration-swift.struct/textproperties-swift.struct/linebreakmode.md)
  The line break mode to use for the text.
- [var numberOfLines: Int](uilistcontentconfiguration-swift.struct/textproperties-swift.struct/numberoflines.md)
  The maximum number of lines for the text.
- [var adjustsFontSizeToFitWidth: Bool](uilistcontentconfiguration-swift.struct/textproperties-swift.struct/adjustsfontsizetofitwidth.md)
  A Boolean value that determines whether the configuration automatically adjusts the font size of the text when necessary to fit in the available width.
- [var minimumScaleFactor: CGFloat](uilistcontentconfiguration-swift.struct/textproperties-swift.struct/minimumscalefactor.md)
  The smallest multiplier for the font size that the configuration uses to make the text fit.
- [var allowsDefaultTighteningForTruncation: Bool](uilistcontentconfiguration-swift.struct/textproperties-swift.struct/allowsdefaulttighteningfortruncation.md)
  A Boolean value that determines whether the configuration tightens the text before truncating.
- [var adjustsFontForContentSizeCategory: Bool](uilistcontentconfiguration-swift.struct/textproperties-swift.struct/adjustsfontforcontentsizecategory.md)
  A Boolean value that determines whether the configuration automatically updates the font when the content size category changes.
- [var transform: UIListContentConfiguration.TextProperties.TextTransform](uilistcontentconfiguration-swift.struct/textproperties-swift.struct/transform.md)
  The transform to apply to the text.
- [UIListContentConfiguration.TextProperties.TextTransform](uilistcontentconfiguration-swift.struct/textproperties-swift.struct/texttransform.md)
  Constants that specify the transform to apply to the text.
- [var showsExpansionTextWhenTruncated: Bool](uilistcontentconfiguration-swift.struct/textproperties-swift.struct/showsexpansiontextwhentruncated.md)
  A Boolean value that determines whether the full text displays when the pointer hovers over the truncated text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uilistcontentconfiguration-swift.struct/textproperties-swift.struct/textalignment)*