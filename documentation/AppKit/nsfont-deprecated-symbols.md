# Deprecated symbols

**Framework**: AppKit  
**Role**: API Collection

Review symbols that are no longer in active development, and their recommended replacements.

#### Overview

Although these symbols are available for use, Apple is no longer actively developing them, and may remove them in a future release. Apple recommends moving away from these symbols and using their indicated replacements instead. Check the individual symbol pages for the recommended replacements.

## Topics

### Deprecated methods
- [func getAdvancements(NSSizeArray, forGlyphs: UnsafePointer<NSGlyph>, count: Int)](./nsfont/getadvancements%28_,forglyphs,count%29.md)
  Returns an array of the advancements for the specified glyphs rendered by the receiver.
- [func getAdvancements(NSSizeArray, forPackedGlyphs: UnsafeRawPointer, length: Int)](./nsfont/getadvancements%28_,forpackedglyphs,length%29.md)
  Returns an array of the advancements for the specified packed glyphs and rendered by the receiver.
- [func advancement(forGlyph: NSGlyph) -> NSSize](./nsfont/advancement%28forglyph%29.md)
  Returns the nominal spacing for the given glyph—the distance the current point moves after showing the glyph—accounting for the receiver’s size.
- [func boundingRect(forGlyph: NSGlyph) -> NSRect](./nsfont/boundingrect%28forglyph%29.md)
  Returns the bounding rectangle for the specified glyph, scaled to the receiver’s size.
- [func getBoundingRects(NSRectArray, forGlyphs: UnsafePointer<NSGlyph>, count: Int)](./nsfont/getboundingrects%28_,forglyphs,count%29.md)
  Returns an array of the bounding rectangles for the specified glyphs rendered by the receiver.
- [func glyph(withName: String) -> NSGlyph](./nsfont/glyph%28withname%29.md)
  Returns the named encoded glyph, or –1 if the receiver contains no such glyph.
- [func screenFont(with: NSFontRenderingMode) -> NSFont](./nsfont/screenfont%28with%29.md)
  Returns a bitmapped screen font, when sent to a font object representing a scalable PostScript font, with the specified rendering mode, matching the receiver in typeface and matrix (or size), or `nil` if such a font can’t be found.
### Deprecated properties
- [var renderingMode: NSFontRenderingMode](./nsfont/renderingmode.md)
  The rendering mode of the font.
- [var printer: NSFont](./nsfont/printer.md)
  The scalable PostScript font corresponding to current font.
- [var screen: NSFont](./nsfont/screen.md)
  The bitmapped screen font for the current font.
### Deprecated types
- [enum NSMultibyteGlyphPacking](./nsmultibyteglyphpacking.md)
  A constant for glyph packing.
- [enum NSFontRenderingMode](./nsfontrenderingmode.md)
  The font rendering mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfont-deprecated-symbols)*