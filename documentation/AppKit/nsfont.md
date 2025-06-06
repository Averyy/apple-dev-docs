# NSFont

**Framework**: AppKit  
**Kind**: class

The representation of a font in an app.

**Availability**:
- macOS ?+

## Declaration

```swift
class NSFont
```

#### Overview

[`NSFont`](nsfont.md) objects represent fonts to an app, providing access to characteristics of the font and assistance in laying out glyphs relative to one another. Font objects are also used to establish the current font for drawing text directly into a graphics context, using the [`set()`](nsfont/set().md) method.

You don’t create [`NSFont`](nsfont.md) objects using the `alloc` and `init` methods. Instead, you use either [`init(descriptor:size:)`](nsfont/init(descriptor:size:).md) or [`init(name:size:)`](nsfont/init(name:size:).md) to look up an available font and alter its size or matrix to your needs. These methods check for an existing font object with the specified characteristics, returning it if there is one. Otherwise, they look up the font data requested and create the appropriate object. [`NSFont`](nsfont.md) also defines a number of methods for getting standard system fonts, such as [`systemFont(ofSize:)`](nsfont/systemfont(ofsize:).md), [`userFont(ofSize:)`](nsfont/userfont(ofsize:).md), and [`messageFont(ofSize:)`](nsfont/messagefont(ofsize:).md). To request the default size for these standard fonts, pass a negative number or `0` as the font size. See [`macOS Human Interface Guidelines`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/OSXHIGuidelines/index.html#//apple_ref/doc/uid/20000957) for more information about system fonts.

## Topics

### Creating Arbitrary Fonts
- [init?(name: String, size: CGFloat)](nsfont/init(name:size:).md)
  Creates a font object for the specified font name and font size.
- [init?(descriptor: NSFontDescriptor, size: CGFloat)](nsfont/init(descriptor:size:).md)
  Returns a font object for the specified font descriptor and font size.
- [init?(descriptor: NSFontDescriptor, textTransform: AffineTransform?)](nsfont/init(descriptor:texttransform:).md)
  Returns a font object for the specified font descriptor and text transform.
- [init?(name: String, matrix: UnsafePointer<CGFloat>)](nsfont/init(name:matrix:).md)
  Returns a font object for the specified font name and matrix.
### Creating User Fonts
- [class func userFont(ofSize: CGFloat) -> NSFont?](nsfont/userfont(ofsize:).md)
  Returns the font used by default for documents and other text under the user’s control (that is, text whose font the user can normally change), in the specified size.
- [class func userFixedPitchFont(ofSize: CGFloat) -> NSFont?](nsfont/userfixedpitchfont(ofsize:).md)
  Returns the font used by default for documents and other text under the user’s control (that is, text whose font the user can normally change), when that font should be fixed-pitch, in the specified size.
### Creating System Fonts
- [class func preferredFont(forTextStyle: NSFont.TextStyle, options: [NSFont.TextStyleOptionKey : Any]) -> NSFont](nsfont/preferredfont(fortextstyle:options:).md)
  Returns the font associated with the text style.
- [class func systemFont(ofSize: CGFloat) -> NSFont](nsfont/systemfont(ofsize:).md)
  Returns the standard system font with the specified size.
- [class func systemFont(ofSize: CGFloat, weight: NSFont.Weight) -> NSFont](nsfont/systemfont(ofsize:weight:).md)
  Returns the standard system font with the specified size and weight.
- [class func boldSystemFont(ofSize: CGFloat) -> NSFont](nsfont/boldsystemfont(ofsize:).md)
  Returns the standard system font in boldface type with the specified size.
- [class func monospacedSystemFont(ofSize: CGFloat, weight: NSFont.Weight) -> NSFont](nsfont/monospacedsystemfont(ofsize:weight:).md)
  Returns a monospace version of the system font with the specified size and weight.
- [class func monospacedDigitSystemFont(ofSize: CGFloat, weight: NSFont.Weight) -> NSFont](nsfont/monospaceddigitsystemfont(ofsize:weight:).md)
  Returns a version of the standard system font that contains monospaced digit glyphs.
- [class var systemFontSize: CGFloat](nsfont/systemfontsize.md)
  Returns the size of the standard system font.
- [class var smallSystemFontSize: CGFloat](nsfont/smallsystemfontsize.md)
  Returns the size of the standard small system font.
- [NSFont.Weight](nsfont/weight.md)
  System-defined font-weight values.
- [NSFont.TextStyle](nsfont/textstyle.md)
  Constants that specify the preferred text styles you use with fonts.
- [NSFont.TextStyleOptionKey](nsfont/textstyleoptionkey.md)
  The options that you apply when requesting the font or font descriptor of a preferred text style.
### Creating UI Element Fonts
- [class func labelFont(ofSize: CGFloat) -> NSFont](nsfont/labelfont(ofsize:).md)
  Returns the font used for standard interface labels in the specified size.
- [class func messageFont(ofSize: CGFloat) -> NSFont](nsfont/messagefont(ofsize:).md)
  Returns the font used for standard interface items, such as button labels, menu items, and so on, in the specified size.
- [class func menuBarFont(ofSize: CGFloat) -> NSFont](nsfont/menubarfont(ofsize:).md)
  Returns the font used for menu bar items, in the specified size.
- [class func menuFont(ofSize: CGFloat) -> NSFont](nsfont/menufont(ofsize:).md)
  Returns the font used for menu items, in the specified size.
- [class func controlContentFont(ofSize: CGFloat) -> NSFont](nsfont/controlcontentfont(ofsize:).md)
  Returns the font used for the content of controls in the specified size.
- [class func titleBarFont(ofSize: CGFloat) -> NSFont](nsfont/titlebarfont(ofsize:).md)
  Returns the font used for window title bars, in the specified size.
- [class func paletteFont(ofSize: CGFloat) -> NSFont](nsfont/palettefont(ofsize:).md)
  Returns the font used for palette window title bars, in the specified size.
- [class func toolTipsFont(ofSize: CGFloat) -> NSFont](nsfont/tooltipsfont(ofsize:).md)
  Returns the font used for tool tips labels, in the specified size.
- [class var labelFontSize: CGFloat](nsfont/labelfontsize.md)
  Returns the size of the standard label font.
- [class func systemFontSize(for: NSControl.ControlSize) -> CGFloat](nsfont/systemfontsize(for:).md)
  Returns the font size used for the specified control size.
### Using a Font to Draw
- [func set()](nsfont/set.md)
  Sets this font as the font for the current graphics context.
- [func set(in: NSGraphicsContext)](nsfont/set(in:).md)
  Sets this font as the font for the specified graphics context.
### Getting Font Metrics and Information
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
- [Advanced Font Metrics](advanced-font-metrics.md)
  Retrieve details about ascender and descender heights, glyph bounding rectangles, glyph advancements, and more.
### Getting Information About Glyphs
- [var numberOfGlyphs: Int](nsfont/numberofglyphs.md)
  The number of glyphs in the font.
- [typealias NSGlyph](nsglyph.md)
  The type used to specify glyphs.
- [var NSControlGlyph: Int](nscontrolglyph.md)
  The reserved code for a control glyph.
- [var NSNullGlyph: Int](nsnullglyph.md)
  The reserved code for a null glyph.
### Getting Font Names
- [var displayName: String?](nsfont/displayname.md)
  The name of the font, including family and face names, to use when displaying the font information to the user.
- [var familyName: String?](nsfont/familyname.md)
  The family name of the font—for example, “Times” or “Helvetica.”
- [var fontName: String](nsfont/fontname.md)
  The full name of the font, as used in PostScript language code—for example, “Times-Roman” or “Helvetica-Oblique.”
### Setting User Fonts
- [class func setUser(NSFont?)](nsfont/setuser(_:).md)
  Sets the font used by default for documents and other text under the user’s control to the specified font.
- [class func setUserFixedPitch(NSFont?)](nsfont/setuserfixedpitch(_:).md)
  Sets the font used by default for documents and other text under the user’s control, when that font should be fixed-pitch, to the specified font.
### Vertical Fonts
- [var isVertical: Bool](nsfont/isvertical.md)
  A Boolean value indicating whether the font is a vertical font.
- [var vertical: NSFont](nsfont/vertical-6ym79.md)
  A vertical version of the font.
### Responding to Font-Related Notifications
- [class let antialiasThresholdChangedNotification: NSNotification.Name](nsfont/antialiasthresholdchangednotification.md)
  Posted after the threshold for antialiasing changes.
- [class let fontSetChangedNotification: NSNotification.Name](nsfont/fontsetchangednotification.md)
  Posted after the currently-set font changes.
### Deprecated
- [Deprecated Symbols](nsfont-deprecated-symbols.md)
  Review unsupported symbols and their replacements.
### Type Aliases
- [NSFont.Width](nsfont/width.md)
### Instance Properties
- [var printer: NSFont](nsfont/printer.md)
  The scalable PostScript font corresponding to current font.
- [var renderingMode: NSFontRenderingMode](nsfont/renderingmode.md)
  The rendering mode of the font.
- [var screen: NSFont](nsfont/screen.md)
  The bitmapped screen font for the current font.
### Instance Methods
- [func advancement(forGlyph: NSGlyph) -> NSSize](nsfont/advancement(forglyph:).md)
  Returns the nominal spacing for the given glyph—the distance the current point moves after showing the glyph—accounting for the receiver’s size.
- [func boundingRect(forGlyph: NSGlyph) -> NSRect](nsfont/boundingrect(forglyph:).md)
  Returns the bounding rectangle for the specified glyph, scaled to the receiver’s size.
- [func getAdvancements(NSSizeArray, forGlyphs: UnsafePointer<NSGlyph>, count: Int)](nsfont/getadvancements(_:forglyphs:count:).md)
  Returns an array of the advancements for the specified glyphs rendered by the receiver.
- [func getAdvancements(NSSizeArray, forPackedGlyphs: UnsafeRawPointer, length: Int)](nsfont/getadvancements(_:forpackedglyphs:length:).md)
  Returns an array of the advancements for the specified packed glyphs and rendered by the receiver.
- [func getBoundingRects(NSRectArray, forGlyphs: UnsafePointer<NSGlyph>, count: Int)](nsfont/getboundingrects(_:forglyphs:count:).md)
  Returns an array of the bounding rectangles for the specified glyphs rendered by the receiver.
- [func glyph(withName: String) -> NSGlyph](nsfont/glyph(withname:).md)
  Returns the named encoded glyph, or –1 if the receiver contains no such glyph.
- [func screenFont(with: NSFontRenderingMode) -> NSFont](nsfont/screenfont(with:).md)
  Returns a bitmapped screen font, when sent to a font object representing a scalable PostScript font, with the specified rendering mode, matching the receiver in typeface and matrix (or size), or `nil` if such a font can’t be found.
- [func withSize(CGFloat) -> NSFont](nsfont/withsize(_:).md)
### Type Methods
- [class func systemFont(ofSize: CGFloat, weight: NSFont.Weight, width: NSFont.Width) -> NSFont](nsfont/systemfont(ofsize:weight:width:).md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

## See Also

- [class NSFontDescriptor](nsfontdescriptor.md)
  A dictionary of attributes that describe a font.
- [struct NSFontTraitMask](nsfonttraitmask.md)
  Constants for isolating specific traits of a font.
- [typealias NSFontFamilyClass](nsfontfamilyclass.md)
  Constants that classify certain stylistic qualities of the font.
- [NSFontDescriptor.SymbolicTraits](nsfontdescriptor/symbolictraits-swift.struct.md)
  A symbolic description of the stylistic aspects of a font.
- [class NSFontAssetRequest](nsfontassetrequest.md)
- [typealias NSFontSymbolicTraits](nsfontsymbolictraits.md)
  A symbolic description of stylistic aspects of a font.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfont)*