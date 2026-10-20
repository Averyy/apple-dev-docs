# convert(to:)

**Framework**: Accelerate  
**Kind**: method  
**Role**: Instance Method

Converts the contents of the 32-bit planar pixel buffer to 8-bit planar format.

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
func convert(to destination: vImage.PixelBuffer<vImage.Planar8>)
```

Available when `Format` is `vImage.PlanarF`.

#### Discussion

This function converts the source values in the range `[0.0, 1.0]` to the destination range `[0, 255]`. The conversion clamps source values to the range `[0.0, 1.0]`.

## Parameters

- `destination`: The destination pixel buffer.

## See Also

### Conversion from 32-bit to 8-bit
- [func convert(to: vImage.PixelBuffer<vImage.Interleaved8x3>)](./convert%28to%29-69qa2.md)
  Converts the contents of the 32-bit-per-channel, 3-channel interleaved pixel buffer to 8-bit-per-channel format.
- [func convert(to: vImage.PixelBuffer<vImage.Interleaved8x4>)](./convert%28to%29-24xu0.md)
  Converts the contents of the 32-bit-per-channel, 4-channel interleaved pixel buffer to 8-bit-per-channel format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimage/pixelbuffer/convert(to:)-1ka0r)*