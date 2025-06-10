# Double-precision horizontal shearing

**Framework**: Accelerate

Apply double-precision horizontal shearing to images.

## Topics

### Shearing 8-bit-per-channel buffers
- [func vImageHorizontalShearD_Planar8(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImagePixelCount, vImagePixelCount, Double, Double, ResamplingFilter!, Pixel_8, vImage_Flags) -> vImage_Error](vimagehorizontalsheard_planar8(_:_:_:_:_:_:_:_:_:).md)
  Performs a double-precision horizontal shear on a region of interest within an 8-bit planar image.
- [func vImageHorizontalShearD_ARGB8888(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImagePixelCount, vImagePixelCount, Double, Double, ResamplingFilter!, UnsafePointer<UInt8>!, vImage_Flags) -> vImage_Error](vimagehorizontalsheard_argb8888(_:_:_:_:_:_:_:_:_:).md)
  Performs a double-precision horizontal shear on a region of interest within an 8-bit-per-channel, 4-channel interleaved image.
### Shearing 16-bit-per-channel buffers
- [func vImageHorizontalShearD_Planar16F(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImagePixelCount, vImagePixelCount, Double, Double, ResamplingFilter!, Pixel_16F, vImage_Flags) -> vImage_Error](vimagehorizontalsheard_planar16f(_:_:_:_:_:_:_:_:_:).md)
  Performs a double-precision horizontal shear on a region of interest within a floating-point 16-bit planar image.
- [func vImageHorizontalShearD_CbCr16F(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImagePixelCount, vImagePixelCount, Double, Double, ResamplingFilter!, UnsafePointer<UInt16>!, vImage_Flags) -> vImage_Error](vimagehorizontalsheard_cbcr16f(_:_:_:_:_:_:_:_:_:).md)
  Performs a double-precision horizontal shear on a region of interest within a floating-point 16-bit-per-channel, 2-channel interleaved image.
- [func vImageHorizontalShearD_ARGB16U(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImagePixelCount, vImagePixelCount, Double, Double, ResamplingFilter!, UnsafePointer<UInt16>!, vImage_Flags) -> vImage_Error](vimagehorizontalsheard_argb16u(_:_:_:_:_:_:_:_:_:).md)
  Performs a double-precision horizontal shear on a region of interest within an unsigned 16-bit-per-channel, 4-channel interleaved image.
- [func vImageHorizontalShearD_ARGB16S(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImagePixelCount, vImagePixelCount, Double, Double, ResamplingFilter!, UnsafePointer<Int16>!, vImage_Flags) -> vImage_Error](vimagehorizontalsheard_argb16s(_:_:_:_:_:_:_:_:_:).md)
  Performs a double-precision horizontal shear on a region of interest within a signed 16-bit-per-channel, 4-channel interleaved image.
- [func vImageHorizontalShearD_ARGB16F(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImagePixelCount, vImagePixelCount, Double, Double, ResamplingFilter!, UnsafePointer<UInt16>!, vImage_Flags) -> vImage_Error](vimagehorizontalsheard_argb16f(_:_:_:_:_:_:_:_:_:).md)
  Performs a double-precision horizontal shear on a region of interest within a floating-point 16-bit-per-channel, 4-channel interleaved image.
- [func vImageHorizontalShearD_CbCr16S(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImagePixelCount, vImagePixelCount, Double, Double, ResamplingFilter!, UnsafePointer<Int16>!, vImage_Flags) -> vImage_Error](vimagehorizontalsheard_cbcr16s(_:_:_:_:_:_:_:_:_:).md)
- [func vImageHorizontalShearD_CbCr16U(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImagePixelCount, vImagePixelCount, Double, Double, ResamplingFilter!, UnsafePointer<UInt16>!, vImage_Flags) -> vImage_Error](vimagehorizontalsheard_cbcr16u(_:_:_:_:_:_:_:_:_:).md)
- [func vImageHorizontalShear_CbCr16S(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImagePixelCount, vImagePixelCount, Float, Float, ResamplingFilter!, UnsafePointer<Int16>!, vImage_Flags) -> vImage_Error](vimagehorizontalshear_cbcr16s(_:_:_:_:_:_:_:_:_:).md)
### Shearing 32-bit-per-channel buffers
- [func vImageHorizontalShearD_PlanarF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImagePixelCount, vImagePixelCount, Double, Double, ResamplingFilter!, Pixel_F, vImage_Flags) -> vImage_Error](vimagehorizontalsheard_planarf(_:_:_:_:_:_:_:_:_:).md)
  Performs a double-precision horizontal shear on a region of interest within a 32-bit planar image.
- [func vImageHorizontalShearD_ARGBFFFF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImagePixelCount, vImagePixelCount, Double, Double, ResamplingFilter!, UnsafePointer<Float>!, vImage_Flags) -> vImage_Error](vimagehorizontalsheard_argbffff(_:_:_:_:_:_:_:_:_:).md)
  Performs a double-precision horizontal shear on a region of interest within a 32-bit-per-channel, 4-channel interleaved image.

## See Also

- [Single-precision horizontal shearing](single-precision-horizontal-shearing.md)
  Apply single-precision horizontal shearing to images.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/double-precision-horizontal-shearing)*