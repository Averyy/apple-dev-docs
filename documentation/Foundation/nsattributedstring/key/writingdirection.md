# writingDirection

**Framework**: Foundation  
**Kind**: property

The writing direction of the text.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
static let writingDirection: NSAttributedString.Key
```

#### Discussion

The value of this attribute is an [`NSArray`](nsarray.md) object containing [`NSNumber`](nsnumber.md) objects representing the nested levels of writing direction overrides, in order from outermost to innermost.

This attribute provides a means to override the default bidirectional text algorithm, equivalent to using the Unicode bidi control characters `LRE`, `RLE`, `LRO`, or `RLO` paired with `PDF`, but as a higher-level attribute. (See [`Unicode Standard Annex #9`](https://developer.apple.comhttp://unicode.org/reports/tr9/) for information about the Unicode bidi formatting codes.) The `NSWritingDirectionAttributeName` constant is a character-level attribute that provides a higher-level alternative to the inclusion of explicit bidirectional control characters in text. It is the `NSAttributedString` equivalent of the HTML markup using `bdo` element with the `dir` attribute.

The values of the `NSNumber` objects should be `0`, `1`, `2`, or `3`, for `LRE`, `RLE`, `LRO`, or `RLO` respectively, and combinations of [`NSWritingDirection.leftToRight`](https://developer.apple.com/documentation/AppKit/NSWritingDirection/leftToRight) and [`NSWritingDirection.rightToLeft`](https://developer.apple.com/documentation/AppKit/NSWritingDirection/rightToLeft) with [`NSTextWritingDirectionEmbedding`](https://developer.apple.com/documentation/AppKit/NSTextWritingDirectionEmbedding) or `NSTextWritingDirectionOverride`, as shown in the following table.

| Array NSNumber Values | Unicode Control Characters | Writing Direction Constants |
| --- | --- | --- |
| `0` | `LRE` | `NSWritingDirectionLeftToRight` | `NSTextWritingDirectionEmbedding` |
| `1` | `RLE` | `NSWritingDirectionRightToLeft` | `NSTextWritingDirectionEmbedding` |
| `2` | `LRO` | `NSWritingDirectionLeftToRight` | `NSTextWritingDirectionOverride` |
| `3` | `RLO` | `NSWritingDirectionRightToLeft` | `NSTextWritingDirectionOverride` |

## See Also

- [static let backgroundColor: NSAttributedString.Key](nsattributedstring/key/backgroundcolor.md)
  The color of the background behind the text.
- [static let baselineOffset: NSAttributedString.Key](nsattributedstring/key/baselineoffset.md)
  The vertical offset for the position of the text.
- [static let font: NSAttributedString.Key](nsattributedstring/key/font.md)
  The font of the text.
- [static let foregroundColor: NSAttributedString.Key](nsattributedstring/key/foregroundcolor.md)
  The color of the text.
- [static let glyphInfo: NSAttributedString.Key](nsattributedstring/key/glyphinfo.md)
  The name of a glyph info object.
- [static let kern: NSAttributedString.Key](nsattributedstring/key/kern.md)
  The kerning of the text.
- [static let ligature: NSAttributedString.Key](nsattributedstring/key/ligature.md)
  The ligature of the text.
- [static let paragraphStyle: NSAttributedString.Key](nsattributedstring/key/paragraphstyle.md)
  The paragraph style of the text.
- [static let strikethroughColor: NSAttributedString.Key](nsattributedstring/key/strikethroughcolor.md)
  The color of the strikethrough.
- [static let strikethroughStyle: NSAttributedString.Key](nsattributedstring/key/strikethroughstyle.md)
  The strikethrough style of the text.
- [static let strokeColor: NSAttributedString.Key](nsattributedstring/key/strokecolor.md)
  The color of the stroke.
- [static let strokeWidth: NSAttributedString.Key](nsattributedstring/key/strokewidth.md)
  The width of the stroke.
- [static let superscript: NSAttributedString.Key](nsattributedstring/key/superscript.md)
  The superscript of the text.
- [static let tracking: NSAttributedString.Key](nsattributedstring/key/tracking.md)
  The amount to modify the default tracking.
- [static let underlineColor: NSAttributedString.Key](nsattributedstring/key/underlinecolor.md)
  The color of the underline.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsattributedstring/key/writingdirection)*