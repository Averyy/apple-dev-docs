# UILineBreakMode

**Framework**: UIKit  
**Kind**: enum  
**Role**: Enumeration

Options for wrapping and truncating text.

**Availability**:
- iOS 2.0+ - Deprecated in 6.0
- iPadOS 2.0+ - Deprecated in 6.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: Use [`NSLineBreakMode`](./nslinebreakmode.md) instead.

## Declaration

```c
enum UILineBreakMode : NSInteger;
```

## Overview

For methods that draw at a specified point (as opposed to those that draw in a rectangular region), these options specify the clipping behavior that UIKit applies to the string.

## Topics

### Deprecated constants
- [UILineBreakModeWordWrap](./uilinebreakmode/uilinebreakmodewordwrap.md)
  Wrap or clip the string only at word boundaries.
- [UILineBreakModeCharacterWrap](./uilinebreakmode/uilinebreakmodecharacterwrap.md)
  Wrap or clip the string at the closest character boundary.
- [UILineBreakModeClip](./uilinebreakmode/uilinebreakmodeclip.md)
  Clip the text when reaching the end of the drawing rectangle.
- [UILineBreakModeHeadTruncation](./uilinebreakmode/uilinebreakmodeheadtruncation.md)
  Truncate text (as necessary) from the beginning of the line.
- [UILineBreakModeTailTruncation](./uilinebreakmode/uilinebreakmodetailtruncation.md)
  Truncate text (as necessary) from the end of the line.
- [UILineBreakModeMiddleTruncation](./uilinebreakmode/uilinebreakmodemiddletruncation.md)
  Truncate text (as necessary) from the middle of the line.

## See Also

### Deprecated enumerations
- [UITextAlignment](./uitextalignment.md)
  Options for aligning text horizontally.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uilinebreakmode)*