# NSTextWritingDirection

**Framework**: UIKit  
**Kind**: enum  
**Role**: Enumeration

Options for specifying text-writing direction.

**Availability**:
- iOS 7.0+ - Deprecated in 9.0 (renamed: NSWritingDirectionFormatType)
- iPadOS 7.0+ - Deprecated in 9.0 (renamed: NSWritingDirectionFormatType)
- Mac Catalyst 13.1+ - Deprecated in 13.1 (renamed: NSWritingDirectionFormatType)
- watchOS 2.0+ - Deprecated in 2.0 (renamed: NSWritingDirectionFormatType)

> **Deprecated**: Use [`NSWritingDirectionFormatType`](./nswritingdirectionformattype.md) instead.

## Declaration

```swift
enum NSTextWritingDirection
```

```c
enum NSTextWritingDirection : NSInteger;
```

## Overview

You can use the logical OR operator to combine these constants with [`NSWritingDirection.leftToRight`](./nswritingdirection/lefttoright.md) or [`NSWritingDirection.rightToLeft`](./nswritingdirection/righttoleft.md) when used with [`writingDirection`](../Foundation/nsattributedstring/key/writingdirection.md) to specify formatting controls defined by the Unicode Bidirectional Algorithm in [Unicode Standard Annex #9](http://unicode.org/reports/tr9/).

## Topics

### Constants
- [NSTextWritingDirection.embedding](./nstextwritingdirection/embedding.md)
  Text is embedded in text with another writing direction.
- [NSTextWritingDirection.override](./nstextwritingdirection/override.md)
  Enables character types with inherent directionality to be overridden when required for special cases, such as for part numbers made of mixed English, digits, and Hebrew letters to be written from right to left.
### Initializers
- [init?(rawValue: Int)](./nstextwritingdirection/init%28rawvalue%29.md)

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
- [enum NSWritingDirectionFormatType](./nswritingdirectionformattype.md)
  Constants for the writing direction attribute key.
- [TextKit string attribute keys](./textkit-string-attribute-keys.md)
  UIKit-specific keys you use to apply attributes to ranges of characters in an attributed string.
- [NSTextHighlightStyle](./nstexthighlightstyle.md)
  Constants that specify the type of highlight to apply to text.
- [NSTextHighlightColorScheme](./nstexthighlightcolorscheme.md)
  Constants that specify the highlight color to use with the text.
- [NSTextEffectStyle](./nstexteffectstyle.md)
  Constants for the type of effect to apply to the text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nstextwritingdirection)*