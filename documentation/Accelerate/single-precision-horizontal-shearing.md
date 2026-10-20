# Single-precision horizontal shearing

**Framework**: Accelerate  
**Role**: API Collection

Apply single-precision horizontal shearing to images.

## Topics

### Shearing 8-bit-per-channel buffers
- [func vImageHorizontalShear_Planar8(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImagePixelCount, vImagePixelCount, Float, Float, ResamplingFilter!, Pixel_8, vImage_Flags) -> vImage_Error](./vimagehorizontalshear_planar8%28_,_,_,_,_,_,_,_,_%29.md)
  Performs a single-precision horizontal shear on a region of interest within an 8-bit planar image.
- [func vImageHorizontalShear_CbCr8(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImagePixelCount, vImagePixelCount, Float, Float, ResamplingFilter!, UnsafePointer<UInt8>!, vImage_Flags) -> vImage_Error](./vimagehorizontalshear_cbcr8%28_,_,_,_,_,_,_,_,_%29.md)
  Performs a single-precision horizontal shear on a region of interest within an 8-bit-per-channel, 2-channel interleaved image.
- [func vImageHorizontalShear_ARGB8888(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImagePixelCount, vImagePixelCount, Float, Float, ResamplingFilter!, UnsafePointer<UInt8>!, vImage_Flags) -> vImage_Error](./vimagehorizontalshear_argb8888%28_,_,_,_,_,_,_,_,_%29.md)
  Performs a single-precision horizontal shear on a region of interest within an 8-bit-per-channel, 4-channel interleaved image.
### Shearing 10-bit-per-channel buffers
- [func vImageHorizontalShear_XRGB2101010W(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImagePixelCount, vImagePixelCount, Float, Float, ResamplingFilter!, Pixel_32U, vImage_Flags) -> vImage_Error](./vimagehorizontalshear_xrgb2101010w%28_,_,_,_,_,_,_,_,_%29.md)
  Performs a single-precision horizontal shear on a region of interest within a 2-bit alpha, 10-bit RGB interleaved image.
### Shearing 16-bit-per-channel buffers
- [func vImageHorizontalShear_Planar16U(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImagePixelCount, vImagePixelCount, Float, Float, ResamplingFilter!, Pixel_16U, vImage_Flags) -> vImage_Error](./vimagehorizontalshear_planar16u%28_,_,_,_,_,_,_,_,_%29.md)
  Performs a single-precision horizontal shear on a region of interest within an unsigned 16-bit planar image.
- [func vImageHorizontalShear_Planar16S(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImagePixelCount, vImagePixelCount, Float, Float, ResamplingFilter!, Pixel_16S, vImage_Flags) -> vImage_Error](./vimagehorizontalshear_planar16s%28_,_,_,_,_,_,_,_,_%29.md)
  Performs a single-precision horizontal shear on a region of interest within a signed 16-bit planar image.
- [func vImageHorizontalShear_Planar16F(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImagePixelCount, vImagePixelCount, Float, Float, ResamplingFilter!, Pixel_16F, vImage_Flags) -> vImage_Error](./vimagehorizontalshear_planar16f%28_,_,_,_,_,_,_,_,_%29.md)
  Performs a single-precision horizontal shear on a region of interest within a floating-point 16-bit planar image.
- [func vImageHorizontalShear_CbCr16U(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImagePixelCount, vImagePixelCount, Float, Float, ResamplingFilter!, UnsafePointer<UInt16>!, vImage_Flags) -> vImage_Error](./vimagehorizontalshear_cbcr16u%28_,_,_,_,_,_,_,_,_%29.md)
  Performs a single-precision horizontal shear on a region of interest within an unsigned 16-bit-per-channel, 2-channel interleaved image.
- [func vImageHorizontalShear_CbCr16F(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImagePixelCount, vImagePixelCount, Float, Float, ResamplingFilter!, UnsafePointer<UInt16>!, vImage_Flags) -> vImage_Error](./vimagehorizontalshear_cbcr16f%28_,_,_,_,_,_,_,_,_%29.md)
  Performs a single-precision horizontal shear on a region of interest within a flloating-point 16-bit-per-channel, 2-channel interleaved image.
- [func vImageHorizontalShear_ARGB16U(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImagePixelCount, vImagePixelCount, Float, Float, ResamplingFilter!, UnsafePointer<UInt16>!, vImage_Flags) -> vImage_Error](./vimagehorizontalshear_argb16u%28_,_,_,_,_,_,_,_,_%29.md)
  Performs a single-precision horizontal shear on a region of interest within an unsigned 16-bit-per-channel, 4-channel interleaved image.
- [func vImageHorizontalShear_ARGB16S(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImagePixelCount, vImagePixelCount, Float, Float, ResamplingFilter!, UnsafePointer<Int16>!, vImage_Flags) -> vImage_Error](./vimagehorizontalshear_argb16s%28_,_,_,_,_,_,_,_,_%29.md)
  Performs a single-precision horizontal shear on a region of interest within a signed 16-bit-per-channel, 4-channel interleaved image.
- [func vImageHorizontalShear_ARGB16F(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImagePixelCount, vImagePixelCount, Float, Float, ResamplingFilter!, UnsafePointer<UInt16>!, vImage_Flags) -> vImage_Error](./vimagehorizontalshear_argb16f%28_,_,_,_,_,_,_,_,_%29.md)
  Performs a single-precision horizontal shear on a region of interest within a floating-point 16-bit-per-channel, 4-channel interleaved image.
### Shearing 32-bit-per-channel buffers
- [func vImageHorizontalShear_PlanarF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImagePixelCount, vImagePixelCount, Float, Float, ResamplingFilter!, Pixel_F, vImage_Flags) -> vImage_Error](./vimagehorizontalshear_planarf%28_,_,_,_,_,_,_,_,_%29.md)
  Performs a single-precision horizontal shear on a region of interest within a 32-bit planar image.
- [func vImageHorizontalShear_ARGBFFFF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImagePixelCount, vImagePixelCount, Float, Float, ResamplingFilter!, UnsafePointer<Float>!, vImage_Flags) -> vImage_Error](./vimagehorizontalshear_argbffff%28_,_,_,_,_,_,_,_,_%29.md)
  Performs a single-precision horizontal shear on a region of interest within a 32-bit-per-channel, 4-channel interleaved image.

## See Also

### Shearing an image horizontally
- [Double-precision horizontal shearing](./double-precision-horizontal-shearing.md)
  Apply double-precision horizontal shearing to images.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/single-precision-horizontal-shearing)*