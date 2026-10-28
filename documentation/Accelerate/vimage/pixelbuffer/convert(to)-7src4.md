# convert(to:)

**Framework**: Accelerate  
**Kind**: method  
**Role**: Instance Method

Converts the contents of the 8-bit planar pixel buffer to 32-bit planar format.

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
func convert(to destination: vImage.PixelBuffer<vImage.PlanarF>)
```

Available when `Format` is `vImage.Planar8`.

## Discussion

This function converts the source values in the range `[0, 255]` to the destination range `[0.0, 1.0]`.

## Parameters

- `destination`: The destination pixel buffer.

## See Also

### Conversion from 8-bit to 32-bit
- [func convert(to: vImage.PixelBuffer<vImage.InterleavedFx3>)](./convert%28to%29-8hivu.md)
  Converts the contents of the 8-bit-per-channel, 3-channel interleaved pixel buffer to 32-bit-per-channel format.
- [func convert(to: vImage.PixelBuffer<vImage.InterleavedFx4>)](./convert%28to%29-1e0nd.md)
  Converts the contents of the 8-bit-per-channel, 4-channel interleaved pixel buffer to 32-bit-per-channel format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimage/pixelbuffer/convert(to:)-7src4)*