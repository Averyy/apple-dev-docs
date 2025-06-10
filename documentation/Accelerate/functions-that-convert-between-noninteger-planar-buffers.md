# Functions that convert between noninteger planar buffers

**Framework**: Accelerate

Convert the bit depths and formats of planar fixed- and floating-point image data.

## Topics

### Converting from floating-point 16-bit-per-channel buffers
- [func vImageConvert_16Fto16Q12(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimageconvert_16fto16q12(_:_:_:).md)
  Converts a floating-point 16-bit planar buffer to a fixed-point 16-bit planar buffer.
- [func vImageConvert_Planar16FtoPlanarF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimageconvert_planar16ftoplanarf(_:_:_:).md)
  Converts a floating-point 16-bit planar buffer to a floating-point 32-bit planar buffer.
### Converting from fixed-point 16-bit-per-channel buffers
- [func vImageConvert_16Q12to16F(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimageconvert_16q12to16f(_:_:_:).md)
  Converts a fixed-point 16-bit planar buffer to a floating-point 16-bit planar buffer.
- [func vImageConvert_16Q12toF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimageconvert_16q12tof(_:_:_:).md)
  Converts a fixed-point 16-bit planar buffer to a floating-point 32-bit planar buffer.
### Converting from floating-point 32-bit-per-channel buffers
- [func vImageConvert_PlanarFtoPlanar16F(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimageconvert_planarftoplanar16f(_:_:_:).md)
  Converts a floating-point 32-bit planar buffer to a floating-point 16-bit planar buffer.
- [func vImageConvert_Fto16Q12(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimageconvert_fto16q12(_:_:_:).md)
  Converts a floating-point 32-bit planar buffer to a fixed-point 16-bit planar buffer.

## See Also

- [Functions that convert between integer planar buffers](functions-that-convert-between-integer-planar-buffers.md)
  Convert the bit depths of planar integer image data.
- [Functions that convert between integer interleaved buffers](functions-that-convert-between-integer-interleaved-buffers.md)
  Convert the bit depths of interleaved integer image data.
- [Functions that convert from integer planar buffers to noninteger planar buffers](functions-that-convert-from-integer-planar-buffers-to-noninteger-planar-buffers.md)
  Convert planar integer image data to fixed- and floating-point format.
- [Functions that convert from integer interleaved buffers to noninteger interleaved buffers](functions-that-convert-from-integer-interleaved-buffers-to-noninteger-interleaved-buffers.md)
  Convert interleaved integer image data to fixed- and floating-point format.
- [Functions that convert between noninteger interleaved buffers](functions-that-convert-between-noninteger-interleaved-buffers.md)
  Convert the bit depths and formats of interleaved fixed- and floating-point image data.
- [Functions that convert from noninteger planar buffers to integer planar buffers](functions-that-convert-from-noninteger-planar-buffers-to-integer-planar-buffers.md)
  Convert planar fixed- and floating-point image data to integer format.
- [Functions that convert from noninteger interleaved buffers to integer interleaved buffers](functions-that-convert-from-noninteger-interleaved-buffers-to-integer-interleaved-buffers.md)
  Convert interleaved fixed- and floating-point image data to integer format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/functions-that-convert-between-noninteger-planar-buffers)*