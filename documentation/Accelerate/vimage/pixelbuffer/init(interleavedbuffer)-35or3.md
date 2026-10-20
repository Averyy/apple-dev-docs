# init(interleavedBuffer:)

**Framework**: Accelerate  
**Kind**: init  
**Role**: Initializer

Creates a 4-channel, 32-bit-per-channel interleaved buffer from a 4-channel, 8-bit-per-channel interleaved buffer.

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
init(interleavedBuffer: vImage.PixelBuffer<vImage.Interleaved8x4>)
```

Available when `Format` is `vImage.InterleavedFx4`.

#### Discussion

This function treats floating point pixels represented by the range `0 ... 1` as the [`UInt8`](../../../kernel/uint8.md) range `0 ... 255`.

For example, the following code initializes an [`vImage.InterleavedFx4`](../interleavedfx4.md) pixel buffer from a [`vImage.Interleaved8x4`](../interleaved8x4.md) pixel buffer:

```swift
let src = vImage.PixelBuffer<vImage.Interleaved8x4>(
    pixelValues: [255 / 17,
                  255 / 15,
                  255 / 5,
                  255 / 3] as [UInt8],
    size: vImage.Size(width: 1,
                      height: 1))

let dest = vImage.PixelBuffer<vImage.InterleavedFx4>(interleavedBuffer: src)
```

## Parameters

- `interleavedBuffer`: The source pixel buffer.

## See Also

### Creating an interleaved buffer from another buffer
- [init(planarBuffers: [vImage.PixelBuffer<vImage.Planar8>])](./init%28planarbuffers%29-727d.md)
  Creates a 2-channel, 8-bit-per-channel interleaved buffer from two 8-bit planar buffers.
- [init(planarBuffers: [vImage.PixelBuffer<vImage.Planar8>])](./init%28planarbuffers%29-6r9p0.md)
  Creates a 3-channel, 8-bit-per-channel interleaved buffer from three 8-bit planar buffers.
- [init(planarBuffers: [vImage.PixelBuffer<vImage.Planar8>])](./init%28planarbuffers%29-6hkso.md)
  Creates a 4-channel, 8-bit-per-channel interleaved buffer from four 8-bit planar buffers.
- [init(planarBuffers: [vImage.PixelBuffer<vImage.PlanarF>])](./init%28planarbuffers%29-8nt2j.md)
  Creates a 4-channel, 8-bit-per-channel interleaved buffer from four 32-bit planar buffers.
- [init(planarBuffers: [vImage.PixelBuffer<vImage.PlanarF>])](./init%28planarbuffers%29-n2mq.md)
  Creates a 2-channel, 32-bit-per-channel interleaved buffer from two 32-bit planar buffers.
- [init(planarBuffers: [vImage.PixelBuffer<vImage.PlanarF>])](./init%28planarbuffers%29-7wt24.md)
  Creates a 3-channel, 32-bit-per-channel interleaved buffer from three 32-bit planar buffers.
- [init(planarBuffers: [vImage.PixelBuffer<vImage.PlanarF>])](./init%28planarbuffers%29-59s4n.md)
  Creates a 4-channel, 32-bit-per-channel interleaved buffer from four 32-bit planar buffers.
- [init(planarBuffers: [vImage.PixelBuffer<vImage.Planar16U>])](./init%28planarbuffers%29-2575t.md)
  Creates a 4-channel, 16-bit-per-channel interleaved buffer from four 16-bit planar buffers.
- [init(lumaSource: vImage.PixelBuffer<vImage.Planar8>, chromaSource: vImage.PixelBuffer<vImage.Interleaved8x2>, conversionInfo: vImage_YpCbCrToARGB)](./init%28lumasource,chromasource,conversioninfo%29.md)
  Creates a 4-channel, 8-bit-per-channel interleaved buffer from a planar Yp buffer and a two-channel interleaved CbCr buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimage/pixelbuffer/init(interleavedbuffer:)-35or3)*