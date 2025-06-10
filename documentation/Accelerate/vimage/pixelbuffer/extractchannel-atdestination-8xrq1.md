# extractChannel(at:destination:)

**Framework**: Accelerate  
**Kind**: method

Extracts a single channel from an 32-bit-per-channel, 4-channel interleaved pixel buffer.

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
func extractChannel(at channelIndex: Int, destination: vImage.PixelBuffer<vImage.PlanarF>)
```

#### Discussion

For example, the following code extracts channel `2` from a four-channel pixel buffer.

```swift
let src = vImage.PixelBuffer<vImage.InterleavedFx4>(
    pixelValues: [0.10, 0.11, 0.12, 0.13,
                  0.20, 0.21, 0.22, 0.23,
                  0.30, 0.31, 0.32, 0.33],
    size: vImage.Size(width: 1, height: 3))

let dest = vImage.PixelBuffer<vImage.PlanarF>(
    size: src.size)

src.extractChannel(at: 2,
                   destination: dest)

// Prints "[0.12, 0.22, 0.32]"
print(dest.array)
```

## Parameters

- `channelIndex`: The index of the channel that the function extracts.
- `destination`: The destination pixel buffer.

## See Also

- [func extractChannel(at: Int, destination: vImage.PixelBuffer<vImage.Planar8>)](vimage/pixelbuffer/extractchannel(at:destination:)-ageg.md)
  Extracts a single channel from an 8-bit-per-channel, 4-channel interleaved pixel buffer.
- [func extractChannel(at: Int, destination: vImage.PixelBuffer<vImage.Planar16U>)](vimage/pixelbuffer/extractchannel(at:destination:)-i1zm.md)
  Extracts a single channel from an unsigned 16-bit-per-channel, 4-channel interleaved pixel buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimage/pixelbuffer/extractchannel(at:destination:)-8xrq1)*