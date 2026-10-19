# vImageHistogramCalculation_PlanarF(_:_:_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Calculates the histogram of a 32-bit planar buffer.

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
func vImageHistogramCalculation_PlanarF(_ src: UnsafePointer<vImage_Buffer>, _ histogram: UnsafeMutablePointer<vImagePixelCount>, _ histogram_entries: UInt32, _ minVal: Pixel_F, _ maxVal: Pixel_F, _ flags: vImage_Flags) -> vImage_Error
```

#### Return Value

[`kvImageNoError`](kvimagenoerror.md); otherwise, one of the error codes in [`Data Types and Constants`](data-types-and-constants.md).

#### Discussion

The following code populates the `histogram` array with the histogram of the specified [`vImage_Buffer`](vimage_buffer.md) structure:

**Swift**:

```swift
let source = vImage.PixelBuffer<vImage.PlanarF>(
    pixelValues: [0.1, 0.4, 0.7, 1.0],
    size: .init(width: 4, height: 1))

let entryCount = 64
var histogram = [vImagePixelCount](repeating: 0, count: entryCount)

source.withUnsafePointerToVImageBuffer { src in
    _ = vImageHistogramCalculation_PlanarF(src,
                                           &histogram,
                                           UInt32(entryCount),
                                           0, 1,
                                           vImage_Flags(kvImageNoFlags))
}

// Prints "1 1 1 1".
print(histogram[6], histogram[25], histogram[44], histogram[63])
```

**Objective-C**:

```objc
float src[4] = {0.1f, 0.4f, 0.7f, 1.0f};

vImage_Buffer srcBuf = {
    .data = src,
    .width = 4,
    .height = 1,
    .rowBytes = 16
};

unsigned int entryCount = 64;
vImagePixelCount histogram[64] = {0};

vImageHistogramCalculation_PlanarF(&srcBuf, histogram,
                                   entryCount, 0, 1,
                                   kvImageNoFlags);

// Prints "1 1 1 1".
printf("%lu %lu %lu %lu\n",
       (unsigned long)histogram[6],  (unsigned long)histogram[25],
       (unsigned long)histogram[44], (unsigned long)histogram[63]);
```

## Parameters

- `src`: The source vImage buffer.
- `histogram`: The collection that contains `histogram_entries` elements that receives the histogram data.
- `histogram_entries`: The number of histogram entries.
- `minVal`: The minimum pixel value. The operation assigns pixel values less than `minVal` to the first histogram entry.
- `maxVal`: The maximum pixel value. The operation assigns pixel values greater than `maxVal` to the last histogram entry.
- `flags`: The options to use when performing the operation. If your code implements its own tiling or its own multithreading, pass [`kvImageDoNotTile`](kvimagedonottile.md); otherwise, pass [`kvImageNoFlags`](kvimagenoflags.md).

## See Also

- [Enhancing image contrast with histogram manipulation](enhancing-image-contrast-with-histogram-manipulation.md)
  Enhance and adjust the contrast of an image with histogram equalization and contrast stretching.
- [Specifying histograms with vImage](specifying-histograms-with-vimage.md)
  Calculate the histogram of one image, and apply it to a second image.
- [func vImageHistogramCalculation_Planar8(UnsafePointer<vImage_Buffer>, UnsafeMutablePointer<vImagePixelCount>, vImage_Flags) -> vImage_Error](vimagehistogramcalculation_planar8(_:_:_:).md)
  Calculates the histogram of an 8-bit planar buffer.
- [func vImageHistogramCalculation_ARGB8888(UnsafePointer<vImage_Buffer>, UnsafeMutablePointer<UnsafeMutablePointer<vImagePixelCount>?>, vImage_Flags) -> vImage_Error](vimagehistogramcalculation_argb8888(_:_:_:).md)
  Calculates the histogram of an 8-bit-per-channel, 4-channel interleaved buffer.
- [func vImageHistogramCalculation_ARGBFFFF(UnsafePointer<vImage_Buffer>, UnsafeMutablePointer<UnsafeMutablePointer<vImagePixelCount>?>, UInt32, Pixel_F, Pixel_F, vImage_Flags) -> vImage_Error](vimagehistogramcalculation_argbffff(_:_:_:_:_:_:).md)
  Calculates the histogram of a 32-bit-per-channel, 4-channel interleaved buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimagehistogramcalculation_planarf(_:_:_:_:_:_:))*