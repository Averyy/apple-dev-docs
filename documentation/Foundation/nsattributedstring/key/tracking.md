# tracking

**Framework**: Foundation  
**Kind**: property  
**Role**: Type Property

The amount to modify the default tracking.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
static let tracking: NSAttributedString.Key
```

## Discussion

The value of this attribute is an [`NSNumber`](../../nsnumber.md) object containing a floating-point value. The value represents the amount of space, in points, to add between the specified characters. A positive value increases the spacing between characters, and a negative value brings the characters closer together. Specify `0` to disable tracking.

The effect of this attribute is similar to the effect of [`kern`](./kern.md), but the system treats tracking as trailing whitespace. A nonzero amount of tracking disables nonessential ligatures, unless the [`ligature`](./ligature.md) attribute is present.

## See Also

### Getting rendering attribute keys
- [static let backgroundColor: NSAttributedString.Key](./backgroundcolor.md)
  The color of the background behind the text.
- [static let baselineOffset: NSAttributedString.Key](./baselineoffset.md)
  The vertical offset for the position of the text.
- [static let font: NSAttributedString.Key](./font.md)
  The font of the text.
- [static let foregroundColor: NSAttributedString.Key](./foregroundcolor.md)
  The color of the text.
- [static let glyphInfo: NSAttributedString.Key](./glyphinfo.md)
  The name of a glyph info object.
- [static let kern: NSAttributedString.Key](./kern.md)
  The kerning of the text.
- [static let ligature: NSAttributedString.Key](./ligature.md)
  The ligature of the text.
- [static let paragraphStyle: NSAttributedString.Key](./paragraphstyle.md)
  The paragraph style of the text.
- [static let strikethroughColor: NSAttributedString.Key](./strikethroughcolor.md)
  The color of the strikethrough.
- [static let strikethroughStyle: NSAttributedString.Key](./strikethroughstyle.md)
  The strikethrough style of the text.
- [static let strokeColor: NSAttributedString.Key](./strokecolor.md)
  The color of the stroke.
- [static let strokeWidth: NSAttributedString.Key](./strokewidth.md)
  The width of the stroke.
- [static let superscript: NSAttributedString.Key](./superscript.md)
  The superscript of the text.
- [static let underlineColor: NSAttributedString.Key](./underlinecolor.md)
  The color of the underline.
- [static let underlineStyle: NSAttributedString.Key](./underlinestyle.md)
  The underline style of the text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsattributedstring/key/tracking)*