# NSAccessibilityForegroundColorTextAttribute

**Framework**: AppKit  
**Kind**: var  
**Role**: Global Variable

Text foreground color (`CGColorRef`).

**Availability**:
- macOS

## Declaration

```c
extern NSAttributedStringKey const NSAccessibilityForegroundColorTextAttribute;
```

## See Also

### Constants
- [NSAccessibilityAttachmentTextAttribute](./nsaccessibilityattachmenttextattribute.md)
  Text attachment (`id`).
- [NSAccessibilityAutocorrectedTextAttribute](./nsaccessibilityautocorrectedtextattribute.md)
  Autocorrected text (`NSNumber` as a Boolean value).
- [NSAccessibilityBackgroundColorTextAttribute](./nsaccessibilitybackgroundcolortextattribute.md)
  Text background color (`CGColorRef`).
- [NSAccessibilityUnderlineColorTextAttribute](./nsaccessibilityunderlinecolortextattribute.md)
  Text underline color (`CGColorRef`).
- [NSAccessibilityStrikethroughColorTextAttribute](./nsaccessibilitystrikethroughcolortextattribute.md)
  Text strikethrough color (`CGColorRef`).
- [NSAccessibilityUnderlineTextAttribute](./nsaccessibilityunderlinetextattribute.md)
  Text underline style (`NSNumber`).
- [NSAccessibilitySuperscriptTextAttribute](./nsaccessibilitysuperscripttextattribute.md)
  Text superscript style (`NSNumber`). Values > 0 are superscript; values < 0 are subscript.
- [NSAccessibilityStrikethroughTextAttribute](./nsaccessibilitystrikethroughtextattribute.md)
  Text strikethrough (`NSNumber` as a Boolean value).
- [NSAccessibilityShadowTextAttribute](./nsaccessibilityshadowtextattribute.md)
  Text shadow (`NSNumber` as a Boolean value).
- [NSAccessibilityLinkTextAttribute](./nsaccessibilitylinktextattribute.md)
  Text link (`id`).
- [NSAccessibilityMarkedMisspelledTextAttribute](./nsaccessibilitymarkedmisspelledtextattribute.md)
  Misspelled text that is visibly marked as misspelled (`NSNumber` as a Boolean value). If you’re implementing a custom text-editing app, use `NSAccessibilityMarkedMisspelledTextAttribute` to ensure that VoiceOver properly identifies misspelled text to users.
- [NSAccessibilityMisspelledTextAttribute](./nsaccessibilitymisspelledtextattribute.md)
  Misspelled text that isn’t necessarily visibly marked as misspelled (`NSNumber` as a Boolean value).
- [NSAccessibilityFontTextAttribute](./nsaccessibilityfonttextattribute.md)
  Font keys (`NSDictionary`).
- [static let fontName: NSAccessibility.FontAttributeKey](./nsaccessibility-swift.struct/fontattributekey/fontname.md)
  A required key for a font name.
- [static let fontFamily: NSAccessibility.FontAttributeKey](./nsaccessibility-swift.struct/fontattributekey/fontfamily.md)
  An optional key for a font family.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsaccessibilityforegroundcolortextattribute)*