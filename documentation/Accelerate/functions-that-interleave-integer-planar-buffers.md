# Functions that interleave integer planar buffers

**Framework**: Accelerate

Combine discrete integer planar buffers into an interleaved buffer.

## Topics

### Interleaving unsigned 8-bit planar buffers
- [func vImageConvert_PlanarToChunky8(UnsafeMutablePointer<UnsafePointer<vImage_Buffer>?>, UnsafeMutablePointer<UnsafeMutableRawPointer?>, UInt32, Int, vImagePixelCount, vImagePixelCount, Int, vImage_Flags) -> vImage_Error](vimageconvert_planartochunky8(_:_:_:_:_:_:_:_:).md)
  Interleaves the specifed number of 8-bit planar buffers into an 8-bit-per-channel interleaved buffer.
### Interleaving three unsigned 8-bit planar buffers
- [func vImageConvert_Planar8toRGB565(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimageconvert_planar8torgb565(_:_:_:_:_:).md)
  Interleaves three 8-bit planar buffers into an RGB565 3-channel interleaved buffer.
- [func vImageConvert_Planar8toRGB888(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimageconvert_planar8torgb888(_:_:_:_:_:).md)
  Interleaves three 8-bit planar buffers into an 8-bit-per-channel, 3-channel interleaved buffer.
- [func vImageConvert_Planar8ToXRGB8888(Pixel_8, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimageconvert_planar8toxrgb8888(_:_:_:_:_:_:).md)
  Interleaves three 8-bit planar buffers into an 8-bit-per-channel, 4-channel interleaved XRGB buffer with the specified constant alpha value.
- [vImageConvert_Planar8ToRGBX8888](vimageconvert_planar8torgbx8888.md)
  Interleaves three 8-bit planar buffers into an 8-bit-per-channel, 4-channel interleaved RGBX buffer with the specified constant alpha value.
- [func vImageConvert_Planar8ToBGRX8888(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, Pixel_8, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimageconvert_planar8tobgrx8888(_:_:_:_:_:_:).md)
  Interleaves three 8-bit planar buffers into an 8-bit-per-channel, 4-channel interleaved BGRX buffer with the specified constant alpha value.
- [func vImageConvert_Planar8ToXRGBFFFF(Pixel_F, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<Float>!, UnsafePointer<Float>!, vImage_Flags) -> vImage_Error](vimageconvert_planar8toxrgbffff(_:_:_:_:_:_:_:_:).md)
  Interleaves three 8-bit planar buffers into a floating-point 32-bit-per-channel, 4-channel interleaved XRGB buffer with the specified constant alpha value.
- [func vImageConvert_Planar8ToBGRXFFFF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, Pixel_F, UnsafePointer<vImage_Buffer>, UnsafePointer<Float>!, UnsafePointer<Float>!, vImage_Flags) -> vImage_Error](vimageconvert_planar8tobgrxffff(_:_:_:_:_:_:_:_:).md)
  Interleaves three 8-bit planar buffers into a floating-point 32-bit-per-channel, 4-channel interleaved BGRX buffer with the specified constant alpha value.
- [vImageConvert_Planar8ToRGBXFFFF](vimageconvert_planar8torgbxffff.md)
  Interleaves three 8-bit planar buffers into a floating-point 32-bit-per-channel, 4-channel interleaved RGBX buffer with the specified constant alpha value.
### Interleaving four unsigned 8-bit planar buffers
- [func vImageConvert_Planar8toARGB1555(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimageconvert_planar8toargb1555(_:_:_:_:_:_:).md)
  Interleaves four 8-bit planar buffers into an ARGB1555 4-channel interleaved buffer.
- [func vImageConvert_Planar8toARGB8888(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimageconvert_planar8toargb8888(_:_:_:_:_:_:).md)
  Interleaves four 8-bit planar buffers into an 8-bit-per-channel, 4-channel interleaved buffer.
- [func vImageConvert_Planar8ToARGBFFFF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<Float>!, UnsafePointer<Float>!, vImage_Flags) -> vImage_Error](vimageconvert_planar8toargbffff(_:_:_:_:_:_:_:_:).md)
  Interleaves four 8-bit planar buffers into a floating-point 32-bit-per-channel, 4-channel interleaved ARGB buffer.
### Interleaving three unsigned 16-bit planar buffers
- [func vImageConvert_Planar16UtoRGB16U(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimageconvert_planar16utorgb16u(_:_:_:_:_:).md)
  Interleaves three unsigned 16-bit planar buffers into an unsigned 16-bit-per-channel, 3-channel interleaved buffer.
### Interleaving four unsigned 16-bit planar buffers
- [func vImageConvert_Planar16UtoARGB16U(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimageconvert_planar16utoargb16u(_:_:_:_:_:_:).md)
  Interleaves four unsigned 16-bit planar buffers into an unsigned 16-bit-per-channel, 4-channel interleaved ARGB buffer.

## See Also

- [Functions that interleave noninteger planar buffers](functions-that-interleave-noninteger-planar-buffers.md)
  Combine discrete fixed- and floating-point planar buffers into an interleaved buffer.
- [Functions that deinterleave integer interleaved buffers](functions-that-deinterleave-integer-interleaved-buffers.md)
  Separate integer interleaved buffers into discrete planar buffers.
- [Functions that deinterleave noninteger interleaved buffers](functions-that-deinterleave-noninteger-interleaved-buffers.md)
  Separate fixed- and floating-point interleaved buffers into discrete planar buffers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/functions-that-interleave-integer-planar-buffers)*