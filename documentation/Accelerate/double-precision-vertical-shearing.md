# Double-precision vertical shearing

**Framework**: Accelerate  
**Role**: API Collection

Apply double-precision vertical shearing to images.

## Topics

### Shearing 8-bit-per-channel buffers
- [func vImageVerticalShearD_Planar8(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImagePixelCount, vImagePixelCount, Double, Double, ResamplingFilter!, Pixel_8, vImage_Flags) -> vImage_Error](./vimageverticalsheard_planar8%28_,_,_,_,_,_,_,_,_%29.md)
  Performs a double-precision vertical shear on a region of interest within an 8-bit planar image.
- [func vImageVerticalShearD_ARGB8888(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImagePixelCount, vImagePixelCount, Double, Double, ResamplingFilter!, UnsafePointer<UInt8>!, vImage_Flags) -> vImage_Error](./vimageverticalsheard_argb8888%28_,_,_,_,_,_,_,_,_%29.md)
  Performs a double-precision vertical shear on a region of interest within an 8-bit-per-channel, 4-channel interleaved image.
### Shearing 16-bit-per-channel buffers
- [func vImageVerticalShearD_Planar16F(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImagePixelCount, vImagePixelCount, Double, Double, ResamplingFilter!, Pixel_16F, vImage_Flags) -> vImage_Error](./vimageverticalsheard_planar16f%28_,_,_,_,_,_,_,_,_%29.md)
  Performs a double-precision vertical shear on a region of interest within a floating-point 16-bit planar image.
- [func vImageVerticalShearD_CbCr16F(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImagePixelCount, vImagePixelCount, Double, Double, ResamplingFilter!, UnsafePointer<UInt16>!, vImage_Flags) -> vImage_Error](./vimageverticalsheard_cbcr16f%28_,_,_,_,_,_,_,_,_%29.md)
  Performs a double-precision vertical shear on a region of interest within a floating-point 16-bit-per-channel, 2-channel interleaved image.
- [func vImageVerticalShearD_ARGB16U(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImagePixelCount, vImagePixelCount, Double, Double, ResamplingFilter!, UnsafePointer<UInt16>!, vImage_Flags) -> vImage_Error](./vimageverticalsheard_argb16u%28_,_,_,_,_,_,_,_,_%29.md)
  Performs a double-precision vertical shear on a region of interest within an unsigned 16-bit-per-channel, 4-channel interleaved image.
- [func vImageVerticalShearD_ARGB16S(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImagePixelCount, vImagePixelCount, Double, Double, ResamplingFilter!, UnsafePointer<Int16>!, vImage_Flags) -> vImage_Error](./vimageverticalsheard_argb16s%28_,_,_,_,_,_,_,_,_%29.md)
  Performs a double-precision vertical shear on a region of interest within a signed 16-bit-per-channel, 4-channel interleaved image.
- [func vImageVerticalShearD_ARGB16F(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImagePixelCount, vImagePixelCount, Double, Double, ResamplingFilter!, UnsafePointer<UInt16>!, vImage_Flags) -> vImage_Error](./vimageverticalsheard_argb16f%28_,_,_,_,_,_,_,_,_%29.md)
  Performs a double-precision vertical shear on a region of interest within a floating-point 16-bit-per-channel, 4-channel interleaved image.
- [func vImageVerticalShearD_CbCr16S(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImagePixelCount, vImagePixelCount, Double, Double, ResamplingFilter!, UnsafePointer<Int16>!, vImage_Flags) -> vImage_Error](./vimageverticalsheard_cbcr16s%28_,_,_,_,_,_,_,_,_%29.md)
- [func vImageVerticalShearD_CbCr16U(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImagePixelCount, vImagePixelCount, Double, Double, ResamplingFilter!, UnsafePointer<UInt16>!, vImage_Flags) -> vImage_Error](./vimageverticalsheard_cbcr16u%28_,_,_,_,_,_,_,_,_%29.md)
- [func vImageVerticalShear_CbCr16S(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImagePixelCount, vImagePixelCount, Float, Float, ResamplingFilter!, UnsafePointer<Int16>!, vImage_Flags) -> vImage_Error](./vimageverticalshear_cbcr16s%28_,_,_,_,_,_,_,_,_%29.md)
### Shearing 32-bit-per-channel buffers
- [func vImageVerticalShearD_PlanarF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImagePixelCount, vImagePixelCount, Double, Double, ResamplingFilter!, Pixel_F, vImage_Flags) -> vImage_Error](./vimageverticalsheard_planarf%28_,_,_,_,_,_,_,_,_%29.md)
  Performs a double-precision vertical shear on a region of interest within a 32-bit planar image.
- [func vImageVerticalShearD_ARGBFFFF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImagePixelCount, vImagePixelCount, Double, Double, ResamplingFilter!, UnsafePointer<Float>!, vImage_Flags) -> vImage_Error](./vimageverticalsheard_argbffff%28_,_,_,_,_,_,_,_,_%29.md)
  Performs a double-precision vertical shear on a region of interest within a 32-bit-per-channel, 4-channel interleaved image.

## See Also

### Shearing an image vertically
- [Single-precision vertical shearing](./single-precision-vertical-shearing.md)
  Apply single-precision vertical shearing to images.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/double-precision-vertical-shearing)*