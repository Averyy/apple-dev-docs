# NSAttributedString.TextHighlightColorScheme

**Framework**: Foundation  
**Kind**: struct  
**Role**: Structure

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

## Overview

Use an [`NSAttributedString.TextHighlightColorScheme`](./texthighlightcolorscheme.md) structure as the value of the [`textHighlightColorScheme`](./key/texthighlightcolorscheme.md) attribute. That attribute specifies which color to use when drawing the highlight on the text. This attribute specifies only the color option. To display the highlight itself, add the [`textHighlightStyle`](./key/texthighlightstyle.md) attribute to the text.

## Topics

### Getting the color schemes
- [static let `default`: NSAttributedString.TextHighlightColorScheme](./texthighlightcolorscheme/default.md)
  The default system highlight color.
- [static let blue: NSAttributedString.TextHighlightColorScheme](./texthighlightcolorscheme/blue.md)
  A blue highlight color.
- [static let mint: NSAttributedString.TextHighlightColorScheme](./texthighlightcolorscheme/mint.md)
  A mint green highlight color.
- [static let orange: NSAttributedString.TextHighlightColorScheme](./texthighlightcolorscheme/orange.md)
  An orange highlight color.
- [static let pink: NSAttributedString.TextHighlightColorScheme](./texthighlightcolorscheme/pink.md)
  A pink highlight color.
- [static let purple: NSAttributedString.TextHighlightColorScheme](./texthighlightcolorscheme/purple.md)
  A purple highlight color.
### Creating a color scheme
- [init(String)](./texthighlightcolorscheme/init%28_%29.md)
- [init(rawValue: String)](./texthighlightcolorscheme/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Getting text content attributes
- [NSAttributedString.Key](./key.md)
  The attributes you apply to ranges of characters in an attributed string.
- [NSAttributedString.TextHighlightStyle](./texthighlightstyle.md)
  Constants that specify the type of highlight to apply to text.
- [NSAttributedString.TextEffectStyle](./texteffectstyle.md)
  Constants for the type of effect to apply to the text.
- [NSAttributedString.SpellingState](./spellingstate.md)
  Constants for the spelling state attribute key.
- [struct NSUnderlineStyle](../../UIKit/nsunderlinestyle.md)
  Constants for the underline style and strikethrough style attribute keys.
- [enum NSWritingDirectionFormatType](../../UIKit/nswritingdirectionformattype.md)
  Constants for the writing direction attribute key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsattributedstring/texthighlightcolorscheme)*