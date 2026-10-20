# Applying channel operations

**Framework**: Accelerate  
**Role**: API Collection

Extract, flatten, permute, and overwrite the individual color channels of a pixel buffer.

## Topics

### Extracting Channels
- [func extractChannel(at: Int, destination: vImage.PixelBuffer<vImage.Planar8>)](./vimage/pixelbuffer/extractchannel%28at,destination%29-ageg.md)
  Extracts a single channel from an 8-bit-per-channel, 4-channel interleaved pixel buffer.
- [func extractChannel(at: Int, destination: vImage.PixelBuffer<vImage.Planar16U>)](./vimage/pixelbuffer/extractchannel%28at,destination%29-i1zm.md)
  Extracts a single channel from an unsigned 16-bit-per-channel, 4-channel interleaved pixel buffer.
- [func extractChannel(at: Int, destination: vImage.PixelBuffer<vImage.PlanarF>)](./vimage/pixelbuffer/extractchannel%28at,destination%29-8xrq1.md)
  Extracts a single channel from an 32-bit-per-channel, 4-channel interleaved pixel buffer.
### Flattening Channels
- [func flatten(channelOrdering: vImage.ChannelOrdering, backgroundColor: Pixel_8888, isPremultiplied: Bool, destination: vImage.PixelBuffer<vImage.Interleaved8x3>)](./vimage/pixelbuffer/flatten%28channelordering,backgroundcolor,ispremultiplied,destination%29-97nx.md)
  Transforms an 8-bit-per-channel RGBA or ARGB buffer to an RGB buffer against an opaque background color.
- [func flatten(channelOrdering: vImage.ChannelOrdering, backgroundColor: Pixel_FFFF, isPremultiplied: Bool, destination: vImage.PixelBuffer<vImage.InterleavedFx3>)](./vimage/pixelbuffer/flatten%28channelordering,backgroundcolor,ispremultiplied,destination%29-5g0c2.md)
  Transforms an 32-bit-per-channel RGBA or ARGB buffer to an RGB buffer against an opaque background color.
- [vImage.ChannelOrdering](./vimage/channelordering.md)
  Constants that specify the channel ordering of a pixel buffer.
### Permuting Channels
- [func permuteChannels(to: (UInt8, UInt8, UInt8), destination: vImage.PixelBuffer<Format>)](./vimage/pixelbuffer/permutechannels%28to,destination%29-4y4rh.md)
  Permutes the channels of an 8-bit-per-channel, 3-channel interleaved pixel buffer.
- [func permuteChannels(to: (UInt8, UInt8, UInt8, UInt8), destination: vImage.PixelBuffer<Format>)](./vimage/pixelbuffer/permutechannels%28to,destination%29-tr2h.md)
  Permutes the channels of an 8-bit-per-channel, 4-channel interleaved pixel buffer.
- [func permuteChannels(to: (UInt8, UInt8, UInt8, UInt8), destination: vImage.PixelBuffer<Format>)](./vimage/pixelbuffer/permutechannels%28to,destination%29-8y213.md)
  Permutes the channels of an unsigned 16-bit-per-channel, 4-channel interleaved pixel buffer.
- [func permuteChannels(to: (UInt8, UInt8, UInt8, UInt8), destination: vImage.PixelBuffer<Format>)](./vimage/pixelbuffer/permutechannels%28to,destination%29-74dmh.md)
  Permutes the channels of a floating-point 16-bit-per-channel, 4-channel interleaved pixel buffer.
- [func permuteChannels(to: (UInt8, UInt8, UInt8, UInt8), destination: vImage.PixelBuffer<Format>)](./vimage/pixelbuffer/permutechannels%28to,destination%29-6n6yi.md)
  Permutes the channels of an 32-bit-per-channel, 4-channel interleaved pixel buffer.
### Overwriting Channels
- [func overwriteChannels(withScalar: Pixel_8)](./vimage/pixelbuffer/overwritechannels%28withscalar%29-3zb93.md)
  Overwrites the pixels of the pixel buffer with the provided 8-bit scalar value.
- [func overwriteChannels(withScalar: Pixel_16F)](./vimage/pixelbuffer/overwritechannels%28withscalar%29-1hrrg.md)
  Overwrites the pixels of the pixel buffer with the provided floating-point 16-bit scalar value.
- [func overwriteChannels(withScalar: Pixel_F)](./vimage/pixelbuffer/overwritechannels%28withscalar%29-1wm1o.md)
  Overwrites the pixels of the pixel buffer with the provided 32-bit scalar value.
- [func overwriteChannels([UInt8], withScalar: Pixel_8, destination: vImage.PixelBuffer<Format>)](./vimage/pixelbuffer/overwritechannels%28_,withscalar,destination%29-57ov2.md)
  Overwrites the pixels of one or more channels of the pixel buffer with the provided 8-bit scalar value.
- [func overwriteChannels([UInt8], withScalar: Pixel_F, destination: vImage.PixelBuffer<Format>)](./vimage/pixelbuffer/overwritechannels%28_,withscalar,destination%29-ev8q.md)
  Overwrites the pixels of one or more channels of the pixel buffer with the provided 32-bit scalar value.
- [func overwriteChannels([UInt8], withPixel: Pixel_8888, destination: vImage.PixelBuffer<Format>)](./vimage/pixelbuffer/overwritechannels%28_,withpixel,destination%29-6fab6.md)
  Overwrites the pixels of one or more channels of the pixel buffer with the provided 8-bit, 4-channel pixel value.
- [func overwriteChannels([UInt8], withPixel: Pixel_ARGB_16U, destination: vImage.PixelBuffer<Format>)](./vimage/pixelbuffer/overwritechannels%28_,withpixel,destination%29-6zw3o.md)
  Overwrites the pixels of one or more channels of the pixel buffer with the provided unsigned 16-bit, 4-channel pixel value.
- [func overwriteChannels([UInt8], withPixel: Pixel_FFFF, destination: vImage.PixelBuffer<Format>)](./vimage/pixelbuffer/overwritechannels%28_,withpixel,destination%29-6pbz8.md)
  Overwrites the pixels of one or more channels of the pixel buffer with the provided 32-bit, 4-channel pixel value.
- [func overwriteChannels([UInt8], withPlanarBuffer: vImage.PixelBuffer<vImage.Planar8>, destination: vImage.PixelBuffer<Format>)](./vimage/pixelbuffer/overwritechannels%28_,withplanarbuffer,destination%29-9jbky.md)
  Overwrites the pixels of one or more channels of the pixel buffer with the provided 8-bit planar pixel buffer.
- [func overwriteChannels([UInt8], withPlanarBuffer: vImage.PixelBuffer<vImage.PlanarF>, destination: vImage.PixelBuffer<Format>)](./vimage/pixelbuffer/overwritechannels%28_,withplanarbuffer,destination%29-hiw0.md)
  Overwrites the pixels of one or more channels of the pixel buffer with the provided 32-bit planar pixel buffer.
- [func overwriteChannels([UInt8], withInterleavedBuffer: vImage.PixelBuffer<Format>, destination: vImage.PixelBuffer<Format>)](./vimage/pixelbuffer/overwritechannels%28_,withinterleavedbuffer,destination%29-74hah.md)
  Overwrites the pixels of one or more channels of the pixel buffer with the provided 8-bit interleaved pixel buffer.
- [func overwriteChannels([UInt8], withInterleavedBuffer: vImage.PixelBuffer<Format>, destination: vImage.PixelBuffer<Format>)](./vimage/pixelbuffer/overwritechannels%28_,withinterleavedbuffer,destination%29-8xkd1.md)
  Overwrites the pixels of one or more channels of the pixel buffer with the provided 32-bit interleaved pixel buffer.

## See Also

### Pixel buffer operations
- [Applying geometric operations to pixel buffers](./applying-geometric-operations-to-pixel-buffers.md)
  Reflect, shear, rotate, scale, and apply affine transforms to image data.
- [Applying color transforms to pixel buffers](./applying-color-transforms-to-pixel-buffers.md)
  Adjust the colors of an image by applying gamma, polynomials, or multidimensional lookup.
- [Blending and compositing pixel buffers](./blending-and-compositing-pixel-buffers.md)
  Composite two pixel buffers to create a single image.
- [Convolving and applying morphology](./convolving-and-applying-morphology.md)
  Apply convolution, dilation, or erosion to a pixel buffer.
- [Thresholding and clipping pixel buffer values](./thresholding-and-clipping-pixel-buffer-values.md)
  Limit the values in a pixel buffer to a threshold or a range.
- [Calculating and transforming histograms](./calculating-and-transforming-histograms.md)
  Enhance and adjust the contrast of an image with histogram equalization, contrast stretching, and specification.
- [Converting pixel buffers](./converting-pixel-buffers.md)
  Convert pixel buffer data between different bit-depths.
- [Interleaving and deinterleaving pixel buffers](./interleaving-and-deinterleaving-pixel-buffers.md)
  Convert pixel buffer data between interleaved and planar formats.
- [Cropping and working with regions of interest](./cropping-and-working-with-regions-of-interest.md)
  Crop images and apply operations to regions of interest.
- [Applying arithmetic operations](./applying-arithmetic-operations.md)
  Multiply the pixel values of a buffer by scalar values or matrices.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/applying-channel-operations)*