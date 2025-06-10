# vImagePerspectiveWarp_Planar16U(_:_:_:_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Applies a perspective warp to a unsigned 16-bit planar image.

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
func vImagePerspectiveWarp_Planar16U(_ src: UnsafePointer<vImage_Buffer>, _ dest: UnsafePointer<vImage_Buffer>, _ tempBuffer: UnsafeMutableRawPointer!, _ transform: UnsafePointer<vImage_PerpsectiveTransform>, _ interpolation: vImage_WarpInterpolation, _ backColor: Pixel_16U, _ flags: vImage_Flags) -> vImage_Error
```

#### Return Value

[`kvImageNoError`](kvimagenoerror.md); otherwise, one of the error codes in [`Data Types and Constants`](data-types-and-constants.md).

#### Discussion

This function doesn’t work in place, that is, the source and destination buffers must point to different underlying memory.

## Parameters

- `src`: A pointer to a vImage buffer structure that contains the source image.
- `dest`: A pointer to the destination vImage buffer structure. You’re responsible for filling out the  ,  , and   fields of this structure and for allocating a data buffer of the appropriate size. On return, the data buffer this structure points to contains the destination image data. When you no longer need the data buffer, deallocate the memory to prevent memory leaks.
- `tempBuffer`: A pointer to a temporary buffer. If you pass  , the function allocates the buffer and then deallocates it before returning. Alternatively, you can allocate the buffer yourself, in which case you’re responsible for deallocating it when you no longer need it.
- `transform`: The   structure that the operation applies to the source buffer.
- `interpolation`: The   enumeration that specifies the interpolation mode.
- `backColor`: The background color. If you set the   flag, pass a pixel value.
- `flags`: To specify how vImage handles pixel locations beyond the edge of the source image, set one of the following flags:   or  .

## See Also

- [Transforming an image in three dimensions](transforming-an-image-in-three-dimensions.md)
  Create and use a projective transformation to apply a perspective warp to an image.
- [func vImagePerspectiveWarp_Planar8(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutableRawPointer!, UnsafePointer<vImage_PerpsectiveTransform>, vImage_WarpInterpolation, Pixel_8, vImage_Flags) -> vImage_Error](vimageperspectivewarp_planar8(_:_:_:_:_:_:_:).md)
  Applies a perspective warp to an 8-bit planar image.
- [func vImagePerspectiveWarp_Planar16F(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutableRawPointer!, UnsafePointer<vImage_PerpsectiveTransform>, vImage_WarpInterpolation, Pixel_16F, vImage_Flags) -> vImage_Error](vimageperspectivewarp_planar16f(_:_:_:_:_:_:_:).md)
  Applies a perspective warp to a floating-point 16-bit planar image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimageperspectivewarp_planar16u(_:_:_:_:_:_:_:))*