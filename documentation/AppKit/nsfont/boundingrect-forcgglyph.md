# boundingRect(forCGGlyph:)

**Framework**: AppKit  
**Kind**: method

Returns the bounding rectangle for the specified glyph, scaled to the receiver’s size.

**Availability**:
- macOS 10.13+

## Declaration

```swift
func boundingRect(forCGGlyph glyph: CGGlyph) -> NSRect
```

#### Discussion

Japanese fonts encoded with the scheme “EUC12-NJE-CFEncoding” do not have individual metrics or bounding boxes available for the glyphs above 127. For those glyphs, this method returns the bounding rectangle for the font instead.

## See Also

- [var boundingRectForFont: NSRect](nsfont/boundingrectforfont.md)
  The font’s bounding rectangle, scaled to the font’s size.
- [func getBoundingRects(NSRectArray, forCGGlyphs: UnsafePointer<CGGlyph>, count: Int)](nsfont/getboundingrects(_:forcgglyphs:count:).md)
  Returns an array of the bounding rectangles for the specified glyphs rendered by the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfont/boundingrect(forcgglyph:))*