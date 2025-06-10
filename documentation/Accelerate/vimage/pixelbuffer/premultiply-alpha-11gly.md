# premultiply(alpha:)

**Framework**: Accelerate  
**Kind**: method

Transforms an 8-bit planar pixel buffer in-place from nonpremultiplied alpha format to premultiplied alpha format.

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
func premultiply(alpha: vImage.PixelBuffer<Format>)
```

#### Discussion

This function multiplies the color values in `self` by the corresponding alpha values. The function treats the values `0 ... 255` in both pixel buffers as the values `0 ... 1`. For example, the following code premultiplies a 4 x 1 planar pixel buffer with the corresponding pixels in a separate planar alpha buffer:

```swift
let src = vImage.PixelBuffer<vImage.Planar8>(
    pixelValues: [32, 64, 128, 255],
    size: vImage.Size(width: 4, height: 1))

let alpha = vImage.PixelBuffer<vImage.Planar8>(
    pixelValues: [0, 128, 128, 255],
    size: vImage.Size(width: 4, height: 1))

src.premultiply(alpha: alpha)

// Prints "[0, 32, 64, 255]".
print(src.array)
```

## Parameters

- `alpha`: An 8-bit planar pixel buffer that contains the alpha.

## See Also

- [func premultiply(alpha: vImage.PixelBuffer<Format>)](vimage/pixelbuffer/premultiply(alpha:)-76rr.md)
  Transforms a 32-bit planar pixel buffer in-place from nonpremultiplied alpha format to premultiplied alpha format.
- [func premultiply(channelOrdering: vImage.ChannelOrdering)](vimage/pixelbuffer/premultiply(channelordering:)-4xpq9.md)
  Transforms an 8-bit ARGB or RGBA pixel buffer in-place from nonpremultiplied alpha format to premultiplied alpha format.
- [func premultiply(channelOrdering: vImage.ChannelOrdering)](vimage/pixelbuffer/premultiply(channelordering:)-302ci.md)
  Transforms an unsigned 16-bit ARGB or RGBA pixel buffer in-place from nonpremultiplied alpha format to premultiplied alpha format.
- [func premultiply()](vimage/pixelbuffer/premultiply.md)
  Transforms a floating-point 16-bit RGBA pixel buffer in-place from nonpremultiplied alpha format to premultiplied alpha format.
- [func premultiply(channelOrdering: vImage.ChannelOrdering)](vimage/pixelbuffer/premultiply(channelordering:)-fzwd.md)
  Transforms a floating-point 32-bit ARGB or RGBA pixel buffer in-place from nonpremultiplied alpha format to premultiplied alpha format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimage/pixelbuffer/premultiply(alpha:)-11gly)*