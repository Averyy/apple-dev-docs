# NSStrokeWidthAttributeName

**Framework**: AppKit  
**Kind**: var  
**Role**: Global Variable

The width of the stroke.

**Availability**:
- macOS 10.0+

## Declaration

```c
extern NSAttributedStringKey NSStrokeWidthAttributeName;
```

## Overview

The value of this attribute is an [`NSNumber`](../Foundation/nsnumber.md) object containing a floating-point value. This value represents the amount to change the stroke width and is specified as a percentage of the font point size. Specify `0` (the default) for no additional changes. Specify positive values to change the stroke width alone. Specify negative values to stroke and fill the text. For example, a typical value for outlined text would be `3.0`.

## See Also

### Getting rendering attribute keys
- [NSBackgroundColorAttributeName](./nsbackgroundcolorattributename.md)
  The color of the background behind the text.
- [NSBaselineOffsetAttributeName](./nsbaselineoffsetattributename.md)
  The vertical offset for the position of the text.
- [NSFontAttributeName](./nsfontattributename.md)
  The font of the text.
- [NSForegroundColorAttributeName](./nsforegroundcolorattributename.md)
  The color of the text.
- [NSGlyphInfoAttributeName](./nsglyphinfoattributename.md)
  The name of a glyph info object.
- [NSKernAttributeName](./nskernattributename.md)
  The kerning of the text.
- [NSLigatureAttributeName](./nsligatureattributename.md)
  The ligature of the text.
- [NSParagraphStyleAttributeName](./nsparagraphstyleattributename.md)
  The paragraph style of the text.
- [NSStrikethroughColorAttributeName](./nsstrikethroughcolorattributename.md)
  The color of the strikethrough.
- [NSStrikethroughStyleAttributeName](./nsstrikethroughstyleattributename.md)
  The strikethrough style of the text.
- [NSStrokeColorAttributeName](./nsstrokecolorattributename.md)
  The color of the stroke.
- [NSSuperscriptAttributeName](./nssuperscriptattributename.md)
  The superscript of the text.
- [NSTrackingAttributeName](./nstrackingattributename.md)
  The amount to modify the default tracking.
- [NSUnderlineColorAttributeName](./nsunderlinecolorattributename.md)
  The color of the underline.
- [NSUnderlineStyleAttributeName](./nsunderlinestyleattributename.md)
  The underline style of the text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsstrokewidthattributename)*