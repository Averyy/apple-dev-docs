# vImageRotate_ARGBFFFF(_:_:_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Rotates a 32-bit-per-channel, 4-channel interleaved image by any angle, which you specify in radians.

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
func vImageRotate_ARGBFFFF(_ src: UnsafePointer<vImage_Buffer>, _ dest: UnsafePointer<vImage_Buffer>, _ tempBuffer: UnsafeMutableRawPointer!, _ angleInRadians: Float, _ backColor: UnsafePointer<Float>!, _ flags: vImage_Flags) -> vImage_Error
```

#### Return Value

[`kvImageNoError`](kvimagenoerror.md); otherwise, one of the error codes from [`Error codes`](1578972-error-codes.md).

#### Discussion

This function maps the center point of the source image to the center point of the destination image. Depending on the relative sizes of the source image and the destination buffer, the function might clip parts of the source image. Areas outside the source image might appear in the destination image if you don’t pass a background color to the function.

To avoid artifacts in high-frequency regions of the image, supply image data that’s nonpremultiplied or that has a constant alpha over the entire image.

This function doesn’t work in place — that is, the source and destination buffers must point to different memory.

## Parameters

- `src`: A pointer to a vImage buffer structure that contains the source image.
- `dest`: A pointer to the destination vImage buffer structure. You’re responsible for filling out the  ,  , and   fields of this structure and for allocating a data buffer of the appropriate size. On return, the data buffer this structure points to contains the destination image data. When you no longer need the data buffer, deallocate the memory to prevent memory leaks.
- `tempBuffer`: A pointer to a temporary buffer. If you pass  , the function allocates the buffer and then deallocates it before returning. Alternatively, you can allocate the buffer yourself, in which case you’re responsible for deallocating it when you no longer need it.
- `angleInRadians`: The rotation angle, in radians.
- `backColor`: A background color. If you set the   flag, pass a pixel value.
- `flags`: This function ignores the   flag.

## See Also

- [Applying geometric transforms to images](applying-geometric-transforms-to-images.md)
  Reflect, shear, rotate, and scale image buffers using vImage.
- [func vImageRotate_PlanarF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutableRawPointer!, Float, Pixel_F, vImage_Flags) -> vImage_Error](vimagerotate_planarf(_:_:_:_:_:_:).md)
  Rotates a 32-bit planar image by any angle, which you specify in radians.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimagerotate_argbffff(_:_:_:_:_:_:))*