# CTFontGetAdvancesForGlyphs(_:_:_:_:_:)

**Framework**: Core Text  
**Kind**: func  
**Role**: Function

Calculates the advances for an array of glyphs and returns the summed advance.

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
func CTFontGetAdvancesForGlyphs(_ font: CTFont, _ orientation: CTFontOrientation, _ glyphs: UnsafePointer<CGGlyph>, _ advances: UnsafeMutablePointer<CGSize>?, _ count: CFIndex) -> Double
```

```c
extern double CTFontGetAdvancesForGlyphs(CTFontRef font, CTFontOrientation orientation, const CGGlyph glyphs[], CGSize advances[], CFIndex count);
```

#### Return Value

The summed glyph advance of an array of glyphs.

#### Discussion

Individual glyph advances are passed back via the `advances` parameter. These are the ideal metrics for each glyph scaled and transformed in font space.

## Parameters

- `font`: The font reference.
- `orientation`: The intended drawing orientation of the glyphs. Used to determined which glyph metrics to return.
- `glyphs`: An array of `count` number of glyphs.
- `advances`: An array of `count` number of [`CGSize`](../CoreFoundation/cgsize.md) objects to receive the computed glyph advances. If `NULL`, only the overall advance is calculated.
- `count`: The capacity of the `glyphs` and `advances` buffers.

## See Also

### Getting Glyph Data
- [func CTFontCreatePathForGlyph(CTFont, CGGlyph, UnsafePointer<CGAffineTransform>?) -> CGPath?](./ctfontcreatepathforglyph%28_,_,_%29.md)
  Creates a path for the specified glyph.
- [func CTFontGetGlyphWithName(CTFont, CFString) -> CGGlyph](./ctfontgetglyphwithname%28_,_%29.md)
  Returns the glyph for the specified name.
- [func CTFontGetBoundingRectsForGlyphs(CTFont, CTFontOrientation, UnsafePointer<CGGlyph>, UnsafeMutablePointer<CGRect>?, CFIndex) -> CGRect](./ctfontgetboundingrectsforglyphs%28_,_,_,_,_%29.md)
  Calculates the bounding rects for an array of glyphs and returns the overall bounding rectangle for the glyph run.
- [func CTFontGetOpticalBoundsForGlyphs(CTFont, UnsafePointer<CGGlyph>, UnsafeMutablePointer<CGRect>?, CFIndex, CFOptionFlags) -> CGRect](./ctfontgetopticalboundsforglyphs%28_,_,_,_,_%29.md)
  Calculates the optical bounds for an array of glyphs and returns the overall optical bounds for the run.
- [func CTFontGetVerticalTranslationsForGlyphs(CTFont, UnsafePointer<CGGlyph>, UnsafeMutablePointer<CGSize>, CFIndex)](./ctfontgetverticaltranslationsforglyphs%28_,_,_,_%29.md)
  Calculates the offset from the default (horizontal) origin to the vertical origin for an array of glyphs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/ctfontgetadvancesforglyphs(_:_:_:_:_:))*