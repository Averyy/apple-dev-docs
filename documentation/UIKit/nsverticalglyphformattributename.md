# NSVerticalGlyphFormAttributeName

**Framework**: UIKit  
**Kind**: var  
**Role**: Global Variable

The vertical glyph form of the text.

**Availability**:
- iOS 7.0+ - Deprecated in 27.0
- iPadOS 7.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.2
- tvOS 9.0+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 2.0+ - Deprecated in 27.2

## Declaration

```c
extern NSAttributedStringKey const NSVerticalGlyphFormAttributeName;
```

## Discussion

The value of this attribute is an [`NSNumber`](../Foundation/nsnumber.md) object containing an integer. The value `0` indicates horizontal text. The value `1` indicates vertical text. In iOS, horizontal text is always used and specifying a different value is undefined.

## See Also

### Deprecated
- [NSExpansionAttributeName](./nsexpansionattributename.md)
  The expansion factor of the text.
- [NSObliquenessAttributeName](./nsobliquenessattributename.md)
  The obliqueness of the text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nsverticalglyphformattributename)*