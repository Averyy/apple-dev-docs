# histogram()

**Framework**: Accelerate  
**Kind**: method  
**Role**: Instance Method

Calculates the histogram of an 8-bit-per-channel, 3-channel multiple-plane pixel buffer.

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
func histogram() -> vImage.PixelBuffer<Format>.Histogram888
```

Available when `Format` is `vImage.Planar8x3`.

## Return Value

The histogram of the pixel buffer.

## See Also

### Related Documentation
- [func specifyHistogram(vImage.PixelBuffer<Format>.Histogram888, destination: vImage.PixelBuffer<Format>)](./specifyhistogram%28_,destination%29-qeqr.md)
  Performs a histogram specification operation on an 8-bit-per-channel, 3-channel multiple-plane pixel buffer.
- [Specifying histograms with vImage](../../specifying-histograms-with-vimage.md)
  Calculate the histogram of one image, and apply it to a second image.
### Histogram calculation
- [func histogram() -> vImage.PixelBuffer<Format>.Histogram8888](./histogram%28%29-14a38.md)
  Calculates the histogram of an 8-bit-per-channel, 4-channel interleaved pixel buffer.
- [func histogram(binCount: Int) -> vImage.PixelBuffer<Format>.HistogramFFFF](./histogram%28bincount%29-6pkfv.md)
  Calculates the histogram of a 32-bit-per-channel, 4-channel interleaved pixel buffer.
- [func histogram(binCount: Int) -> vImage.PixelBuffer<Format>.HistogramFFF](./histogram%28bincount%29-8wymg.md)
  Calculates the histogram of a 32-bit-per-channel, 3-channel multiple-plane pixel buffer.
- [func histogram() -> vImage.PixelBuffer<Format>.Histogram8888](./histogram%28%29-6wxl5.md)
  Calculates the histogram of an 8-bit-per-channel, 4-channel multiple-plane pixel buffer.
- [func histogram(binCount: Int) -> vImage.PixelBuffer<Format>.HistogramFFFF](./histogram%28bincount%29-5bqka.md)
  Calculates the histogram of a 32-bit-per-channel, 4-channel multiple-plane pixel buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimage/pixelbuffer/histogram()-30tsp)*