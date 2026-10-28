# verticalGlyphForm

**Framework**: Foundation  
**Kind**: property  
**Role**: Type Property

The vertical glyph form of the text.

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
static let verticalGlyphForm: NSAttributedString.Key
```

## Discussion

The value of this attribute is an [`NSNumber`](../../nsnumber.md) object containing an integer. The value `0` indicates horizontal text. The value `1` indicates vertical text. In iOS, horizontal text is always used and specifying a different value is undefined.

## See Also

### Deprecated Keys
- [static let expansion: NSAttributedString.Key](./expansion.md)
  The expansion factor of the text.
- [static let obliqueness: NSAttributedString.Key](./obliqueness.md)
  The obliqueness of the text.
- [static let characterShapeAttributeName: NSAttributedString.Key](./charactershapeattributename.md)
  The character shape attribute.
- [static let usesScreenFontsDocumentAttribute: NSAttributedString.Key](./usesscreenfontsdocumentattribute.md)
  The screen fonts attribute.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsattributedstring/key/verticalglyphform)*