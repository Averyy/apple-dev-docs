# interleave(planarSourceBuffers:)

**Framework**: Accelerate  
**Kind**: method

Interleaves the specified planar source buffers and writes the result to the 32-bit-per-channel, three-channel interleaved buffer.

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
func interleave(planarSourceBuffers: [vImage.PixelBuffer<vImage.PlanarF>])
```

#### Discussion

Use this function to interleave a collection of planar buffers and overwrite an interleaved buffer with a copy of the source channels.

## Parameters

- `planarSourceBuffers`: The planar source buffers.

## See Also

- [func interleave(destination: vImage.PixelBuffer<vImage.Interleaved8x3>)](vimage/pixelbuffer/interleave(destination:)-46cgi.md)
  Interleaves the 8-bit-per-channel, three-channel multiple-plane buffer and writes the result to an interleaved pixel buffer.
- [func interleave(destination: vImage.PixelBuffer<vImage.Interleaved8x4>)](vimage/pixelbuffer/interleave(destination:)-6r7se.md)
  Interleaves the 8-bit-per-channel, four-channel multiple-plane buffer and writes the result to an interleaved pixel buffer.
- [func interleave(destination: vImage.PixelBuffer<vImage.InterleavedFx3>)](vimage/pixelbuffer/interleave(destination:)-5ewup.md)
  Interleaves the 32-bit-per-channel, three-channel multiple-plane buffer and writes the result to an interleaved pixel buffer.
- [func interleave(destination: vImage.PixelBuffer<vImage.InterleavedFx4>)](vimage/pixelbuffer/interleave(destination:)-6ib0t.md)
  Interleaves the 32-bit-per-channel, four-channel multiple-plane buffer and writes the result to an interleaved pixel buffer.
- [func interleave(planarSourceBuffers: [vImage.PixelBuffer<vImage.Planar8>])](vimage/pixelbuffer/interleave(planarsourcebuffers:)-10yj5.md)
  Interleaves the specified planar source buffers and writes the result to the 8-bit-per-channel, three-channel interleaved buffer.
- [func interleave(planarSourceBuffers: [vImage.PixelBuffer<vImage.Planar8>])](vimage/pixelbuffer/interleave(planarsourcebuffers:)-67l5.md)
  Interleaves the specified planar source buffers and writes the result to the 8-bit-per-channel, four-channel interleaved buffer.
- [func interleave(planarSourceBuffers: [vImage.PixelBuffer<vImage.Planar16F>])](vimage/pixelbuffer/interleave(planarsourcebuffers:)-7qcri.md)
  Interleaves the specified planar source buffers and writes the result to the 16-bit-per-channel, four-channel interleaved buffer.
- [func interleave(planarSourceBuffers: [vImage.PixelBuffer<vImage.Planar16U>])](vimage/pixelbuffer/interleave(planarsourcebuffers:)-1i8we.md)
  Interleaves the specified planar source buffers and writes the result to the unsigned 16-bit-per-channel, four-channel interleaved buffer.
- [func interleave(planarSourceBuffers: [vImage.PixelBuffer<vImage.PlanarF>])](vimage/pixelbuffer/interleave(planarsourcebuffers:)-7e6cy.md)
  Interleaves the specified planar source buffers and writes the result to the 32-bit-per-channel, four-channel interleaved buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimage/pixelbuffer/interleave(planarsourcebuffers:)-4qotd)*