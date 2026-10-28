# NSVerticalGlyphFormAttributeName

**Framework**: AppKit  
**Kind**: var  
**Role**: Global Variable

The vertical glyph form of the text.

**Availability**:
- macOS 10.0+ - Deprecated in 27.0

## Declaration

```c
extern NSAttributedStringKey NSVerticalGlyphFormAttributeName;
```

## Discussion

The value of this attribute is an [`NSNumber`](../Foundation/nsnumber.md) object containing an integer. The value `0` indicates horizontal text. The value `1` indicates vertical text. In iOS, horizontal text is always used and specifying a different value is undefined.

## See Also

### Deprecated
- [NSAccessibilityAttachmentTextAttribute](./nsaccessibilityattachmenttextattribute.md)
  Text attachment (`id`).
- [NSExpansionAttributeName](./nsexpansionattributename.md)
  The expansion factor of the text.
- [NSObliquenessAttributeName](./nsobliquenessattributename.md)
  The obliqueness of the text.
- [NSCharacterShapeAttributeName](./nscharactershapeattributename.md)
  The character shape attribute.
- [NSUsesScreenFontsDocumentAttribute](./nsusesscreenfontsdocumentattribute.md)
  The screen fonts attribute.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsverticalglyphformattributename)*