# boundingRectForFont

**Framework**: AppKit  
**Kind**: property

The font’s bounding rectangle, scaled to the font’s size.

**Availability**:
- macOS ?+

## Declaration

```swift
var boundingRectForFont: NSRect { get }
```

#### Discussion

The bounding rectangle is the union of the bounding rectangles of every glyph in the font.

## See Also

- [func boundingRect(forGlyph: NSGlyph) -> NSRect](nsfont/boundingrect(forglyph:).md)
  Returns the bounding rectangle for the specified glyph, scaled to the receiver’s size.
- [func boundingRect(forCGGlyph: CGGlyph) -> NSRect](nsfont/boundingrect(forcgglyph:).md)
  Returns the bounding rectangle for the specified glyph, scaled to the receiver’s size.
- [func getBoundingRects(NSRectArray, forCGGlyphs: UnsafePointer<CGGlyph>, count: Int)](nsfont/getboundingrects(_:forcgglyphs:count:).md)
  Returns an array of the bounding rectangles for the specified glyphs rendered by the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfont/boundingrectforfont)*