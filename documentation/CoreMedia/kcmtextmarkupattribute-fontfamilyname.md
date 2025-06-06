# kCMTextMarkupAttribute_FontFamilyName

**Framework**: Core Media  
**Kind**: var

A name of a font family.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
let kCMTextMarkupAttribute_FontFamilyName: CFString
```

#### Discussion

This attribute’s value must be a `CFString` that holds the family name of an installed font (for example, “Helvetica”) that the system uses to render and/or measure text.

When the system specifies legible output, an attributed string has at most one of [`kCMTextMarkupAttribute_FontFamilyName`](kcmtextmarkupattribute_fontfamilyname.md) or [`kCMTextMarkupAttribute_GenericFontFamilyName`](kcmtextmarkupattribute_genericfontfamilyname.md) associated with each character.

## See Also

- [let kCMTextMarkupAttribute_GenericFontFamilyName: CFString](kcmtextmarkupattribute_genericfontfamilyname.md)
  A generic font family name identifier.
- [let kCMTextMarkupAttribute_BaseFontSizePercentageRelativeToVideoHeight: CFString](kcmtextmarkupattribute_basefontsizepercentagerelativetovideoheight.md)
  A base font size as a percentage of the video height.
- [let kCMTextMarkupAttribute_RelativeFontSize: CFString](kcmtextmarkupattribute_relativefontsize.md)
  A font size as a percentage of the current default font size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/kcmtextmarkupattribute_fontfamilyname)*