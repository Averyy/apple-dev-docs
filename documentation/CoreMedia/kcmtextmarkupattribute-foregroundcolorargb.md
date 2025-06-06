# kCMTextMarkupAttribute_ForegroundColorARGB

**Framework**: Core Media  
**Kind**: var

A foreground color for the text.

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
let kCMTextMarkupAttribute_ForegroundColorARGB: CFString
```

#### Discussion

This attribute’s value must be a `CFArray` of four `CFNumber`s representing alpha, red, green, and blue fields with values between `0.0` and `1.0`. The system interprets the red, green, and blue components in the sRGB color space. The alpha indicates the opacity from `0.0` for transparent to `1.0` for 100 percent opaque.

## See Also

- [let kCMTextMarkupAttribute_BackgroundColorARGB: CFString](kcmtextmarkupattribute_backgroundcolorargb.md)
  A background color for the text.
- [let kCMTextMarkupAttribute_CharacterBackgroundColorARGB: CFString](kcmtextmarkupattribute_characterbackgroundcolorargb.md)
  A background color for individual text characters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/kcmtextmarkupattribute_foregroundcolorargb)*