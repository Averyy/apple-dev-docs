# scale(destination:)

**Framework**: Accelerate  
**Kind**: method  
**Role**: Instance Method

Scales an unsigned 16-bit planar pixel buffer to fit the destination buffer.

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
func scale(destination: vImage.PixelBuffer<Format>)
```

Available when `Format` is `vImage.Planar16U`.

## Parameters

- `destination`: The destination pixel buffer.

## See Also

### Related Documentation
- [Applying geometric transforms to images](../../applying-geometric-transforms-to-images.md)
  Reflect, shear, rotate, and scale image buffers using vImage.
### Scaling images
- [func scale(destination: vImage.PixelBuffer<Format>)](./scale%28destination%29-5euvc.md)
  Scales an 8-bit planar pixel buffer to fit the destination buffer.
- [func scale(useFloat16Accumulator: Bool, destination: vImage.PixelBuffer<Format>)](./scale%28usefloat16accumulator,destination%29-5lt9n.md)
  Scales a floating-point 16-bit planar pixel buffer to fit the destination buffer.
- [func scale(destination: vImage.PixelBuffer<Format>)](./scale%28destination%29-6xwro.md)
  Scales a 32-bit planar pixel buffer to fit the destination buffer.
- [func scale(destination: vImage.PixelBuffer<Format>)](./scale%28destination%29-6gy9p.md)
  Scales an 8-bit-per-channel, two-channel interleaved pixel buffer to fit the destination buffer.
- [func scale(destination: vImage.PixelBuffer<Format>)](./scale%28destination%29-4p5r6.md)
  Scales an unsigned 16-bit-per-channel, two-channel interleaved pixel buffer to fit the destination buffer.
- [func scale(useFloat16Accumulator: Bool, destination: vImage.PixelBuffer<Format>)](./scale%28usefloat16accumulator,destination%29-thg7.md)
  Scales a floating-point 16-bit-per-channel, two-channel interleaved pixel buffer to fit the destination buffer.
- [func scale(destination: vImage.PixelBuffer<Format>)](./scale%28destination%29-y1zi.md)
  Scales an 8-bit-per-channel, four-channel interleaved pixel buffer to fit the destination buffer.
- [func scale(destination: vImage.PixelBuffer<Format>)](./scale%28destination%29-5tpok.md)
  Scales an unsigned 16-bit-per-channel, four-channel interleaved pixel buffer to fit the destination buffer.
- [func scale(useFloat16Accumulator: Bool, destination: vImage.PixelBuffer<Format>)](./scale%28usefloat16accumulator,destination%29-st2u.md)
  Scales a floating-point 16-bit-per-channel, four-channel interleaved pixel buffer to fit the destination buffer.
- [func scale(destination: vImage.PixelBuffer<Format>)](./scale%28destination%29-2hqm3.md)
  Scales a 32-bit-per-channel, four-channel interleaved pixel buffer to fit the destination buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimage/pixelbuffer/scale(destination:)-9si6m)*