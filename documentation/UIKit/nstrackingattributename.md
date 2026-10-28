# NSTrackingAttributeName

**Framework**: UIKit  
**Kind**: var  
**Role**: Global Variable

The amount to modify the default tracking.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```c
extern NSAttributedStringKey const NSTrackingAttributeName;
```

## Overview

The value of this attribute is an [`NSNumber`](../Foundation/nsnumber.md) object containing a floating-point value. The value represents the amount of space, in points, to add between the specified characters. A positive value increases the spacing between characters, and a negative value brings the characters closer together. Specify `0` to disable tracking.

The effect of this attribute is similar to the effect of [`NSKernAttributeName`](./nskernattributename.md), but the system treats tracking as trailing whitespace. A nonzero amount of tracking disables nonessential ligatures, unless the [`NSLigatureAttributeName`](./nsligatureattributename.md) attribute is present.

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
- [NSStrokeWidthAttributeName](./nsstrokewidthattributename.md)
  The width of the stroke.
- [NSUnderlineColorAttributeName](./nsunderlinecolorattributename.md)
  The color of the underline.
- [NSUnderlineStyleAttributeName](./nsunderlinestyleattributename.md)
  The underline style of the text.
- [NSWritingDirectionAttributeName](./nswritingdirectionattributename.md)
  The writing direction of the text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nstrackingattributename)*