# specifyHistogram(_:destination:)

**Framework**: Accelerate  
**Kind**: method  
**Role**: Instance Method

Performs a histogram specification operation on a 32-bit-per-channel, 4-channel interleaved pixel buffer.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS
- watchOS 9.0+

## Declaration

```swift
func specifyHistogram(_ histogram: vImage.PixelBuffer<Format>.HistogramFFFF, destination: vImage.PixelBuffer<Format>)
```

Available when `Format` is `vImage.InterleavedFx4`.

## Discussion

*Histogram specification* is a technique that allows you to calculate the histogram of a reference image and apply it to an input image.

The example below shows a source image (bottom left) and a histogram reference image (top left), with the histogram specification output on the right:

![Photos showing original image, histogram source image, and histogram specified result.](https://developer.apple.com/tutorials/images/com.apple.accelerate/media-3958163@2x.png)

The code below initializes the source and reference buffers from the [`CGImage`](../../../CoreGraphics/cgimage.md) instances `sourceImage` and `referenceImage` respectively:

```swift
var cgImageFormat = vImage_CGImageFormat(
    bitsPerComponent: 8,
    bitsPerPixel: 8 * 4,
    colorSpace: CGColorSpaceCreateDeviceRGB(),
    bitmapInfo: CGBitmapInfo(rawValue: CGImageAlphaInfo.noneSkipFirst.rawValue))!

let sourceBuffer = try vImage.PixelBuffer(
    cgImage: sourceImage,
    cgImageFormat: &cgImageFormat,
    pixelFormat: vImage.InterleavedFx4.self)

let referenceBuffer = try vImage.PixelBuffer(
    cgImage: referenceImage,
    cgImageFormat: &cgImageFormat,
    pixelFormat: vImage.InterleavedFx4.self)
```

The following code calls [`histogram()`](./histogram%28%29-14a38.md) to calculate the histogram of the reference image and passes the histogram to [`specifyHistogram(_:destination:)`](./specifyhistogram%28_,destination%29-7xiz4.md) to generate the specification result. This function works in place, that is, the input and output can share the same underlying memory:

```swift
let histogram = referenceBuffer.histogram(binCount: 1024)

sourceBuffer.specifyHistogram(histogram,
                              destination: sourceBuffer)
```

## Parameters

- `histogram`: The histogram.
- `destination`: The destination pixel buffer.

## See Also

### Related Documentation
- [Specifying histograms with vImage](../../specifying-histograms-with-vimage.md)
  Calculate the histogram of one image, and apply it to a second image.
### Histogram specification
- [func specifyHistogram(vImage.PixelBuffer<Format>.Histogram8888, destination: vImage.PixelBuffer<Format>)](./specifyhistogram%28_,destination%29-7xiz4.md)
  Performs a histogram specification operation on an 8-bit-per-channel, 4-channel interleaved pixel buffer.
- [func specifyHistogram(vImage.PixelBuffer<Format>.Histogram888, destination: vImage.PixelBuffer<Format>)](./specifyhistogram%28_,destination%29-qeqr.md)
  Performs a histogram specification operation on an 8-bit-per-channel, 3-channel multiple-plane pixel buffer.
- [func specifyHistogram(vImage.PixelBuffer<Format>.HistogramFFF, destination: vImage.PixelBuffer<Format>)](./specifyhistogram%28_,destination%29-28844.md)
  Performs a histogram specification operation on a 32-bit-per-channel, 3-channel multiple-plane pixel buffer.
- [func specifyHistogram(vImage.PixelBuffer<Format>.Histogram8888, destination: vImage.PixelBuffer<Format>)](./specifyhistogram%28_,destination%29-73dpr.md)
  Performs a histogram specification operation on an 8-bit-per-channel, 4-channel multiple-plane pixel buffer.
- [func specifyHistogram(vImage.PixelBuffer<Format>.HistogramFFFF, destination: vImage.PixelBuffer<Format>)](./specifyhistogram%28_,destination%29-7cvk1.md)
  Performs a histogram specification operation on a 32-bit-per-channel, 3-channel multiple-plane pixel buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimage/pixelbuffer/specifyhistogram(_:destination:)-1x46n)*