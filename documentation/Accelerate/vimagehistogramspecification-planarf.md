# vImageHistogramSpecification_PlanarF(_:_:_:_:_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Specifies the histogram of a 32-bit planar buffer.

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
func vImageHistogramSpecification_PlanarF(_ src: UnsafePointer<vImage_Buffer>, _ dest: UnsafePointer<vImage_Buffer>, _ tempBuffer: UnsafeMutableRawPointer!, _ desired_histogram: UnsafePointer<vImagePixelCount>, _ histogram_entries: UInt32, _ minVal: Pixel_F, _ maxVal: Pixel_F, _ flags: vImage_Flags) -> vImage_Error
```

#### Return Value

[`kvImageNoError`](kvimagenoerror.md); otherwise, a negative value indicates one of the error codes that [`Data Types and Constants`](data-types-and-constants.md) describes, and a positive value indicates the required size for the temporary buffer.

#### Discussion

Use this function to apply a histogram — that you’ve generated using [`vImageHistogramCalculation_PlanarF(_:_:_:_:_:_:)`](vimagehistogramcalculation_planarf(_:_:_:_:_:_:).md) — to another image.

The following code applies a histogram to a planar vImage buffer:

```swift
// `histogram` is a `entryCount`-element array.
histogram.withUnsafeBufferPointer {
    // `buffer` is a `vImage_Buffer` structure.
    _ = vImageHistogramSpecification_PlanarF(&buffer, &buffer,
                                             nil,
                                             $0.baseAddress!,
                                             UInt32(entryCount),
                                             0, 1,
                                             vImage_Flags(kvImageNoFlags))
}
```

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
- `desired_histogram`: The histogram that the operation applies to the source buffer.
- `histogram_entries`: The number of histogram entries.
- `minVal`: The minimum pixel value. The operation assigns pixel values less than   to the first histogram entry.
- `maxVal`: The maximum pixel value. The operation assigns pixel values greater than   to the last histogram entry.
- `flags`: To instruct the function to return the minimum size of the workspace memory, set the   flag.

## See Also

- [Enhancing image contrast with histogram manipulation](enhancing-image-contrast-with-histogram-manipulation.md)
  Enhance and adjust the contrast of an image with histogram equalization and contrast stretching.
- [Specifying histograms with vImage](specifying-histograms-with-vimage.md)
  Calculate the histogram of one image, and apply it to a second image.
- [func vImageHistogramSpecification_Planar8(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImagePixelCount>, vImage_Flags) -> vImage_Error](vimagehistogramspecification_planar8(_:_:_:_:).md)
  Specifies the histogram of an 8-bit planar buffer.
- [func vImageHistogramSpecification_ARGB8888(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutablePointer<UnsafePointer<vImagePixelCount>?>, vImage_Flags) -> vImage_Error](vimagehistogramspecification_argb8888(_:_:_:_:).md)
  Specifies the histogram of an 8-bit-per-channel, 4-channel interleaved buffer.
- [func vImageHistogramSpecification_ARGBFFFF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutableRawPointer!, UnsafeMutablePointer<UnsafePointer<vImagePixelCount>?>!, UInt32, Pixel_F, Pixel_F, vImage_Flags) -> vImage_Error](vimagehistogramspecification_argbffff(_:_:_:_:_:_:_:_:).md)
  Specifes the histogram of a 32-bit-per-channel, 4-channel interleaved buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimagehistogramspecification_planarf(_:_:_:_:_:_:_:_:))*