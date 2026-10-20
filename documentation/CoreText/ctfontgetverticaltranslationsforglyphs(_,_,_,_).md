# CTFontGetVerticalTranslationsForGlyphs(_:_:_:_:)

**Framework**: Core Text  
**Kind**: func  
**Role**: Function

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

```c
extern void CTFontGetVerticalTranslationsForGlyphs(CTFontRef font, const CGGlyph glyphs[], CGSize translations[], CFIndex count);
```

## Parameters

- `font`: The font reference.
- `glyphs`: An array of `count` number of glyphs.
- `translations`: On output, the computed origin offsets in an array of `count` number of [`CGSize`](../CoreFoundation/cgsize.md) objects.
- `count`: The capacity of the `glyphs` and `translations` buffers.

## See Also

### Getting Glyph Data
- [func CTFontCreatePathForGlyph(CTFont, CGGlyph, UnsafePointer<CGAffineTransform>?) -> CGPath?](./ctfontcreatepathforglyph%28_,_,_%29.md)
  Creates a path for the specified glyph.
- [func CTFontGetGlyphWithName(CTFont, CFString) -> CGGlyph](./ctfontgetglyphwithname%28_,_%29.md)
  Returns the glyph for the specified name.
- [func CTFontGetBoundingRectsForGlyphs(CTFont, CTFontOrientation, UnsafePointer<CGGlyph>, UnsafeMutablePointer<CGRect>?, CFIndex) -> CGRect](./ctfontgetboundingrectsforglyphs%28_,_,_,_,_%29.md)
  Calculates the bounding rects for an array of glyphs and returns the overall bounding rectangle for the glyph run.
- [func CTFontGetAdvancesForGlyphs(CTFont, CTFontOrientation, UnsafePointer<CGGlyph>, UnsafeMutablePointer<CGSize>?, CFIndex) -> Double](./ctfontgetadvancesforglyphs%28_,_,_,_,_%29.md)
  Calculates the advances for an array of glyphs and returns the summed advance.
- [func CTFontGetOpticalBoundsForGlyphs(CTFont, UnsafePointer<CGGlyph>, UnsafeMutablePointer<CGRect>?, CFIndex, CFOptionFlags) -> CGRect](./ctfontgetopticalboundsforglyphs%28_,_,_,_,_%29.md)
  Calculates the optical bounds for an array of glyphs and returns the overall optical bounds for the run.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/ctfontgetverticaltranslationsforglyphs(_:_:_:_:))*