# premultiply(channelOrdering:)

**Framework**: Accelerate  
**Kind**: method

Transforms a floating-point 32-bit ARGB or RGBA pixel buffer in-place from nonpremultiplied alpha format to premultiplied alpha format.

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
func premultiply(channelOrdering: vImage.ChannelOrdering)
```

#### Discussion

This function multiplies the color values in each pixel `self` by the corresponding alpha value and copies the alpha value to the destination unchanged.

For example, the following code multiplies the RGB values `[0.125, 0.25, 0.5]` by the alpha value `0.5`:

```swift
let src = vImage.PixelBuffer<vImage.InterleavedFx4>(
    pixelValues: [0.5,
                  0.125, 0.25, 0.5],
    size: vImage.Size(width: 1, height: 1))

src.premultiply(channelOrdering: .ARGB)

// Prints "[0.5, 0.0625, 0.125, 0.25"
print(src.array)
```

## Parameters

- `channelOrdering`: The channel ordering of the source buffer.

## See Also

- [func premultiply(alpha: vImage.PixelBuffer<Format>)](vimage/pixelbuffer/premultiply(alpha:)-11gly.md)
  Transforms an 8-bit planar pixel buffer in-place from nonpremultiplied alpha format to premultiplied alpha format.
- [func premultiply(alpha: vImage.PixelBuffer<Format>)](vimage/pixelbuffer/premultiply(alpha:)-76rr.md)
  Transforms a 32-bit planar pixel buffer in-place from nonpremultiplied alpha format to premultiplied alpha format.
- [func premultiply(channelOrdering: vImage.ChannelOrdering)](vimage/pixelbuffer/premultiply(channelordering:)-4xpq9.md)
  Transforms an 8-bit ARGB or RGBA pixel buffer in-place from nonpremultiplied alpha format to premultiplied alpha format.
- [func premultiply(channelOrdering: vImage.ChannelOrdering)](vimage/pixelbuffer/premultiply(channelordering:)-302ci.md)
  Transforms an unsigned 16-bit ARGB or RGBA pixel buffer in-place from nonpremultiplied alpha format to premultiplied alpha format.
- [func premultiply()](vimage/pixelbuffer/premultiply.md)
  Transforms a floating-point 16-bit RGBA pixel buffer in-place from nonpremultiplied alpha format to premultiplied alpha format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimage/pixelbuffer/premultiply(channelordering:)-fzwd)*