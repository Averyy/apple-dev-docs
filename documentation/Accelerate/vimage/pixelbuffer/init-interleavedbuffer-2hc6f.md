# init(interleavedBuffer:)

**Framework**: Accelerate  
**Kind**: init

Creates a 4-channel, 32-bit-per-channel multiple-plane buffer from a 4-channel, 32-bit-per-channel interleaved buffer.

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
init(interleavedBuffer: vImage.PixelBuffer<vImage.InterleavedFx4>)
```

#### Discussion

Use this function to deinterleave a pixel buffer and store the result as homogeneous planes that are represented by multiple underlying vImage buffers.

For example, the following code creates a new [`vImage.PlanarFx4`](vimage/planarfx4.md) pixel buffer from a [`vImage.InterleavedFx4`](vimage/interleavedfx4.md) pixel buffer:

```swift
let src = vImage.PixelBuffer<vImage.InterleavedFx4>(
    pixelValues: [0.2, 0.4, 0.6, 0.8] as [Float],
    size: vImage.Size(width: 1, height: 1))

let dest = vImage.PixelBuffer<vImage.PlanarFx4>(interleavedBuffer: src)

// Prints "[0.2] [0.4] [0.6] [0.8]"
dest.withUnsafePixelBuffers { pixelBuffers in
    for pixelBuffer in pixelBuffers {
        print(pixelBuffer.array)
    }
}
```

## Parameters

- `interleavedBuffer`: The source pixel buffer.

## See Also

- [init(interleavedBuffer: vImage.PixelBuffer<vImage.Interleaved8x3>)](vimage/pixelbuffer/init(interleavedbuffer:)-9xct6.md)
  Creates a 3-channel, 8-bit-per-channel multiple-plane buffer from a 3-channel, 8-bit-per-channel interleaved buffer.
- [init(interleavedBuffer: vImage.PixelBuffer<vImage.Interleaved8x4>)](vimage/pixelbuffer/init(interleavedbuffer:)-8f6xn.md)
  Creates a 4-channel, 8-bit-per-channel mutiple-plane buffer from a 4-channel, 8-bit-per-channel interleaved buffer.
- [init(interleavedBuffer: vImage.PixelBuffer<vImage.InterleavedFx3>)](vimage/pixelbuffer/init(interleavedbuffer:)-77n3i.md)
  Creates a 3-channel, 32-bit-per-channel multiple-plane buffer from a 3-channel, 32-bit-per-channel interleaved buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimage/pixelbuffer/init(interleavedbuffer:)-2hc6f)*