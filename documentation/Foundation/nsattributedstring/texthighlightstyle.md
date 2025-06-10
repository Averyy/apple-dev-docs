# NSAttributedString.TextHighlightStyle

**Framework**: Foundation  
**Kind**: struct

Constants that specify the type of highlight to apply to text.

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
struct TextHighlightStyle
```

#### Overview

Use an [`NSAttributedString.TextHighlightStyle`](nsattributedstring/texthighlightstyle.md) structure as the value of the [`textHighlightStyle`](nsattributedstring/key/texthighlightstyle.md) attribute. That attribute applies a highlight to the text to emphasize it. The highlight contributes a background color and a contrasting foreground color to the text.

## Topics

### Getting the highlight styles
- [static let `default`: NSAttributedString.TextHighlightStyle](nsattributedstring/texthighlightstyle/default.md)
  The default highlight style to apply to text.
### Creating a highlight style
- [init(String)](nsattributedstring/texthighlightstyle/init(_:).md)
- [init(rawValue: String)](nsattributedstring/texthighlightstyle/init(rawvalue:).md)

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
- [NSAttributedString.TextHighlightColorScheme](nsattributedstring/texthighlightcolorscheme.md)
  Constants that specify the highlight color to use with the text.
- [NSAttributedString.TextEffectStyle](nsattributedstring/texteffectstyle.md)
  Constants for the type of effect to apply to the text.
- [NSAttributedString.SpellingState](nsattributedstring/spellingstate.md)
  Constants for the spelling state attribute key.
- [struct NSUnderlineStyle](../UIKit/NSUnderlineStyle.md)
  Constants for the underline style and strikethrough style attribute keys.
- [enum NSWritingDirectionFormatType](../UIKit/NSWritingDirectionFormatType.md)
  Constants for the writing direction attribute key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsattributedstring/texthighlightstyle)*