# Pixel formats

**Framework**: Accelerate

Specify a pixel buffer’s bit depth, number of channels, and data storage format.

## Topics

### Planar pixel formats
- [vImage.Planar8](vimage/planar8.md)
  A single-channel, 8-bit-per-channel, unsigned-integer buffer.
- [vImage.Planar16U](vimage/planar16u.md)
  A single-channel, 16-bit-per-channel, unsigned-integer buffer.
- [vImage.Planar16F](vimage/planar16f.md)
  A single-channel, 16-bit-per-channel, floating-point buffer.
- [vImage.PlanarF](vimage/planarf.md)
  A single-channel, 32-bit-per-channel, floating-point buffer.
### Multiple-plane pixel formats
- [vImage.Planar8x2](vimage/planar8x2.md)
  A pixel buffer that contains two homogeneous 8-bit planes, for example, CbCr.
- [vImage.Planar8x3](vimage/planar8x3.md)
  A pixel buffer that contains three homogeneous 8-bit planes, for example, RGB.
- [vImage.Planar8x4](vimage/planar8x4.md)
  A pixel buffer that contains four homogeneous 8-bit planes, for example, RGBA or CMYK.
- [vImage.PlanarFx2](vimage/planarfx2.md)
  A pixel buffer that contains two homogeneous 32-bit, floating-point planes, for example, CbCr.
- [vImage.PlanarFx3](vimage/planarfx3.md)
  A pixel buffer that contains three homogeneous 32-bit, floating-point planes, for example, RGB.
- [vImage.PlanarFx4](vimage/planarfx4.md)
  A pixel buffer that contains four homogeneous 32-bit, floating-point planes, for example, RGBA or CMYK.
### Interleaved pixel formats
- [vImage.Interleaved8x2](vimage/interleaved8x2.md)
  A two-channel, 8-bit-per-channel interleaved buffer.
- [vImage.Interleaved8x3](vimage/interleaved8x3.md)
  A three-channel, 8-bit-per-channel interleaved buffer.
- [vImage.Interleaved8x4](vimage/interleaved8x4.md)
  A four-channel, 8-bit-per-channel interleaved buffer.
- [vImage.Interleaved16Ux2](vimage/interleaved16ux2.md)
  A two-channel, 16-bit-per-channel, unsigned-integer interleaved buffer.
- [vImage.Interleaved16Ux4](vimage/interleaved16ux4.md)
  A four-channel, 16-bit-per-channel, unsigned-integer interleaved buffer.
- [vImage.Interleaved16Fx2](vimage/interleaved16fx2.md)
  A two-channel, 16-bit-per-channel, floating-point interleaved buffer.
- [vImage.Interleaved16Fx4](vimage/interleaved16fx4.md)
  A four-channel, 16-bit-per-channel, floating-point interleaved buffer.
- [vImage.InterleavedFx2](vimage/interleavedfx2.md)
  A two-channel, 32-bit-per-channel, floating-point interleaved buffer.
- [vImage.InterleavedFx3](vimage/interleavedfx3.md)
  A three-channel, 32-bit-per-channel, floating-point interleaved buffer.
- [vImage.InterleavedFx4](vimage/interleavedfx4.md)
  A four-channel, 32-bit-per-channel, floating-point interleaved buffer.
### Dynamic pixel formats
- [vImage.DynamicPixelFormat](vimage/dynamicpixelformat.md)
  A buffer that contains pixels with a data type that’s unknown at compile time.
### Protocols
- [protocol PixelFormat](pixelformat.md)
  A pixel buffer pixel format.
- [protocol StaticPixelFormat](staticpixelformat.md)
  A pixel format that’s known at compile time.
- [protocol InitializableFromCGImage](initializablefromcgimage.md)
  A pixel format that supports initialization from a Core Graphics image.
- [protocol SinglePlanePixelFormat](singleplanepixelformat.md)
  A pixel format that contains a single underlying vImage buffer.
- [protocol MultiplePlanePixelFormat](multipleplanepixelformat.md)
  A pixel format that contains multiple homogeneous planes represented by multiple underlying vImage buffers.

## See Also

- [Creating vImage pixel buffers](creating-vimage-pixel-buffers.md)
  Allocate and initialize pixel buffers from raw pixel data, Core Graphics images, and Core Video buffers.
- [Working with underlying data](working-with-underlying-data.md)
  Access a pixel buffer’s underlying pixel data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/pixel-formats)*