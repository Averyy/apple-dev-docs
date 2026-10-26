# NSStringDrawingTruncatesLastVisibleLine

**Framework**: AppKit  
**Kind**: case  
**Role**: Enumeration Case

Truncates and adds the ellipsis character to the last visible line if the text doesn’t fit into the specified bounds.

**Availability**:
- macOS 10.5+

## Declaration

```c
NSStringDrawingTruncatesLastVisibleLine
```

#### Discussion

This option is ignored if `NSStringDrawingUsesLineFragmentOrigin` is not also set. In addition, the line break mode must be either `NSLineBreakByWordWrapping` or `NSLineBreakByCharWrapping` for this option to take effect. The line break mode can be specified in a paragraph style passed in the attributes dictionary argument of the drawing methods.

## See Also

### Constants
- [NSStringDrawingUsesLineFragmentOrigin](./nsstringdrawinguseslinefragmentorigin.md)
  Uses the line fragment origin instead of the baseline origin.
- [NSStringDrawingUsesFontLeading](./nsstringdrawingusesfontleading.md)
  Uses the font leading for calculating line heights.
- [NSStringDrawingUsesDeviceMetrics](./nsstringdrawingusesdevicemetrics.md)
  Uses image glyph bounds instead of typographic bounds.
- [NSStringDrawingDisableScreenFontSubstitution](./nsstringdrawingdisablescreenfontsubstitution.md)
  An option that disables screen font substitution.
- [NSStringDrawingOneShot](./nsstringdrawingoneshot.md)
  Suppresses caching layout information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsstringdrawingoptions/nsstringdrawingtruncateslastvisibleline)*