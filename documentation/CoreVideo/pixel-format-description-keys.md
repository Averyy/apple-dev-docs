# Pixel Format Description Keys

**Framework**: Core Video

The attributes of a pixel format.

#### Overview

If you need to define a custom pixel format, you must specify these keys in a Core Foundation dictionary. For information about registering your pixel format, see [`Technical Q&A 1401: Registering Custom Pixel Formats with QuickTime and Core Video`](https://developer.apple.comhttp://developer.apple.com/qa/qa2005/qa1401.html).

In most cases you do not need to specify your own pixel format.

## Topics

### Constants
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
- [let kCVPixelFormatBlockWidth: CFString](kcvpixelformatblockwidth.md)
- [let kCVPixelFormatBlockHeight: CFString](kcvpixelformatblockheight.md)
  The height, in pixels, of the smallest byte-addressable group of pixels (type `CFNumber`). Assumed to be 1 if this key is not present.
- [let kCVPixelFormatBitsPerBlock: CFString](kcvpixelformatbitsperblock.md)
- [let kCVPixelFormatBlockHorizontalAlignment: CFString](kcvpixelformatblockhorizontalalignment.md)
  The horizontal alignment requirements of this format (type `CFNumber`). For example,the alignment for v210 would be 8 here for the horizontal case to match the standard v210 row alignment value of 48. Assumed to be 1 if this key is not present.
- [let kCVPixelFormatBlockVerticalAlignment: CFString](kcvpixelformatblockverticalalignment.md)
  The vertical alignment requirements of this format (type `CFNumber`). Assumed to be 1 if this key is not present.
- [let kCVPixelFormatBlackBlock: CFString](kcvpixelformatblackblock.md)
  The bit pattern for a block of black pixels (type `CFData`. If this key is absent, black is assumed to be all zeros. If present, this should be `bitsPerPixel` bits long; if `bitsPerPixel` is less than a byte, repeat the bit pattern for the full byte.
- [let kCVPixelFormatHorizontalSubsampling: CFString](kcvpixelformathorizontalsubsampling.md)
  Horizontal subsampling information for this plane (type `CFNumber`). Assumed to be 1 if this key is not present.
- [let kCVPixelFormatVerticalSubsampling: CFString](kcvpixelformatverticalsubsampling.md)
  Vertical subsampling information for this plane (type `CFNumber`). Assumed to be 1 if this key is not present.
- [let kCVPixelFormatOpenGLFormat: CFString](kcvpixelformatopenglformat.md)
  The OpenGL format used to describe this image plane (if applicable). See the [`OpenGL specification`](https://developer.apple.comhttp://www.opengl.org/documentation/) for possible values.
- [let kCVPixelFormatOpenGLType: CFString](kcvpixelformatopengltype.md)
  The OpenGL type to describe this image plane (if applicable). See the [`OpenGL specification`](https://developer.apple.comhttp://www.opengl.org/documentation/) for possible values.
- [let kCVPixelFormatOpenGLInternalFormat: CFString](kcvpixelformatopenglinternalformat.md)
  The OpenGL internal format for this pixel format (if applicable). See the [`OpenGL specification`](https://developer.apple.comhttp://www.opengl.org/documentation/) for possible values.
- [let kCVPixelFormatCGBitmapInfo: CFString](kcvpixelformatcgbitmapinfo.md)
  The Core Graphics bitmap information for this pixel format (if applicable).
- [let kCVPixelFormatQDCompatibility: CFString](kcvpixelformatqdcompatibility.md)
  If true, this format is compatible with QuickDraw (type `CFBoolean`).
- [let kCVPixelFormatCGBitmapContextCompatibility: CFString](kcvpixelformatcgbitmapcontextcompatibility.md)
  If true, this format is compatible with Core Graphics bitmap contexts(type `CFBoolean`).
- [let kCVPixelFormatCGImageCompatibility: CFString](kcvpixelformatcgimagecompatibility.md)
  If true, this format is compatible with the `CGImage` type (type `CFBoolean`).
- [let kCVPixelFormatOpenGLCompatibility: CFString](kcvpixelformatopenglcompatibility.md)
  If true, this format is compatible with OpenGL (type `CFBoolean`).
- [let kCVPixelFormatOpenGLESCompatibility: CFString](kcvpixelformatopenglescompatibility.md)
  If true, this format is compatible with OpenGLES (type `CFBoolean`).
- [let kCVPixelFormatFillExtendedPixelsCallback: CFString](kcvpixelformatfillextendedpixelscallback.md)
  A custom extended pixel fill algorithm (type `CFData`). See [`CVFillExtendedPixelsCallBack`](cvfillextendedpixelscallback.md) and [`CVFillExtendedPixelsCallBackData`](cvfillextendedpixelscallbackdata.md) for more information.

## See Also

- [Pixel Format Identifiers](pixel-format-identifiers.md)
  Core Video does not provide support for all of these formats; this list defines only their names.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/pixel-format-description-keys)*