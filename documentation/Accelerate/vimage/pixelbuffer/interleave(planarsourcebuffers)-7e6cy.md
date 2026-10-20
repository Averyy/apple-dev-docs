# interleave(planarSourceBuffers:)

**Framework**: Accelerate  
**Kind**: method  
**Role**: Instance Method

Interleaves the specified planar source buffers and writes the result to the 32-bit-per-channel, four-channel interleaved buffer.

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
func interleave(planarSourceBuffers: [vImage.PixelBuffer<vImage.PlanarF>])
```

Available when `Format` is `vImage.InterleavedFx4`.

#### Discussion

Use this function to interleave a collection of planar buffers and overwrite an interleaved buffer with a copy of the source channels.

## Parameters

- `planarSourceBuffers`: The planar source buffers.

## See Also

### Interleaving pixel buffers
- [func interleave(destination: vImage.PixelBuffer<vImage.Interleaved8x3>)](./interleave%28destination%29-46cgi.md)
  Interleaves the 8-bit-per-channel, three-channel multiple-plane buffer and writes the result to an interleaved pixel buffer.
- [func interleave(destination: vImage.PixelBuffer<vImage.Interleaved8x4>)](./interleave%28destination%29-6r7se.md)
  Interleaves the 8-bit-per-channel, four-channel multiple-plane buffer and writes the result to an interleaved pixel buffer.
- [func interleave(destination: vImage.PixelBuffer<vImage.InterleavedFx3>)](./interleave%28destination%29-5ewup.md)
  Interleaves the 32-bit-per-channel, three-channel multiple-plane buffer and writes the result to an interleaved pixel buffer.
- [func interleave(destination: vImage.PixelBuffer<vImage.InterleavedFx4>)](./interleave%28destination%29-6ib0t.md)
  Interleaves the 32-bit-per-channel, four-channel multiple-plane buffer and writes the result to an interleaved pixel buffer.
- [func interleave(planarSourceBuffers: [vImage.PixelBuffer<vImage.Planar8>])](./interleave%28planarsourcebuffers%29-10yj5.md)
  Interleaves the specified planar source buffers and writes the result to the 8-bit-per-channel, three-channel interleaved buffer.
- [func interleave(planarSourceBuffers: [vImage.PixelBuffer<vImage.Planar8>])](./interleave%28planarsourcebuffers%29-67l5.md)
  Interleaves the specified planar source buffers and writes the result to the 8-bit-per-channel, four-channel interleaved buffer.
- [func interleave(planarSourceBuffers: [vImage.PixelBuffer<vImage.Planar16F>])](./interleave%28planarsourcebuffers%29-7qcri.md)
  Interleaves the specified planar source buffers and writes the result to the 16-bit-per-channel, four-channel interleaved buffer.
- [func interleave(planarSourceBuffers: [vImage.PixelBuffer<vImage.Planar16U>])](./interleave%28planarsourcebuffers%29-1i8we.md)
  Interleaves the specified planar source buffers and writes the result to the unsigned 16-bit-per-channel, four-channel interleaved buffer.
- [func interleave(planarSourceBuffers: [vImage.PixelBuffer<vImage.PlanarF>])](./interleave%28planarsourcebuffers%29-4qotd.md)
  Interleaves the specified planar source buffers and writes the result to the 32-bit-per-channel, three-channel interleaved buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimage/pixelbuffer/interleave(planarsourcebuffers:)-7e6cy)*