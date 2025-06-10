# reflect(over:destination:)

**Framework**: Accelerate  
**Kind**: method

Reflects a floating-point 16-bit planar pixel buffer over a horizontal or vertical axis.

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
func reflect(over axis: vImage.ReflectionAxis, destination: vImage.PixelBuffer<Format>)
```

## Parameters

- `axis`: The reflection axis.
- `destination`: The destination pixel buffer.

## See Also

- [Applying geometric transforms to images](applying-geometric-transforms-to-images.md)
  Reflect, shear, rotate, and scale image buffers using vImage.
- [func reflect(over: vImage.ReflectionAxis, destination: vImage.PixelBuffer<Format>)](vimage/pixelbuffer/reflect(over:destination:)-9ezqm.md)
  Reflects an 8-bit planar pixel buffer over a horizontal or vertical axis.
- [func reflect(over: vImage.ReflectionAxis, destination: vImage.PixelBuffer<Format>)](vimage/pixelbuffer/reflect(over:destination:)-4i4vi.md)
  Reflects a 32-bit planar pixel buffer over a horizontal or vertical axis.
- [func reflect(over: vImage.ReflectionAxis, destination: vImage.PixelBuffer<Format>)](vimage/pixelbuffer/reflect(over:destination:)-6syq1.md)
  Reflects a floating-point 16-bit-per-channel, two-channel interleaved pixel buffer over a horizontal or vertical axis.
- [func reflect(over: vImage.ReflectionAxis, destination: vImage.PixelBuffer<Format>)](vimage/pixelbuffer/reflect(over:destination:)-7o9tt.md)
  Reflects an 8-bit-per-channel, four-channel interleaved pixel buffer over a horizontal or vertical axis.
- [func reflect(over: vImage.ReflectionAxis, destination: vImage.PixelBuffer<Format>)](vimage/pixelbuffer/reflect(over:destination:)-fg4a.md)
  Reflects an unsigned 16-bit-per-channel, four-channel interleaved pixel buffer over a horizontal or vertical axis.
- [func reflect(over: vImage.ReflectionAxis, destination: vImage.PixelBuffer<Format>)](vimage/pixelbuffer/reflect(over:destination:)-97wi9.md)
  Reflects a floating-point 16-bit-per-channel, four-channel interleaved pixel buffer over a horizontal or vertical axis.
- [func reflect(over: vImage.ReflectionAxis, destination: vImage.PixelBuffer<Format>)](vimage/pixelbuffer/reflect(over:destination:)-7b1md.md)
  Reflects a 32-bit-per-channel, four-channel interleaved pixel buffer over a horizontal or vertical axis.
- [vImage.ReflectionAxis](vimage/reflectionaxis.md)
  The axis to reflect an image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimage/pixelbuffer/reflect(over:destination:)-529j0)*