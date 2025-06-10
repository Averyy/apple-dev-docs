# vImageTentConvolve_Planar8(_:_:_:_:_:_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Applies a tent filter to an 8-bit planar source image.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 5.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
func vImageTentConvolve_Planar8(_ src: UnsafePointer<vImage_Buffer>, _ dest: UnsafePointer<vImage_Buffer>, _ tempBuffer: UnsafeMutableRawPointer!, _ srcOffsetToROI_X: vImagePixelCount, _ srcOffsetToROI_Y: vImagePixelCount, _ kernel_height: UInt32, _ kernel_width: UInt32, _ backgroundColor: Pixel_8, _ flags: vImage_Flags) -> vImage_Error
```

#### Return Value

[`kvImageNoError`](kvimagenoerror.md); otherwise, one of the error codes in [`Data Types and Constants`](data-types-and-constants.md).

#### Discussion

This function uses an implicit divisor and an implicit kernel of specified size instead of a kernel provided by the caller.

If you want to allocate the memory for the `tempBuffer` parameter yourself, call this function twice, as follows:

1. To determine the minimum size for the temporary buffer, the first time you call this function pass the `kvImageGetTempBufferSize` flag. Pass the same values for all other parameters that you intend to use in for the second call. The function returns the required minimum size, which should be a positive value. (A negative returned value indicates an error.) The `kvImageGetTempBufferSize` flag prevents the function from performing any processing other than to determine the minimum buffer size.
2. After you allocate enough space for a buffer of the returned size, call the function a second time, passing a valid pointer in the `tempBuffer` parameter. This time, do not pass the `kvImageGetTempBufferSize` flag.

## Parameters

- `src`: A pointer to a vImage buffer structure that contains data for the source image.
- `dest`: A pointer to a vImage buffer data structure. You’re responsible for filling out the  ,  , and   fields of this structure, and for allocating a data buffer of the appropriate size. On return, the data buffer this structure points to contains the destination image data. When you no longer need the data buffer, you must deallocate the memory. The size (number of rows and number of columns) of the destination buffer also specifies the size of the region of interest in the source buffer.
- `tempBuffer`: If you want to allocate the buffer yourself, see the Discussion for information on how to determine the minimum size that you must allocate.
- `srcOffsetToROI_X`: The horizontal offset, in pixels, to the upper-left pixel of the region of interest within the source image.
- `srcOffsetToROI_Y`: The vertical offset, in pixels, to the upper-left pixel of the region of interest within the source image.
- `kernel_height`: The height of the kernel in pixels. This value must be odd.
- `kernel_width`: The width of the kernel in pixels. This value must be odd.
- `backgroundColor`: A background color. If you supply a color, you must also set the   flag, otherwise the function ignores the color.
- `flags`: Pass one of the following flags to specify how vImage handles pixel locations beyond the edge of the source image:  ,  ,  , or  .

## See Also

- [func vImageConvolve_Planar8(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutableRawPointer!, vImagePixelCount, vImagePixelCount, UnsafePointer<Int16>!, UInt32, UInt32, Int32, Pixel_8, vImage_Flags) -> vImage_Error](vimageconvolve_planar8(_:_:_:_:_:_:_:_:_:_:_:).md)
  Convolves an 8-bit planar image by a 2D kernel and divides the pixel values by a divisor.
- [func vImageBoxConvolve_Planar8(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutableRawPointer!, vImagePixelCount, vImagePixelCount, UInt32, UInt32, Pixel_8, vImage_Flags) -> vImage_Error](vimageboxconvolve_planar8(_:_:_:_:_:_:_:_:_:).md)
  Applies a box filter to an 8-bit planar source image.
- [func vImageBoxConvolve_ARGB8888(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutableRawPointer!, vImagePixelCount, vImagePixelCount, UInt32, UInt32, UnsafePointer<UInt8>!, vImage_Flags) -> vImage_Error](vimageboxconvolve_argb8888(_:_:_:_:_:_:_:_:_:).md)
  Applies a box filter to an 8-bit-per-channel, 4-channel interleaved source image.
- [func vImageTentConvolve_ARGB8888(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutableRawPointer!, vImagePixelCount, vImagePixelCount, UInt32, UInt32, UnsafePointer<UInt8>!, vImage_Flags) -> vImage_Error](vimagetentconvolve_argb8888(_:_:_:_:_:_:_:_:_:).md)
  Applies a tent filter to an 8-bit-per-channel, 4-channel interleaved source image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimagetentconvolve_planar8(_:_:_:_:_:_:_:_:_:))*