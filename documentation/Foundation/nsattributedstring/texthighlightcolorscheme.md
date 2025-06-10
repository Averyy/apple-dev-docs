# NSAttributedString.TextHighlightColorScheme

**Framework**: Foundation  
**Kind**: struct

Constants that specify the highlight color to use with the text.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
struct TextHighlightColorScheme
```

#### Overview

Use an [`NSAttributedString.TextHighlightColorScheme`](nsattributedstring/texthighlightcolorscheme.md) structure as the value of the [`textHighlightColorScheme`](nsattributedstring/key/texthighlightcolorscheme.md) attribute. That attribute specifies which color to use when drawing the highlight on the text. This attribute specifies only the color option. To display the highlight itself, add the [`textHighlightStyle`](nsattributedstring/key/texthighlightstyle.md) attribute to the text.

## Topics

### Getting the color schemes
- [static let `default`: NSAttributedString.TextHighlightColorScheme](nsattributedstring/texthighlightcolorscheme/default.md)
  The default system highlight color.
- [static let blue: NSAttributedString.TextHighlightColorScheme](nsattributedstring/texthighlightcolorscheme/blue.md)
  A blue highlight color.
- [static let mint: NSAttributedString.TextHighlightColorScheme](nsattributedstring/texthighlightcolorscheme/mint.md)
  A mint green highlight color.
- [static let orange: NSAttributedString.TextHighlightColorScheme](nsattributedstring/texthighlightcolorscheme/orange.md)
  An orange highlight color.
- [static let pink: NSAttributedString.TextHighlightColorScheme](nsattributedstring/texthighlightcolorscheme/pink.md)
  A pink highlight color.
- [static let purple: NSAttributedString.TextHighlightColorScheme](nsattributedstring/texthighlightcolorscheme/purple.md)
  A purple highlight color.
### Creating a color scheme
- [init(String)](nsattributedstring/texthighlightcolorscheme/init(_:).md)
- [init(rawValue: String)](nsattributedstring/texthighlightcolorscheme/init(rawvalue:).md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [NSAttributedString.Key](nsattributedstring/key.md)
  The attributes you apply to ranges of characters in an attributed string.
- [NSAttributedString.TextHighlightStyle](nsattributedstring/texthighlightstyle.md)
  Constants that specify the type of highlight to apply to text.
- [NSAttributedString.TextEffectStyle](nsattributedstring/texteffectstyle.md)
  Constants for the type of effect to apply to the text.
- [NSAttributedString.SpellingState](nsattributedstring/spellingstate.md)
  Constants for the spelling state attribute key.
- [struct NSUnderlineStyle](../UIKit/NSUnderlineStyle.md)
  Constants for the underline style and strikethrough style attribute keys.
- [enum NSWritingDirectionFormatType](../UIKit/NSWritingDirectionFormatType.md)
  Constants for the writing direction attribute key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsattributedstring/texthighlightcolorscheme)*