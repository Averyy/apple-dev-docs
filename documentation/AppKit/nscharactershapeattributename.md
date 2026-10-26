# NSCharacterShapeAttributeName

**Framework**: AppKit  
**Kind**: var  
**Role**: Global Variable

The character shape attribute.

**Availability**:
- macOS 10.0+ - Deprecated in 10.11

## Declaration

```c
extern NSAttributedStringKey NSCharacterShapeAttributeName;
```

#### Discussion

An integer value. The value is interpreted as Apple Type Services `kCharacterShapeType selector + 1`.

The character shape feature type (`kCharacterShapeType`) is used when a single font contains different appearances for the same character shape, and these shapes are not traditionally treated as swashes. It is needed for languages such as Chinese that have both traditional and simplified character sets. The default value is `0` (disable). `1` is `kTraditionalCharactersSelector`, and so on. Refer to `<ATS/SFNTLayoutTypes.h>` and Font Features in ATSUI Programming Guide for additional information.

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
- [NSUsesScreenFontsDocumentAttribute](./nsusesscreenfontsdocumentattribute.md)
  The screen fonts attribute.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscharactershapeattributename)*