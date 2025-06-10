# planarBuffers()

**Framework**: Accelerate  
**Kind**: method

Returns four 32-bit planar pixel buffers that contain the deinterleaved channels of the 8-bit buffer.

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

This function treats 32-bit floating point pixels represented by the range `0 ... 1` as the [`Pixel_8`](pixel_8.md) range `0 … 255`.

Use this function to deinterleave a buffer and create four new planar buffers that contain copies of each source channel. For example, the following code generates four 1 x 1 planar buffers from an [`vImage.Interleaved8x4`](vimage/interleaved8x4.md) pixel buffer:

```swift
let src = vImage.PixelBuffer<vImage.Interleaved8x4>(
    pixelValues: [255 / 17, 255 / 15, 255 / 5, 255 / 3] as [UInt8],
    size: vImage.Size(width: 1, height: 1))

let planarBuffers: [vImage.PixelBuffer<vImage.PlanarF>] = src.planarBuffers()

// Prints "[0.058823533] [0.06666667] [0.20000002] [0.33333334]"
// ≅ [ 1 / 17, 1 / 15, 1 / 5, 1 / 3]
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
- [func planarBuffers() -> [vImage.PixelBuffer<vImage.Planar16U>]](vimage/pixelbuffer/planarbuffers-49gf9.md)
  Returns four unsigned 16-bit planar pixel buffers that contain the deinterleaved channels of the buffer.
- [func planarBuffers() -> [vImage.PixelBuffer<vImage.PlanarF>]](vimage/pixelbuffer/planarbuffers-1rj01.md)
  Returns two 32-bit planar pixel buffers that contain the deinterleaved channels of the buffer.
- [func planarBuffers() -> [vImage.PixelBuffer<vImage.PlanarF>]](vimage/pixelbuffer/planarbuffers-82ook.md)
  Returns three 32-bit planar pixel buffers that contain the deinterleaved channels of the buffer.
- [func planarBuffers() -> [vImage.PixelBuffer<vImage.Planar8>]](vimage/pixelbuffer/planarbuffers-l33r.md)
  Returns four 8-bit planar pixel buffers that contain the deinterleaved channels of the 32-bit buffer.
- [func planarBuffers() -> [vImage.PixelBuffer<vImage.PlanarF>]](vimage/pixelbuffer/planarbuffers-35dnv.md)
  Returns four 32-bit planar pixel buffers that contain the deinterleaved channels of the buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimage/pixelbuffer/planarbuffers()-4qws5)*