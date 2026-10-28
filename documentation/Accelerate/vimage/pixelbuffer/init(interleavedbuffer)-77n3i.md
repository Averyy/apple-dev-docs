# init(interleavedBuffer:)

**Framework**: Accelerate  
**Kind**: init  
**Role**: Initializer

Creates a 3-channel, 32-bit-per-channel multiple-plane buffer from a 3-channel, 32-bit-per-channel interleaved buffer.

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
init(interleavedBuffer: vImage.PixelBuffer<vImage.InterleavedFx3>)
```

Available when `Format` is `vImage.PlanarFx3`.

## Discussion

Use this function to deinterleave a pixel buffer and store the result as homogeneous planes that are represented by multiple underlying vImage buffers.

For example, the following code creates a new [`vImage.PlanarFx3`](../planarfx3.md) pixel buffer from a [`vImage.InterleavedFx3`](../interleavedfx3.md) pixel buffer:

```swift
let src = vImage.PixelBuffer<vImage.InterleavedFx3>(
    pixelValues: [0.25, 0.5, 0.75] as [Float],
    size: vImage.Size(width: 1, height: 1))

let dest = vImage.PixelBuffer<vImage.PlanarFx3>(interleavedBuffer: src)

// Prints "[0.25] [0.5] [0.75]".
dest.withUnsafePixelBuffers { pixelBuffers in
    for pixelBuffer in pixelBuffers {
        print(pixelBuffer.array)
    }
}
```

## Parameters

- `interleavedBuffer`: The source pixel buffer.

## See Also

### Creating a multiple-plane buffer from an interleaved buffer
- [init(interleavedBuffer: vImage.PixelBuffer<vImage.Interleaved8x3>)](./init%28interleavedbuffer%29-9xct6.md)
  Creates a 3-channel, 8-bit-per-channel multiple-plane buffer from a 3-channel, 8-bit-per-channel interleaved buffer.
- [init(interleavedBuffer: vImage.PixelBuffer<vImage.Interleaved8x4>)](./init%28interleavedbuffer%29-8f6xn.md)
  Creates a 4-channel, 8-bit-per-channel mutiple-plane buffer from a 4-channel, 8-bit-per-channel interleaved buffer.
- [init(interleavedBuffer: vImage.PixelBuffer<vImage.InterleavedFx4>)](./init%28interleavedbuffer%29-2hc6f.md)
  Creates a 4-channel, 32-bit-per-channel multiple-plane buffer from a 4-channel, 32-bit-per-channel interleaved buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimage/pixelbuffer/init(interleavedbuffer:)-77n3i)*