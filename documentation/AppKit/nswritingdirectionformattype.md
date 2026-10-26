# NSWritingDirectionFormatType

**Framework**: AppKit  
**Kind**: enum  
**Role**: Enumeration

Constants for the writing direction attribute key.

**Availability**:
- macOS 10.11+

## Declaration

```swift
enum NSWritingDirectionFormatType
```

```c
enum NSWritingDirectionFormatType : NSInteger;
```

#### Overview

Use these constants as the values for the [`writingDirection`](../Foundation/nsattributedstring/key/writingdirection.md) key.

You can use the logical `OR` operator to combine these constants with [`NSWritingDirection.leftToRight`](./nswritingdirection/lefttoright.md) or [`NSWritingDirection.rightToLeft`](./nswritingdirection/righttoleft.md) when used with [`writingDirection`](../Foundation/nsattributedstring/key/writingdirection.md) to specify formatting controls defined by the Unicode Bidirectional Algorithm in [Unicode Standard Annex #9](http://unicode.org/reports/tr9/).

## Topics

### Constants
- [NSWritingDirectionFormatType.embedding](./nswritingdirectionformattype/embedding.md)
  Text is embedded in text with another writing direction. For example, an English quotation in the middle of an Arabic sentence could be marked as being embedded left-to-right text.
- [NSWritingDirectionFormatType.override](./nswritingdirectionformattype/override.md)
  Enables character types with inherent directionality to be overridden when required for special cases, such as for part numbers made of mixed English, digits, and Hebrew letters to be written from right to left.
### Initializers
- [init?(rawValue: Int)](./nswritingdirectionformattype/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Getting text content attributes
- [struct NSUnderlineStyle](./nsunderlinestyle.md)
  Constants for the underline style and strikethrough style attribute keys.
- [TextKit string attribute keys](./textkit-string-attribute-keys.md)
  AppKit-specific keys you use to apply attributes to ranges of characters in an attributed string.
- [NSTextHighlightStyle](./nstexthighlightstyle.md)
  Constants that specify the type of highlight to apply to text.
- [NSTextHighlightColorScheme](./nstexthighlightcolorscheme.md)
  Constants that specify the highlight color to use with the text.
- [NSTextEffectStyle](./nstexteffectstyle.md)
  Constants for the type of effect to apply to the text.
- [NSSpellingState](./nsspellingstate.md)
  Constants for the spelling state attribute key.
- [NSUnderlineByWordMask](./nsunderlinebywordmask.md)
  Draw the underline only underneath words, not underneath whitespace.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswritingdirectionformattype)*