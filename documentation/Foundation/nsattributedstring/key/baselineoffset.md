# baselineOffset

**Framework**: Foundation  
**Kind**: property

The vertical offset for the position of the text.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
static let baselineOffset: NSAttributedString.Key
```

#### Discussion

The value of this attribute is an [`NSNumber`](nsnumber.md) object containing a floating point value indicating the character’s offset from the baseline, in points. The default value is `0`.

> ❗ **Important**:  This attribute is different from [`kCTBaselineOffsetAttributeName`](https://developer.apple.com/documentation/CoreText/kCTBaselineOffsetAttributeName); you need to use [`kCTBaselineOffsetAttributeName`](https://developer.apple.com/documentation/CoreText/kCTBaselineOffsetAttributeName) if you are writing code for [`Core Text`](https://developer.apple.com/documentation/CoreText).

## See Also

- [let kCTBaselineOffsetAttributeName: CFString](../CoreText/kCTBaselineOffsetAttributeName.md)
  Vertical offset for text position.
- [static let backgroundColor: NSAttributedString.Key](nsattributedstring/key/backgroundcolor.md)
  The color of the background behind the text.
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
- [static let underlineStyle: NSAttributedString.Key](nsattributedstring/key/underlinestyle.md)
  The underline style of the text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsattributedstring/key/baselineoffset)*