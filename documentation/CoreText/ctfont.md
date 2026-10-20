# CTFont

**Framework**: Core Text  
**Kind**: class  
**Role**: Class

A font object.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
class CTFont
```

```c
typedef const struct __CTFont * CTFontRef;
```

#### Overview

The `CTFont` opaque type represents a Core Text font object.

Font objects represent fonts to an application, providing access to characteristics of the font, such as point size, transform matrix, and other attributes. Fonts provide assistance in laying out glyphs relative to one another and are used to establish the current font when drawing in a graphics context.

## Topics

### Creating Fonts
- [func CTFontCreateWithName(CFString, CGFloat, UnsafePointer<CGAffineTransform>?) -> CTFont](./ctfontcreatewithname%28_,_,_%29.md)
  Returns a new font reference for the given name.
- [func CTFontCreateWithNameAndOptions(CFString, CGFloat, UnsafePointer<CGAffineTransform>?, CTFontOptions) -> CTFont](./ctfontcreatewithnameandoptions%28_,_,_,_%29.md)
  Returns a new font reference for the given name.
- [func CTFontCreateWithFontDescriptor(CTFontDescriptor, CGFloat, UnsafePointer<CGAffineTransform>?) -> CTFont](./ctfontcreatewithfontdescriptor%28_,_,_%29.md)
  Returns a new font reference that best matches the given font descriptor.
- [func CTFontCreateWithFontDescriptorAndOptions(CTFontDescriptor, CGFloat, UnsafePointer<CGAffineTransform>?, CTFontOptions) -> CTFont](./ctfontcreatewithfontdescriptorandoptions%28_,_,_,_%29.md)
  Returns a new font reference that best matches the given font descriptor.
- [func CTFontCreateUIFontForLanguage(CTFontUIFontType, CGFloat, CFString?) -> CTFont?](./ctfontcreateuifontforlanguage%28_,_,_%29.md)
  Returns the special user-interface font for the given language and user-interface type.
- [func CTFontCreateCopyWithAttributes(CTFont, CGFloat, UnsafePointer<CGAffineTransform>?, CTFontDescriptor?) -> CTFont](./ctfontcreatecopywithattributes%28_,_,_,_%29.md)
  Returns a new font with additional attributes based on the original font.
- [func CTFontCreateCopyWithSymbolicTraits(CTFont, CGFloat, UnsafePointer<CGAffineTransform>?, CTFontSymbolicTraits, CTFontSymbolicTraits) -> CTFont?](./ctfontcreatecopywithsymbolictraits%28_,_,_,_,_%29.md)
  Returns a new font in the same font family as the original with the specified symbolic traits.
- [func CTFontCreateCopyWithFamily(CTFont, CGFloat, UnsafePointer<CGAffineTransform>?, CFString) -> CTFont?](./ctfontcreatecopywithfamily%28_,_,_,_%29.md)
  Returns a new font in the specified family based on the traits of the original font.
- [func CTFontCreateForString(CTFont, CFString, CFRange) -> CTFont](./ctfontcreateforstring%28_,_,_%29.md)
  Returns a font reference that most accurately maps the string range based on the current font.
- [func CTFontCreateForStringWithLanguage(CTFont, CFString, CFRange, CFString?) -> CTFont](./ctfontcreateforstringwithlanguage%28_,_,_,_%29.md)
  Returns a font reference that most accurately maps the string range based on the current font and language.
### Getting Font Data
- [func CTFontCopyFontDescriptor(CTFont) -> CTFontDescriptor](./ctfontcopyfontdescriptor%28_%29.md)
  Returns the normalized font descriptor for the given font reference.
- [func CTFontCopyAttribute(CTFont, CFString) -> CFTypeRef?](./ctfontcopyattribute%28_,_%29.md)
  Returns the value associated with an arbitrary attribute of the given font.
- [func CTFontGetSize(CTFont) -> CGFloat](./ctfontgetsize%28_%29.md)
  Returns the point size of the given font.
- [func CTFontGetMatrix(CTFont) -> CGAffineTransform](./ctfontgetmatrix%28_%29.md)
  Returns the transformation matrix of the given font.
- [func CTFontGetSymbolicTraits(CTFont) -> CTFontSymbolicTraits](./ctfontgetsymbolictraits%28_%29.md)
  Returns the symbolic traits of the given font.
- [func CTFontCopyTraits(CTFont) -> CFDictionary](./ctfontcopytraits%28_%29.md)
  Returns the traits dictionary of the given font.
- [func CTFontCopyDefaultCascadeListForLanguages(CTFont, CFArray?) -> CFArray?](./ctfontcopydefaultcascadelistforlanguages%28_,_%29.md)
  Retrieves an ordered list of font substitution preferences.
### Getting Font Names
- [func CTFontCopyPostScriptName(CTFont) -> CFString](./ctfontcopypostscriptname%28_%29.md)
  Returns the PostScript name of the given font.
- [func CTFontCopyFamilyName(CTFont) -> CFString](./ctfontcopyfamilyname%28_%29.md)
  Returns the family name of the given font.
- [func CTFontCopyFullName(CTFont) -> CFString](./ctfontcopyfullname%28_%29.md)
  Returns the full name of the given font.
- [func CTFontCopyDisplayName(CTFont) -> CFString](./ctfontcopydisplayname%28_%29.md)
  Returns the display name of the given font.
- [func CTFontCopyName(CTFont, CFString) -> CFString?](./ctfontcopyname%28_,_%29.md)
  Returns a reference to the requested name of the given font.
- [func CTFontCopyLocalizedName(CTFont, CFString, UnsafeMutablePointer<Unmanaged<CFString>?>?) -> CFString?](./ctfontcopylocalizedname%28_,_,_%29.md)
  Returns a reference to a localized name for the given font.
### Working With Encoding
- [func CTFontCopyCharacterSet(CTFont) -> CFCharacterSet](./ctfontcopycharacterset%28_%29.md)
  Returns the Unicode character set of the font.
- [func CTFontGetStringEncoding(CTFont) -> CFStringEncoding](./ctfontgetstringencoding%28_%29.md)
  Returns the best string encoding for legacy format support.
- [func CTFontCopySupportedLanguages(CTFont) -> CFArray](./ctfontcopysupportedlanguages%28_%29.md)
  Returns an array of languages supported by the font.
### Getting Font Metrics
- [func CTFontGetAscent(CTFont) -> CGFloat](./ctfontgetascent%28_%29.md)
  Returns the scaled font-ascent metric of the given font.
- [func CTFontGetDescent(CTFont) -> CGFloat](./ctfontgetdescent%28_%29.md)
  Returns the scaled font-descent metric of the given font.
- [func CTFontGetLeading(CTFont) -> CGFloat](./ctfontgetleading%28_%29.md)
  Returns the scaled font-leading metric of the given font.
- [func CTFontGetUnitsPerEm(CTFont) -> UInt32](./ctfontgetunitsperem%28_%29.md)
  Returns the units-per-em metric of the given font.
- [func CTFontGetGlyphCount(CTFont) -> CFIndex](./ctfontgetglyphcount%28_%29.md)
  Returns the number of glyphs of the given font.
- [func CTFontGetBoundingBox(CTFont) -> CGRect](./ctfontgetboundingbox%28_%29.md)
  Returns the scaled bounding box of the given font.
- [func CTFontGetUnderlinePosition(CTFont) -> CGFloat](./ctfontgetunderlineposition%28_%29.md)
  Returns the scaled underline position of the given font.
- [func CTFontGetUnderlineThickness(CTFont) -> CGFloat](./ctfontgetunderlinethickness%28_%29.md)
  Returns the scaled underline-thickness metric of the given font.
- [func CTFontGetSlantAngle(CTFont) -> CGFloat](./ctfontgetslantangle%28_%29.md)
  Returns the slant angle of the given font.
- [func CTFontGetCapHeight(CTFont) -> CGFloat](./ctfontgetcapheight%28_%29.md)
  Returns the cap-height metric of the given font.
- [func CTFontGetXHeight(CTFont) -> CGFloat](./ctfontgetxheight%28_%29.md)
  Returns the x-height metric of the given font.
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
- [func CTFontGetVerticalTranslationsForGlyphs(CTFont, UnsafePointer<CGGlyph>, UnsafeMutablePointer<CGSize>, CFIndex)](./ctfontgetverticaltranslationsforglyphs%28_,_,_,_%29.md)
  Calculates the offset from the default (horizontal) origin to the vertical origin for an array of glyphs.
### Working With Font Variations
- [func CTFontCopyVariationAxes(CTFont) -> CFArray?](./ctfontcopyvariationaxes%28_%29.md)
  Returns an array of variation axes.
- [func CTFontCopyVariation(CTFont) -> CFDictionary?](./ctfontcopyvariation%28_%29.md)
  Returns a variation dictionary from the font reference.
### Getting Font Features
- [func CTFontCopyFeatures(CTFont) -> CFArray?](./ctfontcopyfeatures%28_%29.md)
  Returns an array of font features.
- [func CTFontCopyFeatureSettings(CTFont) -> CFArray?](./ctfontcopyfeaturesettings%28_%29.md)
  Returns an array of font feature-setting tuples.
### Working with Glyphs
- [func CTFontGetGlyphsForCharacters(CTFont, UnsafePointer<UniChar>, UnsafeMutablePointer<CGGlyph>, CFIndex) -> Bool](./ctfontgetglyphsforcharacters%28_,_,_,_%29.md)
  Performs basic character-to-glyph mapping.
- [func CTFontDrawGlyphs(CTFont, UnsafePointer<CGGlyph>, UnsafePointer<CGPoint>, Int, CGContext)](./ctfontdrawglyphs%28_,_,_,_,_%29.md)
  Renders the given glyphs of a font at the specified positions in the supplied graphics context.
- [func CTFontGetLigatureCaretPositions(CTFont, CGGlyph, UnsafeMutablePointer<CGFloat>?, CFIndex) -> CFIndex](./ctfontgetligaturecaretpositions%28_,_,_,_%29.md)
  Returns caret positions within a glyph.
### Converting Fonts
- [func CTFontCopyGraphicsFont(CTFont, UnsafeMutablePointer<Unmanaged<CTFontDescriptor>?>?) -> CGFont](./ctfontcopygraphicsfont%28_,_%29.md)
  Returns a Core Graphics font reference and attributes.
- [func CTFontCreateWithGraphicsFont(CGFont, CGFloat, UnsafePointer<CGAffineTransform>?, CTFontDescriptor?) -> CTFont](./ctfontcreatewithgraphicsfont%28_,_,_,_%29.md)
  Creates a new font reference from an existing Core Graphics font reference.
- [func CTFontGetPlatformFont(CTFont, UnsafeMutablePointer<Unmanaged<CTFontDescriptor>?>?) -> ATSFontRef](./ctfontgetplatformfont%28_,_%29.md)
  Returns an ATS font reference and attributes.
- [func CTFontCreateWithPlatformFont(ATSFontRef, CGFloat, UnsafePointer<CGAffineTransform>?, CTFontDescriptor?) -> CTFont?](./ctfontcreatewithplatformfont%28_,_,_,_%29.md)
  Creates a new font reference from an ATS font reference.
- [func CTFontCreateWithQuickdrawInstance(ConstStr255Param?, Int16, UInt8, CGFloat) -> CTFont](./ctfontcreatewithquickdrawinstance%28_,_,_,_%29.md)
  Returns a font reference for the given QuickDraw instance.
### Getting Font Table Data
- [func CTFontCopyAvailableTables(CTFont, CTFontTableOptions) -> CFArray?](./ctfontcopyavailabletables%28_,_%29.md)
  Returns an array of font table tags.
- [func CTFontCopyTable(CTFont, CTFontTableTag, CTFontTableOptions) -> CFData?](./ctfontcopytable%28_,_,_%29.md)
  Returns a reference to the font table data.
### Getting the Type Identifier
- [func CTFontGetTypeID() -> CFTypeID](./ctfontgettypeid%28%29.md)
  Returns the type identifier for Core Text font references.
### Global Variables
- [Name Specifier Constants](./name-specifier-constants.md)
  Name specifier constants provide access to the different names associated with a font.
- [Font Variation Axis Dictionary Keys](./font-variation-axis-dictionary-keys.md)
  These constants provide keys to font variation axis dictionary values.
- [Font Feature Constants](./font-feature-constants.md)
  These constants provide keys to font feature dictionary values.
### Enumerations
- [enum CTFontUIFontType](./ctfontuifonttype.md)
  Constants that represent the specific user-interface purpose to specify for font creation.
- [typealias CTFontTableTag](./ctfonttabletag.md)
  Font table tags provide access to font table data.
- [struct CTFontTableOptions](./ctfonttableoptions.md)
  Constants that describe font table options.
- [struct CTFontOptions](./ctfontoptions.md)
  Options for font creation and descriptor matching.
### Initializers
- [init(CTFontUIFontType, size: CGFloat)](./ctfont/init%28_,size%29-3do9m.md)
- [init(CTFontDescriptor, size: CGFloat)](./ctfont/init%28_,size%29-6lcja.md)
- [init(CFString, size: CGFloat)](./ctfont/init%28_,size%29-8bj7b.md)
- [init(CTFontUIFontType, size: CGFloat, language: CFString?)](./ctfont/init%28_,size,language%29.md)
- [init(CFString, transform: CGAffineTransform)](./ctfont/init%28_,transform%29-3sscp.md)
- [init(CTFontDescriptor, transform: CGAffineTransform)](./ctfont/init%28_,transform%29-a23v.md)
- [init(font: CTFont, string: CFString, range: CFRange)](./ctfont/init%28font,string,range%29.md)
- [init(font: CTFont, string: CFString, range: CFRange, language: CFString?)](./ctfont/init%28font,string,range,language%29.md)

## Relationships

### Conforms To
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)

## See Also

### Opaque Types
- [class CTFontCollection](./ctfontcollection.md)
  A font collection.
- [class CTFontDescriptor](./ctfontdescriptor.md)
  A font descriptor.
- [class CTFrame](./ctframe.md)
  A frame.
- [class CTFramesetter](./ctframesetter.md)
  Generate text frames.
- [class CTGlyphInfo](./ctglyphinfo.md)
  Override a font’s specified mapping from Unicode to the glyph ID.
- [class CTLine](./ctline.md)
  A line of text.
- [class CTParagraphStyle](./ctparagraphstyle.md)
  Paragraph or ruler attributes in an attributed string.
- [class CTRun](./ctrun.md)
  A glyph run.
- [class CTRunDelegate](./ctrundelegate.md)
  A run delegate.
- [class CTTextTab](./cttexttab.md)
  A tab in a paragraph style, storing an alignment type and location.
- [class CTTypesetter](./cttypesetter.md)
  A typesetter which performs line layout.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/ctfont)*