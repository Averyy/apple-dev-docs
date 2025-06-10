# Applying projective transformations to images

**Framework**: Accelerate

Warp images in three dimensions.

## Topics

### Computing a projective transformation from source and destination quadrilaterals
- [Transforming an image in three dimensions](transforming-an-image-in-three-dimensions.md)
  Create and use a projective transformation to apply a perspective warp to an image.
- [func vImageGetPerspectiveWarp(UnsafePointer<(Float, Float)>, UnsafePointer<(Float, Float)>, UnsafeMutablePointer<vImage_PerpsectiveTransform>, vImage_Flags) -> vImage_Error](vimagegetperspectivewarp(_:_:_:_:).md)
  Returns a projective-transformation structure that defines the mapping between a source quadrilateral and a destination quadrilateral.
- [struct vImage_PerpsectiveTransform](vimage_perpsectivetransform.md)
  A projective-transformation matrix.
### Warping planar buffers
- [func vImagePerspectiveWarp_Planar8(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutableRawPointer!, UnsafePointer<vImage_PerpsectiveTransform>, vImage_WarpInterpolation, Pixel_8, vImage_Flags) -> vImage_Error](vimageperspectivewarp_planar8(_:_:_:_:_:_:_:).md)
  Applies a perspective warp to an 8-bit planar image.
- [func vImagePerspectiveWarp_Planar16F(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutableRawPointer!, UnsafePointer<vImage_PerpsectiveTransform>, vImage_WarpInterpolation, Pixel_16F, vImage_Flags) -> vImage_Error](vimageperspectivewarp_planar16f(_:_:_:_:_:_:_:).md)
  Applies a perspective warp to a floating-point 16-bit planar image.
- [func vImagePerspectiveWarp_Planar16U(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutableRawPointer!, UnsafePointer<vImage_PerpsectiveTransform>, vImage_WarpInterpolation, Pixel_16U, vImage_Flags) -> vImage_Error](vimageperspectivewarp_planar16u(_:_:_:_:_:_:_:).md)
  Applies a perspective warp to a unsigned 16-bit planar image.
### Warping interleaved buffers
- [func vImagePerspectiveWarp_ARGB8888(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutableRawPointer!, UnsafePointer<vImage_PerpsectiveTransform>, vImage_WarpInterpolation, UnsafeMutablePointer<UInt8>!, vImage_Flags) -> vImage_Error](vimageperspectivewarp_argb8888(_:_:_:_:_:_:_:).md)
  Applies a perspective warp to an 8-bit-per-channel, four-channel interleaved image.
- [func vImagePerspectiveWarp_ARGB16F(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutableRawPointer!, UnsafePointer<vImage_PerpsectiveTransform>, vImage_WarpInterpolation, UnsafeMutablePointer<UInt16>!, vImage_Flags) -> vImage_Error](vimageperspectivewarp_argb16f(_:_:_:_:_:_:_:).md)
  Applies a perspective warp to a floating-point 16-bit , four-channel interleaved image.
- [func vImagePerspectiveWarp_ARGB16U(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutableRawPointer!, UnsafePointer<vImage_PerpsectiveTransform>, vImage_WarpInterpolation, UnsafeMutablePointer<UInt16>!, vImage_Flags) -> vImage_Error](vimageperspectivewarp_argb16u(_:_:_:_:_:_:_:).md)
  Applies a perspective warp to an unsigned 16-bit , four-channel interleaved image.

## See Also

- [Resampling in vImage](resampling-in-vimage.md)
  Learn how vImage resamples image data during geometric operations.
- [Applying affine transformations to images](applying-affine-transformations-to-images.md)
  Translate, rotate, and scale images.
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

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/applying-projective-transformations-to-images)*