# vImageHistogramCalculation_ARGBFFFF(_:_:_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

Calculates the histogram of a 32-bit-per-channel, 4-channel interleaved buffer.

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
func vImageHistogramCalculation_ARGBFFFF(_ src: UnsafePointer<vImage_Buffer>, _ histogram: UnsafeMutablePointer<UnsafeMutablePointer<vImagePixelCount>?>, _ histogram_entries: UInt32, _ minVal: Pixel_F, _ maxVal: Pixel_F, _ flags: vImage_Flags) -> vImage_Error
```

```c
vImage_Error vImageHistogramCalculation_ARGBFFFF(const vImage_Buffer *src, vImagePixelCount * histogram[4], unsigned int histogram_entries, Pixel_F minVal, Pixel_F maxVal, vImage_Flags flags);
```

#### Return Value

[`kvImageNoError`](./kvimagenoerror.md); otherwise, one of the error codes in [Data Types and Constants](./data-types-and-constants.md).

#### Discussion

The following code populates the `histogramAlpha` , `histogramRed`, `histogramGreen`, and `histogramBlue` arrays with the histograms for each channel of the specified [`vImage_Buffer`](./vimage_buffer.md) structure:

**Swift**:

```swift
let source = vImage.PixelBuffer<vImage.InterleavedFx4>(
    pixelValues: [0.1, 0.2, 0.3, 0.4,
                  0.5, 0.6, 0.7, 0.8],
    size: .init(width: 1, height: 2))

let entryCount = 64
var histogramAlpha = [vImagePixelCount](repeating: 0, count: entryCount)
var histogramRed = [vImagePixelCount](repeating: 0, count: entryCount)
var histogramGreen = [vImagePixelCount](repeating: 0, count: entryCount)
var histogramBlue = [vImagePixelCount](repeating: 0, count: entryCount)

source.withUnsafePointerToVImageBuffer { src in
    histogramAlpha.withUnsafeMutableBufferPointer { zeroPtr in
        histogramRed.withUnsafeMutableBufferPointer { onePtr in
            histogramGreen.withUnsafeMutableBufferPointer { twoPtr in
                histogramBlue.withUnsafeMutableBufferPointer { threePtr in
                    
                    var histogramBins = [zeroPtr.baseAddress, onePtr.baseAddress,
                                         twoPtr.baseAddress, threePtr.baseAddress]
                    
                    histogramBins.withUnsafeMutableBufferPointer { histogramBinsPtr in
                        _ = vImageHistogramCalculation_ARGBFFFF(src,
                                                                histogramBinsPtr.baseAddress!,
                                                                UInt32(entryCount),
                                                                0, 1,
                                                                vImage_Flags(kvImageNoFlags))
                    }
                }
            }
        }
    }
}

// Prints:
// Alpha: 1 1
// Red:   1 1
// Green: 1 1
// Blue:  1 1
print("Alpha:", histogramAlpha[6],  histogramAlpha[32])
print("Red:  ", histogramRed[12],   histogramRed[38])
print("Green:", histogramGreen[19], histogramGreen[44])
print("Blue: ", histogramBlue[25],  histogramBlue[51])
```

**Objective-C**:

```objc
float src[8] = {0.1f, 0.2f, 0.3f, 0.4f,
                0.5f, 0.6f, 0.7f, 0.8f};

vImage_Buffer srcBuf = {
    .data = src,
    .width = 1,
    .height = 2,
    .rowBytes = 16
};

unsigned int entryCount = 64;
vImagePixelCount histogramAlpha[64] = {0};
vImagePixelCount histogramRed[64]   = {0};
vImagePixelCount histogramGreen[64] = {0};
vImagePixelCount histogramBlue[64]  = {0};

vImagePixelCount *histogramBins[4] = {
    histogramAlpha, histogramRed, histogramGreen, histogramBlue
};

vImageHistogramCalculation_ARGBFFFF(&srcBuf, histogramBins,
                                    entryCount, 0, 1,
                                    kvImageNoFlags);

// Prints:
// Alpha: 1 1
// Red:   1 1
// Green: 1 1
// Blue:  1 1
printf("Alpha: %lu %lu\n", (unsigned long)histogramAlpha[6],  (unsigned long)histogramAlpha[32]);
printf("Red:   %lu %lu\n", (unsigned long)histogramRed[12],   (unsigned long)histogramRed[38]);
printf("Green: %lu %lu\n", (unsigned long)histogramGreen[19], (unsigned long)histogramGreen[44]);
printf("Blue:  %lu %lu\n", (unsigned long)histogramBlue[25],  (unsigned long)histogramBlue[51]);
```

## Parameters

- `src`: The source vImage buffer.
- `histogram`: An array of four collections that contain `histogram_entries` elements that receive the histogram data.
- `histogram_entries`: The number of histogram entries.
- `minVal`: The minimum pixel value. The operation assigns pixel values less than `minVal` to the first histogram entry.
- `maxVal`: The maximum pixel value. The operation assigns pixel values greater than `maxVal` to the last histogram entry.
- `flags`: The options to use when performing the operation. If your code implements its own tiling or its own multithreading, pass [`kvImageDoNotTile`](./kvimagedonottile.md); otherwise, pass [`kvImageNoFlags`](./kvimagenoflags.md).

  To specify that the function doesn’t calculate the alpha channel histogram, set the [`kvImageLeaveAlphaUnchanged`](./kvimageleavealphaunchanged.md) flag.

## See Also

### Related Documentation
- [Enhancing image contrast with histogram manipulation](./enhancing-image-contrast-with-histogram-manipulation.md)
  Enhance and adjust the contrast of an image with histogram equalization and contrast stretching.
- [Specifying histograms with vImage](./specifying-histograms-with-vimage.md)
  Calculate the histogram of one image, and apply it to a second image.
### Calculating a histogram
- [func vImageHistogramCalculation_Planar8(UnsafePointer<vImage_Buffer>, UnsafeMutablePointer<vImagePixelCount>, vImage_Flags) -> vImage_Error](./vimagehistogramcalculation_planar8%28_,_,_%29.md)
  Calculates the histogram of an 8-bit planar buffer.
- [func vImageHistogramCalculation_PlanarF(UnsafePointer<vImage_Buffer>, UnsafeMutablePointer<vImagePixelCount>, UInt32, Pixel_F, Pixel_F, vImage_Flags) -> vImage_Error](./vimagehistogramcalculation_planarf%28_,_,_,_,_,_%29.md)
  Calculates the histogram of a 32-bit planar buffer.
- [func vImageHistogramCalculation_ARGB8888(UnsafePointer<vImage_Buffer>, UnsafeMutablePointer<UnsafeMutablePointer<vImagePixelCount>?>, vImage_Flags) -> vImage_Error](./vimagehistogramcalculation_argb8888%28_,_,_%29.md)
  Calculates the histogram of an 8-bit-per-channel, 4-channel interleaved buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimagehistogramcalculation_argbffff(_:_:_:_:_:_:))*