# unpremultiply(channelOrdering:)

**Framework**: Accelerate  
**Kind**: method

Transforms an 8-bit ARGB or RGBA pixel buffer in-place from premultiplied alpha format to nonpremultiplied alpha format.

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
func unpremultiply(channelOrdering: vImage.ChannelOrdering)
```

#### Discussion

This function divides the color values in each pixel `self` by the corresponding alpha value and copies the alpha value to the destination unchanged. The function treats the values `0 ... 255` in the pixel buffer as the values `0 ... 1`.

For example, the following code divides the RGB values `[32, 64, 128]` by  the alpha value `128` (interpreted as `0.5`):

```swift
let src = vImage.PixelBuffer<vImage.Interleaved8x4>(
    pixelValues: [127, 32, 64, 128],
    size: vImage.Size(width: 1, height: 1))

src.unpremultiply(channelOrdering: .ARGB)

// Prints "[127, 64, 129, 255]".
print(src.array)
```

## Parameters

- `channelOrdering`: The channel ordering of the source buffer.

## See Also

- [func unpremultiply(alpha: vImage.PixelBuffer<Format>)](vimage/pixelbuffer/unpremultiply(alpha:)-xnog.md)
  Transforms an 8-bit planar pixel buffer in-place from premultiplied alpha format to nonpremultiplied alpha format.
- [func unpremultiply(alpha: vImage.PixelBuffer<Format>)](vimage/pixelbuffer/unpremultiply(alpha:)-i0ri.md)
  Transforms a 32-bit planar pixel buffer in-place from premultiplied alpha format to nonpremultiplied alpha format.
- [func unpremultiply(channelOrdering: vImage.ChannelOrdering)](vimage/pixelbuffer/unpremultiply(channelordering:)-19l0s.md)
  Transforms an unsigned 16-bit ARGB or RGBA pixel buffer in-place from premultiplied alpha format to nonpremultiplied alpha format.
- [func unpremultiply()](vimage/pixelbuffer/unpremultiply.md)
  Transforms a floating-point 16-bit RGBA pixel buffer in-place from premultiplied alpha format to nonpremultiplied alpha format.
- [func unpremultiply(channelOrdering: vImage.ChannelOrdering)](vimage/pixelbuffer/unpremultiply(channelordering:)-82uq3.md)
  Transforms a 32-bit ARGB or RGBA pixel buffer in-place from premultiplied alpha format to nonpremultiplied alpha format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimage/pixelbuffer/unpremultiply(channelordering:)-1pkat)*