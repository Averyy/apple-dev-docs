# convert(to:)

**Framework**: Accelerate  
**Kind**: method  
**Role**: Instance Method

Converts the contents of the 8-bit-per-channel, 2-channel interleaved pixel buffer to floating-point 16-bit-per-channel format.

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
func convert(to destination: vImage.PixelBuffer<vImage.Interleaved16Fx2>)
```

Available when `Format` is `vImage.Interleaved8x2`.

## Discussion

This function converts the source values in the range `[0, 255]` to the destination range `[0.0, 1.0]`.

## Parameters

- `destination`: The destination pixel buffer.

## See Also

### Conversion from 8-bit to 16-bit
- [func convert(to: vImage.PixelBuffer<vImage.Planar16F>)](./convert%28to%29-3wpdu.md)
  Converts the contents of the 8-bit planar pixel buffer to floating-point 16-bit planar format.
- [func convert(to: vImage.PixelBuffer<vImage.Interleaved16Ux4>)](./convert%28to%29-9j6eu.md)
  Converts the contents of the 8-bit-per-channel, 4-channel interleaved pixel buffer to unsigned 16-bit-per-channel format.
- [func convert(to: vImage.PixelBuffer<vImage.Interleaved16Fx4>)](./convert%28to%29-6ci2d.md)
  Converts the contents of the 8-bit-per-channel, 4-channel interleaved pixel buffer to floating-point 16-bit-per-channel format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimage/pixelbuffer/convert(to:)-4v16)*