# convert(to:)

**Framework**: Accelerate  
**Kind**: method

Converts the contents of the floating-point 16-bit-per-channel, 2-channel interleaved pixel buffer to 8-bit-per-channel format.

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
func convert(to destination: vImage.PixelBuffer<vImage.Interleaved8x2>)
```

#### Discussion

This function converts the source values in the range `[0.0, 1.0]` to the destination range `[0, 255]`. The conversion clamps source values to the range `[0.0, 1.0]`.

## Parameters

- `destination`: The destination pixel buffer.

## See Also

- [func convert(to: vImage.PixelBuffer<vImage.Planar8>)](vimage/pixelbuffer/convert(to:)-449hx.md)
  Converts the contents of the floating-point 16-bit planar pixel buffer to 8-bit planar format.
- [func convert(to: vImage.PixelBuffer<vImage.Interleaved8x4>)](vimage/pixelbuffer/convert(to:)-k50a.md)
  Converts the contents of the unsigned 16-bit-per-channel, 4-channel interleaved pixel buffer to 8-bit-per-channel format.
- [func convert(to: vImage.PixelBuffer<vImage.Interleaved8x4>)](vimage/pixelbuffer/convert(to:)-9xnxc.md)
  Converts the contents of the floating-point 16-bit-per-channel, 4-channel interleaved pixel buffer to 8-bit-per-channel format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimage/pixelbuffer/convert(to:)-1h96t)*