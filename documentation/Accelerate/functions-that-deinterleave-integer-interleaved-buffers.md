# Functions that deinterleave integer interleaved buffers

**Framework**: Accelerate

Separate integer interleaved buffers into discrete planar buffers.

## Topics

### Deinterleaving unsigned 8-bit interleaved buffers
- [func vImageConvert_ChunkyToPlanar8(UnsafeMutablePointer<UnsafeRawPointer?>, UnsafeMutablePointer<UnsafePointer<vImage_Buffer>?>, UInt32, Int, vImagePixelCount, vImagePixelCount, Int, vImage_Flags) -> vImage_Error](vimageconvert_chunkytoplanar8(_:_:_:_:_:_:_:_:).md)
  Deinterleaves an 8-bit-per-channel interleaved buffer with an arbitrary number of channels into the corresponding number of 8-bit planar buffers.
### Deinterleaving unsigned 8-bit, three-channel interleaved buffers
- [func vImageConvert_RGB888toPlanar8(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimageconvert_rgb888toplanar8(_:_:_:_:_:).md)
  Deinterleaves an 8-bit-per-channel, 3-channel interleaved buffer into three 8-bit planar buffers.
- [func vImageConvert_RGB888toPlanar16Q12(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimageconvert_rgb888toplanar16q12(_:_:_:_:_:).md)
  Deinterleaves an 8-bit-per-channel, 3-channel interleaved buffer into three fixed-point 16-bit planar buffers.
### Deinterleaving unsigned 8-bit, four-channel interleaved buffers
- [func vImageConvert_BGRX8888ToPlanar8(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimageconvert_bgrx8888toplanar8(_:_:_:_:_:).md)
  Deinterleaves an 8-bit-per-channel, 4-channel interleaved buffer into three 8-bit planar buffers and discards the last channel.
- [func vImageConvert_XRGB8888ToPlanar8(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimageconvert_xrgb8888toplanar8(_:_:_:_:_:).md)
  Deinterleaves an 8-bit-per-channel, 4-channel interleaved buffer into three 8-bit planar buffers and discards the first channel.
- [func vImageConvert_ARGB8888toPlanar8(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimageconvert_argb8888toplanar8(_:_:_:_:_:_:).md)
  Deinterleaves an 8-bit-per-channel, 4-channel interleaved buffer into four 8-bit planar buffers.
- [func vImageConvert_ARGB8888toPlanar16Q12(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimageconvert_argb8888toplanar16q12(_:_:_:_:_:_:).md)
  Deinterleaves an 8-bit-per-channel, 4-channel interleaved buffer into four fixed-point 16-bit planar buffers.
- [func vImageConvert_ARGB8888toPlanarF(UnsafePointer<vImage_Buffer>!, UnsafePointer<vImage_Buffer>!, UnsafePointer<vImage_Buffer>!, UnsafePointer<vImage_Buffer>!, UnsafePointer<vImage_Buffer>!, UnsafePointer<Float>!, UnsafePointer<Float>!, vImage_Flags) -> vImage_Error](vimageconvert_argb8888toplanarf(_:_:_:_:_:_:_:_:).md)
  Deinterleaves an 8-bit-per-channel, 4-channel interleaved buffer into four floating-point 32-bit planar buffers.
### Deinterleaving unsigned 16-bit three-channel interleaved buffers
- [func vImageConvert_RGB16UtoPlanar16U(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimageconvert_rgb16utoplanar16u(_:_:_:_:_:).md)
  Deinterleaves an unsigned 16-bit-per-channel, 3-channel interleaved buffer into three unsigned 16-bit planar buffers.
### Deinterleaving unsigned 16-bit four-channel interleaved buffers
- [func vImageConvert_ARGB16UtoPlanar16U(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimageconvert_argb16utoplanar16u(_:_:_:_:_:_:).md)
  Deinterleaves an unsigned 16-bit-per-channel, 4-channel interleaved buffer into four unsigned 16-bit planar buffers.
### Deinterleaving RGB565 16-bit three-channel interleaved buffers
- [func vImageConvert_RGB565toPlanar8(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimageconvert_rgb565toplanar8(_:_:_:_:_:).md)
  Deinterleaves an RGB565 3-channel interleaved buffer into three 8-bit planar buffers.
### Deinterleaving ARGB1555 16-bit four-channel interleaved buffers
- [func vImageConvert_ARGB1555toPlanar8(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimageconvert_argb1555toplanar8(_:_:_:_:_:_:).md)
  Deinterleaves an ARGB1555 4-channel interleaved buffer into four 8-bit planar buffers.

## See Also

- [Functions that interleave integer planar buffers](functions-that-interleave-integer-planar-buffers.md)
  Combine discrete integer planar buffers into an interleaved buffer.
- [Functions that interleave noninteger planar buffers](functions-that-interleave-noninteger-planar-buffers.md)
  Combine discrete fixed- and floating-point planar buffers into an interleaved buffer.
- [Functions that deinterleave noninteger interleaved buffers](functions-that-deinterleave-noninteger-interleaved-buffers.md)
  Separate fixed- and floating-point interleaved buffers into discrete planar buffers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/functions-that-deinterleave-integer-interleaved-buffers)*