# vImageEndsInContrastStretch_Planar8(_:_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Performs ends-in contrast stretching on an 8-bit planar buffer.

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
func vImageEndsInContrastStretch_Planar8(_ src: UnsafePointer<vImage_Buffer>, _ dest: UnsafePointer<vImage_Buffer>, _ percent_low: UInt32, _ percent_high: UInt32, _ flags: vImage_Flags) -> vImage_Error
```

#### Return Value

[`kvImageNoError`](kvimagenoerror.md); otherwise, one of the error codes in [`Data Types and Constants`](data-types-and-constants.md).

#### Discussion

Contrast stretching evenly distributes a histogram’s pixel values across the full range of available pixel values. This technique is ideal for enhancing the contrast of an image with pixel values concentrated in one area of the intensity spectrum.

## Parameters

- `src`: The source vImage buffer.
- `dest`: A pointer to the destination vImage buffer structure. You’re responsible for filling out the  ,  , and   fields of this structure, and for allocating a data buffer of the appropriate size. On return, the data buffer this structure points to contains the destination image data. When you no longer need the data buffer, deallocate the memory to prevent memory leaks.
- `percent_low`: The percentage of pixels that the operation maps to the lowest end of the transformed image’s histogram.
- `percent_high`: The percentage of pixels that the operation maps to the highest end of the transformed image’s histogram.
- `flags`: The options to use when performing the operation. If your code implements its own tiling or its own multithreading, pass  ; otherwise, pass  .

## See Also

- [Enhancing image contrast with histogram manipulation](enhancing-image-contrast-with-histogram-manipulation.md)
  Enhance and adjust the contrast of an image with histogram equalization and contrast stretching.
- [Specifying histograms with vImage](specifying-histograms-with-vimage.md)
  Calculate the histogram of one image, and apply it to a second image.
- [func vImageEndsInContrastStretch_PlanarF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutableRawPointer!, UInt32, UInt32, UInt32, Pixel_F, Pixel_F, vImage_Flags) -> vImage_Error](vimageendsincontraststretch_planarf(_:_:_:_:_:_:_:_:_:).md)
  Performs ends-in contrast stretching on a 32-bit planar buffer.
- [func vImageEndsInContrastStretch_ARGB8888(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<UInt32>, UnsafePointer<UInt32>, vImage_Flags) -> vImage_Error](vimageendsincontraststretch_argb8888(_:_:_:_:_:).md)
  Performs ends-in contrast stretching on an 8-bit-per-channel, 4-channel interleaved buffer.
- [func vImageEndsInContrastStretch_ARGBFFFF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutableRawPointer!, UnsafePointer<UInt32>, UnsafePointer<UInt32>, UInt32, Pixel_F, Pixel_F, vImage_Flags) -> vImage_Error](vimageendsincontraststretch_argbffff(_:_:_:_:_:_:_:_:_:).md)
  Performs ends-in contrast stretching on a 32-bit-per-channel, 4-channel interleaved buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimageendsincontraststretch_planar8(_:_:_:_:_:))*