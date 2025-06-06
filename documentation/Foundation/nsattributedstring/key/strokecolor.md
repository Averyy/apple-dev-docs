# strokeColor

**Framework**: Foundation  
**Kind**: property

The color of the stroke.

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
static let strokeColor: NSAttributedString.Key
```

#### Discussion

The value of this parameter is a [`UIColor`](https://developer.apple.com/documentation/UIKit/UIColor) object. If it is not defined  (which is the case by default), it is assumed to be the same as the value of [`foregroundColor`](nsattributedstring/key/foregroundcolor.md); otherwise, it describes the outline color. For more details, see [`Drawing attributed strings that are both filled and stroked`](https://developer.apple.comhttps://developer.apple.com/library/archive/qa/qa1531/_index.html#//apple_ref/doc/uid/DTS40007490).

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

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsattributedstring/key/strokecolor)*