# CTFontGetGlyphWithName(_:_:)

**Framework**: Core Text  
**Kind**: func  
**Role**: Function

Returns the glyph for the specified name.

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
func CTFontGetGlyphWithName(_ font: CTFont, _ glyphName: CFString) -> CGGlyph
```

```c
extern CGGlyph CTFontGetGlyphWithName(CTFontRef font, CFStringRef glyphName);
```

## Return Value

The glyph value for the named glyph as a [`CGGlyph`](../CoreGraphics/cgglyph.md) object, or if the glyph name is not recognized, the `.notdef` glyph index value.

## Discussion

The returned `CGGlyph` object can be used with any of the subsequent glyph data accessors or directly with Core Graphics.

## Parameters

- `font`: The font reference.
- `glyphName`: The glyph name as a `CFString` object.

## See Also

### Getting Glyph Data
- [func CTFontCreatePathForGlyph(CTFont, CGGlyph, UnsafePointer<CGAffineTransform>?) -> CGPath?](./ctfontcreatepathforglyph%28_,_,_%29.md)
  Creates a path for the specified glyph.
- [func CTFontGetBoundingRectsForGlyphs(CTFont, CTFontOrientation, UnsafePointer<CGGlyph>, UnsafeMutablePointer<CGRect>?, CFIndex) -> CGRect](./ctfontgetboundingrectsforglyphs%28_,_,_,_,_%29.md)
  Calculates the bounding rects for an array of glyphs and returns the overall bounding rectangle for the glyph run.
- [func CTFontGetAdvancesForGlyphs(CTFont, CTFontOrientation, UnsafePointer<CGGlyph>, UnsafeMutablePointer<CGSize>?, CFIndex) -> Double](./ctfontgetadvancesforglyphs%28_,_,_,_,_%29.md)
  Calculates the advances for an array of glyphs and returns the summed advance.
- [func CTFontGetOpticalBoundsForGlyphs(CTFont, UnsafePointer<CGGlyph>, UnsafeMutablePointer<CGRect>?, CFIndex, CFOptionFlags) -> CGRect](./ctfontgetopticalboundsforglyphs%28_,_,_,_,_%29.md)
  Calculates the optical bounds for an array of glyphs and returns the overall optical bounds for the run.
- [func CTFontGetVerticalTranslationsForGlyphs(CTFont, UnsafePointer<CGGlyph>, UnsafeMutablePointer<CGSize>, CFIndex)](./ctfontgetverticaltranslationsforglyphs%28_,_,_,_%29.md)
  Calculates the offset from the default (horizontal) origin to the vertical origin for an array of glyphs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/ctfontgetglyphwithname(_:_:))*