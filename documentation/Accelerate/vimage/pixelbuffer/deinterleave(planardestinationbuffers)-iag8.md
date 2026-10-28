# deinterleave(planarDestinationBuffers:)

**Framework**: Accelerate  
**Kind**: method  
**Role**: Instance Method

Deinterleaves the 32-bit-per-channel, four-channel interleaved buffer and writes the result to an array that contains four planar buffers.

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
func deinterleave(planarDestinationBuffers: [vImage.PixelBuffer<vImage.PlanarF>])
```

Available when `Format` is `vImage.InterleavedFx4`.

## Discussion

Use this function to deinterleave a buffer and overwrite planar buffers with copies of each source channel.

## Parameters

- `planarDestinationBuffers`: The destination pixel buffers.

## See Also

### Deinterleaving pixel buffers
- [func deinterleave(destination: vImage.PixelBuffer<vImage.Planar8x3>)](./deinterleave%28destination%29-hrhz.md)
  Deinterleaves the 8-bit-per-channel, three-channel interleaved buffer and writes the result to a multiple-plane pixel buffer.
- [func deinterleave(destination: vImage.PixelBuffer<vImage.Planar8x4>)](./deinterleave%28destination%29-4bj4f.md)
  Deinterleaves the 8-bit-per-channel, four-channel interleaved buffer and writes the result to a multiple-plane pixel buffer.
- [func deinterleave(destination: vImage.PixelBuffer<vImage.PlanarFx3>)](./deinterleave%28destination%29-9gkke.md)
  Deinterleaves the 32-bit-per-channel, three-channel interleaved buffer and writes the result to a multiple-plane pixel buffer.
- [func deinterleave(destination: vImage.PixelBuffer<vImage.PlanarFx4>)](./deinterleave%28destination%29-7hep3.md)
  Deinterleaves the 32-bit-per-channel, four-channel interleaved buffer and writes the result to a multiple-plane pixel buffer.
- [func deinterleave(planarDestinationBuffers: [vImage.PixelBuffer<vImage.Planar8>])](./deinterleave%28planardestinationbuffers%29-72108.md)
  Deinterleaves the 8-bit-per-channel, three-channel interleaved buffer and writes the result to an array that contains three planar buffers.
- [func deinterleave(planarDestinationBuffers: [vImage.PixelBuffer<vImage.Planar8>])](./deinterleave%28planardestinationbuffers%29-3u4kn.md)
  Deinterleaves the 8-bit-per-channel, four-channel interleaved buffer and writes the result to an array that contains four planar buffers.
- [func deinterleave(planarDestinationBuffers: [vImage.PixelBuffer<vImage.Planar16F>])](./deinterleave%28planardestinationbuffers%29-75uki.md)
  Deinterleaves the 16-bit-per-channel, four-channel interleaved buffer and writes the result to an array that contains four planar buffers.
- [func deinterleave(planarDestinationBuffers: [vImage.PixelBuffer<vImage.Planar16U>])](./deinterleave%28planardestinationbuffers%29-3irjf.md)
  Deinterleaves the unsigned 16-bit-per-channel, four-channel interleaved buffer and writes the result to an array that contains four planar buffers.
- [func deinterleave(planarDestinationBuffers: [vImage.PixelBuffer<vImage.PlanarF>])](./deinterleave%28planardestinationbuffers%29-2gt2g.md)
  Deinterleaves the 32-bit-per-channel, three-channel interleaved buffer and writes the result to an array that contains three planar buffers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimage/pixelbuffer/deinterleave(planardestinationbuffers:)-iag8)*