# reflect(over:destination:)

**Framework**: Accelerate  
**Kind**: method  
**Role**: Instance Method

Reflects a 32-bit planar pixel buffer over a horizontal or vertical axis.

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
func reflect(over axis: vImage.ReflectionAxis, destination: vImage.PixelBuffer<Format>)
```

Available when `Format` is `vImage.PlanarF`.

## Parameters

- `axis`: The reflection axis.
- `destination`: The destination pixel buffer.

## See Also

### Related Documentation
- [Applying geometric transforms to images](../../applying-geometric-transforms-to-images.md)
  Reflect, shear, rotate, and scale image buffers using vImage.
### Reflecting images
- [func reflect(over: vImage.ReflectionAxis, destination: vImage.PixelBuffer<Format>)](./reflect%28over,destination%29-9ezqm.md)
  Reflects an 8-bit planar pixel buffer over a horizontal or vertical axis.
- [func reflect(over: vImage.ReflectionAxis, destination: vImage.PixelBuffer<Format>)](./reflect%28over,destination%29-529j0.md)
  Reflects a floating-point 16-bit planar pixel buffer over a horizontal or vertical axis.
- [func reflect(over: vImage.ReflectionAxis, destination: vImage.PixelBuffer<Format>)](./reflect%28over,destination%29-6syq1.md)
  Reflects a floating-point 16-bit-per-channel, two-channel interleaved pixel buffer over a horizontal or vertical axis.
- [func reflect(over: vImage.ReflectionAxis, destination: vImage.PixelBuffer<Format>)](./reflect%28over,destination%29-7o9tt.md)
  Reflects an 8-bit-per-channel, four-channel interleaved pixel buffer over a horizontal or vertical axis.
- [func reflect(over: vImage.ReflectionAxis, destination: vImage.PixelBuffer<Format>)](./reflect%28over,destination%29-fg4a.md)
  Reflects an unsigned 16-bit-per-channel, four-channel interleaved pixel buffer over a horizontal or vertical axis.
- [func reflect(over: vImage.ReflectionAxis, destination: vImage.PixelBuffer<Format>)](./reflect%28over,destination%29-97wi9.md)
  Reflects a floating-point 16-bit-per-channel, four-channel interleaved pixel buffer over a horizontal or vertical axis.
- [func reflect(over: vImage.ReflectionAxis, destination: vImage.PixelBuffer<Format>)](./reflect%28over,destination%29-7b1md.md)
  Reflects a 32-bit-per-channel, four-channel interleaved pixel buffer over a horizontal or vertical axis.
- [vImage.ReflectionAxis](../reflectionaxis.md)
  The axis to reflect an image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimage/pixelbuffer/reflect(over:destination:)-4i4vi)*