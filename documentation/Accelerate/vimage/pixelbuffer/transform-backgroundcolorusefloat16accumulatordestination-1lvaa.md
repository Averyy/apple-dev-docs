# transform(_:backgroundColor:useFloat16Accumulator:destination:)

**Framework**: Accelerate  
**Kind**: method

Applies a Core Graphics affine transformation to a floating-point 16-bit-per-channel, four-channel interleaved pixel buffer.

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
func transform(_ transform: CGAffineTransform, backgroundColor: Pixel_ARGB_16F? = (0, 0, 0, 0), useFloat16Accumulator: Bool = false, destination: vImage.PixelBuffer<Format>)
```

## Parameters

- `transform`: The affine transformation matrix.
- `backgroundColor`: An optional background color. If you pass  , the operation uses the   flag to extend the edges of the image infinitely.
- `useFloat16Accumulator`: A Boolean value that specifies that the function uses faster, but lower-precision, internal arithmetic. For more information, see  .
- `destination`: The destination pixel buffer.

## See Also

- [Applying geometric transforms to images](applying-geometric-transforms-to-images.md)
  Reflect, shear, rotate, and scale image buffers using vImage.
- [func transform(CGAffineTransform, backgroundColor: Pixel_8?, destination: vImage.PixelBuffer<Format>)](vimage/pixelbuffer/transform(_:backgroundcolor:destination:)-4wy4q.md)
  Applies a Core Graphics affine transformation to an 8-bit planar pixel buffer.
- [func transform(CGAffineTransform, backgroundColor: Pixel_16F?, useFloat16Accumulator: Bool, destination: vImage.PixelBuffer<Format>)](vimage/pixelbuffer/transform(_:backgroundcolor:usefloat16accumulator:destination:)-1470p.md)
  Applies a Core Graphics affine transformation to a floating-point 16-bit planar pixel buffer.
- [func transform(CGAffineTransform, backgroundColor: Pixel_F?, destination: vImage.PixelBuffer<Format>)](vimage/pixelbuffer/transform(_:backgroundcolor:destination:)-1s38.md)
  Applies a Core Graphics affine transformation to a floating-point 32-bit planar pixel buffer.
- [func transform(CGAffineTransform, backgroundColor: Pixel_16F16F?, useFloat16Accumulator: Bool, destination: vImage.PixelBuffer<Format>)](vimage/pixelbuffer/transform(_:backgroundcolor:usefloat16accumulator:destination:)-4w4jr.md)
  Applies a Core Graphics affine transformation to a floating-point 16-bit-per-channel, two-channel interleaved pixel buffer.
- [func transform(CGAffineTransform, backgroundColor: Pixel_8888?, destination: vImage.PixelBuffer<Format>)](vimage/pixelbuffer/transform(_:backgroundcolor:destination:)-5kxj6.md)
  Applies a Core Graphics affine transformation to an 8-bit-per-channel, four-channel interleaved pixel buffer.
- [func transform(CGAffineTransform, backgroundColor: Pixel_ARGB_16U?, destination: vImage.PixelBuffer<Format>)](vimage/pixelbuffer/transform(_:backgroundcolor:destination:)-nl6g.md)
  Applies a Core Graphics affine transformation to an unsigned 16-bit-per-channel, four-channel interleaved pixel buffer.
- [func transform(CGAffineTransform, backgroundColor: Pixel_FFFF?, destination: vImage.PixelBuffer<Format>)](vimage/pixelbuffer/transform(_:backgroundcolor:destination:)-9ggt.md)
  Applies a Core Graphics affine transformation to a floating-point 32-bit-per-channel, four-channel interleaved pixel buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimage/pixelbuffer/transform(_:backgroundcolor:usefloat16accumulator:destination:)-1lvaa)*