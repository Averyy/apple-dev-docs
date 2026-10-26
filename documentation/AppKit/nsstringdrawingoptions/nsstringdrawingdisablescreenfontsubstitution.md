# NSStringDrawingDisableScreenFontSubstitution

**Framework**: AppKit  
**Kind**: case  
**Role**: Enumeration Case

An option that disables screen font substitution.

**Availability**:
- macOS 10.0+ - Deprecated in 10.11

## Declaration

```c
NSStringDrawingDisableScreenFontSubstitution
```

#### Discussion

This option is equivalent to setting [`usesScreenFonts`](../nslayoutmanager/usesscreenfonts.md) to [`false`](../../Swift/false.md).

## See Also

### Constants
- [NSStringDrawingUsesLineFragmentOrigin](./nsstringdrawinguseslinefragmentorigin.md)
  Uses the line fragment origin instead of the baseline origin.
- [NSStringDrawingUsesFontLeading](./nsstringdrawingusesfontleading.md)
  Uses the font leading for calculating line heights.
- [NSStringDrawingUsesDeviceMetrics](./nsstringdrawingusesdevicemetrics.md)
  Uses image glyph bounds instead of typographic bounds.
- [NSStringDrawingTruncatesLastVisibleLine](./nsstringdrawingtruncateslastvisibleline.md)
  Truncates and adds the ellipsis character to the last visible line if the text doesn’t fit into the specified bounds.
- [NSStringDrawingOneShot](./nsstringdrawingoneshot.md)
  Suppresses caching layout information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsstringdrawingoptions/nsstringdrawingdisablescreenfontsubstitution)*