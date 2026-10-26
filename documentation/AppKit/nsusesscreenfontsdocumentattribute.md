# NSUsesScreenFontsDocumentAttribute

**Framework**: AppKit  
**Kind**: var  
**Role**: Global Variable

The screen fonts attribute.

**Availability**:
- macOS 10.8+ - Deprecated in 10.11

## Declaration

```c
extern NSAttributedStringKey NSUsesScreenFontsDocumentAttribute;
```

#### Discussion

The value of this attribute is an [`NSNumber`](../Foundation/nsnumber.md) object containing a Boolean; this attribute corresponds to the [`usesScreenFonts`](./nslayoutmanager/usesscreenfonts.md) method of [`NSLayoutManager`](./nslayoutmanager.md); if absent, follows the system default setting.

## See Also

### Deprecated
- [NSAccessibilityAttachmentTextAttribute](./nsaccessibilityattachmenttextattribute.md)
  Text attachment (`id`).
- [NSExpansionAttributeName](./nsexpansionattributename.md)
  The expansion factor of the text.
- [NSObliquenessAttributeName](./nsobliquenessattributename.md)
  The obliqueness of the text.
- [NSVerticalGlyphFormAttributeName](./nsverticalglyphformattributename.md)
  The vertical glyph form of the text.
- [NSCharacterShapeAttributeName](./nscharactershapeattributename.md)
  The character shape attribute.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsusesscreenfontsdocumentattribute)*