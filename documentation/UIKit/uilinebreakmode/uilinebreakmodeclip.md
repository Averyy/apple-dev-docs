# UILineBreakModeClip

**Framework**: UIKit  
**Kind**: case  
**Role**: Enumeration Case

Clip the text when reaching the end of the drawing rectangle.

**Availability**:
- iOS 2.0+ - Deprecated in 6.0
- iPadOS 2.0+ - Deprecated in 6.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: Use [`NSLineBreakMode.byClipping`](../nslinebreakmode/byclipping.md) instead.

## Declaration

```c
UILineBreakModeClip
```

## Discussion

This option could result in a partially rendered character at the end of a string.

## See Also

### Deprecated constants
- [UILineBreakModeWordWrap](./uilinebreakmodewordwrap.md)
  Wrap or clip the string only at word boundaries.
- [UILineBreakModeCharacterWrap](./uilinebreakmodecharacterwrap.md)
  Wrap or clip the string at the closest character boundary.
- [UILineBreakModeHeadTruncation](./uilinebreakmodeheadtruncation.md)
  Truncate text (as necessary) from the beginning of the line.
- [UILineBreakModeTailTruncation](./uilinebreakmodetailtruncation.md)
  Truncate text (as necessary) from the end of the line.
- [UILineBreakModeMiddleTruncation](./uilinebreakmodemiddletruncation.md)
  Truncate text (as necessary) from the middle of the line.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uilinebreakmode/uilinebreakmodeclip)*