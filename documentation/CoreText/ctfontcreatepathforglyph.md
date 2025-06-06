# CTFontCreatePathForGlyph(_:_:_:)

**Framework**: Core Text  
**Kind**: func

Creates a path for the specified glyph.

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
func CTFontCreatePathForGlyph(_ font: CTFont, _ glyph: CGGlyph, _ matrix: UnsafePointer<CGAffineTransform>?) -> CGPath?
```

#### Return Value

A CGPath object containing the glyph outlines, `NULL` on error. Must be released by caller.

#### Discussion

Creates a path from the outlines of the glyph for the specified font. The path reflects the font point size, matrix, and transform parameter, applied in that order. The transform parameter is most commonly be used to provide a translation to the desired glyph origin.

## Parameters

- `font`: The font reference.
- `glyph`: The glyph.
- `matrix`: An affine transform applied to the path. Can be  . If  ,   is used.

## See Also

- [func CTFontGetGlyphWithName(CTFont, CFString) -> CGGlyph](ctfontgetglyphwithname(_:_:).md)
  Returns the glyph for the specified name.
- [func CTFontGetBoundingRectsForGlyphs(CTFont, CTFontOrientation, UnsafePointer<CGGlyph>, UnsafeMutablePointer<CGRect>?, CFIndex) -> CGRect](ctfontgetboundingrectsforglyphs(_:_:_:_:_:).md)
  Calculates the bounding rects for an array of glyphs and returns the overall bounding rectangle for the glyph run.
- [func CTFontGetAdvancesForGlyphs(CTFont, CTFontOrientation, UnsafePointer<CGGlyph>, UnsafeMutablePointer<CGSize>?, CFIndex) -> Double](ctfontgetadvancesforglyphs(_:_:_:_:_:).md)
  Calculates the advances for an array of glyphs and returns the summed advance.
- [func CTFontGetOpticalBoundsForGlyphs(CTFont, UnsafePointer<CGGlyph>, UnsafeMutablePointer<CGRect>?, CFIndex, CFOptionFlags) -> CGRect](ctfontgetopticalboundsforglyphs(_:_:_:_:_:).md)
  Calculates the optical bounds for an array of glyphs and returns the overall optical bounds for the run.
- [func CTFontGetVerticalTranslationsForGlyphs(CTFont, UnsafePointer<CGGlyph>, UnsafeMutablePointer<CGSize>, CFIndex)](ctfontgetverticaltranslationsforglyphs(_:_:_:_:).md)
  Calculates the offset from the default (horizontal) origin to the vertical origin for an array of glyphs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/ctfontcreatepathforglyph(_:_:_:))*