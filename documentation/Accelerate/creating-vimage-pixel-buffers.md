# Creating vImage pixel buffers

**Framework**: Accelerate

Allocate and initialize pixel buffers from raw pixel data, Core Graphics images, and Core Video buffers.

## Topics

### Creating a pixel buffer
- [init(size: vImage.Size, pixelFormat: Format.Type)](vimage/pixelbuffer/init(size:pixelformat:)-12gl9.md)
  Returns a new multiplane pixel buffer with a size that you specify.
- [init(size: vImage.Size, pixelFormat: Format.Type)](vimage/pixelbuffer/init(size:pixelformat:)-96ocu.md)
  Returns a new pixel buffer with a size that you specify.
- [init(width: Int, height: Int, pixelFormat: Format.Type)](vimage/pixelbuffer/init(width:height:pixelformat:).md)
  Returns a new pixel buffer with a width and height that you specify.
- [vImage.Size](vimage/size.md)
  A structure that contains width and height values.
### Creating a pixel buffer from raw pixel data
- [init<U>(pixelValues: U, size: vImage.Size, pixelFormat: Format.Type)](vimage/pixelbuffer/init(pixelvalues:size:pixelformat:).md)
  Creates a new pixel buffer by copying the supplied collection of pixel values.
- [init(data: UnsafeMutableRawPointer, width: Int, height: Int, byteCountPerRow: Int, pixelFormat: Format.Type)](vimage/pixelbuffer/init(data:width:height:bytecountperrow:pixelformat:)-zwzz.md)
  Returns a new buffer that references existing data.
- [init(data: UnsafeMutableRawPointer, width: Int, height: Int, byteCountPerRow: Int?, pixelFormat: Format.Type)](vimage/pixelbuffer/init(data:width:height:bytecountperrow:pixelformat:)-27czc.md)
  Calculates the correct bytes per row and returns a new buffer that references existing data.
### Creating a pixel buffer from a Core Graphics image
- [init(cgImage: CGImage, cgImageFormat: inout vImage_CGImageFormat, pixelFormat: Format.Type) throws](vimage/pixelbuffer/init(cgimage:cgimageformat:pixelformat:).md)
  Returns a new pixel buffer initialized from a Core Graphics image.
### Creating a pixel buffer from a Core Video buffer
- [init(copying: CVPixelBuffer, cvImageFormat: vImageCVImageFormat, cgImageFormat: inout vImage_CGImageFormat, pixelFormat: Format.Type) throws](vimage/pixelbuffer/init(copying:cvimageformat:cgimageformat:pixelformat:).md)
  Initializes a pixel buffer by copying the data from a Core Video pixel buffer.
- [init(referencing: CVPixelBuffer, converter: vImageConverter, destinationPixelFormat: Format.Type)](vimage/pixelbuffer/init(referencing:converter:destinationpixelformat:).md)
  Returns a new pixel buffer that references the specified Core Video pixel buffer and populated converter.
- [init(referencing: CVPixelBuffer, planeIndex: Int, overrideSize: vImage.Size?, pixelFormat: Format.Type)](vimage/pixelbuffer/init(referencing:planeindex:overridesize:pixelformat:).md)
  Initializes a pixel buffer by refencing the data from a single plane of a multiplane Core Video pixel buffer.
### Creating a multiple-plane buffer from an interleaved buffer
- [init(interleavedBuffer: vImage.PixelBuffer<vImage.Interleaved8x3>)](vimage/pixelbuffer/init(interleavedbuffer:)-9xct6.md)
  Creates a 3-channel, 8-bit-per-channel multiple-plane buffer from a 3-channel, 8-bit-per-channel interleaved buffer.
- [init(interleavedBuffer: vImage.PixelBuffer<vImage.Interleaved8x4>)](vimage/pixelbuffer/init(interleavedbuffer:)-8f6xn.md)
  Creates a 4-channel, 8-bit-per-channel mutiple-plane buffer from a 4-channel, 8-bit-per-channel interleaved buffer.
- [init(interleavedBuffer: vImage.PixelBuffer<vImage.InterleavedFx3>)](vimage/pixelbuffer/init(interleavedbuffer:)-77n3i.md)
  Creates a 3-channel, 32-bit-per-channel multiple-plane buffer from a 3-channel, 32-bit-per-channel interleaved buffer.
- [init(interleavedBuffer: vImage.PixelBuffer<vImage.InterleavedFx4>)](vimage/pixelbuffer/init(interleavedbuffer:)-2hc6f.md)
  Creates a 4-channel, 32-bit-per-channel multiple-plane buffer from a 4-channel, 32-bit-per-channel interleaved buffer.
### Creating an interleaved buffer from another buffer
- [init(planarBuffers: [vImage.PixelBuffer<vImage.Planar8>])](vimage/pixelbuffer/init(planarbuffers:)-727d.md)
  Creates a 2-channel, 8-bit-per-channel interleaved buffer from two 8-bit planar buffers.
- [init(planarBuffers: [vImage.PixelBuffer<vImage.Planar8>])](vimage/pixelbuffer/init(planarbuffers:)-6r9p0.md)
  Creates a 3-channel, 8-bit-per-channel interleaved buffer from three 8-bit planar buffers.
- [init(planarBuffers: [vImage.PixelBuffer<vImage.Planar8>])](vimage/pixelbuffer/init(planarbuffers:)-6hkso.md)
  Creates a 4-channel, 8-bit-per-channel interleaved buffer from four 8-bit planar buffers.
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
### Creating a multiple-plane buffer from planar buffers
- [init(planarBuffers: [vImage.PixelBuffer<Format.PlanarPixelFormat>], pixelFormat: Format.Type)](vimage/pixelbuffer/init(planarbuffers:pixelformat:).md)
  Returns an initialized buffer by copying the specified planar buffers.
### Creating a pixel buffer and image format
- [static func makeDynamicPixelBufferAndCGImageFormat(cgImage: CGImage) throws -> (pixelBuffer: vImage.PixelBuffer<vImage.DynamicPixelFormat>, cgImageFormat: vImage_CGImageFormat)](vimage/pixelbuffer/makedynamicpixelbufferandcgimageformat(cgimage:).md)
  Returns a new dynamic pixel format pixel buffer and Core Graphics image format structure from a Core Graphics image.
- [static func makePixelBufferAndCGImageFormat(cgImage: CGImage, pixelFormat: Format.Type) throws -> (pixelBuffer: vImage.PixelBuffer<Format>, cgImageFormat: vImage_CGImageFormat)](vimage/pixelbuffer/makepixelbufferandcgimageformat(cgimage:pixelformat:).md)
  Returns a new pixel buffer and Core Graphics image format structure from a Core Graphics image.

## See Also

- [Pixel formats](pixel-formats.md)
  Specify a pixel buffer’s bit depth, number of channels, and data storage format.
- [Working with underlying data](working-with-underlying-data.md)
  Access a pixel buffer’s underlying pixel data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/creating-vimage-pixel-buffers)*