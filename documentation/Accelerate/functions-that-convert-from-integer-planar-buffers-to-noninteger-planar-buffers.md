# Functions that convert from integer planar buffers to noninteger planar buffers

**Framework**: Accelerate

Convert planar integer image data to fixed- and floating-point format.

## Topics

### Converting from 8-bit buffers
- [func vImageConvert_8to16Q12(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimageconvert_8to16q12(_:_:_:).md)
  Converts an 8-bit planar buffer to a fixed-point 16-bit planar buffer.
- [func vImageConvert_Planar8toPlanar16F(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimageconvert_planar8toplanar16f(_:_:_:).md)
  Converts an 8-bit planar buffer to a floating-point 16-bit planar buffer.
- [func vImageConvert_Planar8toPlanarF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, Pixel_F, Pixel_F, vImage_Flags) -> vImage_Error](vimageconvert_planar8toplanarf(_:_:_:_:_:).md)
  Converts an 8-bit planar buffer to a floating-point 32-bit planar buffer.
### Converting from signed 16-bit-per-channel buffers
- [func vImageConvert_16SToF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, Float, Float, vImage_Flags) -> vImage_Error](vimageconvert_16stof(_:_:_:_:_:).md)
  Converts a signed 16-bit planar buffer to a floating-point 32-bit planar buffer.
### Converting from unsigned 16-bit-per-channel buffers
- [func vImageConvert_16Uto16F(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimageconvert_16uto16f(_:_:_:).md)
  Converts an unsigned 16-bit planar buffer to a floating-point 16-bit planar buffer.
- [func vImageConvert_16Uto16Q12(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimageconvert_16uto16q12(_:_:_:).md)
  Converts an unsigned 16-bit planar buffer to a fixed-point 16-bit planar buffer.
- [func vImageConvert_16UToF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, Float, Float, vImage_Flags) -> vImage_Error](vimageconvert_16utof(_:_:_:_:_:).md)
  Converts an unsigned 16-bit planar buffer to a floating-point 32-bit planar buffer.

## See Also

- [Functions that convert between integer planar buffers](functions-that-convert-between-integer-planar-buffers.md)
  Convert the bit depths of planar integer image data.
- [Functions that convert between integer interleaved buffers](functions-that-convert-between-integer-interleaved-buffers.md)
  Convert the bit depths of interleaved integer image data.
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

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/functions-that-convert-from-integer-planar-buffers-to-noninteger-planar-buffers)*