# Image reflection

**Framework**: Accelerate

Reflect images horizontally and vertically.

## Topics

### Applying horizontal reflection to 8-bit-per-channel buffers
- [func vImageHorizontalReflect_Planar8(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimagehorizontalreflect_planar8(_:_:_:).md)
  Reflects an 8-bit planar image horizontally across the center vertical line.
- [func vImageHorizontalReflect_ARGB8888(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimagehorizontalreflect_argb8888(_:_:_:).md)
  Reflects an 8-bit-per-channel, 4-channel interleaved image horizontally across the center vertical line.
### Applying horizontal reflection to 16-bit-per-channel buffers
- [func vImageHorizontalReflect_Planar16U(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimagehorizontalreflect_planar16u(_:_:_:).md)
  Reflects an unsigned 16-bit planar image horizontally across the center vertical line.
- [func vImageHorizontalReflect_Planar16F(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimagehorizontalreflect_planar16f(_:_:_:).md)
  Reflects a floating-point 16-bit planar image horizontally across the center vertical line.
- [func vImageHorizontalReflect_CbCr16F(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimagehorizontalreflect_cbcr16f(_:_:_:).md)
  Reflects a floating-point 16-bit-per-channel, 2-channel interleaved image horizontally across the center vertical line.
- [func vImageHorizontalReflect_ARGB16U(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimagehorizontalreflect_argb16u(_:_:_:).md)
  Reflects an unsigned 16-bit-per-channel, 4-channel interleaved image horizontally across the center vertical line.
- [func vImageHorizontalReflect_ARGB16S(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimagehorizontalreflect_argb16s(_:_:_:).md)
  Reflects a signed 16-bit-per-channel, 4-channel interleaved image horizontally across the center vertical line.
- [func vImageHorizontalReflect_ARGB16F(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimagehorizontalreflect_argb16f(_:_:_:).md)
  Reflects a floating-point 16-bit-per-channel, 4-channel interleaved image horizontally across the center vertical line.
### Applying horizontal reflection to 32-bit-per-channel buffers
- [func vImageHorizontalReflect_PlanarF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimagehorizontalreflect_planarf(_:_:_:).md)
  Reflects a 32-bit planar image horizontally across the center vertical line.
- [func vImageHorizontalReflect_ARGBFFFF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimagehorizontalreflect_argbffff(_:_:_:).md)
  Reflects a 32-bit-per-channel, 4-channel interleaved image horizontally across the center vertical line.
### Applying vertical reflection to 8-bit-per-channel buffers
- [func vImageVerticalReflect_Planar8(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimageverticalreflect_planar8(_:_:_:).md)
  Reflects an 8-bit planar image vertically across the center horizontal line.
- [func vImageVerticalReflect_ARGB8888(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimageverticalreflect_argb8888(_:_:_:).md)
  Reflects an 8-bit-per-channel, 4-channel interleaved image vertically across the center horizontal line.
### Applying vertical reflection to 16-bit-per-channel buffers
- [func vImageVerticalReflect_Planar16U(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimageverticalreflect_planar16u(_:_:_:).md)
  Reflects an unsigned 16-bit planar image vertically across the center horizontal line.
- [func vImageVerticalReflect_Planar16F(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimageverticalreflect_planar16f(_:_:_:).md)
  Reflects a floating-point 16-bit planar image vertically across the center horizontal line.
- [func vImageVerticalReflect_CbCr16F(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimageverticalreflect_cbcr16f(_:_:_:).md)
  Reflects a floating-point 16-bit-per-channel, 2-channel interleaved image vertically across the center horizontal line.
- [func vImageVerticalReflect_ARGB16U(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimageverticalreflect_argb16u(_:_:_:).md)
  Reflects an unsigned 16-bit-per-channel, 4-channel interleaved image vertically across the center horizontal line.
- [func vImageVerticalReflect_ARGB16S(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimageverticalreflect_argb16s(_:_:_:).md)
  Reflects a signed 16-bit-per-channel, 4-channel interleaved image vertically across the center horizontal line.
- [func vImageVerticalReflect_ARGB16F(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimageverticalreflect_argb16f(_:_:_:).md)
  Reflects a floating-point 16-bit-per-channel, 4-channel interleaved image vertically across the center horizontal line.
### Applying vertical reflection to 32-bit-per-channel buffers
- [func vImageVerticalReflect_PlanarF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimageverticalreflect_planarf(_:_:_:).md)
  Reflects a 32-bit planar image vertically across the center horizontal line.
- [func vImageVerticalReflect_ARGBFFFF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimageverticalreflect_argbffff(_:_:_:).md)
  Reflects a 32-bit-per-channel, 4-channel interleaved image vertically across the center horizontal line.

## See Also

- [Resampling in vImage](resampling-in-vimage.md)
  Learn how vImage resamples image data during geometric operations.
- [Applying affine transformations to images](applying-affine-transformations-to-images.md)
  Translate, rotate, and scale images.
- [Applying projective transformations to images](applying-projective-transformations-to-images.md)
  Warp images in three dimensions.
- [Image shearing](image-shearing.md)
  Shear images horizontally and vertically.
- [Image rotation](image-rotation.md)
  Rotate images by arbitrary angles or by multiples of 90 degrees.
- [Image scaling](image-scaling.md)
  Scale interlaced and planar images.
- [Getting the Buffer Size](getting-the-buffer-size.md)
  Calculate the size of the temporary buffer needed by a high-level geometry functions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/image-reflection)*