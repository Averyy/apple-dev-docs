# vImageHistogramSpecification_ARGBFFFF(_:_:_:_:_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Specifes the histogram of a 32-bit-per-channel, 4-channel interleaved buffer.

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
func vImageHistogramSpecification_ARGBFFFF(_ src: UnsafePointer<vImage_Buffer>, _ dest: UnsafePointer<vImage_Buffer>, _ tempBuffer: UnsafeMutableRawPointer!, _ desired_histogram: UnsafeMutablePointer<UnsafePointer<vImagePixelCount>?>!, _ histogram_entries: UInt32, _ minVal: Pixel_F, _ maxVal: Pixel_F, _ flags: vImage_Flags) -> vImage_Error
```

#### Return Value

[`kvImageNoError`](kvimagenoerror.md); otherwise, one of the error codes in [`Data Types and Constants`](data-types-and-constants.md).

#### Discussion

Use this function to apply a histogram — that you’ve generated using [`vImageHistogramSpecification_ARGBFFFF(_:_:_:_:_:_:_:_:)`](vimagehistogramspecification_argbffff(_:_:_:_:_:_:_:_:).md) — to each channel of another image.

The following code applies a histogram to a 4-channel interleaved vImage buffer:

```swift
// `histogramAlpha`, `histogramRed`, `histogramGreen`, and `histogramBlue` are `entryCount` element arrays.
histogramAlpha.withUnsafeBufferPointer { zeroPtr in
    histogramRed.withUnsafeBufferPointer { onePtr in
        histogramGreen.withUnsafeBufferPointer { twoPtr in
            histogramBlue.withUnsafeBufferPointer { threePtr in
                
                var histogramBins = [zeroPtr.baseAddress, onePtr.baseAddress,
                                     twoPtr.baseAddress, threePtr.baseAddress]
                
                histogramBins.withUnsafeMutableBufferPointer { histogramBinsPtr in
                    // `buffer` is a `vImage_Buffer` structure.
                    _ = vImageHistogramSpecification_ARGBFFFF(&buffer, &buffer,
                                                              nil,
                                                              histogramBinsPtr.baseAddress!,
                                                              UInt32(entryCount),
                                                              0, 1,
                                                              vImage_Flags(kvImageNoFlags))
                }
            }
        }
    }
}
```

## Parameters

- `src`: The source vImage buffer.
- `dest`: A pointer to the destination vImage buffer structure. You’re responsible for filling out the  ,  , and   fields of this structure, and for allocating a data buffer of the appropriate size. On return, the data buffer this structure points to contains the destination image data. When you no longer need the data buffer, deallocate the memory to prevent memory leaks.
- `tempBuffer`: A pointer to a temporary buffer. If you pass  , the function allocates the buffer and then deallocates it before returning. Alternatively, you can allocate the buffer yourself, in which case you’re responsible for deallocating it when you no longer need it.
- `desired_histogram`: The histograms that the operation applies to the source buffer.
- `histogram_entries`: The number of histogram entries.
- `minVal`: The minimum pixel value. The operation assigns pixel values less than   to the first histogram entry.
- `maxVal`: The maximum pixel value. The operation assigns pixel values greater than   to the last histogram entry.
- `flags`: To specify that the function doesn’t apply the operation to the alpha channel, set the   flag.

## See Also

- [Enhancing image contrast with histogram manipulation](enhancing-image-contrast-with-histogram-manipulation.md)
  Enhance and adjust the contrast of an image with histogram equalization and contrast stretching.
- [Specifying histograms with vImage](specifying-histograms-with-vimage.md)
  Calculate the histogram of one image, and apply it to a second image.
- [func vImageHistogramSpecification_Planar8(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImagePixelCount>, vImage_Flags) -> vImage_Error](vimagehistogramspecification_planar8(_:_:_:_:).md)
  Specifies the histogram of an 8-bit planar buffer.
- [func vImageHistogramSpecification_PlanarF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutableRawPointer!, UnsafePointer<vImagePixelCount>, UInt32, Pixel_F, Pixel_F, vImage_Flags) -> vImage_Error](vimagehistogramspecification_planarf(_:_:_:_:_:_:_:_:).md)
  Specifies the histogram of a 32-bit planar buffer.
- [func vImageHistogramSpecification_ARGB8888(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutablePointer<UnsafePointer<vImagePixelCount>?>, vImage_Flags) -> vImage_Error](vimagehistogramspecification_argb8888(_:_:_:_:).md)
  Specifies the histogram of an 8-bit-per-channel, 4-channel interleaved buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimagehistogramspecification_argbffff(_:_:_:_:_:_:_:_:))*