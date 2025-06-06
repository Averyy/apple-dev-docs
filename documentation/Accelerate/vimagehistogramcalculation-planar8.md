# vImageHistogramCalculation_Planar8(_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Calculates the histogram of an 8-bit planar buffer.

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
func vImageHistogramCalculation_Planar8(_ src: UnsafePointer<vImage_Buffer>, _ histogram: UnsafeMutablePointer<vImagePixelCount>, _ flags: vImage_Flags) -> vImage_Error
```

#### Return Value

[`kvImageNoError`](kvimagenoerror.md); otherwise, one of the error codes in [`Data Types and Constants`](data-types-and-constants.md).

#### Discussion

The following code populates the `histogram` array with the histogram of the specified [`vImage_Buffer`](vimage_buffer.md) structure.

```swift
var histogram = [vImagePixelCount](repeating: 0, count: 256)

// `buffer` is a `vImage_Buffer` structure.
_ = vImageHistogramCalculation_Planar8(&buffer,
                                       &histogram,
                                       vImage_Flags(kvImageNoFlags))
```

## Parameters

- `src`: The source vImage buffer.
- `histogram`: The collection that contains 256 elements that receives the histogram data.
- `flags`: The options to use when performing the operation. If your code implements its own tiling or its own multithreading, pass  ; otherwise, pass  .

## See Also

- [Enhancing image contrast with histogram manipulation](enhancing-image-contrast-with-histogram-manipulation.md)
  Enhance and adjust the contrast of an image with histogram equalization and contrast stretching.
- [Specifying histograms with vImage](specifying-histograms-with-vimage.md)
  Calculate the histogram of one image, and apply it to a second image.
- [func vImageHistogramCalculation_PlanarF(UnsafePointer<vImage_Buffer>, UnsafeMutablePointer<vImagePixelCount>, UInt32, Pixel_F, Pixel_F, vImage_Flags) -> vImage_Error](vimagehistogramcalculation_planarf(_:_:_:_:_:_:).md)
  Calculates the histogram of a 32-bit planar buffer.
- [func vImageHistogramCalculation_ARGB8888(UnsafePointer<vImage_Buffer>, UnsafeMutablePointer<UnsafeMutablePointer<vImagePixelCount>?>, vImage_Flags) -> vImage_Error](vimagehistogramcalculation_argb8888(_:_:_:).md)
  Calculates the histogram of an 8-bit-per-channel, 4-channel interleaved buffer.
- [func vImageHistogramCalculation_ARGBFFFF(UnsafePointer<vImage_Buffer>, UnsafeMutablePointer<UnsafeMutablePointer<vImagePixelCount>?>, UInt32, Pixel_F, Pixel_F, vImage_Flags) -> vImage_Error](vimagehistogramcalculation_argbffff(_:_:_:_:_:_:).md)
  Calculates the histogram of a 32-bit-per-channel, 4-channel interleaved buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimagehistogramcalculation_planar8(_:_:_:))*