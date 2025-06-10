# rotate(_:backgroundColor:useFloat16Accumulator:destination:)

**Framework**: Accelerate  
**Kind**: method

Rotates a floating-point 16-bit planar pixel buffer.

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
func rotate(_ rotation: vImage.Rotation, backgroundColor: Pixel_16F? = Pixel_16F(0), useFloat16Accumulator: Bool = false, destination: vImage.PixelBuffer<Format>)
```

#### Discussion

Use this function to either rotate an image by a multiple of 90° or by an angle, which you specify in degrees or radians.

When you specify a rotation that’s a multiple of 90° (such as [`vImage.Rotation.clockwise270Degrees`](vimage/rotation/clockwise270degrees.md)), this function maps the center point of the source image to the center point of the destination image. It doesn’t scale or resample; instead, the function copies individual pixels unchanged to new locations.

The 90° and 270° rotations don’t rotate around the true center of the image if either of the following is true:

- The parities of the source height and the destination width don’t match. For example, the source height is odd and the destination width is even.
- The parities of the source width and the destination height don’t match. For example, the source width is odd and the destination height is even.

The 0° and 180° rotations don’t rotate around the true center of the image if either of the following is true:

- The parities of the source height and the destination height don’t match. For example, the source height is odd and the destination height is even.
- The parities of the source width and the destination width don’t match. For example, the source width is odd and the destination width is even.

To overcome this limitation, specify [`vImage.Rotation.angleInRadians(_:)`](vimage/rotation/angleinradians(_:).md) or [`vImage.Rotation.angleInDegrees(_:)`](vimage/rotation/angleindegrees(_:).md) to invoke the high-level rotate function.

## Parameters

- `rotation`: An enumeration that specifies the rotation angle.
- `backgroundColor`: An optional background color. If you pass  , the operation uses the   flag to extend the edges of the image infinitely.
- `useFloat16Accumulator`: A Boolean value that specifies that the function uses faster, but lower-precision, internal arithmetic. For more information, see  .
- `destination`: The destination pixel buffer.

## See Also

- [Applying geometric transforms to images](applying-geometric-transforms-to-images.md)
  Reflect, shear, rotate, and scale image buffers using vImage.
- [func rotate(vImage.Rotation, backgroundColor: Pixel_8?, destination: vImage.PixelBuffer<Format>)](vimage/pixelbuffer/rotate(_:backgroundcolor:destination:)-7patt.md)
  Rotates an 8-bit planar pixel buffer.
- [func rotate(vImage.Rotation, backgroundColor: Pixel_F?, destination: vImage.PixelBuffer<Format>)](vimage/pixelbuffer/rotate(_:backgroundcolor:destination:)-7tzsn.md)
  Rotates a 32-bit planar pixel buffer.
- [func rotate(vImage.Rotation, backgroundColor: Pixel_16F16F?, useFloat16Accumulator: Bool, destination: vImage.PixelBuffer<Format>)](vimage/pixelbuffer/rotate(_:backgroundcolor:usefloat16accumulator:destination:)-61l7b.md)
  Rotates a floating-point 16-bit-per-channel, two-channel interleaved pixel buffer.
- [func rotate(vImage.Rotation, backgroundColor: Pixel_8888?, destination: vImage.PixelBuffer<Format>)](vimage/pixelbuffer/rotate(_:backgroundcolor:destination:)-2li9v.md)
  Rotates an 8-bit-per-channel, four-channel interleaved pixel buffer.
- [func rotate(vImage.Rotation, backgroundColor: Pixel_ARGB_16U?, destination: vImage.PixelBuffer<Format>)](vimage/pixelbuffer/rotate(_:backgroundcolor:destination:)-692ke.md)
  Rotates an unsigned 16-bit-per-channel, four-channel interleaved pixel buffer.
- [func rotate(vImage.Rotation, backgroundColor: Pixel_ARGB_16F?, useFloat16Accumulator: Bool, destination: vImage.PixelBuffer<Format>)](vimage/pixelbuffer/rotate(_:backgroundcolor:usefloat16accumulator:destination:)-8glur.md)
  Rotates a floating-point 16-bit-per-channel, four-channel interleaved pixel buffer.
- [func rotate(vImage.Rotation, backgroundColor: Pixel_FFFF?, destination: vImage.PixelBuffer<Format>)](vimage/pixelbuffer/rotate(_:backgroundcolor:destination:)-9bnb6.md)
  Rotates a 32-bit-per-channel, four-channel interleaved pixel buffer.
- [vImage.Rotation](vimage/rotation.md)
  The angle to rotate an image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimage/pixelbuffer/rotate(_:backgroundcolor:usefloat16accumulator:destination:)-9harr)*