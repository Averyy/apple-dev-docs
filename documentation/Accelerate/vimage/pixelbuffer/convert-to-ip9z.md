# convert(to:)

**Framework**: Accelerate  
**Kind**: method

Converts the contents of the floating-point 16-bit planar pixel buffer to unsigned 16-bit planar format.

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
func convert(to destination: vImage.PixelBuffer<vImage.Planar16U>)
```

#### Discussion

This function converts the source values in the range `[0.0, 1.0]` to the destination range `[0, UInt16.max]`. The conversion clamps source values to the range `[0.0, 1.0]`.

## Parameters

- `destination`: The destination pixel buffer.

## See Also

- [func convert(to: vImage.PixelBuffer<vImage.Planar16F>)](vimage/pixelbuffer/convert(to:)-1zk6k.md)
  Converts the contents of the unsigned 16-bit planar pixel buffer to floating-point 16-bit planar format.
- [func convert(to: vImage.PixelBuffer<vImage.Interleaved16Ux2>)](vimage/pixelbuffer/convert(to:)-7dx2c.md)
  Converts the contents of the floating-point 16-bit-per-channel, 2-channel interleaved pixel buffer to unsigned 16-bit-per-channel format.
- [func convert(to: vImage.PixelBuffer<vImage.Interleaved16Fx4>)](vimage/pixelbuffer/convert(to:)-7tdb1.md)
  Converts the contents of the unsigned 16-bit-per-channel, 4-channel interleaved pixel buffer to floating-point 16-bit-per-channel format.
- [func convert(to: vImage.PixelBuffer<vImage.Interleaved16Ux4>)](vimage/pixelbuffer/convert(to:)-3lg9p.md)
  Converts the contents of the floating-point 16-bit-per-channel, 4-channel interleaved pixel buffer to unsigned 16-bit-per-channel format.
- [func convert(to: vImage.PixelBuffer<vImage.Interleaved16Fx2>)](vimage/pixelbuffer/convert(to:)-8u16v.md)
  Converts the contents of the unsigned 16-bit-per-channel, 2-channel interleaved pixel buffer to floating-point 16-bit-per-channel format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimage/pixelbuffer/convert(to:)-ip9z)*