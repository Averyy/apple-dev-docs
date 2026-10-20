# convert(to:)

**Framework**: Accelerate  
**Kind**: method  
**Role**: Instance Method

Converts the contents of the floating-point 16-bit-per-channel, 4-channel interleaved pixel buffer to 32-bit-per-channel format.

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
func convert(to destination: vImage.PixelBuffer<vImage.InterleavedFx4>)
```

Available when `Format` is `vImage.Interleaved16Fx4`.

## Parameters

- `destination`: The destination pixel buffer.

## See Also

### Conversion from 16-bit to 32-bit
- [func convert(to: vImage.PixelBuffer<vImage.PlanarF>)](./convert%28to%29-4876v.md)
  Converts the contents of the floating-point 16-bit planar pixel buffer to 32-bit planar format.
- [func convert(to: vImage.PixelBuffer<vImage.InterleavedFx2>)](./convert%28to%29-1xpk2.md)
  Converts the contents of the floating-point 16-bit-per-channel, 2-channel interleaved pixel buffer to 32-bit-per-channel format.
- [func convert(to: vImage.PixelBuffer<vImage.InterleavedFx4>)](./convert%28to%29-674t9.md)
  Converts the contents of the unsigned 16-bit-per-channel, 4-channel interleaved pixel buffer to 32-bit-per-channel format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimage/pixelbuffer/convert(to:)-8ljhz)*