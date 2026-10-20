# characterShapeAttributeName

**Framework**: Foundation  
**Kind**: property  
**Role**: Type Property

The character shape attribute.

**Availability**:
- macOS 10.0+ - Deprecated in 10.11

> **Deprecated**: This attribute is bound to a specific implementation of ATS feature and not generically supported by wide range of fonts. The majority of characters accessed through this API are now encoded in the Unicode standard. Use the CTFont feature API for fine control over character shape choices.

## Declaration

```swift
static let characterShapeAttributeName: NSAttributedString.Key
```

#### Discussion

An integer value. The value is interpreted as Apple Type Services `kCharacterShapeType selector + 1`.

The character shape feature type (`kCharacterShapeType`) is used when a single font contains different appearances for the same character shape, and these shapes are not traditionally treated as swashes. It is needed for languages such as Chinese that have both traditional and simplified character sets.

The default value is 0 (disable). 1 is `kTraditionalCharactersSelector,` and so on. Refer to `<ATS/SFNTLayoutTypes.h>` and Font Features in ATSUI Programming Guide for additional information.

## See Also

### Deprecated Keys
- [static let expansion: NSAttributedString.Key](./expansion.md)
  The expansion factor of the text.
- [static let obliqueness: NSAttributedString.Key](./obliqueness.md)
  The obliqueness of the text.
- [static let verticalGlyphForm: NSAttributedString.Key](./verticalglyphform.md)
  The vertical glyph form of the text.
- [static let usesScreenFontsDocumentAttribute: NSAttributedString.Key](./usesscreenfontsdocumentattribute.md)
  The screen fonts attribute.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsattributedstring/key/charactershapeattributename)*