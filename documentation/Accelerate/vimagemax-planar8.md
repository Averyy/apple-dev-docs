# vImageMax_Planar8(_:_:_:_:_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Maximizes an 8-bit planar buffer.

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
func vImageMax_Planar8(_ src: UnsafePointer<vImage_Buffer>, _ dest: UnsafePointer<vImage_Buffer>, _ tempBuffer: UnsafeMutableRawPointer!, _ srcOffsetToROI_X: vImagePixelCount, _ srcOffsetToROI_Y: vImagePixelCount, _ kernel_height: vImagePixelCount, _ kernel_width: vImagePixelCount, _ flags: vImage_Flags) -> vImage_Error
```

#### Return Value

[`kvImageNoError`](kvimagenoerror.md); otherwise, one of the error codes described in [`Data Types and Constants`](data-types-and-constants.md).

#### Discussion

The maximize filter is an optimized version of the dilation in which all the filter elements are zero.

##### Allocating Temporary Buffer Memory

If you want to allocate the memory for the `tempBuffer` parameter yourself, call this function twice, as follows:

1. To determine the minimum size for the temporary buffer, the first time you call this function, pass the [`kvImageGetTempBufferSize`](kvimagegettempbuffersize.md) flag. Pass the same values for all other parameters that you intend to use for the second call. The function returns the required minimum size, which should be a positive value (a negative returned value indicates an error). The [`kvImageGetTempBufferSize`](kvimagegettempbuffersize.md) flag prevents the function from performing any processing other than to determine the minimum buffer size.
2. After you allocate enough space for a buffer of the returned size, call the function a second time, passing a valid pointer in the `tempBuffer` parameter. This time, don’t pass the [`kvImageGetTempBufferSize`](kvimagegettempbuffersize.md) flag.

## Parameters

- `src`: The source vImage buffer.
- `dest`: A pointer to the destination vImage buffer structure. You’re responsible for filling out the  ,  , and   fields of this structure, and for allocating a data buffer of the appropriate size. On return, the data buffer this structure points to contains the destination image data. When you no longer need the data buffer, deallocate the memory to prevent memory leaks.
- `tempBuffer`: A pointer to a temporary buffer. If you pass  , the function allocates the buffer and then deallocates it before returning. Alternatively, you can allocate the buffer yourself, in which case you’re responsible for deallocating it when you no longer need it.
- `srcOffsetToROI_X`: The horizontal offset, in pixels, to the upper-left pixel of the region of interest within the source image.
- `srcOffsetToROI_Y`: The vertical offset, in pixels, to the upper-left pixel of the region of interest within the source image.
- `kernel_height`: The height of the kernel in pixels. This value must be odd.
- `kernel_width`: The width of the kernel in pixels. This value must be odd.
- `flags`: To determine the minimum size for the temporary buffer, set the   flag.

## See Also

- [Adding a bokeh effect to images](adding-a-bokeh-effect-to-images.md)
  Simulate a bokeh effect by applying dilation.
- [func vImageMax_PlanarF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutableRawPointer!, vImagePixelCount, vImagePixelCount, vImagePixelCount, vImagePixelCount, vImage_Flags) -> vImage_Error](vimagemax_planarf(_:_:_:_:_:_:_:_:).md)
  Maximizes a 32-bit planar buffer.
- [func vImageMax_ARGB8888(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutableRawPointer!, vImagePixelCount, vImagePixelCount, vImagePixelCount, vImagePixelCount, vImage_Flags) -> vImage_Error](vimagemax_argb8888(_:_:_:_:_:_:_:_:).md)
  Maximizes an 8-bit-per-channel, 4-channel interleaved buffer.
- [func vImageMax_ARGBFFFF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutableRawPointer!, vImagePixelCount, vImagePixelCount, vImagePixelCount, vImagePixelCount, vImage_Flags) -> vImage_Error](vimagemax_argbffff(_:_:_:_:_:_:_:_:).md)
  Maximizes a 32-bit-per-channel, 4-channel interleaved buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimagemax_planar8(_:_:_:_:_:_:_:_:))*