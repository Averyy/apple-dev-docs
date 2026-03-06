# Pixel Format Identifiers

**Framework**: Core Video

Core Video does not provide support for all of these formats; this list defines only their names.

## Topics

### Constants
- [var kCVPixelFormatType_1Monochrome: OSType](kcvpixelformattype_1monochrome.md)
  1 bit indexed.
- [var kCVPixelFormatType_2Indexed: OSType](kcvpixelformattype_2indexed.md)
  2-bit indexed.
- [var kCVPixelFormatType_4Indexed: OSType](kcvpixelformattype_4indexed.md)
  4-bit indexed.
- [var kCVPixelFormatType_8Indexed: OSType](kcvpixelformattype_8indexed.md)
  8-bit indexed.
- [var kCVPixelFormatType_1IndexedGray_WhiteIsZero: OSType](kcvpixelformattype_1indexedgray_whiteiszero.md)
  1 bit indexed gray, white is zero.
- [var kCVPixelFormatType_2IndexedGray_WhiteIsZero: OSType](kcvpixelformattype_2indexedgray_whiteiszero.md)
  2-bit indexed gray, white is zero.
- [var kCVPixelFormatType_4IndexedGray_WhiteIsZero: OSType](kcvpixelformattype_4indexedgray_whiteiszero.md)
  4-bit indexed gray, white is zero.
- [var kCVPixelFormatType_8IndexedGray_WhiteIsZero: OSType](kcvpixelformattype_8indexedgray_whiteiszero.md)
  8-bit indexed gray, white is zero.
- [var kCVPixelFormatType_16BE555: OSType](kcvpixelformattype_16be555.md)
  16-bit BE RGB 555.
- [var kCVPixelFormatType_16LE555: OSType](kcvpixelformattype_16le555.md)
  16-bit LE RGB 555.
- [var kCVPixelFormatType_16LE5551: OSType](kcvpixelformattype_16le5551.md)
  16-bit LE RGB 5551.
- [var kCVPixelFormatType_16BE565: OSType](kcvpixelformattype_16be565.md)
  16-bit BE RGB 565.
- [var kCVPixelFormatType_16LE565: OSType](kcvpixelformattype_16le565.md)
  16-bit LE RGB 565.
- [var kCVPixelFormatType_24RGB: OSType](kcvpixelformattype_24rgb.md)
  24-bit RGB.
- [var kCVPixelFormatType_24BGR: OSType](kcvpixelformattype_24bgr.md)
  24-bit BGR.
- [var kCVPixelFormatType_32ARGB: OSType](kcvpixelformattype_32argb.md)
  32-bit ARGB.
- [var kCVPixelFormatType_32BGRA: OSType](kcvpixelformattype_32bgra.md)
  32-bit BGRA.
- [var kCVPixelFormatType_32ABGR: OSType](kcvpixelformattype_32abgr.md)
  32-bit ABGR.
- [var kCVPixelFormatType_32RGBA: OSType](kcvpixelformattype_32rgba.md)
  32-bit RGBA.
- [var kCVPixelFormatType_64ARGB: OSType](kcvpixelformattype_64argb.md)
  64-bit ARGB, 16-bit big-endian samples.
- [var kCVPixelFormatType_48RGB: OSType](kcvpixelformattype_48rgb.md)
  48-bit RGB, 16-bit big-endian samples.
- [var kCVPixelFormatType_32AlphaGray: OSType](kcvpixelformattype_32alphagray.md)
  32-bit AlphaGray, 16-bit big-endian samples, black is zero.
- [var kCVPixelFormatType_16Gray: OSType](kcvpixelformattype_16gray.md)
  16-bit Grayscale, 16-bit big-endian samples, black is zero.
- [var kCVPixelFormatType_30RGB: OSType](kcvpixelformattype_30rgb.md)
  30-bit RGB, 10-bit big-endian samples, 2 unused padding bits (at least significant end).
- [var kCVPixelFormatType_422YpCbCr8: OSType](kcvpixelformattype_422ypcbcr8.md)
  Component Y’CbCr 8-bit 4:2:2, ordered Cb Y’0 Cr Y’1.
- [var kCVPixelFormatType_4444YpCbCrA8: OSType](kcvpixelformattype_4444ypcbcra8.md)
  Component Y’CbCrA 8-bit 4:4:4:4, ordered Cb Y’ Cr A.
- [var kCVPixelFormatType_4444YpCbCrA8R: OSType](kcvpixelformattype_4444ypcbcra8r.md)
  Component Y’CbCrA 8-bit 4:4:4:4, rendering format. Full range alpha, zero biased YUV, ordered A Y’ Cb Cr.
- [var kCVPixelFormatType_4444AYpCbCr8: OSType](kcvpixelformattype_4444aypcbcr8.md)
  Component Y’CbCrA 8-bit 4:4:4:4, ordered A Y’ Cb Cr, full range alpha, video range Y’CbCr.
- [var kCVPixelFormatType_4444AYpCbCr16: OSType](kcvpixelformattype_4444aypcbcr16.md)
  Component Y’CbCrA 16-bit 4:4:4:4, ordered A Y’ Cb Cr, full range alpha, video range Y’CbCr, 16-bit little-endian samples.
- [var kCVPixelFormatType_444YpCbCr8: OSType](kcvpixelformattype_444ypcbcr8.md)
  Component Y’CbCr 8-bit 4:4:4.
- [var kCVPixelFormatType_422YpCbCr16: OSType](kcvpixelformattype_422ypcbcr16.md)
  Component Y’CbCr 10,12,14,16-bit 4:2:2.
- [var kCVPixelFormatType_422YpCbCr10: OSType](kcvpixelformattype_422ypcbcr10.md)
  Component Y’CbCr 10-bit 4:2:2.
- [var kCVPixelFormatType_444YpCbCr10: OSType](kcvpixelformattype_444ypcbcr10.md)
  Component Y’CbCr 10-bit 4:4:4.
- [var kCVPixelFormatType_420YpCbCr8Planar: OSType](kcvpixelformattype_420ypcbcr8planar.md)
  Planar Component Y’CbCr 8-bit 4:2:0. `baseAddr` points to a big-endian `CVPlanarPixelBufferInfo_YCbCrPlanar` struct.
- [var kCVPixelFormatType_420YpCbCr8PlanarFullRange: OSType](kcvpixelformattype_420ypcbcr8planarfullrange.md)
  Planar Component Y’CbCr 8-bit 4:2:0, full range.  `baseAddr` points to a big-endian `CVPlanarPixelBufferInfo_YCbCrPlanar` struct.
- [var kCVPixelFormatType_422YpCbCr_4A_8BiPlanar: OSType](kcvpixelformattype_422ypcbcr_4a_8biplanar.md)
  First plane: Video-range Component Y’CbCr 8-bit 4:2:2, ordered Cb Y’0 Cr Y’1; second plane: alpha 8-bit 0-255.
- [var kCVPixelFormatType_420YpCbCr8BiPlanarVideoRange: OSType](kcvpixelformattype_420ypcbcr8biplanarvideorange.md)
  Bi-Planar Component Y’CbCr 8-bit 4:2:0, video-range (luma=[16,235] chroma=[16,240]).  `baseAddr` points to a big-endian `CVPlanarPixelBufferInfo_YCbCrBiPlanar` struct.
- [var kCVPixelFormatType_420YpCbCr8BiPlanarFullRange: OSType](kcvpixelformattype_420ypcbcr8biplanarfullrange.md)
  Bi-Planar Component Y’CbCr 8-bit 4:2:0, full-range (luma=[0,255] chroma=[1,255]).  `baseAddr` points to a big-endian `CVPlanarPixelBufferInfo_YCbCrBiPlanar` struct.
- [var kCVPixelFormatType_422YpCbCr8_yuvs: OSType](kcvpixelformattype_422ypcbcr8_yuvs.md)
  Component Y’CbCr 8-bit 4:2:2, ordered Y’0 Cb Y’1 Cr.
- [var kCVPixelFormatType_422YpCbCr8FullRange: OSType](kcvpixelformattype_422ypcbcr8fullrange.md)
  Component Y’CbCr 8-bit 4:2:2, full range, ordered Y’0 Cb Y’1 Cr.
- [var kCVPixelFormatType_OneComponent8: OSType](kcvpixelformattype_onecomponent8.md)
  8-bit one component, black is zero.
- [var kCVPixelFormatType_TwoComponent8: OSType](kcvpixelformattype_twocomponent8.md)
  8-bit two component, black is zero.
- [var kCVPixelFormatType_OneComponent16Half: OSType](kcvpixelformattype_onecomponent16half.md)
  6-bit one component IEEE half-precision float, 16-bit little-endian samples.
- [var kCVPixelFormatType_OneComponent32Float: OSType](kcvpixelformattype_onecomponent32float.md)
  32-bit one component IEEE float, 32-bit little-endian samples.
- [var kCVPixelFormatType_TwoComponent16Half: OSType](kcvpixelformattype_twocomponent16half.md)
  16-bit two component IEEE half-precision float, 16-bit little-endian samples.
- [var kCVPixelFormatType_TwoComponent32Float: OSType](kcvpixelformattype_twocomponent32float.md)
  32-bit two component IEEE float, 32-bit little-endian samples.
- [var kCVPixelFormatType_64RGBAHalf: OSType](kcvpixelformattype_64rgbahalf.md)
  64-bit RGBA IEEE half-precision float, 16-bit little-endian samples.
- [var kCVPixelFormatType_128RGBAFloat: OSType](kcvpixelformattype_128rgbafloat.md)
  128-bit RGBA IEEE float, 32-bit little-endian samples.
- [var kCVPixelFormatType_14Bayer_BGGR: OSType](kcvpixelformattype_14bayer_bggr.md)
- [var kCVPixelFormatType_14Bayer_GBRG: OSType](kcvpixelformattype_14bayer_gbrg.md)
- [var kCVPixelFormatType_14Bayer_GRBG: OSType](kcvpixelformattype_14bayer_grbg.md)
- [var kCVPixelFormatType_14Bayer_RGGB: OSType](kcvpixelformattype_14bayer_rggb.md)
- [var kCVPixelFormatType_30RGBLEPackedWideGamut: OSType](kcvpixelformattype_30rgblepackedwidegamut.md)
- [var kCVPixelFormatType_ARGB2101010LEPacked: OSType](kcvpixelformattype_argb2101010lepacked.md)
- [var kCVPixelFormatType_420YpCbCr10BiPlanarFullRange: OSType](kcvpixelformattype_420ypcbcr10biplanarfullrange.md)
- [var kCVPixelFormatType_420YpCbCr10BiPlanarVideoRange: OSType](kcvpixelformattype_420ypcbcr10biplanarvideorange.md)
- [var kCVPixelFormatType_422YpCbCr10BiPlanarFullRange: OSType](kcvpixelformattype_422ypcbcr10biplanarfullrange.md)
- [var kCVPixelFormatType_422YpCbCr10BiPlanarVideoRange: OSType](kcvpixelformattype_422ypcbcr10biplanarvideorange.md)
- [var kCVPixelFormatType_444YpCbCr10BiPlanarFullRange: OSType](kcvpixelformattype_444ypcbcr10biplanarfullrange.md)
- [var kCVPixelFormatType_444YpCbCr10BiPlanarVideoRange: OSType](kcvpixelformattype_444ypcbcr10biplanarvideorange.md)
- [var kCVPixelFormatType_DepthFloat16: OSType](kcvpixelformattype_depthfloat16.md)
- [var kCVPixelFormatType_DepthFloat32: OSType](kcvpixelformattype_depthfloat32.md)
- [var kCVPixelFormatType_DisparityFloat16: OSType](kcvpixelformattype_disparityfloat16.md)
- [var kCVPixelFormatType_DisparityFloat32: OSType](kcvpixelformattype_disparityfloat32.md)
- [var kCVPixelFormatType_16VersatileBayer: OSType](kcvpixelformattype_16versatilebayer.md)
- [var kCVPixelFormatType_40ARGBLEWideGamut: OSType](kcvpixelformattype_40argblewidegamut.md)
- [var kCVPixelFormatType_40ARGBLEWideGamutPremultiplied: OSType](kcvpixelformattype_40argblewidegamutpremultiplied.md)
- [var kCVPixelFormatType_420YpCbCr8VideoRange_8A_TriPlanar: OSType](kcvpixelformattype_420ypcbcr8videorange_8a_triplanar.md)
- [var kCVPixelFormatType_422YpCbCr16BiPlanarVideoRange: OSType](kcvpixelformattype_422ypcbcr16biplanarvideorange.md)
- [var kCVPixelFormatType_422YpCbCr8BiPlanarFullRange: OSType](kcvpixelformattype_422ypcbcr8biplanarfullrange.md)
- [var kCVPixelFormatType_422YpCbCr8BiPlanarVideoRange: OSType](kcvpixelformattype_422ypcbcr8biplanarvideorange.md)
- [var kCVPixelFormatType_4444AYpCbCrFloat: OSType](kcvpixelformattype_4444aypcbcrfloat.md)
- [var kCVPixelFormatType_444YpCbCr16BiPlanarVideoRange: OSType](kcvpixelformattype_444ypcbcr16biplanarvideorange.md)
- [var kCVPixelFormatType_444YpCbCr16VideoRange_16A_TriPlanar: OSType](kcvpixelformattype_444ypcbcr16videorange_16a_triplanar.md)
- [var kCVPixelFormatType_444YpCbCr8BiPlanarFullRange: OSType](kcvpixelformattype_444ypcbcr8biplanarfullrange.md)
- [var kCVPixelFormatType_444YpCbCr8BiPlanarVideoRange: OSType](kcvpixelformattype_444ypcbcr8biplanarvideorange.md)
- [var kCVPixelFormatType_64RGBALE: OSType](kcvpixelformattype_64rgbale.md)
- [var kCVPixelFormatType_64RGBA_DownscaledProResRAW: OSType](kcvpixelformattype_64rgba_downscaledproresraw.md)
- [var kCVPixelFormatType_OneComponent10: OSType](kcvpixelformattype_onecomponent10.md)
- [var kCVPixelFormatType_OneComponent12: OSType](kcvpixelformattype_onecomponent12.md)
- [var kCVPixelFormatType_OneComponent16: OSType](kcvpixelformattype_onecomponent16.md)
- [var kCVPixelFormatType_TwoComponent16: OSType](kcvpixelformattype_twocomponent16.md)

## See Also

- [Pixel Format Description Keys](pixel-format-description-keys.md)
  The attributes of a pixel format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/pixel-format-identifiers)*