# kCMTextMarkupAttribute_BaseFontSizePercentageRelativeToVideoHeight

**Framework**: Core Media  
**Kind**: var

A base font size as a percentage of the video height.

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
let kCMTextMarkupAttribute_BaseFontSizePercentageRelativeToVideoHeight: CFString
```

#### Discussion

This attribute’s value must be a non-negative `CFNumber`. This is a number holding a percentage of the height of the video frame. For example, a value of `5` indicates that the base font size should be 5% of the height of the video.

## See Also

- [let kCMTextMarkupAttribute_FontFamilyName: CFString](kcmtextmarkupattribute_fontfamilyname.md)
  A name of a font family.
- [let kCMTextMarkupAttribute_GenericFontFamilyName: CFString](kcmtextmarkupattribute_genericfontfamilyname.md)
  A generic font family name identifier.
- [let kCMTextMarkupAttribute_RelativeFontSize: CFString](kcmtextmarkupattribute_relativefontsize.md)
  A font size as a percentage of the current default font size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/kcmtextmarkupattribute_basefontsizepercentagerelativetovideoheight)*