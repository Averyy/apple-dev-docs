# Functions that convert from noninteger interleaved buffers to integer interleaved buffers

**Framework**: Accelerate

Convert interleaved fixed- and floating-point image data to integer format.

## Topics

### Converting from floating-point 32-bit-per-channel buffers
- [func vImageConvert_RGBFFFtoRGB888_dithered(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<Pixel_F>, UnsafePointer<Pixel_F>, Int32, vImage_Flags) -> vImage_Error](vimageconvert_rgbffftorgb888_dithered(_:_:_:_:_:_:).md)
  Converts a floating-point 32-bit-per-channel, 3-channel buffer to an 8-bit-per-channel, 3-channel buffer using the specified dithering algorithm.
- [func vImageConvert_ARGBFFFFtoARGB8888_dithered(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<Float>, UnsafePointer<Float>, Int32, UnsafePointer<UInt8>!, vImage_Flags) -> vImage_Error](vimageconvert_argbfffftoargb8888_dithered(_:_:_:_:_:_:_:).md)
  Converts a floating-point 32-bit-per-channel, 4-channel buffer to an 8-bit-per-channel, 4-channel buffer using the specified dithering algorithm.
### Converting from XRGB2101010 32-bit buffers
- [func vImageConvert_ARGB2101010ToARGB8888(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, Int32, Int32, UnsafePointer<UInt8>!, vImage_Flags) -> vImage_Error](vimageconvert_argb2101010toargb8888(_:_:_:_:_:_:).md)
  Converts an ARGB2101010 32-bit, 4-channel interleaved buffer to an 8-bit-per-channel, 4-channel interleaved buffer with permutation.
- [func vImageConvert_XRGB2101010ToARGB8888(UnsafePointer<vImage_Buffer>, Pixel_8, UnsafePointer<vImage_Buffer>, Int32, Int32, UnsafePointer<UInt8>!, vImage_Flags) -> vImage_Error](vimageconvert_xrgb2101010toargb8888(_:_:_:_:_:_:_:).md)
  Converts an XRGB2101010 32-bit, 4-channel interleaved buffer to an 8-bit-per-channel, 4-channel interleaved buffer with permutation.
- [func vImageConvert_ARGB2101010ToARGB16U(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, Int32, Int32, UnsafePointer<UInt8>!, vImage_Flags) -> vImage_Error](vimageconvert_argb2101010toargb16u(_:_:_:_:_:_:).md)
  Converts an ARGB2101010 32-bit, 4-channel interleaved buffer to an unsigned 16-bit-per-channel, 4-channel interleaved buffer with permutation.
- [func vImageConvert_XRGB2101010ToARGB16U(UnsafePointer<vImage_Buffer>, UInt16, UnsafePointer<vImage_Buffer>, Int32, Int32, UnsafePointer<UInt8>!, vImage_Flags) -> vImage_Error](vimageconvert_xrgb2101010toargb16u(_:_:_:_:_:_:_:).md)
  Converts an XRGB2101010 32-bit, 4-channel interleaved buffer to an unsigned 16-bit-per-channel, 4-channel interleaved buffer with permutation.
### Converting from RGBX1010102 32-bit buffers
- [func vImageConvert_RGBA1010102ToARGB8888(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, Int32, Int32, UnsafePointer<UInt8>!, vImage_Flags) -> vImage_Error](vimageconvert_rgba1010102toargb8888(_:_:_:_:_:_:).md)
  Converts an RGBA1010102 32-bit, 4-channel interleaved buffer to an 8-bit-per-channel, 4-channel interleaved buffer with permutation.
- [func vImageConvert_RGBA1010102ToARGB16U(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, Int32, Int32, UnsafePointer<UInt8>!, vImage_Flags) -> vImage_Error](vimageconvert_rgba1010102toargb16u(_:_:_:_:_:_:).md)
  Converts an RGBA1010102 32-bit, 4-channel interleaved buffer to an unsigned 16-bit-per-channel, 4-channel interleaved buffer with permutation.

## See Also

- [Functions that convert between integer planar buffers](functions-that-convert-between-integer-planar-buffers.md)
  Convert the bit depths of planar integer image data.
- [Functions that convert between integer interleaved buffers](functions-that-convert-between-integer-interleaved-buffers.md)
  Convert the bit depths of interleaved integer image data.
- [Functions that convert from integer planar buffers to noninteger planar buffers](functions-that-convert-from-integer-planar-buffers-to-noninteger-planar-buffers.md)
  Convert planar integer image data to fixed- and floating-point format.
- [Functions that convert from integer interleaved buffers to noninteger interleaved buffers](functions-that-convert-from-integer-interleaved-buffers-to-noninteger-interleaved-buffers.md)
  Convert interleaved integer image data to fixed- and floating-point format.
- [Functions that convert between noninteger planar buffers](functions-that-convert-between-noninteger-planar-buffers.md)
  Convert the bit depths and formats of planar fixed- and floating-point image data.
- [Functions that convert between noninteger interleaved buffers](functions-that-convert-between-noninteger-interleaved-buffers.md)
  Convert the bit depths and formats of interleaved fixed- and floating-point image data.
- [Functions that convert from noninteger planar buffers to integer planar buffers](functions-that-convert-from-noninteger-planar-buffers-to-integer-planar-buffers.md)
  Convert planar fixed- and floating-point image data to integer format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/functions-that-convert-from-noninteger-interleaved-buffers-to-integer-interleaved-buffers)*