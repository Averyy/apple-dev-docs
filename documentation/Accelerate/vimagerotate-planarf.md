# vImageRotate_PlanarF(_:_:_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Rotates a 32-bit planar image by any angle, which you specify in radians.

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
func vImageRotate_PlanarF(_ src: UnsafePointer<vImage_Buffer>, _ dest: UnsafePointer<vImage_Buffer>, _ tempBuffer: UnsafeMutableRawPointer!, _ angleInRadians: Float, _ backColor: Pixel_F, _ flags: vImage_Flags) -> vImage_Error
```

#### Return Value

[`kvImageNoError`](kvimagenoerror.md); otherwise, a negative value indicates one of the error codes that [`Data Types and Constants`](data-types-and-constants.md) describes, and a positive value indicates the required size for the temporary buffer.

#### Discussion

This function maps the center point of the source image to the center point of the destination image. Depending on the relative sizes of the source image and the destination buffer, the function might clip parts of the source image. Areas outside the source image might appear in the destination image if you don’t pass a background color to the function.

To avoid artifacts in high-frequency regions of the image, supply image data that’s nonpremultiplied or that has a constant alpha over the entire image.

This function doesn’t work in place — that is, the source and destination buffers need to point to different memory.

##### Optimize Performance with Temporary Buffers

This function uses a multiple-pass algorithm that saves intermediate pixel values between passes. In some cases, the destination buffer may not be large enough to store that intermediate data, so the operation requires additional storage.

Pass `nil` to the `tempBuffer` parameter to have vImage create and manage this temporary storage for you.

In cases where your code calls the function frequently (for example, when processing video), create and manage this temporary buffer yourself and reuse it across function calls. Reusing a buffer avoids vImage allocating the temporary storage with each call.

To use your own temporary buffer, first call the function with the same values for all other parameters that you intend to use for subsequent calls. In addition, pass the `kvImageGetTempBufferSize` flag. The `kvImageGetTempBufferSize` instructs the function not to perform any processing, and to return a positive value that represents the minimum size, in bytes, of the temporary buffer. A negative return value represents an error.

After you allocate the memory for the temporary buffer, pass that to the `tempBuffer` parameter for subsequent calls to the function, and don’t pass the `kvImageGetTempBufferSize` flag.

You can use the same workspace memory for a group of images that are different sizes. To do this, create a vImage buffer structure with a size that shares the maximum width and maximum height of the images that you’re working with. For example, to create a workspace memory that’s suitable for 4x4, 5x4, and 4x5 images, pass a buffer with the size 5x5.

## Parameters

- `src`: A pointer to a vImage buffer structure that contains the source image.
- `dest`: A pointer to the destination vImage buffer structure. You’re responsible for filling out the `height`, `width`, and `rowBytes` fields of this structure and for allocating a data buffer of the appropriate size. On return, the data buffer this structure points to contains the destination image data. When you no longer need the data buffer, deallocate the memory to prevent memory leaks.
- `tempBuffer`: A pointer to workspace memory the function uses as it operates on an image. Pass `nil` to instruct the function to allocate, use, and then free its own temporary buffer.
- `angleInRadians`: The rotation angle, in radians.
- `backColor`: A background color. If you set the `kvImageBackgroundColorFill` flag, pass a pixel value.
- `flags`: The options to use when applying the rotation. To instruct the function to return the minimum size of the workspace memory, set the [`kvImageGetTempBufferSize`](kvimagegettempbuffersize.md) flag. To specify how vImage handles pixel locations beyond the edge of the source image, set one of the following flags: [`kvImageBackgroundColorFill`](kvimagebackgroundcolorfill.md) or [`kvImageEdgeExtend`](kvimageedgeextend.md). If you want vImage to use a higher quality but a slower resampling filter, set the [`kvImageHighQualityResampling`](kvimagehighqualityresampling.md) flag. If your code implements its own tiling or its own multithreading, pass [`kvImageDoNotTile`](kvimagedonottile.md). This function ignores the [`kvImageLeaveAlphaUnchanged`](kvimageleavealphaunchanged.md) flag.

## See Also

- [Applying geometric transforms to images](applying-geometric-transforms-to-images.md)
  Reflect, shear, rotate, and scale image buffers using vImage.
- [func vImageRotate_ARGBFFFF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutableRawPointer!, Float, UnsafePointer<Float>!, vImage_Flags) -> vImage_Error](vimagerotate_argbffff(_:_:_:_:_:_:).md)
  Rotates a 32-bit-per-channel, 4-channel interleaved image by any angle, which you specify in radians.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimagerotate_planarf(_:_:_:_:_:_:))*