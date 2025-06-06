# strokeWidth

**Framework**: Foundation  
**Kind**: property

The width of the stroke.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
static let strokeWidth: NSAttributedString.Key
```

#### Discussion

The value of this attribute is an [`NSNumber`](nsnumber.md) object containing a floating-point value. This value represents the amount to change the stroke width and is specified as a percentage of the font point size. Specify `0` (the default) for no additional changes. Specify positive values to change the stroke width alone. Specify negative values to stroke and fill the text. For example, a typical value for outlined text would be `3.0`.

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
- [static let superscript: NSAttributedString.Key](nsattributedstring/key/superscript.md)
  The superscript of the text.
- [static let tracking: NSAttributedString.Key](nsattributedstring/key/tracking.md)
  The amount to modify the default tracking.
- [static let underlineColor: NSAttributedString.Key](nsattributedstring/key/underlinecolor.md)
  The color of the underline.
- [static let underlineStyle: NSAttributedString.Key](nsattributedstring/key/underlinestyle.md)
  The underline style of the text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsattributedstring/key/strokewidth)*