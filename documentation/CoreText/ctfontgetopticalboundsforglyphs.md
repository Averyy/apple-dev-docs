# CTFontGetOpticalBoundsForGlyphs(_:_:_:_:_:)

**Framework**: Core Text  
**Kind**: func

Calculates the optical bounds for an array of glyphs and returns the overall optical bounds for the run.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func CTFontGetOpticalBoundsForGlyphs(_ font: CTFont, _ glyphs: UnsafePointer<CGGlyph>, _ boundingRects: UnsafeMutablePointer<CGRect>?, _ count: CFIndex, _ options: CFOptionFlags) -> CGRect
```

#### Return Value

This function returns the overall bounding rectangle for an array of glyphs. The `boundingRects` parameter returns the bounding rectangles of the individual glyphs. These rectangles are the design metrics from the font transformed in font space.

#### Discussion

Fonts may specify the optical edges of glyphs that can be used to make the edges of lines of text line up in a more visually pleasing way. This function returns bounding rectangles that correspond to these specifications if the font provides them; otherwise, it returns typographic bounding rectangles, composed of the font’s ascender and descender and a glyph’s advance width.

## Parameters

- `font`: The font reference.
- `glyphs`: An array of glyphs.
- `boundingRects`: An array of  s to receive the computed glyph bounds. This parameter can be  , in which case the function only calculates the overall bounding rectangle.
- `count`: The capacity of the   and   buffers.
- `options`: Reserved, set to zero.

## See Also

- [func CTFontCreatePathForGlyph(CTFont, CGGlyph, UnsafePointer<CGAffineTransform>?) -> CGPath?](ctfontcreatepathforglyph(_:_:_:).md)
  Creates a path for the specified glyph.
- [func CTFontGetGlyphWithName(CTFont, CFString) -> CGGlyph](ctfontgetglyphwithname(_:_:).md)
  Returns the glyph for the specified name.
- [func CTFontGetBoundingRectsForGlyphs(CTFont, CTFontOrientation, UnsafePointer<CGGlyph>, UnsafeMutablePointer<CGRect>?, CFIndex) -> CGRect](ctfontgetboundingrectsforglyphs(_:_:_:_:_:).md)
  Calculates the bounding rects for an array of glyphs and returns the overall bounding rectangle for the glyph run.
- [func CTFontGetAdvancesForGlyphs(CTFont, CTFontOrientation, UnsafePointer<CGGlyph>, UnsafeMutablePointer<CGSize>?, CFIndex) -> Double](ctfontgetadvancesforglyphs(_:_:_:_:_:).md)
  Calculates the advances for an array of glyphs and returns the summed advance.
- [func CTFontGetVerticalTranslationsForGlyphs(CTFont, UnsafePointer<CGGlyph>, UnsafeMutablePointer<CGSize>, CFIndex)](ctfontgetverticaltranslationsforglyphs(_:_:_:_:).md)
  Calculates the offset from the default (horizontal) origin to the vertical origin for an array of glyphs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/ctfontgetopticalboundsforglyphs(_:_:_:_:_:))*