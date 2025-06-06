# Typeface Information

**Framework**: AppKit

Constants for type faces such as italic or bold.

#### Overview

Typeface information is specified by the lower 16 bits of `NSFontSymbolicTraits` using the following constants.

## Topics

### Constants
- [var NSFontItalicTrait: Int](nsfontitalictrait.md)
  The font’s typestyle is italic.
- [var NSFontBoldTrait: Int](nsfontboldtrait.md)
  The font’s typestyle is boldface.
- [var NSFontExpandedTrait: Int](nsfontexpandedtrait.md)
  The font’s typestyle is expanded. Expanded and condensed traits are mutually exclusive.
- [var NSFontCondensedTrait: Int](nsfontcondensedtrait.md)
  The font’s typestyle is condensed. Expanded and condensed traits are mutually exclusive.
- [var NSFontMonoSpaceTrait: Int](nsfontmonospacetrait.md)
  The font uses fixed-pitch glyphs if available. The font may have multiple glyph advances (many CJK glyphs contain two spaces).
- [var NSFontVerticalTrait: Int](nsfontverticaltrait.md)
  The font uses vertical glyph variants and metrics.
- [var NSFontUIOptimizedTrait: Int](nsfontuioptimizedtrait.md)
  The font synthesizes appropriate attributes for user interface rendering, such as control titles, if necessary.

## See Also

- [var fontAttributes: [NSFontDescriptor.AttributeName : Any]](nsfontdescriptor/fontattributes.md)
  The receiver’s dictionary of attributes.
- [func object(forKey: NSFontDescriptor.AttributeName) -> Any?](nsfontdescriptor/object(forkey:).md)
  Returns the font attribute specified by the given key.
- [NSFontDescriptor.AttributeName](nsfontdescriptor/attributename.md)
  Constants for the names of font attributes.
- [NSFontDescriptor.SymbolicTraits](nsfontdescriptor/symbolictraits-swift.struct.md)
  A symbolic description of the stylistic aspects of a font.
- [var matrix: AffineTransform?](nsfontdescriptor/matrix.md)
  The current transform matrix of the receiver.
- [var pointSize: CGFloat](nsfontdescriptor/pointsize.md)
  The point size of the receiver.
- [var postscriptName: String?](nsfontdescriptor/postscriptname.md)
  The PostScript name of the receiver.
- [NSFontDescriptor.FeatureKey](nsfontdescriptor/featurekey.md)
  Constants to use as keys to retrieve information about a font descriptor from its feature dictionary.
- [typealias NSFontFamilyClass](nsfontfamilyclass.md)
  Constants that classify certain stylistic qualities of the font.
- [var NSFontFamilyClassMask: UInt32](nsfontfamilyclassmask.md)
  Constant you use to access `NSFontFamilyClass` values in the upper four bits of `NSFontSymbolicTraits`.
- [NSFontDescriptor.VariationKey](nsfontdescriptor/variationkey.md)
  Constants that can be used as keys to retrieve information about a font descriptor from its variation axis dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/typeface-information)*