# convert(to:)

**Framework**: Accelerate  
**Kind**: method

Converts the contents of a 32-bit, four-plane pixel buffer to a four-channel interleaved pixel buffer.

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
func convert(to destination: vImage.PixelBuffer<vImage.InterleavedFx4>)
```

## Parameters

- `destination`: The destination pixel buffer.

## See Also

- [func convert(to: vImage.PixelBuffer<vImage.InterleavedFx3>)](vimage/pixelbuffer/convert(to:)-8bqjc.md)
  Converts the contents of a 32-bit, three-plane pixel buffer to a three-channel interleaved pixel buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimage/pixelbuffer/convert(to:)-26s6v)*