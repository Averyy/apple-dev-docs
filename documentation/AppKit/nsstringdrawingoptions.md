# NSStringDrawingOptions

**Framework**: AppKit  
**Kind**: enum  
**Role**: Enumeration

Constants that specify the rendering options for drawing a string.

**Availability**:
- macOS 10.0+

## Declaration

```c
enum NSStringDrawingOptions : NSInteger;
```

## Topics

### Constants
- [NSStringDrawingUsesLineFragmentOrigin](./nsstringdrawingoptions/nsstringdrawinguseslinefragmentorigin.md)
  Uses the line fragment origin instead of the baseline origin.
- [NSStringDrawingUsesFontLeading](./nsstringdrawingoptions/nsstringdrawingusesfontleading.md)
  Uses the font leading for calculating line heights.
- [NSStringDrawingUsesDeviceMetrics](./nsstringdrawingoptions/nsstringdrawingusesdevicemetrics.md)
  Uses image glyph bounds instead of typographic bounds.
- [NSStringDrawingTruncatesLastVisibleLine](./nsstringdrawingoptions/nsstringdrawingtruncateslastvisibleline.md)
  Truncates and adds the ellipsis character to the last visible line if the text doesn’t fit into the specified bounds.
- [NSStringDrawingDisableScreenFontSubstitution](./nsstringdrawingoptions/nsstringdrawingdisablescreenfontsubstitution.md)
  An option that disables screen font substitution.
- [NSStringDrawingOneShot](./nsstringdrawingoptions/nsstringdrawingoneshot.md)
  Suppresses caching layout information.
### Enumeration Cases
- [NSStringDrawingOptionsResolvesNaturalAlignmentWithBaseWritingDirection](./nsstringdrawingoptions/nsstringdrawingoptionsresolvesnaturalalignmentwithbasewritingdirection.md)
  Specifies the behavior for resolving [`NSTextAlignment.natural`](./nstextalignment/natural.md) to the visual alignment.

## See Also

### Strings
- [class NSStringDrawingContext](./nsstringdrawingcontext.md)
  An object that manages metrics for drawing attributed strings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsstringdrawingoptions)*