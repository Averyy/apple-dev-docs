# flatten(channelOrdering:backgroundColor:isPremultiplied:destination:)

**Framework**: Accelerate  
**Kind**: method

Transforms an 8-bit-per-channel RGBA or ARGB buffer to an RGB buffer against an opaque background color.

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
func flatten(channelOrdering: vImage.ChannelOrdering, backgroundColor: Pixel_8888, isPremultiplied: Bool, destination: vImage.PixelBuffer<vImage.Interleaved8x3>)
```

## Parameters

- `channelOrdering`: The channel ordering of the source buffer.
- `backgroundColor`: The background color that the function composites against.
- `isPremultiplied`: A Boolean values that specifies whether the source image is premultiplied.
- `destination`: The destination pixel buffer.

## See Also

- [func flatten(channelOrdering: vImage.ChannelOrdering, backgroundColor: Pixel_FFFF, isPremultiplied: Bool, destination: vImage.PixelBuffer<vImage.InterleavedFx3>)](vimage/pixelbuffer/flatten(channelordering:backgroundcolor:ispremultiplied:destination:)-5g0c2.md)
  Transforms an 32-bit-per-channel RGBA or ARGB buffer to an RGB buffer against an opaque background color.
- [vImage.ChannelOrdering](vimage/channelordering.md)
  Constants that specify the channel ordering of a pixel buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimage/pixelbuffer/flatten(channelordering:backgroundcolor:ispremultiplied:destination:)-97nx)*