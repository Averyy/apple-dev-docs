# unpremultiply(channelOrdering:)

**Framework**: Accelerate  
**Kind**: method

Transforms an unsigned 16-bit ARGB or RGBA pixel buffer in-place from premultiplied alpha format to nonpremultiplied alpha format.

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

This function divides the color values in each pixel `self` by the corresponding alpha value and copies the alpha value to the destination unchanged. The function treats the values `0 ... UInt16.max` in the pixel buffer as the values `0 ... 1`.

For example, the following code divides the RGB values `[UInt16.max / 8, UInt16.max / 4, UInt16.max / 2]` by the alpha value `UInt16.max / 2`:

```swift
let src = vImage.PixelBuffer<vImage.Interleaved16Ux4>(
    pixelValues: [UInt16.max / 2,
                  UInt16.max / 8, UInt16.max / 4, UInt16.max / 2],
    size: vImage.Size(width: 1, height: 1))

src.unpremultiply(channelOrdering: .ARGB)

// Prints "[32767, 16383, 32767, 65535]"
//  ≅ [UInt16.max / 2, UInt16.max / 4, UInt16.max / 2, UInt16.max]
print(src.array)
```

## Parameters

- `channelOrdering`: The channel ordering of the source buffer.

## See Also

- [func unpremultiply(alpha: vImage.PixelBuffer<Format>)](vimage/pixelbuffer/unpremultiply(alpha:)-xnog.md)
  Transforms an 8-bit planar pixel buffer in-place from premultiplied alpha format to nonpremultiplied alpha format.
- [func unpremultiply(alpha: vImage.PixelBuffer<Format>)](vimage/pixelbuffer/unpremultiply(alpha:)-i0ri.md)
  Transforms a 32-bit planar pixel buffer in-place from premultiplied alpha format to nonpremultiplied alpha format.
- [func unpremultiply(channelOrdering: vImage.ChannelOrdering)](vimage/pixelbuffer/unpremultiply(channelordering:)-1pkat.md)
  Transforms an 8-bit ARGB or RGBA pixel buffer in-place from premultiplied alpha format to nonpremultiplied alpha format.
- [func unpremultiply()](vimage/pixelbuffer/unpremultiply.md)
  Transforms a floating-point 16-bit RGBA pixel buffer in-place from premultiplied alpha format to nonpremultiplied alpha format.
- [func unpremultiply(channelOrdering: vImage.ChannelOrdering)](vimage/pixelbuffer/unpremultiply(channelordering:)-82uq3.md)
  Transforms a 32-bit ARGB or RGBA pixel buffer in-place from premultiplied alpha format to nonpremultiplied alpha format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimage/pixelbuffer/unpremultiply(channelordering:)-19l0s)*