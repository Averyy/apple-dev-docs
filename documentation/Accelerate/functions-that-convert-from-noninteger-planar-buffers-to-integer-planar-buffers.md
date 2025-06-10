# Functions that convert from noninteger planar buffers to integer planar buffers

**Framework**: Accelerate

Convert planar fixed- and floating-point image data to integer format.

## Topics

### Converting from fixed-point 16-bit-per-channel buffers
- [func vImageConvert_16Q12to8(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimageconvert_16q12to8(_:_:_:).md)
  Converts a fixed-point 16-bit planar buffer to an 8-bit planar buffer.
- [func vImageConvert_16Q12to16U(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimageconvert_16q12to16u(_:_:_:).md)
  Converts a fixed-point 16-bit planar buffer to an unsigned 16-bit planar buffer.
### Converting from floating-point 16-bit-per-channel buffers
- [func vImageConvert_Planar16FtoPlanar8(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimageconvert_planar16ftoplanar8(_:_:_:).md)
  Converts a floaing-point 16-bit planar buffer to an 8-bit planar buffer.
- [func vImageConvert_16Fto16U(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimageconvert_16fto16u(_:_:_:).md)
  Converts a floating-point 16-bit planar buffer to an unsigned 16-bit planar buffer.
### Converting from floating-point 32-bit-per-channel buffers
- [func vImageConvert_PlanarFtoPlanar8(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, Pixel_F, Pixel_F, vImage_Flags) -> vImage_Error](vimageconvert_planarftoplanar8(_:_:_:_:_:).md)
  Converts a floating-point 32-bit planar buffer to an 8-bit planar buffer.
- [func vImageConvert_PlanarFtoPlanar8_dithered(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, Pixel_F, Pixel_F, Int32, vImage_Flags) -> vImage_Error](vimageconvert_planarftoplanar8_dithered(_:_:_:_:_:_:).md)
  Converts a floating-point 32-bit planar buffer to an 8-bit planar buffer using the specified dithering algorithm.
- [func vImageConvert_FTo16S(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, Float, Float, vImage_Flags) -> vImage_Error](vimageconvert_fto16s(_:_:_:_:_:).md)
  Converts a floating-point 32-bit planar buffer to a signed 16-bit planar buffer.
- [func vImageConvert_FTo16U(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, Float, Float, vImage_Flags) -> vImage_Error](vimageconvert_fto16u(_:_:_:_:_:).md)
  Converts a floating-point 32-bit planar buffer to an unsigned 16-bit planar buffer.

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
- [Functions that convert from noninteger interleaved buffers to integer interleaved buffers](functions-that-convert-from-noninteger-interleaved-buffers-to-integer-interleaved-buffers.md)
  Convert interleaved fixed- and floating-point image data to integer format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/functions-that-convert-from-noninteger-planar-buffers-to-integer-planar-buffers)*