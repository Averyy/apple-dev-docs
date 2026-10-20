# kCMTextMarkupAttribute_RelativeFontSize

**Framework**: Core Media  
**Kind**: var

A font size as a percentage of the current default font size.

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
let kCMTextMarkupAttribute_RelativeFontSize: CFString
```

#### Discussion

This attribute’s value must be a non-negative `CFNumber`. This is a number holding a percentage of the size of the calculated default font size. A value of `120` indicates 20% larger than the default font size. A value of `80` indicates 80% of the default font size. The default value of `100` indicates no size difference.

## See Also

- [let kCMTextMarkupAttribute_FontFamilyName: CFString](kcmtextmarkupattribute_fontfamilyname.md)
  A name of a font family.
- [let kCMTextMarkupAttribute_GenericFontFamilyName: CFString](kcmtextmarkupattribute_genericfontfamilyname.md)
  A generic font family name identifier.
- [let kCMTextMarkupAttribute_BaseFontSizePercentageRelativeToVideoHeight: CFString](kcmtextmarkupattribute_basefontsizepercentagerelativetovideoheight.md)
  A base font size as a percentage of the video height.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/kcmtextmarkupattribute_relativefontsize)*