# NSExpansionAttributeName

**Framework**: AppKit  
**Kind**: var  
**Role**: Global Variable

The expansion factor of the text.

**Availability**:
- macOS 10.0+ - Deprecated in 27.0

## Declaration

```c
extern NSAttributedStringKey NSExpansionAttributeName;
```

## Discussion

The value of this attribute is an [`NSNumber`](../Foundation/nsnumber.md) object containing a floating point value indicating the log of the expansion factor to be applied to glyphs. The default value is `0`, indicating no expansion.

## See Also

### Deprecated
- [NSAccessibilityAttachmentTextAttribute](./nsaccessibilityattachmenttextattribute.md)
  Text attachment (`id`).
- [NSObliquenessAttributeName](./nsobliquenessattributename.md)
  The obliqueness of the text.
- [NSVerticalGlyphFormAttributeName](./nsverticalglyphformattributename.md)
  The vertical glyph form of the text.
- [NSCharacterShapeAttributeName](./nscharactershapeattributename.md)
  The character shape attribute.
- [NSUsesScreenFontsDocumentAttribute](./nsusesscreenfontsdocumentattribute.md)
  The screen fonts attribute.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsexpansionattributename)*