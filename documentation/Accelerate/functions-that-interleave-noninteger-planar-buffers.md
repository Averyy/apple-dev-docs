# Functions that interleave noninteger planar buffers

**Framework**: Accelerate

Combine discrete fixed- and floating-point planar buffers into an interleaved buffer.

## Topics

### Interleaving three fixed-point 16-bit planar buffers
- [func vImageConvert_Planar16Q12toRGB888(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimageconvert_planar16q12torgb888(_:_:_:_:_:).md)
  Interleaves three fixed-point 16-bit planar buffers into an 8-bit-per-channel, 3-channel interleaved buffer.
- [func vImageConvert_Planar16Q12toRGB16F(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimageconvert_planar16q12torgb16f(_:_:_:_:_:).md)
  Interleaves three fixed-point 16-bit planar buffers into a floating-point 32-bit-per-channel, 3-channel interleaved buffer.
### Interleaving four fixed-point 16-bit planar buffers
- [func vImageConvert_Planar16Q12toARGB8888(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimageconvert_planar16q12toargb8888(_:_:_:_:_:_:).md)
  Interleaves four fixed-point 16-bit planar buffers into an 8-bit-per-channel, 4-channel interleaved buffer.
- [func vImageConvert_Planar16Q12toARGB16F(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimageconvert_planar16q12toargb16f(_:_:_:_:_:_:).md)
  Interleaves four fixed-point 16-bit planar buffers into a floating-point 32-bit-per-channel, 4-channel interleaved buffer.
### Interleaving floating-point 32-bit planar buffers
- [func vImageConvert_PlanarToChunkyF(UnsafeMutablePointer<UnsafePointer<vImage_Buffer>?>, UnsafeMutablePointer<UnsafeMutableRawPointer?>, UInt32, Int, vImagePixelCount, vImagePixelCount, Int, vImage_Flags) -> vImage_Error](vimageconvert_planartochunkyf(_:_:_:_:_:_:_:_:).md)
  Interleaves the specifed number of floating-point 32-bit planar buffers into a floating-point 32 -bit-per-channel interleaved buffer.
### Interleaving three floating-point 32-bit planar buffers
- [func vImageConvert_PlanarFToBGRX8888(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, Pixel_8, UnsafePointer<vImage_Buffer>, UnsafePointer<Float>, UnsafePointer<Float>, vImage_Flags) -> vImage_Error](vimageconvert_planarftobgrx8888(_:_:_:_:_:_:_:_:).md)
  Interleaves three 32-bit planar buffers into an 8-bit-per-channel, 4-channel interleaved BGRX buffer with the specified constant alpha value.
- [vImageConvert_PlanarFToRGBX8888](vimageconvert_planarftorgbx8888.md)
  Interleaves three 32-bit planar buffers into an 8-bit-per-channel, 4-channel interleaved RGBX buffer with the specified constant alpha value.
- [func vImageConvert_PlanarFToXRGB8888(Pixel_8, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<Float>, UnsafePointer<Float>, vImage_Flags) -> vImage_Error](vimageconvert_planarftoxrgb8888(_:_:_:_:_:_:_:_:).md)
  Interleaves three 32-bit planar buffers into an 8-bit-per-channel, 4-channel interleaved XRGB buffer with the specified constant alpha value.
- [func vImageConvert_PlanarFtoRGBFFF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimageconvert_planarftorgbfff(_:_:_:_:_:).md)
  Interleaves three floating-point 32-bit planar buffers into a floating-point 32-bit-per-channel, 3-channel interleaved buffer.
- [vImageConvert_PlanarFToRGBXFFFF](vimageconvert_planarftorgbxffff.md)
  Interleaves three 32-bit planar buffers into a floating-point 32-bit-per-channel, 4-channel interleaved RGBX buffer with the specified constant alpha value.
- [func vImageConvert_PlanarFToXRGBFFFF(Pixel_F, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimageconvert_planarftoxrgbffff(_:_:_:_:_:_:).md)
  Interleaves three 32-bit planar buffers into a floating-point 32-bit-per-channel, 4-channel interleaved XRGB buffer with the specified constant alpha value.
### Interleaving four floating-point 32-bit planar buffers
- [func vImageConvert_PlanarFToARGB8888(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<Float>, UnsafePointer<Float>, vImage_Flags) -> vImage_Error](vimageconvert_planarftoargb8888(_:_:_:_:_:_:_:_:).md)
  Interleaves four 32-bit planar buffers into an 8-bit-per-channel, 4-channel interleaved buffer.
- [func vImageConvert_PlanarFtoARGBFFFF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimageconvert_planarftoargbffff(_:_:_:_:_:_:).md)
  Interleaves four floating-point 32-bit planar buffers into a floating-point 32-bit-per-channel, 4-channel ARGB interleaved buffer.
- [func vImageConvert_PlanarFToBGRXFFFF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, Pixel_F, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimageconvert_planarftobgrxffff(_:_:_:_:_:_:).md)
  Interleaves four floating-point 32-bit planar buffers into a floating-point 32-bit-per-channel, 4-channel BGRXARGB interleaved buffer.

## See Also

- [Functions that interleave integer planar buffers](functions-that-interleave-integer-planar-buffers.md)
  Combine discrete integer planar buffers into an interleaved buffer.
- [Functions that deinterleave integer interleaved buffers](functions-that-deinterleave-integer-interleaved-buffers.md)
  Separate integer interleaved buffers into discrete planar buffers.
- [Functions that deinterleave noninteger interleaved buffers](functions-that-deinterleave-noninteger-interleaved-buffers.md)
  Separate fixed- and floating-point interleaved buffers into discrete planar buffers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/functions-that-interleave-noninteger-planar-buffers)*