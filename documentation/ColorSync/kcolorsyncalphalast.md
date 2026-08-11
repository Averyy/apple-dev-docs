# kColorSyncAlphaLast

**Framework**: ColorSync  
**Kind**: var

The alpha component is stored last and is not premultiplied. For example, non-premultiplied RGBA.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
var kColorSyncAlphaLast: ColorSyncAlphaInfo { get }
```

## See Also

- [var kColorSyncAlphaFirst: ColorSyncAlphaInfo](kcolorsyncalphafirst.md)
  The alpha component is stored first and is not premultiplied. For example, non-premultiplied ARGB.
- [var kColorSyncAlphaInfoMask: Int](kcolorsyncalphainfomask.md)
  The mask for extracting the [`ColorSyncAlphaInfo`](colorsyncalphainfo.md) value from a [`ColorSyncDataLayout`](colorsyncdatalayout.md).
- [var kColorSyncAlphaNone: ColorSyncAlphaInfo](kcolorsyncalphanone.md)
  There is no alpha channel. For example, RGB.
- [var kColorSyncAlphaNoneSkipFirst: ColorSyncAlphaInfo](kcolorsyncalphanoneskipfirst.md)
  There is no alpha channel; the most significant bits are ignored. For example, XRGB.
- [var kColorSyncAlphaNoneSkipLast: ColorSyncAlphaInfo](kcolorsyncalphanoneskiplast.md)
  There is no alpha channel; the least significant bits are ignored. For example, RGBX.
- [var kColorSyncAlphaPremultipliedFirst: ColorSyncAlphaInfo](kcolorsyncalphapremultipliedfirst.md)
  The alpha component is stored first and the color components are premultiplied by it. For example, premultiplied ARGB.
- [var kColorSyncAlphaPremultipliedLast: ColorSyncAlphaInfo](kcolorsyncalphapremultipliedlast.md)
  The alpha component is stored last and the color components are premultiplied by it. For example, premultiplied RGBA.


---

*[View on Apple Developer](https://developer.apple.com/documentation/colorsync/kcolorsyncalphalast)*