# vImageHistogramCalculation_ARGB8888(_:_:_:)

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

Calculates the histogram of an 8-bit-per-channel, 4-channel interleaved buffer.

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
func vImageHistogramCalculation_ARGB8888(_ src: UnsafePointer<vImage_Buffer>, _ histogram: UnsafeMutablePointer<UnsafeMutablePointer<vImagePixelCount>?>, _ flags: vImage_Flags) -> vImage_Error
```

```c
vImage_Error vImageHistogramCalculation_ARGB8888(const vImage_Buffer *src, vImagePixelCount * histogram[4], vImage_Flags flags);
```

#### Return Value

[`kvImageNoError`](./kvimagenoerror.md); otherwise, one of the error codes in [Data Types and Constants](./data-types-and-constants.md).

#### Discussion

The following code populates the `histogramAlpha` , `histogramRed`, `histogramGreen`, and `histogramBlue` arrays with the histograms for each channel of the specified [`vImage_Buffer`](./vimage_buffer.md) structure:

**Swift**:

```swift
let source = vImage.PixelBuffer<vImage.Interleaved8x4>(
    pixelValues: [10, 20, 30, 40,
                  50, 60, 70, 80],
    size: .init(width: 1, height: 2))

var histogramAlpha = [vImagePixelCount](repeating: 0, count: 256)
var histogramRed = [vImagePixelCount](repeating: 0, count: 256)
var histogramGreen = [vImagePixelCount](repeating: 0, count: 256)
var histogramBlue = [vImagePixelCount](repeating: 0, count: 256)

source.withUnsafePointerToVImageBuffer { src in
    histogramAlpha.withUnsafeMutableBufferPointer { zeroPtr in
        histogramRed.withUnsafeMutableBufferPointer { onePtr in
            histogramGreen.withUnsafeMutableBufferPointer { twoPtr in
                histogramBlue.withUnsafeMutableBufferPointer { threePtr in
                    
                    var histogramBins = [zeroPtr.baseAddress, onePtr.baseAddress,
                                         twoPtr.baseAddress, threePtr.baseAddress]
                    
                    histogramBins.withUnsafeMutableBufferPointer { histogramBinsPtr in
                        _ = vImageHistogramCalculation_ARGB8888(src,
                                                                histogramBinsPtr.baseAddress!,
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
print("Alpha:", histogramAlpha[10], histogramAlpha[50])
print("Red:  ", histogramRed[20],   histogramRed[60])
print("Green:", histogramGreen[30], histogramGreen[70])
print("Blue: ", histogramBlue[40],  histogramBlue[80])
```

**Objective-C**:

```objc
uint8_t src[8] = {10, 20, 30, 40, 50, 60, 70, 80};

vImage_Buffer srcBuf = {
    .data = src,
    .width = 1,
    .height = 2,
    .rowBytes = 4
};

vImagePixelCount histogramAlpha[256] = {0};
vImagePixelCount histogramRed[256]   = {0};
vImagePixelCount histogramGreen[256] = {0};
vImagePixelCount histogramBlue[256]  = {0};

vImagePixelCount *histogramBins[4] = {
    histogramAlpha, histogramRed, histogramGreen, histogramBlue
};

vImageHistogramCalculation_ARGB8888(&srcBuf, histogramBins, kvImageNoFlags);

// Prints:
// Alpha: 1 1
// Red:   1 1
// Green: 1 1
// Blue:  1 1
printf("Alpha: %lu %lu\n", (unsigned long)histogramAlpha[10], (unsigned long)histogramAlpha[50]);
printf("Red:   %lu %lu\n", (unsigned long)histogramRed[20],   (unsigned long)histogramRed[60]);
printf("Green: %lu %lu\n", (unsigned long)histogramGreen[30], (unsigned long)histogramGreen[70]);
printf("Blue:  %lu %lu\n", (unsigned long)histogramBlue[40],  (unsigned long)histogramBlue[80]);
```

## Parameters

- `src`: The source vImage buffer.
- `histogram`: An array of four collections that contain 256 elements that receive the histogram data.
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
- [func vImageHistogramCalculation_ARGBFFFF(UnsafePointer<vImage_Buffer>, UnsafeMutablePointer<UnsafeMutablePointer<vImagePixelCount>?>, UInt32, Pixel_F, Pixel_F, vImage_Flags) -> vImage_Error](./vimagehistogramcalculation_argbffff%28_,_,_,_,_,_%29.md)
  Calculates the histogram of a 32-bit-per-channel, 4-channel interleaved buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimagehistogramcalculation_argb8888(_:_:_:))*