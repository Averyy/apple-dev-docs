# CTFontGetUnderlineThickness(_:)

**Framework**: Core Text  
**Kind**: func

Returns the scaled underline-thickness metric of the given font.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func CTFontGetUnderlineThickness(_ font: CTFont) -> CGFloat
```

#### Return Value

The font underline-thickness metric scaled according to the point size and matrix of the font reference.

## Parameters

- `font`: The font reference.

## See Also

- [func CTFontGetAscent(CTFont) -> CGFloat](ctfontgetascent(_:).md)
  Returns the scaled font-ascent metric of the given font.
- [func CTFontGetDescent(CTFont) -> CGFloat](ctfontgetdescent(_:).md)
  Returns the scaled font-descent metric of the given font.
- [func CTFontGetLeading(CTFont) -> CGFloat](ctfontgetleading(_:).md)
  Returns the scaled font-leading metric of the given font.
- [func CTFontGetUnitsPerEm(CTFont) -> UInt32](ctfontgetunitsperem(_:).md)
  Returns the units-per-em metric of the given font.
- [func CTFontGetGlyphCount(CTFont) -> CFIndex](ctfontgetglyphcount(_:).md)
  Returns the number of glyphs of the given font.
- [func CTFontGetBoundingBox(CTFont) -> CGRect](ctfontgetboundingbox(_:).md)
  Returns the scaled bounding box of the given font.
- [func CTFontGetUnderlinePosition(CTFont) -> CGFloat](ctfontgetunderlineposition(_:).md)
  Returns the scaled underline position of the given font.
- [func CTFontGetSlantAngle(CTFont) -> CGFloat](ctfontgetslantangle(_:).md)
  Returns the slant angle of the given font.
- [func CTFontGetCapHeight(CTFont) -> CGFloat](ctfontgetcapheight(_:).md)
  Returns the cap-height metric of the given font.
- [func CTFontGetXHeight(CTFont) -> CGFloat](ctfontgetxheight(_:).md)
  Returns the x-height metric of the given font.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/ctfontgetunderlinethickness(_:))*