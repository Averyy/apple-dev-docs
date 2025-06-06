# kCMTextMarkupAttribute_GenericFontFamilyName

**Framework**: Core Media  
**Kind**: var

A generic font family name identifier.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
let kCMTextMarkupAttribute_GenericFontFamilyName: CFString
```

#### Discussion

This attribute’s value must be one of the constants listed below. You need to map generic fonts to the family name of an installed font before rendering and/or measuring text (see [`Media Accessibility`](https://developer.apple.com/documentation/MediaAccessibility)).

When the system specifies legible output, an attributed string has at most one of [`kCMTextMarkupAttribute_FontFamilyName`](kcmtextmarkupattribute_fontfamilyname.md) or [`kCMTextMarkupAttribute_GenericFontFamilyName`](kcmtextmarkupattribute_genericfontfamilyname.md) associated with each character.

## Topics

### Font Names
- [let kCMTextMarkupGenericFontName_Default: CFString](kcmtextmarkupgenericfontname_default.md)
  The default font.
- [let kCMTextMarkupGenericFontName_Serif: CFString](kcmtextmarkupgenericfontname_serif.md)
  A font with serifs.
- [let kCMTextMarkupGenericFontName_SansSerif: CFString](kcmtextmarkupgenericfontname_sansserif.md)
  A font without serifs.
- [let kCMTextMarkupGenericFontName_Monospace: CFString](kcmtextmarkupgenericfontname_monospace.md)
  A monospaced font with or without serifs.
- [let kCMTextMarkupGenericFontName_MonospaceSerif: CFString](kcmtextmarkupgenericfontname_monospaceserif.md)
  A monospaced font with serifs.
- [let kCMTextMarkupGenericFontName_MonospaceSansSerif: CFString](kcmtextmarkupgenericfontname_monospacesansserif.md)
  A monospaced font without serifs.
- [let kCMTextMarkupGenericFontName_ProportionalSerif: CFString](kcmtextmarkupgenericfontname_proportionalserif.md)
  A proportional font with serifs.
- [let kCMTextMarkupGenericFontName_ProportionalSansSerif: CFString](kcmtextmarkupgenericfontname_proportionalsansserif.md)
  A proportional font without serifs.
- [let kCMTextMarkupGenericFontName_SmallCapital: CFString](kcmtextmarkupgenericfontname_smallcapital.md)
  A font with lowercase letters set as small capital letters.
- [let kCMTextMarkupGenericFontName_Casual: CFString](kcmtextmarkupgenericfontname_casual.md)
  A casual font.
- [let kCMTextMarkupGenericFontName_Cursive: CFString](kcmtextmarkupgenericfontname_cursive.md)
  A cursive font.
- [let kCMTextMarkupGenericFontName_Fantasy: CFString](kcmtextmarkupgenericfontname_fantasy.md)
  A fantasy font.

## See Also

- [let kCMTextMarkupAttribute_FontFamilyName: CFString](kcmtextmarkupattribute_fontfamilyname.md)
  A name of a font family.
- [let kCMTextMarkupAttribute_BaseFontSizePercentageRelativeToVideoHeight: CFString](kcmtextmarkupattribute_basefontsizepercentagerelativetovideoheight.md)
  A base font size as a percentage of the video height.
- [let kCMTextMarkupAttribute_RelativeFontSize: CFString](kcmtextmarkupattribute_relativefontsize.md)
  A font size as a percentage of the current default font size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/kcmtextmarkupattribute_genericfontfamilyname)*