# kCVPixelFormatPlanes

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
let kCVPixelFormatPlanes: CFString
```

#### Discussion

The number of image planes associated with this format (type `CFNumber`). Each plane may contain a single component or an interleaved set of components. Note that if your pixel format is not planar, you can put the required format keys at the top-level dictionary.

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
- [let kCVPixelFormatBlockWidth: CFString](kcvpixelformatblockwidth.md)
- [let kCVPixelFormatBlockHeight: CFString](kcvpixelformatblockheight.md)
  The height, in pixels, of the smallest byte-addressable group of pixels (type `CFNumber`). Assumed to be 1 if this key is not present.
- [let kCVPixelFormatBitsPerBlock: CFString](kcvpixelformatbitsperblock.md)
- [let kCVPixelFormatBlockHorizontalAlignment: CFString](kcvpixelformatblockhorizontalalignment.md)
  The horizontal alignment requirements of this format (type `CFNumber`). For example,the alignment for v210 would be 8 here for the horizontal case to match the standard v210 row alignment value of 48. Assumed to be 1 if this key is not present.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/kcvpixelformatplanes)*