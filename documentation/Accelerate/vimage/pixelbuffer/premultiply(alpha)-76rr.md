# premultiply(alpha:)

**Framework**: Accelerate  
**Kind**: method  
**Role**: Instance Method

Transforms a 32-bit planar pixel buffer in-place from nonpremultiplied alpha format to premultiplied alpha format.

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
func premultiply(alpha: vImage.PixelBuffer<Format>)
```

Available when `Format` is `vImage.PlanarF`.

#### Discussion

This function multiplies the color values in `self` by the corresponding alpha values. For example, the following code premultiplies a 4 x 1 planar pixel buffer with the corresponding pixels in a separate planar alpha buffer:

```swift
let src = vImage.PixelBuffer<vImage.PlanarF>(
    pixelValues: [0.125, 0.25, 0.5, 1],
    size: vImage.Size(width: 4, height: 1))

let alpha = vImage.PixelBuffer<vImage.PlanarF>(
    pixelValues: [0, 0.25, 0.5, 1],
    size: vImage.Size(width: 4, height: 1))

src.premultiply(alpha: alpha)

// Prints "[0, 0.0625, 0.25, 1]".
print(src.array)

```

## Parameters

- `alpha`: An 32-bit planar pixel buffer that contains the alpha.

## See Also

### Premultiply
- [func premultiply(alpha: vImage.PixelBuffer<Format>)](./premultiply%28alpha%29-11gly.md)
  Transforms an 8-bit planar pixel buffer in-place from nonpremultiplied alpha format to premultiplied alpha format.
- [func premultiply(channelOrdering: vImage.ChannelOrdering)](./premultiply%28channelordering%29-4xpq9.md)
  Transforms an 8-bit ARGB or RGBA pixel buffer in-place from nonpremultiplied alpha format to premultiplied alpha format.
- [func premultiply(channelOrdering: vImage.ChannelOrdering)](./premultiply%28channelordering%29-302ci.md)
  Transforms an unsigned 16-bit ARGB or RGBA pixel buffer in-place from nonpremultiplied alpha format to premultiplied alpha format.
- [func premultiply()](./premultiply%28%29.md)
  Transforms a floating-point 16-bit RGBA pixel buffer in-place from nonpremultiplied alpha format to premultiplied alpha format.
- [func premultiply(channelOrdering: vImage.ChannelOrdering)](./premultiply%28channelordering%29-fzwd.md)
  Transforms a floating-point 32-bit ARGB or RGBA pixel buffer in-place from nonpremultiplied alpha format to premultiplied alpha format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimage/pixelbuffer/premultiply(alpha:)-76rr)*