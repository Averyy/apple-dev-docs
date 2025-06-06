# usesScreenFontsDocumentAttribute

**Framework**: Foundation  
**Kind**: property

The screen fonts attribute.

**Availability**:
- macOS 10.8+

## Declaration

```swift
static let usesScreenFontsDocumentAttribute: NSAttributedString.Key
```

#### Discussion

The value of this attribute is an [`NSNumber`](nsnumber.md) object containing a Boolean; this attribute corresponds to the [`usesScreenFonts`](https://developer.apple.com/documentation/AppKit/NSLayoutManager/usesScreenFonts) method of [`NSLayoutManager`](https://developer.apple.com/documentation/AppKit/NSLayoutManager); if absent, follows the system default setting.

## See Also

- [static let expansion: NSAttributedString.Key](nsattributedstring/key/expansion.md)
  The expansion factor of the text.
- [static let obliqueness: NSAttributedString.Key](nsattributedstring/key/obliqueness.md)
  The obliqueness of the text.
- [static let verticalGlyphForm: NSAttributedString.Key](nsattributedstring/key/verticalglyphform.md)
  The vertical glyph form of the text.
- [static let characterShapeAttributeName: NSAttributedString.Key](nsattributedstring/key/charactershapeattributename.md)
  The character shape attribute.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsattributedstring/key/usesscreenfontsdocumentattribute)*