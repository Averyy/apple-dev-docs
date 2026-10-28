# expansion

**Framework**: Foundation  
**Kind**: property  
**Role**: Type Property

The expansion factor of the text.

**Availability**:
- iOS 7.0+ - Deprecated in 27.2
- iPadOS 7.0+ - Deprecated in 27.2
- Mac Catalyst 13.1+ - Deprecated in 27.2
- macOS 10.0+ - Deprecated in 27.2
- tvOS 9.0+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 2.0+ - Deprecated in 27.2

> **Deprecated**: This attribute is not supported with TextKit 2

## Declaration

```swift
static let expansion: NSAttributedString.Key
```

## Discussion

The value of this attribute is an [`NSNumber`](../../nsnumber.md) object containing a floating point value indicating the log of the expansion factor to be applied to glyphs. The default value is `0`, indicating no expansion.

## See Also

### Deprecated Keys
- [static let obliqueness: NSAttributedString.Key](./obliqueness.md)
  The obliqueness of the text.
- [static let verticalGlyphForm: NSAttributedString.Key](./verticalglyphform.md)
  The vertical glyph form of the text.
- [static let characterShapeAttributeName: NSAttributedString.Key](./charactershapeattributename.md)
  The character shape attribute.
- [static let usesScreenFontsDocumentAttribute: NSAttributedString.Key](./usesscreenfontsdocumentattribute.md)
  The screen fonts attribute.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsattributedstring/key/expansion)*