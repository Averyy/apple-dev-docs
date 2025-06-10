# histogram(binCount:)

**Framework**: Accelerate  
**Kind**: method

Calculates the histogram of a 32-bit-per-channel, 4-channel multiple-plane pixel buffer.

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
func histogram(binCount: Int) -> vImage.PixelBuffer<Format>.HistogramFFFF
```

#### Return Value

The histogram of the pixel buffer.

## Parameters

- `binCount`: The number of histogram entries for each channel.

## See Also

- [func specifyHistogram(vImage.PixelBuffer<Format>.HistogramFFFF, destination: vImage.PixelBuffer<Format>)](vimage/pixelbuffer/specifyhistogram(_:destination:)-7cvk1.md)
  Performs a histogram specification operation on a 32-bit-per-channel, 3-channel multiple-plane pixel buffer.
- [Specifying histograms with vImage](specifying-histograms-with-vimage.md)
  Calculate the histogram of one image, and apply it to a second image.
- [func histogram() -> vImage.PixelBuffer<Format>.Histogram8888](vimage/pixelbuffer/histogram-14a38.md)
  Calculates the histogram of an 8-bit-per-channel, 4-channel interleaved pixel buffer.
- [func histogram(binCount: Int) -> vImage.PixelBuffer<Format>.HistogramFFFF](vimage/pixelbuffer/histogram(bincount:)-6pkfv.md)
  Calculates the histogram of a 32-bit-per-channel, 4-channel interleaved pixel buffer.
- [func histogram() -> vImage.PixelBuffer<Format>.Histogram888](vimage/pixelbuffer/histogram-30tsp.md)
  Calculates the histogram of an 8-bit-per-channel, 3-channel multiple-plane pixel buffer.
- [func histogram(binCount: Int) -> vImage.PixelBuffer<Format>.HistogramFFF](vimage/pixelbuffer/histogram(bincount:)-8wymg.md)
  Calculates the histogram of a 32-bit-per-channel, 3-channel multiple-plane pixel buffer.
- [func histogram() -> vImage.PixelBuffer<Format>.Histogram8888](vimage/pixelbuffer/histogram-6wxl5.md)
  Calculates the histogram of an 8-bit-per-channel, 4-channel multiple-plane pixel buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimage/pixelbuffer/histogram(bincount:)-5bqka)*