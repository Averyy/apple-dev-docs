# vImagePerspectiveWarp_Planar8(_:_:_:_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Applies a perspective warp to an 8-bit planar image.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
func vImagePerspectiveWarp_Planar8(_ src: UnsafePointer<vImage_Buffer>, _ dest: UnsafePointer<vImage_Buffer>, _ tempBuffer: UnsafeMutableRawPointer!, _ transform: UnsafePointer<vImage_PerpsectiveTransform>, _ interpolation: vImage_WarpInterpolation, _ backColor: Pixel_8, _ flags: vImage_Flags) -> vImage_Error
```

#### Return Value

[`kvImageNoError`](kvimagenoerror.md); otherwise, a negative value indicates one of the error codes that [`Data Types and Constants`](data-types-and-constants.md) describes, and a positive value indicates the required size for the temporary buffer.

#### Discussion

This function doesn’t work in place, that is, the source and destination buffers need to point to different underlying memory.

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
- `transform`: The   structure that the operation applies to the source buffer.
- `interpolation`: The   enumeration that specifies the interpolation mode.
- `backColor`: The background color. If you set the   flag, pass a pixel value.
- `flags`: To specify how vImage handles pixel locations beyond the edge of the source image, set one of the following flags:   or  .

## See Also

- [Transforming an image in three dimensions](transforming-an-image-in-three-dimensions.md)
  Create and use a projective transformation to apply a perspective warp to an image.
- [func vImagePerspectiveWarp_Planar16F(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutableRawPointer!, UnsafePointer<vImage_PerpsectiveTransform>, vImage_WarpInterpolation, Pixel_16F, vImage_Flags) -> vImage_Error](vimageperspectivewarp_planar16f(_:_:_:_:_:_:_:).md)
  Applies a perspective warp to a floating-point 16-bit planar image.
- [func vImagePerspectiveWarp_Planar16U(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutableRawPointer!, UnsafePointer<vImage_PerpsectiveTransform>, vImage_WarpInterpolation, Pixel_16U, vImage_Flags) -> vImage_Error](vimageperspectivewarp_planar16u(_:_:_:_:_:_:_:).md)
  Applies a perspective warp to a unsigned 16-bit planar image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimageperspectivewarp_planar8(_:_:_:_:_:_:_:))*