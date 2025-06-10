# scale(useFloat16Accumulator:destination:)

**Framework**: Accelerate  
**Kind**: method

Scales a floating-point 16-bit-per-channel, two-channel interleaved pixel buffer to fit the destination buffer.

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
func scale(useFloat16Accumulator: Bool = false, destination: vImage.PixelBuffer<Format>)
```

## Parameters

- `useFloat16Accumulator`: A Boolean value that specifies that the function uses faster, but lower-precision, internal arithmetic. For more information, see  .
- `destination`: The destination pixel buffer.

## See Also

- [Applying geometric transforms to images](applying-geometric-transforms-to-images.md)
  Reflect, shear, rotate, and scale image buffers using vImage.
- [func scale(destination: vImage.PixelBuffer<Format>)](vimage/pixelbuffer/scale(destination:)-5euvc.md)
  Scales an 8-bit planar pixel buffer to fit the destination buffer.
- [func scale(destination: vImage.PixelBuffer<Format>)](vimage/pixelbuffer/scale(destination:)-9si6m.md)
  Scales an unsigned 16-bit planar pixel buffer to fit the destination buffer.
- [func scale(useFloat16Accumulator: Bool, destination: vImage.PixelBuffer<Format>)](vimage/pixelbuffer/scale(usefloat16accumulator:destination:)-5lt9n.md)
  Scales a floating-point 16-bit planar pixel buffer to fit the destination buffer.
- [func scale(destination: vImage.PixelBuffer<Format>)](vimage/pixelbuffer/scale(destination:)-6xwro.md)
  Scales a 32-bit planar pixel buffer to fit the destination buffer.
- [func scale(destination: vImage.PixelBuffer<Format>)](vimage/pixelbuffer/scale(destination:)-6gy9p.md)
  Scales an 8-bit-per-channel, two-channel interleaved pixel buffer to fit the destination buffer.
- [func scale(destination: vImage.PixelBuffer<Format>)](vimage/pixelbuffer/scale(destination:)-4p5r6.md)
  Scales an unsigned 16-bit-per-channel, two-channel interleaved pixel buffer to fit the destination buffer.
- [func scale(destination: vImage.PixelBuffer<Format>)](vimage/pixelbuffer/scale(destination:)-y1zi.md)
  Scales an 8-bit-per-channel, four-channel interleaved pixel buffer to fit the destination buffer.
- [func scale(destination: vImage.PixelBuffer<Format>)](vimage/pixelbuffer/scale(destination:)-5tpok.md)
  Scales an unsigned 16-bit-per-channel, four-channel interleaved pixel buffer to fit the destination buffer.
- [func scale(useFloat16Accumulator: Bool, destination: vImage.PixelBuffer<Format>)](vimage/pixelbuffer/scale(usefloat16accumulator:destination:)-st2u.md)
  Scales a floating-point 16-bit-per-channel, four-channel interleaved pixel buffer to fit the destination buffer.
- [func scale(destination: vImage.PixelBuffer<Format>)](vimage/pixelbuffer/scale(destination:)-2hqm3.md)
  Scales a 32-bit-per-channel, four-channel interleaved pixel buffer to fit the destination buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimage/pixelbuffer/scale(usefloat16accumulator:destination:)-thg7)*