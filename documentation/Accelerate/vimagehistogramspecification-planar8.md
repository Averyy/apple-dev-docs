# vImageHistogramSpecification_Planar8(_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Specifies the histogram of an 8-bit planar buffer.

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
func vImageHistogramSpecification_Planar8(_ src: UnsafePointer<vImage_Buffer>, _ dest: UnsafePointer<vImage_Buffer>, _ desired_histogram: UnsafePointer<vImagePixelCount>, _ flags: vImage_Flags) -> vImage_Error
```

#### Return Value

[`kvImageNoError`](kvimagenoerror.md); otherwise, one of the error codes in [`Data Types and Constants`](data-types-and-constants.md).

#### Discussion

Use this function to apply a histogram — that you’ve generated using [`vImageHistogramCalculation_Planar8(_:_:_:)`](vimagehistogramcalculation_planar8(_:_:_:).md) — to another image.

The following code applies a histogram to a planar vImage buffer:

```swift
// `histogram` is a 256-element array.
histogram.withUnsafeBufferPointer {
    // `buffer` is a `vImage_Buffer` structure.
    _ = vImageHistogramSpecification_Planar8(&buffer, &buffer,
                                             $0.baseAddress!,
                                             vImage_Flags(kvImageNoFlags))
}
```

## Parameters

- `src`: The source vImage buffer.
- `dest`: A pointer to the destination vImage buffer structure. You’re responsible for filling out the  ,  , and   fields of this structure, and for allocating a data buffer of the appropriate size. On return, the data buffer this structure points to contains the destination image data. When you no longer need the data buffer, deallocate the memory to prevent memory leaks.
- `desired_histogram`: The histogram that the operation applies to the source buffer.
- `flags`: The options to use when performing the operation. If your code implements its own tiling or its own multithreading, pass  ; otherwise, pass  .

## See Also

- [Enhancing image contrast with histogram manipulation](enhancing-image-contrast-with-histogram-manipulation.md)
  Enhance and adjust the contrast of an image with histogram equalization and contrast stretching.
- [Specifying histograms with vImage](specifying-histograms-with-vimage.md)
  Calculate the histogram of one image, and apply it to a second image.
- [func vImageHistogramSpecification_PlanarF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutableRawPointer!, UnsafePointer<vImagePixelCount>, UInt32, Pixel_F, Pixel_F, vImage_Flags) -> vImage_Error](vimagehistogramspecification_planarf(_:_:_:_:_:_:_:_:).md)
  Specifies the histogram of a 32-bit planar buffer.
- [func vImageHistogramSpecification_ARGB8888(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutablePointer<UnsafePointer<vImagePixelCount>?>, vImage_Flags) -> vImage_Error](vimagehistogramspecification_argb8888(_:_:_:_:).md)
  Specifies the histogram of an 8-bit-per-channel, 4-channel interleaved buffer.
- [func vImageHistogramSpecification_ARGBFFFF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutableRawPointer!, UnsafeMutablePointer<UnsafePointer<vImagePixelCount>?>!, UInt32, Pixel_F, Pixel_F, vImage_Flags) -> vImage_Error](vimagehistogramspecification_argbffff(_:_:_:_:_:_:_:_:).md)
  Specifes the histogram of a 32-bit-per-channel, 4-channel interleaved buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimagehistogramspecification_planar8(_:_:_:_:))*