# glyphInfo

**Framework**: Foundation  
**Kind**: property  
**Role**: Type Property

The name of a glyph info object.

**Availability**:
- macOS 10.0+

## Declaration

```swift
static let glyphInfo: NSAttributedString.Key
```

#### Discussion

The [`NSLayoutManager`](../../../AppKit/nslayoutmanager.md) object assigns the glyph specified by this [`NSGlyphInfo`](../../../AppKit/nsglyphinfo.md) object to the entire attribute range, provided that its contents match the specified base string, and that the specified glyph is available in the font specified by `NSFontAttributeName`.

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
- [static let tracking: NSAttributedString.Key](./tracking.md)
  The amount to modify the default tracking.
- [static let underlineColor: NSAttributedString.Key](./underlinecolor.md)
  The color of the underline.
- [static let underlineStyle: NSAttributedString.Key](./underlinestyle.md)
  The underline style of the text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsattributedstring/key/glyphinfo)*