# vImageContrastStretch_ARGBFFFF(_:_:_:_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Performs contrast stretching on a 32-bit-per-channel, 4-channel interleaved buffer.

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
func vImageContrastStretch_ARGBFFFF(_ src: UnsafePointer<vImage_Buffer>, _ dest: UnsafePointer<vImage_Buffer>, _ tempBuffer: UnsafeMutableRawPointer!, _ histogram_entries: UInt32, _ minVal: Pixel_F, _ maxVal: Pixel_F, _ flags: vImage_Flags) -> vImage_Error
```

#### Return Value

[`kvImageNoError`](kvimagenoerror.md); otherwise, a negative value indicates one of the error codes that [`Data Types and Constants`](data-types-and-constants.md) describes, and a positive value indicates the required size for the temporary buffer.

#### Discussion

Contrast stretching evenly distributes a histogram’s pixel values across the full range of available pixel values. This technique is ideal for enhancing the contrast of an image with pixel values concentrated in one area of the intensity spectrum.

##### Optimize Performance with Temporary Buffers

This function uses a multiple-pass algorithm that saves intermediate pixel values between passes. In some cases, the destination buffer may not be large enough to store that intermediate data, so the operation requires additional storage.

Pass `nil` to the `tempBuffer` parameter to have vImage create and manage this temporary storage for you.

In cases where your code calls the function frequently (for example, when processing video), create and manage this temporary buffer yourself and reuse it across function calls. Reusing a buffer avoids vImage allocating the temporary storage with each call.

To use your own temporary buffer, first call the function with the same values for all other parameters that you intend to use for subsequent calls. In addition, pass the `kvImageGetTempBufferSize` flag. The `kvImageGetTempBufferSize` instructs the function not to perform any processing, and to return a positive value that represents the minimum size, in bytes, of the temporary buffer. A negative return value represents an error.

After you allocate the memory for the temporary buffer, pass that to the `tempBuffer` parameter for subsequent calls to the function, and don’t pass the `kvImageGetTempBufferSize` flag.

## Parameters

- `src`: The source vImage buffer.
- `dest`: A pointer to the destination vImage buffer structure. You’re responsible for filling out the  ,  , and   fields of this structure, and for allocating a data buffer of the appropriate size. On return, the data buffer this structure points to contains the destination image data. When you no longer need the data buffer, deallocate the memory to prevent memory leaks.
- `tempBuffer`: A pointer to workspace memory the function uses as it operates on an image. Pass   to instruct the function to allocate, use, and then free its own temporary buffer.
- `histogram_entries`: The number of histogram entries.
- `minVal`: The minimum pixel value. The operation assigns pixel values less than   to the first histogram entry.
- `maxVal`: The maximum pixel value. The operation assigns pixel values greater than   to the last histogram entry.
- `flags`: To specify that the function doesn’t apply the operation to the alpha channel, set the   flag.

## See Also

- [Enhancing image contrast with histogram manipulation](enhancing-image-contrast-with-histogram-manipulation.md)
  Enhance and adjust the contrast of an image with histogram equalization and contrast stretching.
- [Specifying histograms with vImage](specifying-histograms-with-vimage.md)
  Calculate the histogram of one image, and apply it to a second image.
- [func vImageContrastStretch_Planar8(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimagecontraststretch_planar8(_:_:_:).md)
  Performs contrast stretching on an 8-bit planar buffer.
- [func vImageContrastStretch_PlanarF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutableRawPointer!, UInt32, Pixel_F, Pixel_F, vImage_Flags) -> vImage_Error](vimagecontraststretch_planarf(_:_:_:_:_:_:_:).md)
  Performs contrast stretching on a 32-bit planar buffer.
- [func vImageContrastStretch_ARGB8888(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimagecontraststretch_argb8888(_:_:_:).md)
  Performs contrast stretching on an 8-bit-per-channel, 4-channel interleaved buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimagecontraststretch_argbffff(_:_:_:_:_:_:_:))*