# init(planarBuffers:)

**Framework**: Accelerate  
**Kind**: init

Creates a 4-channel, 8-bit-per-channel interleaved buffer from four 8-bit planar buffers.

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
init(planarBuffers: [vImage.PixelBuffer<vImage.Planar8>])
```

#### Discussion

Use this function to interleave four discrete planar buffers. For example, the following code creates a four-channel interleaved buffer from four planar buffers:

```swift
let planar0 = vImage.PixelBuffer<vImage.Planar8>(
    pixelValues: [UInt8(50)],
    size: vImage.Size(width: 1, height: 1))

let planar1 = vImage.PixelBuffer<vImage.Planar8>(
    pixelValues: [UInt8(100)],
    size: vImage.Size(width: 1, height: 1))

let planar2 = vImage.PixelBuffer<vImage.Planar8>(
    pixelValues: [UInt8(150)],
    size: vImage.Size(width: 1, height: 1))

let planar3 = vImage.PixelBuffer<vImage.Planar8>(
    pixelValues: [UInt8(200)],
    size: vImage.Size(width: 1, height: 1))

let interleaved = vImage.PixelBuffer<vImage.Interleaved8x4>(
    planarBuffers: [planar0, planar1, planar2, planar3])

// Prints "[50, 100, 150, 200]"
print(interleaved.array)
```

## Parameters

- `planarBuffers`: An array that contains four 8-bit planar buffers.

## See Also

- [init(planarBuffers: [vImage.PixelBuffer<vImage.Planar8>])](vimage/pixelbuffer/init(planarbuffers:)-727d.md)
  Creates a 2-channel, 8-bit-per-channel interleaved buffer from two 8-bit planar buffers.
- [init(planarBuffers: [vImage.PixelBuffer<vImage.Planar8>])](vimage/pixelbuffer/init(planarbuffers:)-6r9p0.md)
  Creates a 3-channel, 8-bit-per-channel interleaved buffer from three 8-bit planar buffers.
- [init(planarBuffers: [vImage.PixelBuffer<vImage.PlanarF>])](vimage/pixelbuffer/init(planarbuffers:)-8nt2j.md)
  Creates a 4-channel, 8-bit-per-channel interleaved buffer from four 32-bit planar buffers.
- [init(planarBuffers: [vImage.PixelBuffer<vImage.PlanarF>])](vimage/pixelbuffer/init(planarbuffers:)-n2mq.md)
  Creates a 2-channel, 32-bit-per-channel interleaved buffer from two 32-bit planar buffers.
- [init(planarBuffers: [vImage.PixelBuffer<vImage.PlanarF>])](vimage/pixelbuffer/init(planarbuffers:)-7wt24.md)
  Creates a 3-channel, 32-bit-per-channel interleaved buffer from three 32-bit planar buffers.
- [init(planarBuffers: [vImage.PixelBuffer<vImage.PlanarF>])](vimage/pixelbuffer/init(planarbuffers:)-59s4n.md)
  Creates a 4-channel, 32-bit-per-channel interleaved buffer from four 32-bit planar buffers.
- [init(planarBuffers: [vImage.PixelBuffer<vImage.Planar16U>])](vimage/pixelbuffer/init(planarbuffers:)-2575t.md)
  Creates a 4-channel, 16-bit-per-channel interleaved buffer from four 16-bit planar buffers.
- [init(lumaSource: vImage.PixelBuffer<vImage.Planar8>, chromaSource: vImage.PixelBuffer<vImage.Interleaved8x2>, conversionInfo: vImage_YpCbCrToARGB)](vimage/pixelbuffer/init(lumasource:chromasource:conversioninfo:).md)
  Creates a 4-channel, 8-bit-per-channel interleaved buffer from a planar Yp buffer and a two-channel interleaved CbCr buffer.
- [init(interleavedBuffer: vImage.PixelBuffer<vImage.Interleaved8x4>)](vimage/pixelbuffer/init(interleavedbuffer:)-35or3.md)
  Creates a 4-channel, 32-bit-per-channel interleaved buffer from a 4-channel, 8-bit-per-channel interleaved buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimage/pixelbuffer/init(planarbuffers:)-6hkso)*