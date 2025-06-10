# Functions that convert between integer interleaved buffers

**Framework**: Accelerate

Convert the bit depths of interleaved integer image data.

## Topics

### Converting from 8-bit buffers
- [func vImageConvert_RGB888toRGB565_dithered(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutableRawPointer!, Int32, vImage_Flags) -> vImage_Error](vimageconvert_rgb888torgb565_dithered(_:_:_:_:_:).md)
  Converts an 8-bit-per-channel, 3-channel interleaved buffer to an RGB565 3-channel interleaved buffer using the specified dithering algorithm.
- [func vImageConvert_ARGB8888toARGB1555(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimageconvert_argb8888toargb1555(_:_:_:).md)
  Converts an 8-bit-per-channel, 4-channel interleaved buffer to an ARGB1555 4-channel interleaved buffer.
- [func vImageConvert_ARGB8888toARGB1555_dithered(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutableRawPointer!, Int32, vImage_Flags) -> vImage_Error](vimageconvert_argb8888toargb1555_dithered(_:_:_:_:_:).md)
  Converts an 8-bit-per-channel, 4-channel interleaved buffer to an ARGB1555 4-channel interleaved buffer usng the specified dithering algorithm.
- [func vImageConvert_RGBA8888toRGBA5551(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimageconvert_rgba8888torgba5551(_:_:_:).md)
  Converts an 8-bit-per-channel, 4-channel interleaved buffer to an RGBA5551 4-channel interleaved buffer.
- [func vImageConvert_RGBA8888toRGBA5551_dithered(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutableRawPointer!, Int32, vImage_Flags) -> vImage_Error](vimageconvert_rgba8888torgba5551_dithered(_:_:_:_:_:).md)
  Converts an 8-bit-per-channel, 4-channel interleaved buffer to an RGBA5551 4-channel interleaved buffer usng the specified dithering algorithm.
- [func vImageConvert_ARGB8888ToARGB16U(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<UInt8>, UInt8, UnsafePointer<UInt16>, vImage_Flags) -> vImage_Error](vimageconvert_argb8888toargb16u(_:_:_:_:_:_:).md)
  Converts an 8-bit-per-channel, 4-channel interleaved buffer to an unsigned 16-bit-per-channel, 4-channel buffer with permutation.
### Converting from unsigned 16-bit-per-channel buffers
- [func vImageConvert_RGB16UtoRGB888_dithered(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, Int32, vImage_Flags) -> vImage_Error](vimageconvert_rgb16utorgb888_dithered(_:_:_:_:).md)
  Converts an unsigned 16-bit-per-channel, 3-channel interleaved buffer to an 8-bit-per-channel, 3-channel interleaved buffer using the specified dithering algorithm.
- [func vImageConvert_ARGB16UToARGB8888(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<UInt8>, UInt8, UnsafePointer<UInt8>, vImage_Flags) -> vImage_Error](vimageconvert_argb16utoargb8888(_:_:_:_:_:_:).md)
  Converts an unsigned 16-bit-per-channel, 4-channel interleaved buffer to an 8-bit-per-channel, 4-channel interleaved buffer.
- [func vImageConvert_ARGB16UtoARGB8888_dithered(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, Int32, UnsafePointer<UInt8>!, vImage_Flags) -> vImage_Error](vimageconvert_argb16utoargb8888_dithered(_:_:_:_:_:).md)
  Converts an unsigned 16-bit-per-channel, 4-channel interleaved buffer to an 8-bit-per-channel, 4-channel interleaved buffer using the specified dithering algorithm.
### Converting from RGB565 16-bit-per-channel buffers
- [func vImageConvert_RGB565toRGB888(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimageconvert_rgb565torgb888(_:_:_:).md)
  Converts an RGB565 3-channel interleaved buffer to an 8-bit-per-channel, 3-channel interleaved buffer.
### Converting from ARGB1555 16-bit-per-channel buffers
- [func vImageConvert_RGBA5551toRGBA8888(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimageconvert_rgba5551torgba8888(_:_:_:).md)
  Converts an RGB5651 4-channel interleaved buffer to an 8-bit-per-channel, 4-channel interleaved buffer.
- [func vImageConvert_ARGB1555toARGB8888(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimageconvert_argb1555toargb8888(_:_:_:).md)
  Converts an ARGB1555 4-channel interleaved buffer to an 8-bit-per-channel, 4-channel interleaved buffer.

## See Also

- [Functions that convert between integer planar buffers](functions-that-convert-between-integer-planar-buffers.md)
  Convert the bit depths of planar integer image data.
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
- [Functions that convert from noninteger interleaved buffers to integer interleaved buffers](functions-that-convert-from-noninteger-interleaved-buffers-to-integer-interleaved-buffers.md)
  Convert interleaved fixed- and floating-point image data to integer format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/functions-that-convert-between-integer-interleaved-buffers)*