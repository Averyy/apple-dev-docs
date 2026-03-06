# kCVPixelFormatBlockWidth

**Framework**: Core Video  
**Kind**: var

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
let kCVPixelFormatBlockWidth: CFString
```

#### Discussion

The width, in pixels, of the smallest byte-addressable group of pixels (type `CFNumber`). Used to assist with allocating memory for pixel formats that don’t have an integer value for bytes per pixel. Assumed to be 1 if this key is not present. Here are some examples of block widths for standard pixel formats:

- 8-bit luminance only, block width is 1, the bits per block value is 8.
- 16-bit 1555 RGB, block width is 1, the bits per block value is 16.
- 32-bit 8888 ARGB, block width is 1, the bits per block value is 32.
- 2vuy (CbYCrY), block width is 2, the bits per block value is 32.
- 1-bit bitmap, block width is 8, the bits per block value is 8.
- v210, block width is 6, the bits per block value is 128 .

## See Also

- [let kCVPixelFormatComponentRange: CFString](kcvpixelformatcomponentrange.md)
- [let kCVPixelFormatComponentRange_FullRange: CFString](kcvpixelformatcomponentrange_fullrange.md)
- [let kCVPixelFormatComponentRange_VideoRange: CFString](kcvpixelformatcomponentrange_videorange.md)
- [let kCVPixelFormatComponentRange_WideRange: CFString](kcvpixelformatcomponentrange_widerange.md)
- [let kCVPixelFormatContainsRGB: CFString](kcvpixelformatcontainsrgb.md)
- [let kCVPixelFormatContainsYCbCr: CFString](kcvpixelformatcontainsycbcr.md)
- [let kCVPixelFormatName: CFString](kcvpixelformatname.md)
  The name of the pixel format (type `CFString`). This should be the same as the codec name you would use in QuickTime.
- [let kCVPixelFormatConstant: CFString](kcvpixelformatconstant.md)
  The pixel format constant for QuickTime.
- [let kCVPixelFormatCodecType: CFString](kcvpixelformatcodectype.md)
  The codec type (type `CFString`). For example, `'2vuy'` or `k422YpCbCr8CodecType`.
- [let kCVPixelFormatFourCC: CFString](kcvpixelformatfourcc.md)
  The Microsoft FourCC equivalent code for this pixel format (type `CFString`).
- [let kCVPixelFormatContainsAlpha: CFString](kcvpixelformatcontainsalpha.md)
  A Boolean value where [`kCFBooleanTrue`](https://developer.apple.com/documentation/CoreFoundation/kCFBooleanTrue) indicates that the format contains alpha and some images may be considered transparent; [`kCFBooleanFalse`](https://developer.apple.com/documentation/CoreFoundation/kCFBooleanFalse) indicates that there is no alpha and images are always opaque.
- [let kCVPixelFormatPlanes: CFString](kcvpixelformatplanes.md)
- [let kCVPixelFormatBlockHeight: CFString](kcvpixelformatblockheight.md)
  The height, in pixels, of the smallest byte-addressable group of pixels (type `CFNumber`). Assumed to be 1 if this key is not present.
- [let kCVPixelFormatBitsPerBlock: CFString](kcvpixelformatbitsperblock.md)
- [let kCVPixelFormatBlockHorizontalAlignment: CFString](kcvpixelformatblockhorizontalalignment.md)
  The horizontal alignment requirements of this format (type `CFNumber`). For example,the alignment for v210 would be 8 here for the horizontal case to match the standard v210 row alignment value of 48. Assumed to be 1 if this key is not present.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/kcvpixelformatblockwidth)*