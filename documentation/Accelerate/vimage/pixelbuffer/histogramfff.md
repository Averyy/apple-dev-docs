# vImage.PixelBuffer.HistogramFFF

**Framework**: Accelerate  
**Kind**: typealias  
**Role**: Type Alias

The histogram for three channel 32-bit pixel buffers.

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
typealias HistogramFFF = (binCount: Int, [vImagePixelCount], [vImagePixelCount], [vImagePixelCount])
```

Available when `Format` conforms to `PixelFormat` and `Format.ComponentType` is `Float`.

## See Also

### Type aliases
- [vImage.PixelBuffer.Histogram888](./histogram888.md)
  The histogram for three channel 8-bit pixel buffers.
- [vImage.PixelBuffer.Histogram8888](./histogram8888.md)
  The histogram for four channel 8-bit pixel buffers.
- [vImage.PixelBuffer.HistogramFFFF](./histogramffff.md)
  The histogram for four channel 32-bit pixel buffers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimage/pixelbuffer/histogramfff)*