# Functions that add an alpha channel to three-channel buffers

**Framework**: Accelerate

Add a constant alpha value or planar alpha buffer to an RGB image.

## Topics

### Conversion from 8-bit-per-channel, 3-channel interleaved buffers
- [func vImageConvert_RGB888toARGB8888(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>!, Pixel_8, UnsafePointer<vImage_Buffer>, Bool, vImage_Flags) -> vImage_Error](vimageconvert_rgb888toargb8888(_:_:_:_:_:_:).md)
  Combines an 8-bit-per-channel, 3-channel RGB buffer and either an 8-bit alpha buffer or constant alpha value to produce an ARGB result.
- [func vImageConvert_RGB888toBGRA8888(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>!, Pixel_8, UnsafePointer<vImage_Buffer>, Bool, vImage_Flags) -> vImage_Error](vimageconvert_rgb888tobgra8888(_:_:_:_:_:_:).md)
  Combines an 8-bit-per-channel, 3-channel RGB buffer and either an 8-bit alpha buffer or constant alpha value to produce a BGRA result.
- [func vImageConvert_RGB888toRGBA8888(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>!, Pixel_8, UnsafePointer<vImage_Buffer>, Bool, vImage_Flags) -> vImage_Error](vimageconvert_rgb888torgba8888(_:_:_:_:_:_:).md)
  Combines an 8-bit-per-channel, 3-channel RGB buffer and either an 8-bit alpha buffer or constant alpha value to produce an RGBA result.
### Conversion from unsigned 16-bit-per-channel, 3-channel interleaved buffers
- [func vImageConvert_RGB16UToARGB8888(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<UInt8>, UInt8, UnsafePointer<UInt8>, vImage_Flags) -> vImage_Error](vimageconvert_rgb16utoargb8888(_:_:_:_:_:_:).md)
  Converts an unsigned 16-bit-per-channel, 3-channel interleaved buffer to an 8-bit-per-channel, 4-channel interleaved buffer using permutation.
- [func vImageConvert_RGB16UtoARGB16U(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>!, Pixel_16U, UnsafePointer<vImage_Buffer>, Bool, vImage_Flags) -> vImage_Error](vimageconvert_rgb16utoargb16u(_:_:_:_:_:_:).md)
  Combines an unsigned 16-bit-per-channel, 3-channel RGB buffer and either an unsigned 16-bit alpha buffer or constant alpha value to produce an ARGB result.
- [func vImageConvert_RGB16UtoBGRA16U(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>!, Pixel_16U, UnsafePointer<vImage_Buffer>, Bool, vImage_Flags) -> vImage_Error](vimageconvert_rgb16utobgra16u(_:_:_:_:_:_:).md)
  Combines an unsigned 16-bit-per-channel, 3-channel RGB buffer and either an unsigned 16-bit alpha buffer or constant alpha value to produce a BGRA result.
- [func vImageConvert_RGB16UtoRGBA16U(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>!, Pixel_16U, UnsafePointer<vImage_Buffer>, Bool, vImage_Flags) -> vImage_Error](vimageconvert_rgb16utorgba16u(_:_:_:_:_:_:).md)
  Combines an unsigned 16-bit-per-channel, 3-channel RGB buffer and either an unsigned 16-bit alpha buffer or constant alpha value to produce an RGBA result.
### Conversion from RGB565 16-bit-per-channel, 3-channel interleaved buffers
- [func vImageConvert_RGB565toARGB8888(Pixel_8, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimageconvert_rgb565toargb8888(_:_:_:_:).md)
  Combines an RGB565 3-channel RGB buffer and a constant alpha value to produce an 8-bit-per-channel, 4-channel ARGB buffer.
- [func vImageConvert_RGB565toBGRA8888(Pixel_8, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimageconvert_rgb565tobgra8888(_:_:_:_:).md)
  Combines an RGB565 3-channel RGB buffer and a constant alpha value to produce an 8-bit-per-channel, 4-channel BGRA buffer.
- [func vImageConvert_RGB565toRGBA8888(Pixel_8, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimageconvert_rgb565torgba8888(_:_:_:_:).md)
  Combines an RGB565 3-channel RGB buffer and a constant alpha value to produce an 8-bit-per-channel, 4-channel RGBA buffer.
- [func vImageConvert_RGB565toARGB1555(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, Int32, vImage_Flags) -> vImage_Error](vimageconvert_rgb565toargb1555(_:_:_:_:).md)
  Combines an RGB565 3-channel RGB buffer and a constant alpha value to produce a 4-channel ARGB1555 buffer.
- [func vImageConvert_RGB565toRGBA5551(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, Int32, vImage_Flags) -> vImage_Error](vimageconvert_rgb565torgba5551(_:_:_:_:).md)
  Combines an RGB565 3-channel RGB buffer and a constant alpha value to produce a 4-channel RGBA5551 buffer.
### Conversion from 32-bit-per-channel, 3-channel interleaved buffers
- [func vImageConvert_RGBFFFtoARGBFFFF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>!, Pixel_F, UnsafePointer<vImage_Buffer>, Bool, vImage_Flags) -> vImage_Error](vimageconvert_rgbffftoargbffff(_:_:_:_:_:_:).md)
  Combines a floating-point 32-bit-per-channel, 3-channel RGB buffer and either an 32-bit alpha buffer or constant alpha value to produce an ARGB result.
- [func vImageConvert_RGBFFFtoBGRAFFFF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>!, Pixel_F, UnsafePointer<vImage_Buffer>, Bool, vImage_Flags) -> vImage_Error](vimageconvert_rgbffftobgraffff(_:_:_:_:_:_:).md)
  Combines a floating-point 32-bit-per-channel, 3-channel RGB buffer and either an 32-bit alpha buffer or constant alpha value to produce a BGRA result.
- [func vImageConvert_RGBFFFtoRGBAFFFF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>!, Pixel_F, UnsafePointer<vImage_Buffer>, Bool, vImage_Flags) -> vImage_Error](vimageconvert_rgbffftorgbaffff(_:_:_:_:_:_:).md)
  Combines a floating-point 32-bit-per-channel, 3-channel RGB buffer and either an 32-bit alpha buffer or constant alpha value to produce an RGBA result.

## See Also

- [Functions that remove an alpha channel from four-channel buffers](functions-that-remove-an-alpha-channel-from-four-channel-buffers.md)
  Remove the alpha channel from an RGBA or ARGB buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/functions-that-add-an-alpha-channel-to-three-channel-buffers)*