# vImageHistogramSpecification_ARGB8888(_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

Specifies the histogram of an 8-bit-per-channel, 4-channel interleaved buffer.

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
func vImageHistogramSpecification_ARGB8888(_ src: UnsafePointer<vImage_Buffer>, _ dest: UnsafePointer<vImage_Buffer>, _ desired_histogram: UnsafeMutablePointer<UnsafePointer<vImagePixelCount>?>, _ flags: vImage_Flags) -> vImage_Error
```

```c
vImage_Error vImageHistogramSpecification_ARGB8888(const vImage_Buffer *src, const vImage_Buffer *dest, const vImagePixelCount * desired_histogram[4], vImage_Flags flags);
```

#### Return Value

[`kvImageNoError`](./kvimagenoerror.md); otherwise, one of the error codes in [Data Types and Constants](./data-types-and-constants.md).

#### Discussion

Use this function to apply a histogram — that you’ve generated using [`vImageHistogramSpecification_ARGBFFFF(_:_:_:_:_:_:_:_:)`](./vimagehistogramspecification_argbffff%28_,_,_,_,_,_,_,_%29.md) — to each channel of another image.

The following code applies a histogram to a four-channel interleaved vImage buffer:

**Swift**:

```swift
let source = vImage.PixelBuffer<vImage.Interleaved8x4>(
    pixelValues: [10, 20, 30, 40,
                  50, 60, 70, 80],
    size: .init(width: 1, height: 2))

var histogramAlpha = [vImagePixelCount](repeating: 0, count: 256)
var histogramRed   = [vImagePixelCount](repeating: 0, count: 256)
var histogramGreen = [vImagePixelCount](repeating: 0, count: 256)
var histogramBlue  = [vImagePixelCount](repeating: 0, count: 256)

histogramAlpha[64] = 1; histogramAlpha[192] = 1
histogramRed[64]   = 1; histogramRed[192]   = 1
histogramGreen[64] = 1; histogramGreen[192] = 1
histogramBlue[64]  = 1; histogramBlue[192]  = 1

let destination = vImage.PixelBuffer<vImage.Interleaved8x4>(
    size: .init(width: 1, height: 2))

source.withUnsafePointerToVImageBuffer { src in
    destination.withUnsafePointerToVImageBuffer { dest in
        histogramAlpha.withUnsafeBufferPointer { zeroPtr in
            histogramRed.withUnsafeBufferPointer { onePtr in
                histogramGreen.withUnsafeBufferPointer { twoPtr in
                    histogramBlue.withUnsafeBufferPointer { threePtr in
                        
                        var histogramBins = [zeroPtr.baseAddress, onePtr.baseAddress,
                                             twoPtr.baseAddress, threePtr.baseAddress]
                        
                        histogramBins.withUnsafeMutableBufferPointer { histogramBinsPtr in
                            _ = vImageHistogramSpecification_ARGB8888(src,
                                                                      dest,
                                                                      histogramBinsPtr.baseAddress!,
                                                                      vImage_Flags(kvImageNoFlags))
                        }
                    }
                }
            }
        }
    }
}

// Prints "[64, 64, 64, 64, 192, 192, 192, 192]".
print(destination.array)
```

**Objective-C**:

```objc
// All `histogramAlpha`, `histogramRed`, `histogramGreen`, and `histogramBlue` are 256-element arrays.
const vImagePixelCount *histogramBins[4] = {
    histogramAlpha, histogramRed, histogramGreen, histogramBlue
};

// The `buffer` is a `vImage_Buffer` structure.
vImageHistogramSpecification_ARGB8888(&buffer, &buffer,
                                      histogramBins,
                                      kvImageNoFlags);
```

## Parameters

- `src`: The source vImage buffer.
- `dest`: A pointer to the destination vImage buffer structure. You’re responsible for filling out the [`height`](./vimage_buffer/height.md), [`width`](./vimage_buffer/width.md), and [`rowBytes`](./vimage_buffer/rowbytes.md) fields of this structure, and for allocating a data buffer of the appropriate size. On return, the data buffer this structure points to contains the destination image data. When you no longer need the data buffer, deallocate the memory to prevent memory leaks.
- `desired_histogram`: The histograms that the operation applies to the source buffer.
- `flags`: The options to use when performing the operation. If your code implements its own tiling or its own multithreading, pass [`kvImageDoNotTile`](./kvimagedonottile.md); otherwise, pass [`kvImageNoFlags`](./kvimagenoflags.md).

  To specify that the function doesn’t apply the operation to the alpha channel, set the [`kvImageLeaveAlphaUnchanged`](./kvimageleavealphaunchanged.md) flag.

## See Also

### Related Documentation
- [Enhancing image contrast with histogram manipulation](./enhancing-image-contrast-with-histogram-manipulation.md)
  Enhance and adjust the contrast of an image with histogram equalization and contrast stretching.
- [Specifying histograms with vImage](./specifying-histograms-with-vimage.md)
  Calculate the histogram of one image, and apply it to a second image.
### Specifying a histogram
- [func vImageHistogramSpecification_Planar8(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImagePixelCount>, vImage_Flags) -> vImage_Error](./vimagehistogramspecification_planar8%28_,_,_,_%29.md)
  Specifies the histogram of an 8-bit planar buffer.
- [func vImageHistogramSpecification_PlanarF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutableRawPointer!, UnsafePointer<vImagePixelCount>, UInt32, Pixel_F, Pixel_F, vImage_Flags) -> vImage_Error](./vimagehistogramspecification_planarf%28_,_,_,_,_,_,_,_%29.md)
  Specifies the histogram of a 32-bit planar buffer.
- [func vImageHistogramSpecification_ARGBFFFF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutableRawPointer!, UnsafeMutablePointer<UnsafePointer<vImagePixelCount>?>!, UInt32, Pixel_F, Pixel_F, vImage_Flags) -> vImage_Error](./vimagehistogramspecification_argbffff%28_,_,_,_,_,_,_,_%29.md)
  Specifes the histogram of a 32-bit-per-channel, 4-channel interleaved buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimagehistogramspecification_argb8888(_:_:_:_:))*