# NSLigatureAttributeName

**Framework**: AppKit  
**Kind**: var  
**Role**: Global Variable

The ligature of the text.

**Availability**:
- macOS 10.0+

## Declaration

```c
extern NSAttributedStringKey NSLigatureAttributeName;
```

#### Overview

The value of this attribute is an [`NSNumber`](../Foundation/nsnumber.md) object containing an integer. Ligatures cause specific character combinations to be rendered using a single custom glyph that corresponds to those characters. The value `0` indicates no ligatures. The value `1` indicates the use of the default ligatures. The value `2` indicates the use of all ligatures. The default value for this attribute is `1`. (Value `2` is unsupported on iOS.)

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
- [NSParagraphStyleAttributeName](./nsparagraphstyleattributename.md)
  The paragraph style of the text.
- [NSStrikethroughColorAttributeName](./nsstrikethroughcolorattributename.md)
  The color of the strikethrough.
- [NSStrikethroughStyleAttributeName](./nsstrikethroughstyleattributename.md)
  The strikethrough style of the text.
- [NSStrokeColorAttributeName](./nsstrokecolorattributename.md)
  The color of the stroke.
- [NSStrokeWidthAttributeName](./nsstrokewidthattributename.md)
  The width of the stroke.
- [NSSuperscriptAttributeName](./nssuperscriptattributename.md)
  The superscript of the text.
- [NSTrackingAttributeName](./nstrackingattributename.md)
  The amount to modify the default tracking.
- [NSUnderlineColorAttributeName](./nsunderlinecolorattributename.md)
  The color of the underline.
- [NSUnderlineStyleAttributeName](./nsunderlinestyleattributename.md)
  The underline style of the text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsligatureattributename)*