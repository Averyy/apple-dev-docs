# NSStrokeColorAttributeName

**Framework**: AppKit  
**Kind**: var  
**Role**: Global Variable

The color of the stroke.

**Availability**:
- macOS 10.0+

## Declaration

```c
extern NSAttributedStringKey NSStrokeColorAttributeName;
```

#### Overview

The value of this parameter is a [`UIColor`](../UIKit/uicolor.md) object. If it is not defined (which is the case by default), it is assumed to be the same as the value of [`NSForegroundColorAttributeName`](./nsforegroundcolorattributename.md); otherwise, it describes the outline color. For more details, see [Drawing attributed strings that are both filled and stroked](https://developer.apple.com/library/archive/qa/qa1531/_index.html#//apple_ref/doc/uid/DTS40007490).

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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsstrokecolorattributename)*