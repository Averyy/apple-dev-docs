# UIListContentConfiguration.TextProperties.TextAlignment

**Framework**: UIKit  
**Kind**: enum  
**Role**: Enumeration

Constants that specify the visual alignment of the text.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- tvOS 14.0+
- visionOS

## Declaration

```swift
enum TextAlignment
```

## Topics

### Text alignment
- [UIListContentConfiguration.TextProperties.TextAlignment.center](./textalignment/center.md)
  The text has centered alignment.
- [UIListContentConfiguration.TextProperties.TextAlignment.justified](./textalignment/justified.md)
  The text has justified alignment.
- [UIListContentConfiguration.TextProperties.TextAlignment.natural](./textalignment/natural.md)
  The text uses the default alignment that the system associates with the current localization of the app.

## Relationships

### Conforms To
- [Equatable](../../../Swift/equatable.md)
- [Hashable](../../../Swift/hashable.md)

## See Also

### Configuring text properties
- [var font: UIFont](./font.md)
  The font for the text.
- [var color: UIColor](./color.md)
  The color of the text.
- [var colorTransformer: UIConfigurationColorTransformer?](./colortransformer.md)
  The color transformer for resolving the text color.
- [func resolvedColor() -> UIColor](./resolvedcolor%28%29.md)
  Generates the resolved color for the specified color, using the text color and color transformer.
- [var alignment: UIListContentConfiguration.TextProperties.TextAlignment](./alignment.md)
  The alignment for the text.
- [var lineBreakMode: NSLineBreakMode](./linebreakmode.md)
  The line break mode to use for the text.
- [var numberOfLines: Int](./numberoflines.md)
  The maximum number of lines for the text.
- [var adjustsFontSizeToFitWidth: Bool](./adjustsfontsizetofitwidth.md)
  A Boolean value that determines whether the configuration automatically adjusts the font size of the text when necessary to fit in the available width.
- [var minimumScaleFactor: CGFloat](./minimumscalefactor.md)
  The smallest multiplier for the font size that the configuration uses to make the text fit.
- [var allowsDefaultTighteningForTruncation: Bool](./allowsdefaulttighteningfortruncation.md)
  A Boolean value that determines whether the configuration tightens the text before truncating.
- [var adjustsFontForContentSizeCategory: Bool](./adjustsfontforcontentsizecategory.md)
  A Boolean value that determines whether the configuration automatically updates the font when the content size category changes.
- [var transform: UIListContentConfiguration.TextProperties.TextTransform](./transform.md)
  The transform to apply to the text.
- [UIListContentConfiguration.TextProperties.TextTransform](./texttransform.md)
  Constants that specify the transform to apply to the text.
- [var showsExpansionTextWhenTruncated: Bool](./showsexpansiontextwhentruncated.md)
  A Boolean value that determines whether the full text displays when the pointer hovers over the truncated text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uilistcontentconfiguration-swift.struct/textproperties-swift.struct/textalignment)*