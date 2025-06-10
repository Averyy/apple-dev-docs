# unpremultiply()

**Framework**: Accelerate  
**Kind**: method

Transforms a floating-point 16-bit RGBA pixel buffer in-place from premultiplied alpha format to nonpremultiplied alpha format.

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
func unpremultiply()
```

#### Discussion

This function divides the color values in each pixel `self` by the corresponding alpha value and copies the alpha value to the destination unchanged.

For example, the following code divides the RGB values `[0.125, 0.25, 0.5]` by the alpha value `0.5`:

```swift
let pixelValues = [0.125, 0.25, 0.5,
                   Float(0.5)].map {
    return vImage.Planar16F.makePixel($0)
}

let src = vImage.PixelBuffer<vImage.Interleaved16Fx4>(
    pixelValues: pixelValues,
    size: vImage.Size(width: 1, height: 1))
    
src.unpremultiply()

let result = src.array.map {
    return vImage.PlanarF.makePixel($0)
}

// Prints "[0.25, 0.5, 1.0, 0.5]".
print(result)
```

## See Also

- [func unpremultiply(alpha: vImage.PixelBuffer<Format>)](vimage/pixelbuffer/unpremultiply(alpha:)-xnog.md)
  Transforms an 8-bit planar pixel buffer in-place from premultiplied alpha format to nonpremultiplied alpha format.
- [func unpremultiply(alpha: vImage.PixelBuffer<Format>)](vimage/pixelbuffer/unpremultiply(alpha:)-i0ri.md)
  Transforms a 32-bit planar pixel buffer in-place from premultiplied alpha format to nonpremultiplied alpha format.
- [func unpremultiply(channelOrdering: vImage.ChannelOrdering)](vimage/pixelbuffer/unpremultiply(channelordering:)-1pkat.md)
  Transforms an 8-bit ARGB or RGBA pixel buffer in-place from premultiplied alpha format to nonpremultiplied alpha format.
- [func unpremultiply(channelOrdering: vImage.ChannelOrdering)](vimage/pixelbuffer/unpremultiply(channelordering:)-19l0s.md)
  Transforms an unsigned 16-bit ARGB or RGBA pixel buffer in-place from premultiplied alpha format to nonpremultiplied alpha format.
- [func unpremultiply(channelOrdering: vImage.ChannelOrdering)](vimage/pixelbuffer/unpremultiply(channelordering:)-82uq3.md)
  Transforms a 32-bit ARGB or RGBA pixel buffer in-place from premultiplied alpha format to nonpremultiplied alpha format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimage/pixelbuffer/unpremultiply())*