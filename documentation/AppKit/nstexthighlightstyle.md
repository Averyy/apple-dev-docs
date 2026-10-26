# NSTextHighlightStyle

**Framework**: AppKit  
**Kind**: typealias  
**Role**: Type Alias

Constants that specify the type of highlight to apply to text.

**Availability**:
- macOS 15.0+

## Declaration

```c
typedef NSString * NSTextHighlightStyle;
```

#### Discussion

Use an [`NSTextHighlightStyle`](./nstexthighlightstyle.md) structure as the value of the [`NSTextHighlightStyleAttributeName`](./nstexthighlightstyleattributename.md) attribute. That attribute applies a highlight to the text to emphasize it. The highlight contributes a background color and a contrasting foreground color to the text.

## Topics

### Getting the highlight styles
- [NSTextHighlightStyleDefault](./nstexthighlightstyledefault.md)
  The default highlight style to apply to text.

## See Also

### Getting text content attributes
- [TextKit string attribute keys](./textkit-string-attribute-keys.md)
  AppKit-specific keys you use to apply attributes to ranges of characters in an attributed string.
- [NSTextHighlightColorScheme](./nstexthighlightcolorscheme.md)
  Constants that specify the highlight color to use with the text.
- [NSTextEffectStyle](./nstexteffectstyle.md)
  Constants for the type of effect to apply to the text.
- [NSSpellingState](./nsspellingstate.md)
  Constants for the spelling state attribute key.
- [struct NSUnderlineStyle](./nsunderlinestyle.md)
  Constants for the underline style and strikethrough style attribute keys.
- [enum NSWritingDirectionFormatType](./nswritingdirectionformattype.md)
  Constants for the writing direction attribute key.
- [NSUnderlineByWordMask](./nsunderlinebywordmask.md)
  Draw the underline only underneath words, not underneath whitespace.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstexthighlightstyle)*