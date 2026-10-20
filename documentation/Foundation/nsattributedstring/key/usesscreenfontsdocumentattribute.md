# usesScreenFontsDocumentAttribute

**Framework**: Foundation  
**Kind**: property  
**Role**: Type Property

The screen fonts attribute.

**Availability**:
- macOS 10.8+ - Deprecated in 10.11

## Declaration

```swift
static let usesScreenFontsDocumentAttribute: NSAttributedString.Key
```

#### Discussion

The value of this attribute is an [`NSNumber`](../../nsnumber.md) object containing a Boolean; this attribute corresponds to the [`usesScreenFonts`](../../../AppKit/nslayoutmanager/usesscreenfonts.md) method of [`NSLayoutManager`](../../../AppKit/nslayoutmanager.md); if absent, follows the system default setting.

## See Also

### Deprecated Keys
- [static let expansion: NSAttributedString.Key](./expansion.md)
  The expansion factor of the text.
- [static let obliqueness: NSAttributedString.Key](./obliqueness.md)
  The obliqueness of the text.
- [static let verticalGlyphForm: NSAttributedString.Key](./verticalglyphform.md)
  The vertical glyph form of the text.
- [static let characterShapeAttributeName: NSAttributedString.Key](./charactershapeattributename.md)
  The character shape attribute.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsattributedstring/key/usesscreenfontsdocumentattribute)*