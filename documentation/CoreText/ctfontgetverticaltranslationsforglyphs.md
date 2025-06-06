# CTFontGetVerticalTranslationsForGlyphs(_:_:_:_:)

**Framework**: Core Text  
**Kind**: func

Calculates the offset from the default (horizontal) origin to the vertical origin for an array of glyphs.

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
func CTFontGetVerticalTranslationsForGlyphs(_ font: CTFont, _ glyphs: UnsafePointer<CGGlyph>, _ translations: UnsafeMutablePointer<CGSize>, _ count: CFIndex)
```

## Parameters

- `font`: The font reference.
- `glyphs`: An array of   number of glyphs.
- `translations`: On output, the computed origin offsets in an array of   number of   objects.
- `count`: The capacity of the   and   buffers.

## See Also

- [func CTFontCreatePathForGlyph(CTFont, CGGlyph, UnsafePointer<CGAffineTransform>?) -> CGPath?](ctfontcreatepathforglyph(_:_:_:).md)
  Creates a path for the specified glyph.
- [func CTFontGetGlyphWithName(CTFont, CFString) -> CGGlyph](ctfontgetglyphwithname(_:_:).md)
  Returns the glyph for the specified name.
- [func CTFontGetBoundingRectsForGlyphs(CTFont, CTFontOrientation, UnsafePointer<CGGlyph>, UnsafeMutablePointer<CGRect>?, CFIndex) -> CGRect](ctfontgetboundingrectsforglyphs(_:_:_:_:_:).md)
  Calculates the bounding rects for an array of glyphs and returns the overall bounding rectangle for the glyph run.
- [func CTFontGetAdvancesForGlyphs(CTFont, CTFontOrientation, UnsafePointer<CGGlyph>, UnsafeMutablePointer<CGSize>?, CFIndex) -> Double](ctfontgetadvancesforglyphs(_:_:_:_:_:).md)
  Calculates the advances for an array of glyphs and returns the summed advance.
- [func CTFontGetOpticalBoundsForGlyphs(CTFont, UnsafePointer<CGGlyph>, UnsafeMutablePointer<CGRect>?, CFIndex, CFOptionFlags) -> CGRect](ctfontgetopticalboundsforglyphs(_:_:_:_:_:).md)
  Calculates the optical bounds for an array of glyphs and returns the overall optical bounds for the run.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/ctfontgetverticaltranslationsforglyphs(_:_:_:_:))*