# convert(to:channelOrdering:)

**Framework**: Accelerate  
**Kind**: method  
**Role**: Instance Method

Converts the 32-bit-per-channel RGBA or ARGB pixel buffer to RGB.

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
func convert(to destination: vImage.PixelBuffer<vImage.InterleavedFx3>, channelOrdering: vImage.ChannelOrdering)
```

Available when `Format` is `vImage.InterleavedFx4`.

## Parameters

- `destination`: The destination pixel buffer.
- `channelOrdering`: An enumeration that specifies whether the source is either ARGB or RGBA.

## See Also

### Conversion from four channels to three channels
- [func convert(to: vImage.PixelBuffer<vImage.Interleaved8x3>, channelOrdering: vImage.ChannelOrdering)](./convert%28to,channelordering%29-9h53.md)
  Converts the 8-bit-per-channel RGBA or ARGB pixel buffer to RGB.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimage/pixelbuffer/convert(to:channelordering:)-1nll2)*