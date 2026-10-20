# convert(to:)

**Framework**: Accelerate  
**Kind**: method  
**Role**: Instance Method

Converts the contents of an 8-bit, three-plane pixel buffer to a three-channel interleaved pixel buffer.

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
func convert(to destination: vImage.PixelBuffer<vImage.Interleaved8x3>)
```

Available when `Format` is `vImage.Planar8x3`.

## Parameters

- `destination`: The destination pixel buffer.

## See Also

### Converting from 8-bit multiple plane to 8-bit interleaved
- [func convert(to: vImage.PixelBuffer<vImage.Interleaved8x4>)](./convert%28to%29-1jtfh.md)
  Converts the contents of an 8-bit, four-plane pixel buffer to a four-channel interleaved pixel buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimage/pixelbuffer/convert(to:)-7xv7)*