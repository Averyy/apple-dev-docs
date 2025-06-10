# Applying affine transformations to images

**Framework**: Accelerate

Translate, rotate, and scale images.

## Topics

### Single-Precision Affine Transformation
- [func vImageAffineWarp_Planar8(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutableRawPointer!, UnsafePointer<vImage_AffineTransform>, Pixel_8, vImage_Flags) -> vImage_Error](vimageaffinewarp_planar8(_:_:_:_:_:_:).md)
  Applies a single-precision affine transformation to an 8-bit planar image.
- [func vImageAffineWarp_PlanarF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutableRawPointer!, UnsafePointer<vImage_AffineTransform>, Pixel_F, vImage_Flags) -> vImage_Error](vimageaffinewarp_planarf(_:_:_:_:_:_:).md)
  Applies a single-precision affine transformation to a 32-bit planar image.
- [func vImageAffineWarp_ARGB16U(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutableRawPointer!, UnsafePointer<vImage_AffineTransform>, UnsafePointer<UInt16>!, vImage_Flags) -> vImage_Error](vimageaffinewarp_argb16u(_:_:_:_:_:_:).md)
  Applies a single-precision affine transformation to an unsigned 16-bit-per-channel, 4-channel interleaved image.
- [func vImageAffineWarp_ARGB16S(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutableRawPointer!, UnsafePointer<vImage_AffineTransform>, UnsafePointer<Int16>!, vImage_Flags) -> vImage_Error](vimageaffinewarp_argb16s(_:_:_:_:_:_:).md)
  Applies a single-precision affine transformation to a signed 16-bit-per-channel, 4-channel interleaved image.
- [func vImageAffineWarp_ARGB8888(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutableRawPointer!, UnsafePointer<vImage_AffineTransform>, UnsafePointer<UInt8>!, vImage_Flags) -> vImage_Error](vimageaffinewarp_argb8888(_:_:_:_:_:_:).md)
  Applies a single-precision affine transformation to an 8-bit-per-channel, 4-channel interleaved image.
- [func vImageAffineWarp_ARGBFFFF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutableRawPointer!, UnsafePointer<vImage_AffineTransform>, UnsafePointer<Float>!, vImage_Flags) -> vImage_Error](vimageaffinewarp_argbffff(_:_:_:_:_:_:).md)
  Applies a single-precision affine transformation to a 32-bit-per-channel, 4-channel interleaved image.
- [func vImageAffineWarp_ARGB16F(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutableRawPointer!, UnsafePointer<vImage_AffineTransform>, UnsafePointer<UInt16>!, vImage_Flags) -> vImage_Error](vimageaffinewarp_argb16f(_:_:_:_:_:_:).md)
- [func vImageAffineWarp_CbCr16F(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutableRawPointer!, UnsafePointer<vImage_AffineTransform>, UnsafePointer<UInt16>!, vImage_Flags) -> vImage_Error](vimageaffinewarp_cbcr16f(_:_:_:_:_:_:).md)
- [func vImageAffineWarp_Planar16F(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutableRawPointer!, UnsafePointer<vImage_AffineTransform>, Pixel_16F, vImage_Flags) -> vImage_Error](vimageaffinewarp_planar16f(_:_:_:_:_:_:).md)
### Double-Precision Affine Transformation
- [func vImageAffineWarpD_Planar8(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutableRawPointer!, UnsafePointer<vImage_AffineTransform_Double>, Pixel_8, vImage_Flags) -> vImage_Error](vimageaffinewarpd_planar8(_:_:_:_:_:_:).md)
  Applies a double-precision affine transformation to an 8-bit planar image.
- [func vImageAffineWarpD_PlanarF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutableRawPointer!, UnsafePointer<vImage_AffineTransform_Double>, Pixel_F, vImage_Flags) -> vImage_Error](vimageaffinewarpd_planarf(_:_:_:_:_:_:).md)
  Applies a double-precision affine transformation to a 32-bit planar image.
- [func vImageAffineWarpD_Planar16F(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutableRawPointer!, UnsafePointer<vImage_AffineTransform_Double>, Pixel_16F, vImage_Flags) -> vImage_Error](vimageaffinewarpd_planar16f(_:_:_:_:_:_:).md)
  Applies a double-precision affine transformation to a floating-point 16-bit planar image.
- [func vImageAffineWarpD_CbCr16F(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutableRawPointer!, UnsafePointer<vImage_AffineTransform_Double>, UnsafePointer<UInt16>!, vImage_Flags) -> vImage_Error](vimageaffinewarpd_cbcr16f(_:_:_:_:_:_:).md)
  Applies a double-precision affine transformation to a floating-point 16-bit-per-channel, 2-channel interleaved image.
- [func vImageAffineWarpD_ARGB8888(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutableRawPointer!, UnsafePointer<vImage_AffineTransform_Double>, UnsafePointer<UInt8>!, vImage_Flags) -> vImage_Error](vimageaffinewarpd_argb8888(_:_:_:_:_:_:).md)
  Applies a double-precision affine transformation to an 8-bit-per-channel, 4-channel interleaved image.
- [func vImageAffineWarpD_ARGB16U(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutableRawPointer!, UnsafePointer<vImage_AffineTransform_Double>, UnsafePointer<UInt16>!, vImage_Flags) -> vImage_Error](vimageaffinewarpd_argb16u(_:_:_:_:_:_:).md)
  Applies a double-precision affine transformation to an unsigned 16-bit-per-channel, 4-channel interleaved image.
- [func vImageAffineWarpD_ARGB16S(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutableRawPointer!, UnsafePointer<vImage_AffineTransform_Double>, UnsafePointer<Int16>!, vImage_Flags) -> vImage_Error](vimageaffinewarpd_argb16s(_:_:_:_:_:_:).md)
  Applies a double-precision affine transformation to a signed 16-bit-per-channel, 4-channel interleaved image.
- [func vImageAffineWarpD_ARGB16F(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutableRawPointer!, UnsafePointer<vImage_AffineTransform_Double>, UnsafePointer<UInt16>!, vImage_Flags) -> vImage_Error](vimageaffinewarpd_argb16f(_:_:_:_:_:_:).md)
  Applies a double-precision affine transformation to a floating-point 16-bit-per-channel, 4-channel interleaved image.
- [func vImageAffineWarpD_ARGBFFFF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutableRawPointer!, UnsafePointer<vImage_AffineTransform_Double>, UnsafePointer<Float>!, vImage_Flags) -> vImage_Error](vimageaffinewarpd_argbffff(_:_:_:_:_:_:).md)
  Applies a double-precision affine transformation to a 32-bit-per-channel, 4-channel interleaved image.
### Core Graphics Affine Transformation
- [func vImageAffineWarpCG_Planar8(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutableRawPointer!, UnsafePointer<vImage_CGAffineTransform>, Pixel_8, vImage_Flags) -> vImage_Error](vimageaffinewarpcg_planar8(_:_:_:_:_:_:).md)
  Applies a Core Graphics affine transformation to a Planar8 source image.
- [func vImageAffineWarpCG_PlanarF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutableRawPointer!, UnsafePointer<vImage_CGAffineTransform>, Pixel_F, vImage_Flags) -> vImage_Error](vimageaffinewarpcg_planarf(_:_:_:_:_:_:).md)
  Applies a Core Graphics affine transformation to a PlanarF source image.
- [func vImageAffineWarpCG_ARGB16U(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutableRawPointer!, UnsafePointer<vImage_CGAffineTransform>, UnsafePointer<UInt16>!, vImage_Flags) -> vImage_Error](vimageaffinewarpcg_argb16u(_:_:_:_:_:_:).md)
  Applies a Core Graphics affine transformation to an ARGB16U source image.
- [func vImageAffineWarpCG_ARGB16S(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutableRawPointer!, UnsafePointer<vImage_CGAffineTransform>, UnsafePointer<Int16>!, vImage_Flags) -> vImage_Error](vimageaffinewarpcg_argb16s(_:_:_:_:_:_:).md)
  Applies a Core Graphics affine transformation to an ARGB16S source image.
- [func vImageAffineWarpCG_ARGB8888(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutableRawPointer!, UnsafePointer<vImage_CGAffineTransform>, UnsafePointer<UInt8>!, vImage_Flags) -> vImage_Error](vimageaffinewarpcg_argb8888(_:_:_:_:_:_:).md)
  Applies a Core Graphics affine transformation to an ARGB8888 source image.
- [func vImageAffineWarpCG_ARGBFFFF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutableRawPointer!, UnsafePointer<vImage_CGAffineTransform>, UnsafePointer<Float>!, vImage_Flags) -> vImage_Error](vimageaffinewarpcg_argbffff(_:_:_:_:_:_:).md)
  Applies a Core Graphics affine transformation to an ARGBFFFF source image.

## See Also

- [Resampling in vImage](resampling-in-vimage.md)
  Learn how vImage resamples image data during geometric operations.
- [Applying projective transformations to images](applying-projective-transformations-to-images.md)
  Warp images in three dimensions.
- [Image reflection](image-reflection.md)
  Reflect images horizontally and vertically.
- [Image shearing](image-shearing.md)
  Shear images horizontally and vertically.
- [Image rotation](image-rotation.md)
  Rotate images by arbitrary angles or by multiples of 90 degrees.
- [Image scaling](image-scaling.md)
  Scale interlaced and planar images.
- [Getting the Buffer Size](getting-the-buffer-size.md)
  Calculate the size of the temporary buffer needed by a high-level geometry functions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/applying-affine-transformations-to-images)*