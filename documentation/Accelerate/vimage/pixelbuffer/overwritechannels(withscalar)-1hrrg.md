# overwriteChannels(withScalar:)

**Framework**: Accelerate  
**Kind**: method  
**Role**: Instance Method

Overwrites the pixels of the pixel buffer with the provided floating-point 16-bit scalar value.

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
func overwriteChannels(withScalar scalar: Pixel_16F)
```

Available when `Format` is `vImage.Planar16F`.

## Parameters

- `scalar`: The value that the function writes to the channels.

## See Also

### Overwriting Channels
- [func overwriteChannels(withScalar: Pixel_8)](./overwritechannels%28withscalar%29-3zb93.md)
  Overwrites the pixels of the pixel buffer with the provided 8-bit scalar value.
- [func overwriteChannels(withScalar: Pixel_F)](./overwritechannels%28withscalar%29-1wm1o.md)
  Overwrites the pixels of the pixel buffer with the provided 32-bit scalar value.
- [func overwriteChannels([UInt8], withScalar: Pixel_8, destination: vImage.PixelBuffer<Format>)](./overwritechannels%28_,withscalar,destination%29-57ov2.md)
  Overwrites the pixels of one or more channels of the pixel buffer with the provided 8-bit scalar value.
- [func overwriteChannels([UInt8], withScalar: Pixel_F, destination: vImage.PixelBuffer<Format>)](./overwritechannels%28_,withscalar,destination%29-ev8q.md)
  Overwrites the pixels of one or more channels of the pixel buffer with the provided 32-bit scalar value.
- [func overwriteChannels([UInt8], withPixel: Pixel_8888, destination: vImage.PixelBuffer<Format>)](./overwritechannels%28_,withpixel,destination%29-6fab6.md)
  Overwrites the pixels of one or more channels of the pixel buffer with the provided 8-bit, 4-channel pixel value.
- [func overwriteChannels([UInt8], withPixel: Pixel_ARGB_16U, destination: vImage.PixelBuffer<Format>)](./overwritechannels%28_,withpixel,destination%29-6zw3o.md)
  Overwrites the pixels of one or more channels of the pixel buffer with the provided unsigned 16-bit, 4-channel pixel value.
- [func overwriteChannels([UInt8], withPixel: Pixel_FFFF, destination: vImage.PixelBuffer<Format>)](./overwritechannels%28_,withpixel,destination%29-6pbz8.md)
  Overwrites the pixels of one or more channels of the pixel buffer with the provided 32-bit, 4-channel pixel value.
- [func overwriteChannels([UInt8], withPlanarBuffer: vImage.PixelBuffer<vImage.Planar8>, destination: vImage.PixelBuffer<Format>)](./overwritechannels%28_,withplanarbuffer,destination%29-9jbky.md)
  Overwrites the pixels of one or more channels of the pixel buffer with the provided 8-bit planar pixel buffer.
- [func overwriteChannels([UInt8], withPlanarBuffer: vImage.PixelBuffer<vImage.PlanarF>, destination: vImage.PixelBuffer<Format>)](./overwritechannels%28_,withplanarbuffer,destination%29-hiw0.md)
  Overwrites the pixels of one or more channels of the pixel buffer with the provided 32-bit planar pixel buffer.
- [func overwriteChannels([UInt8], withInterleavedBuffer: vImage.PixelBuffer<Format>, destination: vImage.PixelBuffer<Format>)](./overwritechannels%28_,withinterleavedbuffer,destination%29-74hah.md)
  Overwrites the pixels of one or more channels of the pixel buffer with the provided 8-bit interleaved pixel buffer.
- [func overwriteChannels([UInt8], withInterleavedBuffer: vImage.PixelBuffer<Format>, destination: vImage.PixelBuffer<Format>)](./overwritechannels%28_,withinterleavedbuffer,destination%29-8xkd1.md)
  Overwrites the pixels of one or more channels of the pixel buffer with the provided 32-bit interleaved pixel buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimage/pixelbuffer/overwritechannels(withscalar:)-1hrrg)*