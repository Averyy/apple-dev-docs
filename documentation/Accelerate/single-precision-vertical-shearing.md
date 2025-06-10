# Single-precision vertical shearing

**Framework**: Accelerate

Apply single-precision vertical shearing to images.

## Topics

### Shearing 8-bit-per-channel buffers
- [func vImageVerticalShear_Planar8(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImagePixelCount, vImagePixelCount, Float, Float, ResamplingFilter!, Pixel_8, vImage_Flags) -> vImage_Error](vimageverticalshear_planar8(_:_:_:_:_:_:_:_:_:).md)
  Performs a single-precision vertical shear on a region of interest within an 8-bit planar image.
- [func vImageVerticalShear_CbCr8(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImagePixelCount, vImagePixelCount, Float, Float, ResamplingFilter!, UnsafePointer<UInt8>!, vImage_Flags) -> vImage_Error](vimageverticalshear_cbcr8(_:_:_:_:_:_:_:_:_:).md)
  Performs a single-precision vertical shear on a region of interest within an 8-bit-per-channel, 2-channel interleaved image.
- [func vImageVerticalShear_ARGB8888(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImagePixelCount, vImagePixelCount, Float, Float, ResamplingFilter!, UnsafePointer<UInt8>!, vImage_Flags) -> vImage_Error](vimageverticalshear_argb8888(_:_:_:_:_:_:_:_:_:).md)
  Performs a single-precision vertical shear on a region of interest within an 8-bit-per-channel, 4-channel interleaved image.
### Shearing 10-bit-per-channel buffers
- [func vImageVerticalShear_XRGB2101010W(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImagePixelCount, vImagePixelCount, Float, Float, ResamplingFilter!, Pixel_32U, vImage_Flags) -> vImage_Error](vimageverticalshear_xrgb2101010w(_:_:_:_:_:_:_:_:_:).md)
  Performs a single-precision vertical shear on a region of interest within a 2-bit alpha, 10-bit RGB interleaved image.
### Shearing 16-bit-per-channel buffers
- [func vImageVerticalShear_Planar16U(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImagePixelCount, vImagePixelCount, Float, Float, ResamplingFilter!, Pixel_16U, vImage_Flags) -> vImage_Error](vimageverticalshear_planar16u(_:_:_:_:_:_:_:_:_:).md)
  Performs a single-precision vertical shear on a region of interest within an unsigned 16-bit planar image.
- [func vImageVerticalShear_Planar16S(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImagePixelCount, vImagePixelCount, Float, Float, ResamplingFilter!, Pixel_16S, vImage_Flags) -> vImage_Error](vimageverticalshear_planar16s(_:_:_:_:_:_:_:_:_:).md)
  Performs a single-precision vertical shear on a region of interest within a signed 16-bit planar image.
- [func vImageVerticalShear_Planar16F(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImagePixelCount, vImagePixelCount, Float, Float, ResamplingFilter!, Pixel_16F, vImage_Flags) -> vImage_Error](vimageverticalshear_planar16f(_:_:_:_:_:_:_:_:_:).md)
  Performs a single-precision vertical shear on a region of interest within a floating-point 16-bit planar image.
- [func vImageVerticalShear_CbCr16U(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImagePixelCount, vImagePixelCount, Float, Float, ResamplingFilter!, UnsafePointer<UInt16>!, vImage_Flags) -> vImage_Error](vimageverticalshear_cbcr16u(_:_:_:_:_:_:_:_:_:).md)
  Performs a single-precision vertical shear on a region of interest within an unsigned 16-bit-per-channel, 2-channel interleaved image.
- [func vImageVerticalShear_CbCr16F(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImagePixelCount, vImagePixelCount, Float, Float, ResamplingFilter!, UnsafePointer<UInt16>!, vImage_Flags) -> vImage_Error](vimageverticalshear_cbcr16f(_:_:_:_:_:_:_:_:_:).md)
  Performs a single-precision vertical shear on a region of interest within a floating-point 16-bit-per-channel, 2-channel interleaved image.
- [func vImageVerticalShear_ARGB16U(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImagePixelCount, vImagePixelCount, Float, Float, ResamplingFilter!, UnsafePointer<UInt16>!, vImage_Flags) -> vImage_Error](vimageverticalshear_argb16u(_:_:_:_:_:_:_:_:_:).md)
  Performs a single-precision vertical shear on a region of interest within an unsigned 16-bit-per-channel, 4-channel interleaved image.
- [func vImageVerticalShear_ARGB16S(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImagePixelCount, vImagePixelCount, Float, Float, ResamplingFilter!, UnsafePointer<Int16>!, vImage_Flags) -> vImage_Error](vimageverticalshear_argb16s(_:_:_:_:_:_:_:_:_:).md)
  Performs a single-precision vertical shear on a region of interest within a signed 16-bit-per-channel, 4-channel interleaved image.
- [func vImageVerticalShear_ARGB16F(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImagePixelCount, vImagePixelCount, Float, Float, ResamplingFilter!, UnsafePointer<UInt16>!, vImage_Flags) -> vImage_Error](vimageverticalshear_argb16f(_:_:_:_:_:_:_:_:_:).md)
  Performs a single-precision vertical shear on a region of interest within a floating-point 16-bit-per-channel, 4-channel interleaved image.
### Shearing 32-bit-per-channel buffers
- [func vImageVerticalShear_PlanarF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImagePixelCount, vImagePixelCount, Float, Float, ResamplingFilter!, Pixel_F, vImage_Flags) -> vImage_Error](vimageverticalshear_planarf(_:_:_:_:_:_:_:_:_:).md)
  Performs a single-precision vertical shear on a region of interest within a 32-bit planar image.
- [func vImageVerticalShear_ARGBFFFF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImagePixelCount, vImagePixelCount, Float, Float, ResamplingFilter!, UnsafePointer<Float>!, vImage_Flags) -> vImage_Error](vimageverticalshear_argbffff(_:_:_:_:_:_:_:_:_:).md)
  Performs a single-precision vertical shear on a region of interest within a 32-bit-per-channel, 4-channel interleaved image.

## See Also

- [Double-precision vertical shearing](double-precision-vertical-shearing.md)
  Apply double-precision vertical shearing to images.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/single-precision-vertical-shearing)*