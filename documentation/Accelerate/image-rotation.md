# Image rotation

**Framework**: Accelerate

Rotate images by arbitrary angles or by multiples of 90 degrees.

## Topics

### Rotating 8-bit-per-channel buffers by any angle
- [func vImageRotate_Planar8(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutableRawPointer!, Float, Pixel_8, vImage_Flags) -> vImage_Error](vimagerotate_planar8(_:_:_:_:_:_:).md)
  Rotates an 8-bit planar image by any angle, which you specify in radians.
- [func vImageRotate_ARGB8888(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutableRawPointer!, Float, UnsafePointer<UInt8>!, vImage_Flags) -> vImage_Error](vimagerotate_argb8888(_:_:_:_:_:_:).md)
  Rotates an 8-bit-per-channel, 4-channel interleaved image by any angle, which you specify in radians.
### Rotating 16-bit-per-channel buffers by any angle
- [func vImageRotate_Planar16F(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutableRawPointer!, Float, Pixel_16F, vImage_Flags) -> vImage_Error](vimagerotate_planar16f(_:_:_:_:_:_:).md)
  Rotates a floating-point 16-bit planar image by any angle, which you specify in radians.
- [func vImageRotate_CbCr16F(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutableRawPointer!, Float, UnsafePointer<UInt16>!, vImage_Flags) -> vImage_Error](vimagerotate_cbcr16f(_:_:_:_:_:_:).md)
  Rotates a floating-point 16-bit-per-channel, 2-channel interleaved image by any angle, which you specify in radians.
- [func vImageRotate_ARGB16U(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutableRawPointer!, Float, UnsafePointer<UInt16>!, vImage_Flags) -> vImage_Error](vimagerotate_argb16u(_:_:_:_:_:_:).md)
  Rotates an unsigned 16-bit-per-channel, 4-channel interleaved image by any angle, which you specify in radians.
- [func vImageRotate_ARGB16S(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutableRawPointer!, Float, UnsafePointer<Int16>!, vImage_Flags) -> vImage_Error](vimagerotate_argb16s(_:_:_:_:_:_:).md)
  Rotates a signed 16-bit-per-channel, 4-channel interleaved image by any angle, which you specify in radians.
- [func vImageRotate_ARGB16F(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutableRawPointer!, Float, UnsafePointer<UInt16>!, vImage_Flags) -> vImage_Error](vimagerotate_argb16f(_:_:_:_:_:_:).md)
  Rotates a floating-point 16-bit-per-channel, 4-channel interleaved image by any angle, which you specify in radians.
### Rotating 32-bit-per-channel buffers by any angle
- [func vImageRotate_PlanarF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutableRawPointer!, Float, Pixel_F, vImage_Flags) -> vImage_Error](vimagerotate_planarf(_:_:_:_:_:_:).md)
  Rotates a 32-bit planar image by any angle, which you specify in radians.
- [func vImageRotate_ARGBFFFF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutableRawPointer!, Float, UnsafePointer<Float>!, vImage_Flags) -> vImage_Error](vimagerotate_argbffff(_:_:_:_:_:_:).md)
  Rotates a 32-bit-per-channel, 4-channel interleaved image by any angle, which you specify in radians.
### Rotating 8-bit-per-channel buffers by multiples of 90°
- [func vImageRotate90_Planar8(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UInt8, Pixel_8, vImage_Flags) -> vImage_Error](vimagerotate90_planar8(_:_:_:_:_:).md)
  Rotates an 8-bit planar image by a multiple of 90°.
- [func vImageRotate90_ARGB8888(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UInt8, UnsafePointer<UInt8>, vImage_Flags) -> vImage_Error](vimagerotate90_argb8888(_:_:_:_:_:).md)
  Rotates an 8-bit-per-channel, 4-channel interleaved image by a multiple of 90°.
### Rotating 16-bit-per-channel buffers by multiples of 90°
- [func vImageRotate90_Planar16U(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UInt8, Pixel_16U, vImage_Flags) -> vImage_Error](vimagerotate90_planar16u(_:_:_:_:_:).md)
  Rotates an unsigned 16-bit planar image by a multiple of 90°.
- [func vImageRotate90_Planar16F(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UInt8, Pixel_16F, vImage_Flags) -> vImage_Error](vimagerotate90_planar16f(_:_:_:_:_:).md)
  Rotates a floating-point 16-bit planar image by a multiple of 90°.
- [func vImageRotate90_CbCr16F(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UInt8, UnsafePointer<UInt16>!, vImage_Flags) -> vImage_Error](vimagerotate90_cbcr16f(_:_:_:_:_:).md)
  Rotates a floating-point 16-bit-per-channel, 2-channel interleaved image by a multiple of 90°.
- [func vImageRotate90_ARGB16U(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UInt8, UnsafePointer<UInt16>, vImage_Flags) -> vImage_Error](vimagerotate90_argb16u(_:_:_:_:_:).md)
  Rotates an unsigned 16-bit-per-channel, 4-channel interleaved image by a multiple of 90°.
- [func vImageRotate90_ARGB16S(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UInt8, UnsafePointer<Int16>, vImage_Flags) -> vImage_Error](vimagerotate90_argb16s(_:_:_:_:_:).md)
  Rotates a signed 16-bit-per-channel, 4-channel interleaved image by a multiple of 90°.
- [func vImageRotate90_ARGB16F(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UInt8, UnsafePointer<UInt16>!, vImage_Flags) -> vImage_Error](vimagerotate90_argb16f(_:_:_:_:_:).md)
  Rotates a floating-point 16-bit-per-channel, 4-channel interleaved image by a multiple of 90°.
### Rotating 32-bit-per-channel buffers by multiples of 90°
- [func vImageRotate90_PlanarF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UInt8, Pixel_F, vImage_Flags) -> vImage_Error](vimagerotate90_planarf(_:_:_:_:_:).md)
  Rotates a 32-bit planar image by a multiple of 90°.
- [func vImageRotate90_ARGBFFFF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UInt8, UnsafePointer<Float>, vImage_Flags) -> vImage_Error](vimagerotate90_argbffff(_:_:_:_:_:).md)
  Rotates a 32-bit-per-channel, 4-channel interleaved image by a multiple of 90°.
### Specifying the angle of a multiple of 90° rotation
- [Rotation constants](1509228-rotation-constants.md)
  The number of degrees to rotate an image.

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
- [Image scaling](image-scaling.md)
  Scale interlaced and planar images.
- [Getting the Buffer Size](getting-the-buffer-size.md)
  Calculate the size of the temporary buffer needed by a high-level geometry functions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/image-rotation)*