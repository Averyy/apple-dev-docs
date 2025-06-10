# convert(to:)

**Framework**: Accelerate  
**Kind**: method

Converts the contents of the 32-bit-per-channel, 4-channel interleaved pixel buffer to floating-point 16-bit-per-channel format.

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
func convert(to destination: vImage.PixelBuffer<vImage.Interleaved16Fx4>)
```

## Parameters

- `destination`: The destination pixel buffer.

## See Also

- [func convert(to: vImage.PixelBuffer<vImage.Planar16F>)](vimage/pixelbuffer/convert(to:)-2bc8n.md)
  Converts the contents of the 32-bit planar pixel buffer to floating-point 16-bit planar format.
- [func convert(to: vImage.PixelBuffer<vImage.Interleaved16Fx2>)](vimage/pixelbuffer/convert(to:)-56zhe.md)
  Converts the contents of the 32-bit-per-channel, 2-channel interleaved pixel buffer to floating-point 16-bit-per-channel format.
- [func convert(to: vImage.PixelBuffer<vImage.Interleaved16Ux4>)](vimage/pixelbuffer/convert(to:)-2dbbo.md)
  Converts the contents of the 32-bit-per-channel, 4-channel interleaved pixel buffer to unsigned 16-bit-per-channel format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimage/pixelbuffer/convert(to:)-1132q)*