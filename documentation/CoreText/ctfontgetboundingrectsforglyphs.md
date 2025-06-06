# CTFontGetBoundingRectsForGlyphs(_:_:_:_:_:)

**Framework**: Core Text  
**Kind**: func

Calculates the bounding rects for an array of glyphs and returns the overall bounding rectangle for the glyph run.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func CTFontGetBoundingRectsForGlyphs(_ font: CTFont, _ orientation: CTFontOrientation, _ glyphs: UnsafePointer<CGGlyph>, _ boundingRects: UnsafeMutablePointer<CGRect>?, _ count: CFIndex) -> CGRect
```

#### Return Value

The overall bounding rectangle for an array or run of glyphs. Returns [`CGRectNull`](https://developer.apple.com/documentation/CoreGraphics/CGRectNull) on error.

#### Discussion

The bounding rectangles of the individual glyphs are returned through the `boundingRects` parameter. These are the design metrics from the font transformed in font space.

## Parameters

- `font`: The font reference.
- `orientation`: The intended drawing orientation of the glyphs. Used to determined which glyph metrics to return.
- `glyphs`: An array of   number of glyphs.
- `boundingRects`: On output, the computed glyph rectangles in an array of   number of   objects. If  , only the overall bounding rectangle is calculated.
- `count`: The capacity of the   and   buffers.

## See Also

- [func CTFontCreatePathForGlyph(CTFont, CGGlyph, UnsafePointer<CGAffineTransform>?) -> CGPath?](ctfontcreatepathforglyph(_:_:_:).md)
  Creates a path for the specified glyph.
- [func CTFontGetGlyphWithName(CTFont, CFString) -> CGGlyph](ctfontgetglyphwithname(_:_:).md)
  Returns the glyph for the specified name.
- [func CTFontGetAdvancesForGlyphs(CTFont, CTFontOrientation, UnsafePointer<CGGlyph>, UnsafeMutablePointer<CGSize>?, CFIndex) -> Double](ctfontgetadvancesforglyphs(_:_:_:_:_:).md)
  Calculates the advances for an array of glyphs and returns the summed advance.
- [func CTFontGetOpticalBoundsForGlyphs(CTFont, UnsafePointer<CGGlyph>, UnsafeMutablePointer<CGRect>?, CFIndex, CFOptionFlags) -> CGRect](ctfontgetopticalboundsforglyphs(_:_:_:_:_:).md)
  Calculates the optical bounds for an array of glyphs and returns the overall optical bounds for the run.
- [func CTFontGetVerticalTranslationsForGlyphs(CTFont, UnsafePointer<CGGlyph>, UnsafeMutablePointer<CGSize>, CFIndex)](ctfontgetverticaltranslationsforglyphs(_:_:_:_:).md)
  Calculates the offset from the default (horizontal) origin to the vertical origin for an array of glyphs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/ctfontgetboundingrectsforglyphs(_:_:_:_:_:))*