# vImageAffineWarpD_ARGB8888(_:_:_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Applies a double-precision affine transformation to an 8-bit-per-channel, 4-channel interleaved image.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 6.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
func vImageAffineWarpD_ARGB8888(_ src: UnsafePointer<vImage_Buffer>, _ dest: UnsafePointer<vImage_Buffer>, _ tempBuffer: UnsafeMutableRawPointer!, _ transform: UnsafePointer<vImage_AffineTransform_Double>, _ backColor: UnsafePointer<UInt8>!, _ flags: vImage_Flags) -> vImage_Error
```

#### Return Value

[`kvImageNoError`](kvimagenoerror.md); otherwise, a negative value indicates one of the error codes that [`Data Types and Constants`](data-types-and-constants.md) describes, and a positive value indicates the required size for the temporary buffer.

#### Discussion

This function maps each pixel in the source image `[x, y]` to a new position `[x’, y’]` in the destination image using the following formula:

```objc
(x', y') = (x, y) * transform
```

In the preceding function, `transform` is the 3 x 3 affine transformation matrix.

The coordinate space places the origin at the bottom-left corner of the image. Positive movement in the horizontal direction moves pixels to the right. Positive movement in the vertical direction moves pixels up.

To avoid artifacts in high-frequency regions of the image, supply image data that’s nonpremultiplied or that has a constant alpha over the entire image.

This function doesn’t work in place — that is, the source and destination buffers need to point to different memory.

##### Optimize Performance with Temporary Buffers

This function uses a multiple-pass algorithm that saves intermediate pixel values between passes. In some cases, the destination buffer may not be large enough to store that intermediate data, so the operation requires additional storage.

Pass `nil` to the `tempBuffer` parameter to have vImage create and manage this temporary storage for you.

In cases where your code calls the function frequently (for example, when processing video), create and manage this temporary buffer yourself and reuse it across function calls. Reusing a buffer avoids vImage allocating the temporary storage with each call.

To use your own temporary buffer, first call the function with the same values for all other parameters that you intend to use for subsequent calls. In addition, pass the `kvImageGetTempBufferSize` flag. The `kvImageGetTempBufferSize` instructs the function not to perform any processing, and to return a positive value that represents the minimum size, in bytes, of the temporary buffer. A negative return value represents an error.

After you allocate the memory for the temporary buffer, pass that to the `tempBuffer` parameter for subsequent calls to the function, and don’t pass the `kvImageGetTempBufferSize` flag.

## Parameters

- `src`: A pointer to a vImage buffer structure that contains the source image.
- `dest`: A pointer to the destination vImage buffer structure. You’re responsible for filling out the  ,  , and   fields of this structure and for allocating a data buffer of the appropriate size. On return, the data buffer this structure points to contains the destination image data. When you no longer need the data buffer, deallocate the memory to prevent memory leaks.
- `tempBuffer`: A pointer to workspace memory the function uses as it operates on an image. Pass   to instruct the function to allocate, use, and then free its own temporary buffer.
- `transform`: The affine transformation matrix that the function applies to the source image.
- `backColor`: A background color. If you set the   flag, pass a pixel value.
- `flags`: This function ignores the   flag.

## See Also

- [Applying geometric transforms to images](applying-geometric-transforms-to-images.md)
  Reflect, shear, rotate, and scale image buffers using vImage.
- [func vImageAffineWarpD_Planar8(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutableRawPointer!, UnsafePointer<vImage_AffineTransform_Double>, Pixel_8, vImage_Flags) -> vImage_Error](vimageaffinewarpd_planar8(_:_:_:_:_:_:).md)
  Applies a double-precision affine transformation to an 8-bit planar image.
- [func vImageAffineWarpD_PlanarF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutableRawPointer!, UnsafePointer<vImage_AffineTransform_Double>, Pixel_F, vImage_Flags) -> vImage_Error](vimageaffinewarpd_planarf(_:_:_:_:_:_:).md)
  Applies a double-precision affine transformation to a 32-bit planar image.
- [func vImageAffineWarpD_Planar16F(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutableRawPointer!, UnsafePointer<vImage_AffineTransform_Double>, Pixel_16F, vImage_Flags) -> vImage_Error](vimageaffinewarpd_planar16f(_:_:_:_:_:_:).md)
  Applies a double-precision affine transformation to a floating-point 16-bit planar image.
- [func vImageAffineWarpD_CbCr16F(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutableRawPointer!, UnsafePointer<vImage_AffineTransform_Double>, UnsafePointer<UInt16>!, vImage_Flags) -> vImage_Error](vimageaffinewarpd_cbcr16f(_:_:_:_:_:_:).md)
  Applies a double-precision affine transformation to a floating-point 16-bit-per-channel, 2-channel interleaved image.
- [func vImageAffineWarpD_ARGB16U(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutableRawPointer!, UnsafePointer<vImage_AffineTransform_Double>, UnsafePointer<UInt16>!, vImage_Flags) -> vImage_Error](vimageaffinewarpd_argb16u(_:_:_:_:_:_:).md)
  Applies a double-precision affine transformation to an unsigned 16-bit-per-channel, 4-channel interleaved image.
- [func vImageAffineWarpD_ARGB16S(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutableRawPointer!, UnsafePointer<vImage_AffineTransform_Double>, UnsafePointer<Int16>!, vImage_Flags) -> vImage_Error](vimageaffinewarpd_argb16s(_:_:_:_:_:_:).md)
  Applies a double-precision affine transformation to a signed 16-bit-per-channel, 4-channel interleaved image.
- [func vImageAffineWarpD_ARGB16F(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutableRawPointer!, UnsafePointer<vImage_AffineTransform_Double>, UnsafePointer<UInt16>!, vImage_Flags) -> vImage_Error](vimageaffinewarpd_argb16f(_:_:_:_:_:_:).md)
  Applies a double-precision affine transformation to a floating-point 16-bit-per-channel, 4-channel interleaved image.
- [func vImageAffineWarpD_ARGBFFFF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutableRawPointer!, UnsafePointer<vImage_AffineTransform_Double>, UnsafePointer<Float>!, vImage_Flags) -> vImage_Error](vimageaffinewarpd_argbffff(_:_:_:_:_:_:).md)
  Applies a double-precision affine transformation to a 32-bit-per-channel, 4-channel interleaved image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimageaffinewarpd_argb8888(_:_:_:_:_:_:))*