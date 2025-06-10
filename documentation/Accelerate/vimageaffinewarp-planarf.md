# vImageAffineWarp_PlanarF(_:_:_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Applies a single-precision affine transformation to a 32-bit planar image.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.3+
- tvOS 5.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
func vImageAffineWarp_PlanarF(_ src: UnsafePointer<vImage_Buffer>, _ dest: UnsafePointer<vImage_Buffer>, _ tempBuffer: UnsafeMutableRawPointer!, _ transform: UnsafePointer<vImage_AffineTransform>, _ backColor: Pixel_F, _ flags: vImage_Flags) -> vImage_Error
```

#### Return Value

[`kvImageNoError`](kvimagenoerror.md); otherwise, one of the error codes described in [`Data Types and Constants`](data-types-and-constants.md).

#### Discussion

This function maps each pixel in the source image `[x, y]` to a new position `[x’, y’]` in the destination image using the following formula:

```objc
(x', y') = (x, y) * transform
```

In the preceding function, `transform` is the 3 x 3 affine transformation matrix.

The coordinate space places the origin at the bottom-left corner of the image. Positive movement in the horizontal direction moves pixels to the right. Positive movement in the vertical direction moves pixels up.

To avoid artifacts in high-frequency regions of the image, supply image data that’s nonpremultiplied or that has a constant alpha over the entire image.

This function doesn’t work in place — that is, the source and destination buffers must point to different memory.

## Parameters

- `src`: A pointer to a vImage buffer structure that contains the source image.
- `dest`: A pointer to the destination vImage buffer structure. You’re responsible for filling out the  ,  , and   fields of this structure and for allocating a data buffer of the appropriate size. On return, the data buffer this structure points to contains the destination image data. When you no longer need the data buffer, deallocate the memory to prevent memory leaks.
- `tempBuffer`: A pointer to a temporary buffer. If you pass  , the function allocates the buffer and then deallocates it before returning. Alternatively, you can allocate the buffer yourself, in which case you’re responsible for deallocating it when you no longer need it.
- `transform`: The affine transformation matrix that the function applies to the source image.
- `backColor`: A background color. If you set the   flag, pass a pixel value.
- `flags`: This function ignores the   flag.

## See Also

- [Applying geometric transforms to images](applying-geometric-transforms-to-images.md)
  Reflect, shear, rotate, and scale image buffers using vImage.
- [func vImageAffineWarp_Planar8(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutableRawPointer!, UnsafePointer<vImage_AffineTransform>, Pixel_8, vImage_Flags) -> vImage_Error](vimageaffinewarp_planar8(_:_:_:_:_:_:).md)
  Applies a single-precision affine transformation to an 8-bit planar image.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimageaffinewarp_planarf(_:_:_:_:_:_:))*