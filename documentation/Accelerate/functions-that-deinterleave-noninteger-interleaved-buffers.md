# Functions that deinterleave noninteger interleaved buffers

**Framework**: Accelerate

Separate fixed- and floating-point interleaved buffers into discrete planar buffers.

## Topics

### Deinterleaving 32-bit interleaved buffers
- [func vImageConvert_ChunkyToPlanarF(UnsafeMutablePointer<UnsafeRawPointer?>, UnsafeMutablePointer<UnsafePointer<vImage_Buffer>?>, UInt32, Int, vImagePixelCount, vImagePixelCount, Int, vImage_Flags) -> vImage_Error](vimageconvert_chunkytoplanarf(_:_:_:_:_:_:_:_:).md)
  Deinterleaves a floating-point 32-bit-per-channel interleaved buffer with an arbitrary number of channels into the corresponding number of 32-bit planar buffers.
### Deinterleaving 32-bit three-channel interleaved buffers
- [func vImageConvert_RGBFFFtoPlanarF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimageconvert_rgbffftoplanarf(_:_:_:_:_:).md)
  Deinterleaves a floating-point 32-bit-per-channel, 3-channel interleaved buffer into three floating-point 32-bit planar buffers.
### Deinterleaving 32-bit four-channel interleaved buffers
- [func vImageConvert_ARGBFFFFtoPlanar8(UnsafePointer<vImage_Buffer>!, UnsafePointer<vImage_Buffer>!, UnsafePointer<vImage_Buffer>!, UnsafePointer<vImage_Buffer>!, UnsafePointer<vImage_Buffer>!, UnsafePointer<Float>!, UnsafePointer<Float>!, vImage_Flags) -> vImage_Error](vimageconvert_argbfffftoplanar8(_:_:_:_:_:_:_:_:).md)
  Deinterleaves a floating-point 32-bit-per-channel, 4-channel interleaved buffer into four 8-bit planar buffers.
- [func vImageConvert_BGRXFFFFToPlanarF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimageconvert_bgrxfffftoplanarf(_:_:_:_:_:).md)
  Deinterleaves a floating-point 32-bit-per-channel, 4-channel interleaved buffer into three floating-point 32-bit planar buffers and discards the last channel.
- [func vImageConvert_XRGBFFFFToPlanarF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimageconvert_xrgbfffftoplanarf(_:_:_:_:_:).md)
  Deinterleaves a floating-point 32-bit-per-channel, 4-channel interleaved buffer into three floating-point 32-bit planar buffers and discards the first channel.
- [func vImageConvert_ARGBFFFFtoPlanarF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimageconvert_argbfffftoplanarf(_:_:_:_:_:_:).md)
  Deinterleaves a floating-point 32-bit-per-channel, 4-channel interleaved buffer into four floating-point 38-bit planar buffers.

## See Also

- [Functions that interleave integer planar buffers](functions-that-interleave-integer-planar-buffers.md)
  Combine discrete integer planar buffers into an interleaved buffer.
- [Functions that interleave noninteger planar buffers](functions-that-interleave-noninteger-planar-buffers.md)
  Combine discrete fixed- and floating-point planar buffers into an interleaved buffer.
- [Functions that deinterleave integer interleaved buffers](functions-that-deinterleave-integer-interleaved-buffers.md)
  Separate integer interleaved buffers into discrete planar buffers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/functions-that-deinterleave-noninteger-interleaved-buffers)*