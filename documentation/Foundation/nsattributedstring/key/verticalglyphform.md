# verticalGlyphForm

**Framework**: Foundation  
**Kind**: property

The vertical glyph form of the text.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
static let verticalGlyphForm: NSAttributedString.Key
```

#### Discussion

The value of this attribute is an [`NSNumber`](nsnumber.md) object containing an integer. The value `0` indicates horizontal text. The value `1` indicates vertical text. In iOS, horizontal text is always used and specifying a different value is undefined.

## See Also

- [static let expansion: NSAttributedString.Key](nsattributedstring/key/expansion.md)
  The expansion factor of the text.
- [static let obliqueness: NSAttributedString.Key](nsattributedstring/key/obliqueness.md)
  The obliqueness of the text.
- [static let characterShapeAttributeName: NSAttributedString.Key](nsattributedstring/key/charactershapeattributename.md)
  The character shape attribute.
- [static let usesScreenFontsDocumentAttribute: NSAttributedString.Key](nsattributedstring/key/usesscreenfontsdocumentattribute.md)
  The screen fonts attribute.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsattributedstring/key/verticalglyphform)*