# NSTextHighlightColorScheme

**Framework**: UIKit  
**Kind**: typealias  
**Role**: Type Alias

Constants that specify the highlight color to use with the text.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```c
typedef NSString * NSTextHighlightColorScheme;
```

## Overview

Use an [`NSTextHighlightColorScheme`](./nstexthighlightcolorscheme.md) structure as the value of the [`NSTextHighlightColorSchemeAttributeName`](./nstexthighlightcolorschemeattributename.md) attribute. That attribute specifies which color to use when drawing the highlight on the text. This attribute specifies only the color option. To display the highlight itself, add the [`NSTextHighlightStyleAttributeName`](./nstexthighlightstyleattributename.md) attribute to the text.

## Topics

### Getting the color schemes
- [NSTextHighlightColorSchemeDefault](./nstexthighlightcolorschemedefault.md)
  The default system highlight color.
- [NSTextHighlightColorSchemeBlue](./nstexthighlightcolorschemeblue.md)
  A blue highlight color.
- [NSTextHighlightColorSchemeMint](./nstexthighlightcolorschememint.md)
  A mint green highlight color.
- [NSTextHighlightColorSchemeOrange](./nstexthighlightcolorschemeorange.md)
  An orange highlight color.
- [NSTextHighlightColorSchemePink](./nstexthighlightcolorschemepink.md)
  A pink highlight color.
- [NSTextHighlightColorSchemePurple](./nstexthighlightcolorschemepurple.md)
  A purple highlight color.

## See Also

### Getting text content attributes
- [TextKit string attribute keys](./textkit-string-attribute-keys.md)
  UIKit-specific keys you use to apply attributes to ranges of characters in an attributed string.
- [NSTextHighlightStyle](./nstexthighlightstyle.md)
  Constants that specify the type of highlight to apply to text.
- [NSTextEffectStyle](./nstexteffectstyle.md)
  Constants for the type of effect to apply to the text.
- [struct NSUnderlineStyle](./nsunderlinestyle.md)
  Constants for the underline style and strikethrough style attribute keys.
- [enum NSWritingDirectionFormatType](./nswritingdirectionformattype.md)
  Constants for the writing direction attribute key.
- [enum NSTextWritingDirection](./nstextwritingdirection.md)
  Options for specifying text-writing direction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nstexthighlightcolorscheme)*