# convert(to:)

**Framework**: Accelerate  
**Kind**: method

Converts the contents of the floating-point 16-bit-per-channel, 2-channel interleaved pixel buffer to 32-bit-per-channel format.

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
func convert(to destination: vImage.PixelBuffer<vImage.InterleavedFx2>)
```

## Parameters

- `destination`: The destination pixel buffer.

## See Also

- [func convert(to: vImage.PixelBuffer<vImage.PlanarF>)](vimage/pixelbuffer/convert(to:)-4876v.md)
  Converts the contents of the floating-point 16-bit planar pixel buffer to 32-bit planar format.
- [func convert(to: vImage.PixelBuffer<vImage.InterleavedFx4>)](vimage/pixelbuffer/convert(to:)-674t9.md)
  Converts the contents of the unsigned 16-bit-per-channel, 4-channel interleaved pixel buffer to 32-bit-per-channel format.
- [func convert(to: vImage.PixelBuffer<vImage.InterleavedFx4>)](vimage/pixelbuffer/convert(to:)-8ljhz.md)
  Converts the contents of the floating-point 16-bit-per-channel, 4-channel interleaved pixel buffer to 32-bit-per-channel format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimage/pixelbuffer/convert(to:)-1xpk2)*