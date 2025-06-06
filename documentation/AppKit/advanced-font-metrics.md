# Advanced Font Metrics

**Framework**: AppKit

Retrieve details about ascender and descender heights, glyph bounding rectangles, glyph advancements, and more.

## Topics

### Getting the Font Metrics
- [var ascender: CGFloat](nsfont/ascender.md)
  The top y-coordinate, offset from the baseline, of the font’s longest ascender.
- [var descender: CGFloat](nsfont/descender.md)
  The bottom y-coordinate, offset from the baseline, of the font’s longest descender.
- [var capHeight: CGFloat](nsfont/capheight.md)
  The cap height of the font.
- [var leading: CGFloat](nsfont/leading.md)
  The leading value of the font.
- [var xHeight: CGFloat](nsfont/xheight.md)
  The x-height of the font.
### Getting Underline and Italic Metrics
- [var italicAngle: CGFloat](nsfont/italicangle.md)
  The number of degrees that the font is slanted counterclockwise from the vertical.
- [var underlinePosition: CGFloat](nsfont/underlineposition.md)
  The baseline offset to use when drawing underlines with the font.
- [var underlineThickness: CGFloat](nsfont/underlinethickness.md)
  The thickness to use when drawing underlines with the font.
### Getting Bounding Rectangles
- [var boundingRectForFont: NSRect](nsfont/boundingrectforfont.md)
  The font’s bounding rectangle, scaled to the font’s size.
- [func boundingRect(forCGGlyph: CGGlyph) -> NSRect](nsfont/boundingrect(forcgglyph:).md)
  Returns the bounding rectangle for the specified glyph, scaled to the receiver’s size.
- [func getBoundingRects(NSRectArray, forCGGlyphs: UnsafePointer<CGGlyph>, count: Int)](nsfont/getboundingrects(_:forcgglyphs:count:).md)
  Returns an array of the bounding rectangles for the specified glyphs rendered by the receiver.
### Getting Glyph Advancements
- [var maximumAdvancement: NSSize](nsfont/maximumadvancement.md)
  The maximum advance of any of the font’s glyphs.
- [func advancement(forCGGlyph: CGGlyph) -> NSSize](nsfont/advancement(forcgglyph:).md)
  Returns the nominal spacing for the given glyph—the distance the current point moves after showing the glyph—accounting for the receiver’s size.
- [func getAdvancements(NSSizeArray, forCGGlyphs: UnsafePointer<CGGlyph>, count: Int)](nsfont/getadvancements(_:forcgglyphs:count:).md)
  Returns an array of the advancements for the specified glyphs rendered by the receiver.
### Getting the Font Matrices
- [var matrix: UnsafePointer<CGFloat>](nsfont/matrix.md)
  The transformation matrix associated with the font.
- [var textTransform: AffineTransform](nsfont/texttransform.md)
  The current transformation matrix of the font.
- [class var identityMatrix: UnsafePointer<CGFloat>](nsfont/identitymatrix.md)
  The identify matrix for the font.

## See Also

- [var pointSize: CGFloat](nsfont/pointsize.md)
  The point size of the font.
- [var coveredCharacterSet: CharacterSet](nsfont/coveredcharacterset.md)
  The character set containing all of the nominal characters that the font can render.
- [var fontDescriptor: NSFontDescriptor](nsfont/fontdescriptor.md)
  The font descriptor object for the font.
- [var isFixedPitch: Bool](nsfont/isfixedpitch.md)
  A Boolean value indicating whether all glyphs in the font have the same advancement.
- [var mostCompatibleStringEncoding: UInt](nsfont/mostcompatiblestringencoding.md)
  The string encoding that works best with the font.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/advanced-font-metrics)*