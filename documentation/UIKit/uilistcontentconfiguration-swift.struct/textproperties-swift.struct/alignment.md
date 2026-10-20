# alignment

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The alignment for the text.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- tvOS 14.0+
- visionOS

## Declaration

```swift
var alignment: UIListContentConfiguration.TextProperties.TextAlignment { get set }
```

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
- [UIListContentConfiguration.TextProperties.TextAlignment](./textalignment.md)
  Constants that specify the visual alignment of the text.
- [var transform: UIListContentConfiguration.TextProperties.TextTransform](./transform.md)
  The transform to apply to the text.
- [UIListContentConfiguration.TextProperties.TextTransform](./texttransform.md)
  Constants that specify the transform to apply to the text.
- [var showsExpansionTextWhenTruncated: Bool](./showsexpansiontextwhentruncated.md)
  A Boolean value that determines whether the full text displays when the pointer hovers over the truncated text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uilistcontentconfiguration-swift.struct/textproperties-swift.struct/alignment)*