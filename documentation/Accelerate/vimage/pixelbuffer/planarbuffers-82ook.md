# planarBuffers()

**Framework**: Accelerate  
**Kind**: method

Returns three 32-bit planar pixel buffers that contain the deinterleaved channels of the buffer.

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
func planarBuffers() -> [vImage.PixelBuffer<vImage.PlanarF>]
```

#### Return Value

An array of planar pixel buffers.

#### Discussion

Use this function to deinterleave a buffer and create three new planar buffers that contain copies of each source channel. For example, the following code generates three 1 x 1 planar buffers from an [`vImage.InterleavedFx3`](vimage/interleavedfx3.md) pixel buffer:

```swift
let src = vImage.PixelBuffer<vImage.InterleavedFx3>(
    pixelValues: [0.125, 0.25, 0.5] as [Float],
    size: vImage.Size(width: 1, height: 1))

let planarBuffers = src.planarBuffers()

// Prints "[0.125] [0.25] [0.5]"
for planarBuffer in planarBuffers {
    print(planarBuffer.array)
}
```

## See Also

- [func planarBuffers() -> [vImage.PixelBuffer<vImage.Planar8>]](vimage/pixelbuffer/planarbuffers-462ja.md)
  Returns two 8-bit planar pixel buffers that contain the deinterleaved channels of the buffer.
- [func planarBuffers() -> [vImage.PixelBuffer<vImage.Planar8>]](vimage/pixelbuffer/planarbuffers-5r3ds.md)
  Returns three 8-bit planar pixel buffers that contain the deinterleaved channels of the buffer.
- [func planarBuffers() -> [vImage.PixelBuffer<vImage.Planar8>]](vimage/pixelbuffer/planarbuffers-5rx2w.md)
  Returns four 8-bit planar pixel buffers that contain the deinterleaved channels of the buffer.
- [func planarBuffers() -> [vImage.PixelBuffer<vImage.PlanarF>]](vimage/pixelbuffer/planarbuffers-4qws5.md)
  Returns four 32-bit planar pixel buffers that contain the deinterleaved channels of the 8-bit buffer.
- [func planarBuffers() -> [vImage.PixelBuffer<vImage.Planar16U>]](vimage/pixelbuffer/planarbuffers-49gf9.md)
  Returns four unsigned 16-bit planar pixel buffers that contain the deinterleaved channels of the buffer.
- [func planarBuffers() -> [vImage.PixelBuffer<vImage.PlanarF>]](vimage/pixelbuffer/planarbuffers-1rj01.md)
  Returns two 32-bit planar pixel buffers that contain the deinterleaved channels of the buffer.
- [func planarBuffers() -> [vImage.PixelBuffer<vImage.Planar8>]](vimage/pixelbuffer/planarbuffers-l33r.md)
  Returns four 8-bit planar pixel buffers that contain the deinterleaved channels of the 32-bit buffer.
- [func planarBuffers() -> [vImage.PixelBuffer<vImage.PlanarF>]](vimage/pixelbuffer/planarbuffers-35dnv.md)
  Returns four 32-bit planar pixel buffers that contain the deinterleaved channels of the buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimage/pixelbuffer/planarbuffers()-82ook)*