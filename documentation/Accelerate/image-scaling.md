# Image scaling

**Framework**: Accelerate

Scale interlaced and planar images.

## Topics

### Planar Image Scaling
- [func vImageScale_Planar8(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutableRawPointer!, vImage_Flags) -> vImage_Error](vimagescale_planar8(_:_:_:_:).md)
  Scales an 8-bit planar image to fit a destination buffer.
- [func vImageScale_Planar16U(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutableRawPointer!, vImage_Flags) -> vImage_Error](vimagescale_planar16u(_:_:_:_:).md)
  Scales an unsigned 16-bit planar image to fit a destination buffer.
- [func vImageScale_Planar16S(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutableRawPointer!, vImage_Flags) -> vImage_Error](vimagescale_planar16s(_:_:_:_:).md)
  Scales a signed 16-bit planar image to fit a destination buffer.
- [func vImageScale_Planar16F(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutableRawPointer!, vImage_Flags) -> vImage_Error](vimagescale_planar16f(_:_:_:_:).md)
  Scales a floating-point 16-bit planar image to fit a destination buffer.
- [func vImageScale_PlanarF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutableRawPointer!, vImage_Flags) -> vImage_Error](vimagescale_planarf(_:_:_:_:).md)
  Scales a 32-bit planar image to fit a destination buffer.
### Interleaved Image Scaling
- [func vImageScale_CbCr8(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutableRawPointer!, vImage_Flags) -> vImage_Error](vimagescale_cbcr8(_:_:_:_:).md)
  Scales an 8-bit-per-channel, 2-channel interleaved image to fit a destination buffer.
- [func vImageScale_CbCr16U(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutableRawPointer!, vImage_Flags) -> vImage_Error](vimagescale_cbcr16u(_:_:_:_:).md)
  Scales an unsigned 16-bit-per-channel, 2-channel interleaved image to fit a destination buffer.
- [func vImageScale_CbCr16F(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutableRawPointer!, vImage_Flags) -> vImage_Error](vimagescale_cbcr16f(_:_:_:_:).md)
  Scales a floating-point 16-bit-per-channel, 2-channel interleaved image to fit a destination buffer.
- [func vImageScale_ARGB8888(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutableRawPointer!, vImage_Flags) -> vImage_Error](vimagescale_argb8888(_:_:_:_:).md)
  Scales an 8-bit-per-channel, 4-channel interleaved image to fit a destination buffer.
- [func vImageScale_ARGB16U(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutableRawPointer!, vImage_Flags) -> vImage_Error](vimagescale_argb16u(_:_:_:_:).md)
  Scales an unsigned 16-bit-per-channel, 4-channel interleaved image to fit a destination buffer.
- [func vImageScale_ARGB16S(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutableRawPointer!, vImage_Flags) -> vImage_Error](vimagescale_argb16s(_:_:_:_:).md)
  Scales a signed 16-bit-per-channel, 4-channel interleaved image to fit a destination buffer.
- [func vImageScale_ARGB16F(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutableRawPointer!, vImage_Flags) -> vImage_Error](vimagescale_argb16f(_:_:_:_:).md)
  Scales a floating-point 16-bit-per-channel, 4-channel interleaved image to fit a destination buffer.
- [func vImageScale_ARGBFFFF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutableRawPointer!, vImage_Flags) -> vImage_Error](vimagescale_argbffff(_:_:_:_:).md)
  Scales a 32-bit-per-channel, 4-channel interleaved image to fit a destination buffer.
- [func vImageScale_XRGB2101010W(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutableRawPointer!, vImage_Flags) -> vImage_Error](vimagescale_xrgb2101010w(_:_:_:_:).md)
  Scales a 2-bit alpha, 10-bit RGB interleaved image to fit a destination buffer.

## See Also

- [Resampling in vImage](resampling-in-vimage.md)
  Learn how vImage resamples image data during geometric operations.
- [Applying affine transformations to images](applying-affine-transformations-to-images.md)
  Translate, rotate, and scale images.
- [Applying projective transformations to images](applying-projective-transformations-to-images.md)
  Warp images in three dimensions.
- [Image reflection](image-reflection.md)
  Reflect images horizontally and vertically.
- [Image shearing](image-shearing.md)
  Shear images horizontally and vertically.
- [Image rotation](image-rotation.md)
  Rotate images by arbitrary angles or by multiples of 90 degrees.
- [Getting the Buffer Size](getting-the-buffer-size.md)
  Calculate the size of the temporary buffer needed by a high-level geometry functions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/image-scaling)*