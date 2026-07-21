# Pixel format and data layout

**Framework**: ColorSync

Describe the memory layout of the pixel buffers a color transform reads and writes.

#### Overview

When you convert color with [`ColorSyncTransformConvert(_:_:_:_:_:_:_:_:_:_:_:_:)`](colorsynctransformconvert(_:_:_:_:_:_:_:_:_:_:_:_:).md), you describe each buffer’s bit depth, byte order, and alpha handling using these constants and the [`ColorSyncDataLayout`](colorsyncdatalayout.md) type.

## Topics

### Describing data layout
- [struct ColorSyncAlphaInfo](colorsyncalphainfo.md)
- [struct ColorSyncDataDepth](colorsyncdatadepth.md)
- [typealias ColorSyncDataLayout](colorsyncdatalayout.md)
### Handling alpha
- [var kColorSyncAlphaFirst: ColorSyncAlphaInfo](kcolorsyncalphafirst.md)
- [var kColorSyncAlphaInfoMask: Int](kcolorsyncalphainfomask.md)
- [var kColorSyncAlphaLast: ColorSyncAlphaInfo](kcolorsyncalphalast.md)
- [var kColorSyncAlphaNone: ColorSyncAlphaInfo](kcolorsyncalphanone.md)
- [var kColorSyncAlphaNoneSkipFirst: ColorSyncAlphaInfo](kcolorsyncalphanoneskipfirst.md)
- [var kColorSyncAlphaNoneSkipLast: ColorSyncAlphaInfo](kcolorsyncalphanoneskiplast.md)
- [var kColorSyncAlphaPremultipliedFirst: ColorSyncAlphaInfo](kcolorsyncalphapremultipliedfirst.md)
- [var kColorSyncAlphaPremultipliedLast: ColorSyncAlphaInfo](kcolorsyncalphapremultipliedlast.md)
### Setting byte order
- [var kColorSyncByteOrder16Big: Int](kcolorsyncbyteorder16big.md)
- [var kColorSyncByteOrder16Little: Int](kcolorsyncbyteorder16little.md)
- [var kColorSyncByteOrder32Big: Int](kcolorsyncbyteorder32big.md)
- [var kColorSyncByteOrder32Little: Int](kcolorsyncbyteorder32little.md)
- [var kColorSyncByteOrderDefault: Int](kcolorsyncbyteorderdefault.md)
- [var kColorSyncByteOrderMask: Int](kcolorsyncbyteordermask.md)
### Choosing bit depth and range
- [var kColorSync10BitInteger: ColorSyncDataDepth](kcolorsync10bitinteger.md)
- [var kColorSync16BitFloat: ColorSyncDataDepth](kcolorsync16bitfloat.md)
- [var kColorSync16BitInteger: ColorSyncDataDepth](kcolorsync16bitinteger.md)
- [var kColorSync1BitGamut: ColorSyncDataDepth](kcolorsync1bitgamut.md)
- [var kColorSync32BitFloat: ColorSyncDataDepth](kcolorsync32bitfloat.md)
- [var kColorSync32BitInteger: ColorSyncDataDepth](kcolorsync32bitinteger.md)
- [var kColorSync32BitNamedColorIndex: ColorSyncDataDepth](kcolorsync32bitnamedcolorindex.md)
- [var kColorSync8BitInteger: ColorSyncDataDepth](kcolorsync8bitinteger.md)

## See Also

- [Color transforms](color-transforms.md)
  Convert color from one profile’s color space to another.


---

*[View on Apple Developer](https://developer.apple.com/documentation/colorsync/pixel-format)*