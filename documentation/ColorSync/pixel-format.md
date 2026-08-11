# Pixel format and data layout

**Framework**: ColorSync

Describe the memory layout of the pixel buffers a color transform reads and writes.

#### Overview

When you convert color with [`ColorSyncTransformConvert(_:_:_:_:_:_:_:_:_:_:_:_:)`](colorsynctransformconvert(_:_:_:_:_:_:_:_:_:_:_:_:).md), you describe each buffer’s bit depth, byte order, and alpha handling using these constants and the [`ColorSyncDataLayout`](colorsyncdatalayout.md) type.

## Topics

### Describing data layout
- [struct ColorSyncAlphaInfo](colorsyncalphainfo.md)
  The location of the alpha component in a pixel, and whether it’s premultiplied.
- [struct ColorSyncDataDepth](colorsyncdatadepth.md)
  The bit depth and numeric type of a color component in a pixel.
- [typealias ColorSyncDataLayout](colorsyncdatalayout.md)
  A bit field describing the alpha information and byte order of a pixel layout.
### Handling alpha
- [var kColorSyncAlphaFirst: ColorSyncAlphaInfo](kcolorsyncalphafirst.md)
  The alpha component is stored first and is not premultiplied. For example, non-premultiplied ARGB.
- [var kColorSyncAlphaInfoMask: Int](kcolorsyncalphainfomask.md)
  The mask for extracting the [`ColorSyncAlphaInfo`](colorsyncalphainfo.md) value from a [`ColorSyncDataLayout`](colorsyncdatalayout.md).
- [var kColorSyncAlphaLast: ColorSyncAlphaInfo](kcolorsyncalphalast.md)
  The alpha component is stored last and is not premultiplied. For example, non-premultiplied RGBA.
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
### Setting byte order
- [var kColorSyncByteOrder16Big: Int](kcolorsyncbyteorder16big.md)
  16-bit, big-endian byte order.
- [var kColorSyncByteOrder16Little: Int](kcolorsyncbyteorder16little.md)
  16-bit, little-endian byte order.
- [var kColorSyncByteOrder32Big: Int](kcolorsyncbyteorder32big.md)
  32-bit, big-endian byte order.
- [var kColorSyncByteOrder32Little: Int](kcolorsyncbyteorder32little.md)
  32-bit, little-endian byte order.
- [var kColorSyncByteOrderDefault: Int](kcolorsyncbyteorderdefault.md)
  The default (host) byte order.
- [var kColorSyncByteOrderMask: Int](kcolorsyncbyteordermask.md)
  The mask for extracting the byte-order value from a [`ColorSyncDataLayout`](colorsyncdatalayout.md).
### Choosing bit depth and range
- [var kColorSync10BitInteger: ColorSyncDataDepth](kcolorsync10bitinteger.md)
  10-bit integer components.
- [var kColorSync16BitFloat: ColorSyncDataDepth](kcolorsync16bitfloat.md)
  16-bit floating-point (half-float) components.
- [var kColorSync16BitInteger: ColorSyncDataDepth](kcolorsync16bitinteger.md)
  16-bit integer components.
- [var kColorSync1BitGamut: ColorSyncDataDepth](kcolorsync1bitgamut.md)
  One-bit values, used for gamut-check results.
- [var kColorSync32BitFloat: ColorSyncDataDepth](kcolorsync32bitfloat.md)
  32-bit floating-point components.
- [var kColorSync32BitInteger: ColorSyncDataDepth](kcolorsync32bitinteger.md)
  32-bit integer components.
- [var kColorSync32BitNamedColorIndex: ColorSyncDataDepth](kcolorsync32bitnamedcolorindex.md)
  32-bit named-color index values.
- [var kColorSync8BitInteger: ColorSyncDataDepth](kcolorsync8bitinteger.md)
  8-bit integer components.

## See Also

- [Color transforms](color-transforms.md)
  Convert color from one profile’s color space to another.


---

*[View on Apple Developer](https://developer.apple.com/documentation/colorsync/pixel-format)*