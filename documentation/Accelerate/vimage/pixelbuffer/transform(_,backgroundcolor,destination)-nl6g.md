# transform(_:backgroundColor:destination:)

**Framework**: Accelerate  
**Kind**: method  
**Role**: Instance Method

Applies a Core Graphics affine transformation to an unsigned 16-bit-per-channel, four-channel interleaved pixel buffer.

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
func transform(_ transform: CGAffineTransform, backgroundColor: Pixel_ARGB_16U? = (0, 0, 0, 0), destination: vImage.PixelBuffer<Format>)
```

Available when `Format` is `vImage.Interleaved16Ux4`.

## Parameters

- `transform`: The affine transformation matrix.
- `backgroundColor`: An optional background color. If you pass `nil`, the operation uses the [`kvImageEdgeExtend`](../../kvimageedgeextend.md) flag to extend the edges of the image infinitely.
- `destination`: The destination pixel buffer.

## See Also

### Related Documentation
- [Applying geometric transforms to images](../../applying-geometric-transforms-to-images.md)
  Reflect, shear, rotate, and scale image buffers using vImage.
### Applying affine transformations to images
- [func transform(CGAffineTransform, backgroundColor: Pixel_8?, destination: vImage.PixelBuffer<Format>)](./transform%28_,backgroundcolor,destination%29-4wy4q.md)
  Applies a Core Graphics affine transformation to an 8-bit planar pixel buffer.
- [func transform(CGAffineTransform, backgroundColor: Pixel_16F?, useFloat16Accumulator: Bool, destination: vImage.PixelBuffer<Format>)](./transform%28_,backgroundcolor,usefloat16accumulator,destination%29-1470p.md)
  Applies a Core Graphics affine transformation to a floating-point 16-bit planar pixel buffer.
- [func transform(CGAffineTransform, backgroundColor: Pixel_F?, destination: vImage.PixelBuffer<Format>)](./transform%28_,backgroundcolor,destination%29-1s38.md)
  Applies a Core Graphics affine transformation to a floating-point 32-bit planar pixel buffer.
- [func transform(CGAffineTransform, backgroundColor: Pixel_16F16F?, useFloat16Accumulator: Bool, destination: vImage.PixelBuffer<Format>)](./transform%28_,backgroundcolor,usefloat16accumulator,destination%29-4w4jr.md)
  Applies a Core Graphics affine transformation to a floating-point 16-bit-per-channel, two-channel interleaved pixel buffer.
- [func transform(CGAffineTransform, backgroundColor: Pixel_8888?, destination: vImage.PixelBuffer<Format>)](./transform%28_,backgroundcolor,destination%29-5kxj6.md)
  Applies a Core Graphics affine transformation to an 8-bit-per-channel, four-channel interleaved pixel buffer.
- [func transform(CGAffineTransform, backgroundColor: Pixel_ARGB_16F?, useFloat16Accumulator: Bool, destination: vImage.PixelBuffer<Format>)](./transform%28_,backgroundcolor,usefloat16accumulator,destination%29-1lvaa.md)
  Applies a Core Graphics affine transformation to a floating-point 16-bit-per-channel, four-channel interleaved pixel buffer.
- [func transform(CGAffineTransform, backgroundColor: Pixel_FFFF?, destination: vImage.PixelBuffer<Format>)](./transform%28_,backgroundcolor,destination%29-9ggt.md)
  Applies a Core Graphics affine transformation to a floating-point 32-bit-per-channel, four-channel interleaved pixel buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimage/pixelbuffer/transform(_:backgroundcolor:destination:)-nl6g)*