# kCMTextMarkupAttribute_BackgroundColorARGB

**Framework**: Core Media  
**Kind**: var

A background color for the text.

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
let kCMTextMarkupAttribute_BackgroundColorARGB: CFString
```

#### Discussion

This attribute’s value must be a `CFArray` of four `CFNumber`s representing alpha, red, green, and blue fields with values between `0.0` and `1.0`. The system interprets the red, green, and blue components in the sRGB color space. The alpha indicates the opacity from `0.0` for transparent to `1.0` for 100 percent opaque.

The color applies to the geometry (for example, a box) containing the text. The container’s background color may have an alpha of `0` so the system doesn’t display it even though the system displays the text. You can optionally control the color behind individual characters with the [`kCMTextMarkupAttribute_CharacterBackgroundColorARGB`](kcmtextmarkupattribute_characterbackgroundcolorargb.md) attribute.

If you use this attribute, apply it to the entire attributed string.

## See Also

- [let kCMTextMarkupAttribute_ForegroundColorARGB: CFString](kcmtextmarkupattribute_foregroundcolorargb.md)
  A foreground color for the text.
- [let kCMTextMarkupAttribute_CharacterBackgroundColorARGB: CFString](kcmtextmarkupattribute_characterbackgroundcolorargb.md)
  A background color for individual text characters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/kcmtextmarkupattribute_backgroundcolorargb)*