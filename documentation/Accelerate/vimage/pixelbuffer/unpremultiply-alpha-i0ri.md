# unpremultiply(alpha:)

**Framework**: Accelerate  
**Kind**: method

Transforms a 32-bit planar pixel buffer in-place from premultiplied alpha format to nonpremultiplied alpha format.

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
func unpremultiply(alpha: vImage.PixelBuffer<Format>)
```

#### Discussion

This function divides the color values in `self` by the corresponding alpha values. For example, the following code premultiplies a 4 x 1 planar pixel buffer with the corresponding pixels in a separate planar alpha buffer:

```swift
let src = vImage.PixelBuffer<vImage.PlanarF>(
    pixelValues: [0.125, 0.25, 0.5, 1],
    size: vImage.Size(width: 4, height: 1))

let alpha = vImage.PixelBuffer<vImage.PlanarF>(
    pixelValues: [0, 0.25, 0.5, 1],
    size: vImage.Size(width: 4, height: 1))

src.unpremultiply(alpha: alpha)

// Prints "[0.0, ~1.0, ~1.0, ~1.0]".
print(src.array)

```

## Parameters

- `alpha`: An 32-bit planar pixel buffer that contains the alpha.

## See Also

- [func unpremultiply(alpha: vImage.PixelBuffer<Format>)](vimage/pixelbuffer/unpremultiply(alpha:)-xnog.md)
  Transforms an 8-bit planar pixel buffer in-place from premultiplied alpha format to nonpremultiplied alpha format.
- [func unpremultiply(channelOrdering: vImage.ChannelOrdering)](vimage/pixelbuffer/unpremultiply(channelordering:)-1pkat.md)
  Transforms an 8-bit ARGB or RGBA pixel buffer in-place from premultiplied alpha format to nonpremultiplied alpha format.
- [func unpremultiply(channelOrdering: vImage.ChannelOrdering)](vimage/pixelbuffer/unpremultiply(channelordering:)-19l0s.md)
  Transforms an unsigned 16-bit ARGB or RGBA pixel buffer in-place from premultiplied alpha format to nonpremultiplied alpha format.
- [func unpremultiply()](vimage/pixelbuffer/unpremultiply.md)
  Transforms a floating-point 16-bit RGBA pixel buffer in-place from premultiplied alpha format to nonpremultiplied alpha format.
- [func unpremultiply(channelOrdering: vImage.ChannelOrdering)](vimage/pixelbuffer/unpremultiply(channelordering:)-82uq3.md)
  Transforms a 32-bit ARGB or RGBA pixel buffer in-place from premultiplied alpha format to nonpremultiplied alpha format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimage/pixelbuffer/unpremultiply(alpha:)-i0ri)*