# CGFont

**Framework**: Core Graphics  
**Kind**: class

A set of character glyphs and layout information for drawing text.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
class CGFont
```

#### Overview

A glyph can represent a single character (such as ‘b’), more than one character (such as the “ﬁ” ligature), or a special character such as a space. Core Graphics retrieves the glyphs for the font from ATS (Apple Type Services) and paints the glyphs based on the relevant parameters of the current graphics state.

Core Graphics provides a limited, low-level interface for drawing text. For information on text-drawing functions, see [`CGContext`](cgcontext.md). For full Unicode and text-layout support,  use the services provided by TextKit).

## Topics

### Creating Font Objects
- [init?(CGDataProvider)](cgfont/init(_:)-9aour.md)
  Creates a font object from data supplied from a data provider.
- [init?(CFString)](cgfont/init(_:)-1p4b.md)
  Creates a font object corresponding to the font specified by a PostScript or full name.
### Examining Font Metadata
- [var fullName: CFString?](cgfont/fullname.md)
  Returns the full name associated with a font object.
### Examining Font Metrics
- [var ascent: Int32](cgfont/ascent.md)
  Returns the ascent of a font.
- [var capHeight: Int32](cgfont/capheight.md)
  Returns the cap height of a font.
- [var descent: Int32](cgfont/descent.md)
  Returns the descent of a font.
- [var fontBBox: CGRect](cgfont/fontbbox.md)
  Returns the bounding box of a font.
- [var italicAngle: CGFloat](cgfont/italicangle.md)
  Returns the italic angle of a font.
- [var leading: Int32](cgfont/leading.md)
  Returns the leading of a font.
- [var stemV: CGFloat](cgfont/stemv.md)
  Returns the thickness of the dominant vertical stems of glyphs in a font.
- [var unitsPerEm: Int32](cgfont/unitsperem.md)
  Returns the number of glyph space units per em for the provided font.
- [var xHeight: Int32](cgfont/xheight.md)
  Returns the x-height of a font.
### Working with PostScript Fonts
- [var postScriptName: CFString?](cgfont/postscriptname.md)
  Obtains the PostScript name of a font.
- [func canCreatePostScriptSubset(CGFontPostScriptFormat) -> Bool](cgfont/cancreatepostscriptsubset(_:).md)
  Determines whether Core Graphics can create a subset of the font in PostScript format.
- [func createPostScriptSubset(subsetName: CFString, format: CGFontPostScriptFormat, glyphs: UnsafePointer<CGGlyph>?, count: Int, encoding: UnsafePointer<CGGlyph>?) -> CFData?](cgfont/createpostscriptsubset(subsetname:format:glyphs:count:encoding:).md)
  Creates a subset of the font in the specified PostScript format.
- [enum CGFontPostScriptFormat](cgfontpostscriptformat.md)
  Possible formats for a PostScript font subset.
- [func createPostScriptEncoding(encoding: UnsafePointer<CGGlyph>?) -> CFData?](cgfont/createpostscriptencoding(encoding:).md)
  Creates a PostScript encoding of a font.
### Working with Font Tables
- [var tableTags: CFArray?](cgfont/tabletags.md)
  Returns an array of tags that correspond to the font tables for a font.
- [func table(for: UInt32) -> CFData?](cgfont/table(for:).md)
  Returns the font table that corresponds to the provided tag.
- [Font Table Index Values](font-table-index-values.md)
  Possible values for an index into a font table.
- [Obsolete Font Table Index Values](obsolete-font-table-index-values.md)
  Deprecated values for an index into a font table.
### Working with Variations
- [func copy(withVariations: CFDictionary?) -> CGFont?](cgfont/copy(withvariations:).md)
  Creates a copy of a font using a variation specification dictionary.
- [var variations: CFDictionary?](cgfont/variations.md)
  Returns the variation specification dictionary for a font.
- [var variationAxes: CFArray?](cgfont/variationaxes.md)
  Returns an array of the variation axis dictionaries for a font.
- [Font Variation Axis Keys](font-variation-axis-keys.md)
  Keys used for a font variation axis dictionary.
### Working with Glyphs
- [var numberOfGlyphs: Int](cgfont/numberofglyphs.md)
  Returns the number of glyphs in a font.
- [func name(for: CGGlyph) -> CFString?](cgfont/name(for:).md)
  Returns the glyph name of the specified glyph in the specified font.
- [func getGlyphWithGlyphName(name: CFString) -> CGGlyph](cgfont/getglyphwithglyphname(name:).md)
  Returns the glyph for the glyph name associated with the specified font object.
- [func getGlyphBBoxes(glyphs: UnsafePointer<CGGlyph>, count: Int, bboxes: UnsafeMutablePointer<CGRect>) -> Bool](cgfont/getglyphbboxes(glyphs:count:bboxes:).md)
  Get the bounding box of each glyph in an array.
- [func getGlyphAdvances(glyphs: UnsafePointer<CGGlyph>, count: Int, advances: UnsafeMutablePointer<Int32>) -> Bool](cgfont/getglyphadvances(glyphs:count:advances:).md)
  Gets the advance width of each glyph in the provided array.
- [typealias CGGlyph](cgglyph.md)
  An index into the internal glyph table of a font.
- [let kCGGlyphMax: CGFontIndex](kcgglyphmax.md)
  The maximum allowed value of a [`CGGlyph`](cgglyph.md).
- [typealias CGFontIndex](cgfontindex.md)
  An index into a font table.
- [let kCGFontIndexMax: CGFontIndex](kcgfontindexmax.md)
  The maximum allowed value of a [`CGFontIndex`](cgfontindex.md).
- [let kCGFontIndexInvalid: CGFontIndex](kcgfontindexinvalid.md)
  An invalid font index (a value which never represents a valid glyph).
### Working with Core Foundation Types
- [class var typeID: CFTypeID](cgfont/typeid.md)
  Returns the Core Foundation type identifier for Core Graphics fonts.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)

## See Also

- [Quartz 2D Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/drawingwithquartz2d/Introduction/Introduction.html#//apple_ref/doc/uid/TP30001066)
- [class CGColor](cgcolor.md)
  A set of components that define a color, with a color space specifying how to interpret them.
- [class CGColorConversionInfo](cgcolorconversioninfo.md)
  An object that describes how to convert between color spaces for use by other system services.
- [class CGColorSpace](cgcolorspace.md)
  A profile that specifies how to interpret a color value for display.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgfont)*