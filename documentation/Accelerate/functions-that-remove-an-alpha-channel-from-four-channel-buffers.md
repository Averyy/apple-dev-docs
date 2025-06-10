# Functions that remove an alpha channel from four-channel buffers

**Framework**: Accelerate

Remove the alpha channel from an RGBA or ARGB buffer.

## Topics

### Conversion from 8-bit-per-channel, 4-channel interleaved buffers
- [func vImageConvert_ARGB8888toRGB888(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimageconvert_argb8888torgb888(_:_:_:).md)
  Removes the alpha channel from an 8-bit-per-channel ARGB buffer to produce an 8-bit-per-channel RGB result.
- [func vImageConvert_RGBA8888toRGB888(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimageconvert_rgba8888torgb888(_:_:_:).md)
  Removes the alpha channel from an 8-bit-per-channel RGBA buffer to produce an 8-bit-per-channel RGB result.
- [func vImageConvert_BGRA8888toRGB888(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimageconvert_bgra8888torgb888(_:_:_:).md)
  Removes the alpha channel from an 8-bit-per-channel BGRA buffer to produce an 8-bit-per-channel RGB result.
- [vImageConvert_BGRA8888toBGR888](vimageconvert_bgra8888tobgr888.md)
  Removes the alpha channel from an 8-bit-per-channel BGRA buffer to produce an 8-bit-per-channel BGR result.
- [vImageConvert_RGBA8888toBGR888](vimageconvert_rgba8888tobgr888.md)
  Removes the alpha channel from an 8-bit-per-channel RGBA buffer to produce an 8-bit-per-channel BGR result.
- [func vImageConvert_ARGB8888toRGB565(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimageconvert_argb8888torgb565(_:_:_:).md)
  Removes the alpha channel from an 8-bit-per-channel ARGB buffer to produce an RGB565 result.
- [func vImageConvert_ARGB8888toRGB565_dithered(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutableRawPointer!, Int32, vImage_Flags) -> vImage_Error](vimageconvert_argb8888torgb565_dithered(_:_:_:_:_:).md)
  Removes the alpha channel from an 8-bit-per-channel ARGB buffer using the specified dithering algorithm to produce an RGB565 result.
- [func vImageConvert_BGRA8888toRGB565(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimageconvert_bgra8888torgb565(_:_:_:).md)
  Removes the alpha channel from an 8-bit-per-channel RGBA buffer to produce an RGB565 result.
- [func vImageConvert_BGRA8888toRGB565_dithered(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutableRawPointer!, Int32, vImage_Flags) -> vImage_Error](vimageconvert_bgra8888torgb565_dithered(_:_:_:_:_:).md)
  Removes the alpha channel from an 8-bit-per-channel BGRA buffer using the specified dithering algorithm to produce an RGB565 result.
- [func vImageConvert_RGBA8888toRGB565_dithered(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutableRawPointer!, Int32, vImage_Flags) -> vImage_Error](vimageconvert_rgba8888torgb565_dithered(_:_:_:_:_:).md)
  Removes the alpha channel from an 8-bit-per-channel RGBA buffer using the specified dithering algorithm to produce an RGB565 result.
- [func vImageConvert_RGBA8888toRGB565(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimageconvert_rgba8888torgb565(_:_:_:).md)
  Removes the alpha channel from an 8-bit-per-channel RGBA buffer to produce an RGB565 result.
- [func vImageConvert_ARGB8888ToRGB16U(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<UInt8>, UInt8, UnsafePointer<Pixel_16U>, vImage_Flags) -> vImage_Error](vimageconvert_argb8888torgb16u(_:_:_:_:_:_:).md)
  Removes the alpha channel from an 8-bit-per-channel ARGB buffer to produce an unsigned 16-bit-per-channel RGB result.
### Conversion from unsigned 16-bit-per-channel, 4-channel interleaved buffers
- [func vImageConvert_ARGB16UtoRGB16U(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimageconvert_argb16utorgb16u(_:_:_:).md)
  Removes the alpha channel from an unsigned 16-bit-per-channel ARGB buffer to produce an unsigned 16-bit-per-channel RGB result.
- [func vImageConvert_BGRA16UtoRGB16U(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimageconvert_bgra16utorgb16u(_:_:_:).md)
  Removes the alpha channel from an unsigned 16-bit-per-channel BGRA buffer to produce an unsigned 16-bit-per-channel RGB result.
- [func vImageConvert_RGBA16UtoRGB16U(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimageconvert_rgba16utorgb16u(_:_:_:).md)
  Removes the alpha channel from an unsigned 16-bit-per-channel RGBA buffer to produce an unsigned 16-bit-per-channel RGB result.
### Conversion from ARGB1555 16-bit-per-channel, 4-channel interleaved buffers
- [func vImageConvert_ARGB1555toRGB565(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimageconvert_argb1555torgb565(_:_:_:).md)
  Removes the alpha channel from an ARGB1555 buffer to produce an RGB565 result.
- [func vImageConvert_RGBA5551toRGB565(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimageconvert_rgba5551torgb565(_:_:_:).md)
  Removes the alpha channel from an RGBA5551 buffer to produce an RGB565 result.
### Conversion from 32-bit-per-channel, 4-channel interleaved buffers
- [func vImageConvert_ARGBFFFFtoRGBFFF(UnsafePointer<vImage_Buffer>!, UnsafePointer<vImage_Buffer>!, vImage_Flags) -> vImage_Error](vimageconvert_argbfffftorgbfff(_:_:_:).md)
  Removes the alpha channel from a floating-point 32-bit-per-channel ARGB buffer to produce a floating-point 32-bit-per-channel RGB result.
- [func vImageConvert_BGRAFFFFtoRGBFFF(UnsafePointer<vImage_Buffer>!, UnsafePointer<vImage_Buffer>!, vImage_Flags) -> vImage_Error](vimageconvert_bgrafffftorgbfff(_:_:_:).md)
  Removes the alpha channel from a floating-point 32-bit-per-channel BGRA buffer to produce a floating-point 32-bit-per-channel RGB result.
- [func vImageConvert_RGBAFFFFtoRGBFFF(UnsafePointer<vImage_Buffer>!, UnsafePointer<vImage_Buffer>!, vImage_Flags) -> vImage_Error](vimageconvert_rgbafffftorgbfff(_:_:_:).md)
  Removes the alpha channel from a floating-point 32-bit-per-channel RGBA buffer to produce a floating-point 32-bit-per-channel RGB result.

## See Also

- [Functions that add an alpha channel to three-channel buffers](functions-that-add-an-alpha-channel-to-three-channel-buffers.md)
  Add a constant alpha value or planar alpha buffer to an RGB image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/functions-that-remove-an-alpha-channel-from-four-channel-buffers)*