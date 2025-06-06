# vImageEqualization_ARGBFFFF(_:_:_:_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Performs histogram equalization on a 32-bit-per-channel, 4-channel interleaved buffer.

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
func vImageEqualization_ARGBFFFF(_ src: UnsafePointer<vImage_Buffer>, _ dest: UnsafePointer<vImage_Buffer>, _ tempBuffer: UnsafeMutableRawPointer!, _ histogram_entries: UInt32, _ minVal: Pixel_F, _ maxVal: Pixel_F, _ flags: vImage_Flags) -> vImage_Error
```

#### Return Value

[`kvImageNoError`](kvimagenoerror.md); otherwise, one of the error codes in [`Data Types and Constants`](data-types-and-constants.md).

#### Discussion

Histogram equalization transforms an image so that its histogram is more uniformly distributed across the entire range of values. The operation stretches dense parts of the histogram, where contrast is low, and condenses sparse parts of the histogram, where contrast is high. A truly uniform histogram is one in which each histogram bin contains the same value, that is, its cumulative histogram is a diagonal line. The vImage histogram equalization functions approximate that truly uniform histogram.

## Parameters

- `src`: The source vImage buffer.
- `dest`: A pointer to the destination vImage buffer structure. You’re responsible for filling out the  ,  , and   fields of this structure, and for allocating a data buffer of the appropriate size. On return, the data buffer this structure points to contains the destination image data. When you no longer need the data buffer, deallocate the memory to prevent memory leaks.
- `tempBuffer`: A pointer to a temporary buffer. If you pass  , the function allocates the buffer and then deallocates it before returning. Alternatively, you can allocate the buffer yourself, in which case you’re responsible for deallocating it when you no longer need it.
- `histogram_entries`: The number of histogram entries.
- `minVal`: The minimum pixel value. The operation assigns pixel values less than   to the first histogram entry.
- `maxVal`: The maximum pixel value. The operation assigns pixel values greater than   to the last histogram entry.
- `flags`: To specify that the function doesn’t apply the operation to the alpha channel, set the   flag.

## See Also

- [Enhancing image contrast with histogram manipulation](enhancing-image-contrast-with-histogram-manipulation.md)
  Enhance and adjust the contrast of an image with histogram equalization and contrast stretching.
- [Specifying histograms with vImage](specifying-histograms-with-vimage.md)
  Calculate the histogram of one image, and apply it to a second image.
- [func vImageEqualization_Planar8(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimageequalization_planar8(_:_:_:).md)
  Performs histogram equalization on an 8-bit planar buffer.
- [func vImageEqualization_PlanarF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutableRawPointer!, UInt32, Pixel_F, Pixel_F, vImage_Flags) -> vImage_Error](vimageequalization_planarf(_:_:_:_:_:_:_:).md)
  Performs histogram equalization on a 32-bit planar buffer.
- [func vImageEqualization_ARGB8888(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimageequalization_argb8888(_:_:_:).md)
  Performs histogram equalization on an 8-bit-per-channel, 4-channel interleaved buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimageequalization_argbffff(_:_:_:_:_:_:_:))*