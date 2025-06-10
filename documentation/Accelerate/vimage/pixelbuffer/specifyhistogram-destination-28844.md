# specifyHistogram(_:destination:)

**Framework**: Accelerate  
**Kind**: method

Performs a histogram specification operation on a 32-bit-per-channel, 3-channel multiple-plane pixel buffer.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst ?+
- macOS 13.0+
- tvOS 16.0+
- visionOS ?+
- watchOS 9.0+

## Declaration

```swift
func specifyHistogram(_ histogram: vImage.PixelBuffer<Format>.HistogramFFF, destination: vImage.PixelBuffer<Format>)
```

#### Discussion

 is a technique that allows you to calculate the histogram of a reference image and apply it to an input image.

The example below shows a source image (bottom left) and a histogram reference image (top left), with the histogram specification output on the right:

![Photos showing original image, histogram source image, and histogram specified result.](https://docs-assets.developer.apple.com/published/227e8dda814cb49fe07834e4436fdc61/media-3958176%402x.png)

The code below initializes the source and reference buffers from the [`CGImage`](https://developer.apple.com/documentation/CoreGraphics/CGImage) instances `sourceImage` and `referenceImage` respectively:

```swift
var cgImageFormat = vImage_CGImageFormat(
    bitsPerComponent: 32,
    bitsPerPixel: 32 * 3,
    colorSpace: CGColorSpaceCreateDeviceRGB(),
    bitmapInfo: CGBitmapInfo(rawValue: CGBitmapInfo.byteOrder32Little.rawValue |
                             CGBitmapInfo.floatComponents.rawValue |
                             CGImageAlphaInfo.none.rawValue))!

let interleavedSource = try vImage.PixelBuffer(
    cgImage: sourceImage,
    cgImageFormat: &cgImageFormat,
    pixelFormat: vImage.InterleavedFx3.self)
let multiplePlaneSource = vImage.PixelBuffer<vImage.PlanarFx3>(
    planarBuffers: interleavedSource.planarBuffers())

let interleavedReference = try vImage.PixelBuffer(
    cgImage: referenceImage,
    cgImageFormat: &cgImageFormat,
    pixelFormat: vImage.InterleavedFx3.self)
let multiplePlaneReference = vImage.PixelBuffer<vImage.PlanarFx3>(
    planarBuffers: interleavedReference.planarBuffers())
```

The following code calls [`histogram()`](vimage/pixelbuffer/histogram()-14a38.md) to calculate the histogram of the reference image and passes the histogram to [`specifyHistogram(_:destination:)`](vimage/pixelbuffer/specifyhistogram(_:destination:)-7xiz4.md) to generate the specification result. This function works in place, that is, the input and output can share the same underlying memory.

```swift
let histogram = multiplePlaneReference.histogram(binCount: 1024)

multiplePlaneSource.specifyHistogram(histogram,
                                     destination: multiplePlaneSource)
```

## Parameters

- `histogram`: The histogram.
- `destination`: The destination pixel buffer.

## See Also

- [Specifying histograms with vImage](specifying-histograms-with-vimage.md)
  Calculate the histogram of one image, and apply it to a second image.
- [func specifyHistogram(vImage.PixelBuffer<Format>.Histogram8888, destination: vImage.PixelBuffer<Format>)](vimage/pixelbuffer/specifyhistogram(_:destination:)-7xiz4.md)
  Performs a histogram specification operation on an 8-bit-per-channel, 4-channel interleaved pixel buffer.
- [func specifyHistogram(vImage.PixelBuffer<Format>.HistogramFFFF, destination: vImage.PixelBuffer<Format>)](vimage/pixelbuffer/specifyhistogram(_:destination:)-1x46n.md)
  Performs a histogram specification operation on a 32-bit-per-channel, 4-channel interleaved pixel buffer.
- [func specifyHistogram(vImage.PixelBuffer<Format>.Histogram888, destination: vImage.PixelBuffer<Format>)](vimage/pixelbuffer/specifyhistogram(_:destination:)-qeqr.md)
  Performs a histogram specification operation on an 8-bit-per-channel, 3-channel multiple-plane pixel buffer.
- [func specifyHistogram(vImage.PixelBuffer<Format>.Histogram8888, destination: vImage.PixelBuffer<Format>)](vimage/pixelbuffer/specifyhistogram(_:destination:)-73dpr.md)
  Performs a histogram specification operation on an 8-bit-per-channel, 4-channel multiple-plane pixel buffer.
- [func specifyHistogram(vImage.PixelBuffer<Format>.HistogramFFFF, destination: vImage.PixelBuffer<Format>)](vimage/pixelbuffer/specifyhistogram(_:destination:)-7cvk1.md)
  Performs a histogram specification operation on a 32-bit-per-channel, 3-channel multiple-plane pixel buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimage/pixelbuffer/specifyhistogram(_:destination:)-28844)*