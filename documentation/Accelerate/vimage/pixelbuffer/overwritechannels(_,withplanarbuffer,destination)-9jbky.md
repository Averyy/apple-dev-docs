# overwriteChannels(_:withPlanarBuffer:destination:)

**Framework**: Accelerate  
**Kind**: method  
**Role**: Instance Method

Overwrites the pixels of one or more channels of the pixel buffer with the provided 8-bit planar pixel buffer.

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
func overwriteChannels(_ channels: [UInt8], withPlanarBuffer buffer: vImage.PixelBuffer<vImage.Planar8>, destination: vImage.PixelBuffer<Format>)
```

Available when `Format` is `vImage.Interleaved8x4`.

## Discussion

Use this function to overwrite one or more channels of an interleaved buffer with a planar buffer. The following code overwrites channels `1` and `3` with the values in `overwriteValues`:

```swift
let pixelValues: [Pixel_8] = [ 1, 2, 3, 4,
                               5, 6, 7, 8 ]
let buffer = vImage.PixelBuffer(pixelValues: pixelValues,
                                size: vImage.Size(width: 1,
                                                  height: 2),
                                pixelFormat: vImage.Interleaved8x4.self)

let destination = vImage.PixelBuffer(size: vImage.Size(width: 1,
                                                       height: 2),
                                     pixelFormat: vImage.Interleaved8x4.self)

let overwriteValues: [Pixel_8] = [ 101,
                                   102 ]

let overwriteBuffer = vImage.PixelBuffer<vImage.Planar8>(pixelValues: overwriteValues,
                                                         size: vImage.Size(width: 1,
                                                                           height: 2))

buffer.overwriteChannels([3, 1],
                         withPlanarBuffer: overwriteBuffer,
                         destination: destination)
```

On return, `destination.array` contains the following values:

```swift
[ 1, 101, 3, 101,
  5, 102, 7, 102 ]
```

## Parameters

- `channels`: An array that contains the indices of the channels that the function overwrites.
- `buffer`: The planar buffer that the function writes to the channels.
- `destination`: The destination pixel buffer.

## See Also

### Overwriting Channels
- [func overwriteChannels(withScalar: Pixel_8)](./overwritechannels%28withscalar%29-3zb93.md)
  Overwrites the pixels of the pixel buffer with the provided 8-bit scalar value.
- [func overwriteChannels(withScalar: Pixel_16F)](./overwritechannels%28withscalar%29-1hrrg.md)
  Overwrites the pixels of the pixel buffer with the provided floating-point 16-bit scalar value.
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
- [func overwriteChannels([UInt8], withPlanarBuffer: vImage.PixelBuffer<vImage.PlanarF>, destination: vImage.PixelBuffer<Format>)](./overwritechannels%28_,withplanarbuffer,destination%29-hiw0.md)
  Overwrites the pixels of one or more channels of the pixel buffer with the provided 32-bit planar pixel buffer.
- [func overwriteChannels([UInt8], withInterleavedBuffer: vImage.PixelBuffer<Format>, destination: vImage.PixelBuffer<Format>)](./overwritechannels%28_,withinterleavedbuffer,destination%29-74hah.md)
  Overwrites the pixels of one or more channels of the pixel buffer with the provided 8-bit interleaved pixel buffer.
- [func overwriteChannels([UInt8], withInterleavedBuffer: vImage.PixelBuffer<Format>, destination: vImage.PixelBuffer<Format>)](./overwritechannels%28_,withinterleavedbuffer,destination%29-8xkd1.md)
  Overwrites the pixels of one or more channels of the pixel buffer with the provided 32-bit interleaved pixel buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimage/pixelbuffer/overwritechannels(_:withplanarbuffer:destination:)-9jbky)*