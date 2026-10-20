# Working with underlying data

**Framework**: Accelerate  
**Role**: API Collection

Access a pixel buffer’s underlying pixel data.

## Topics

### Converting to an array
- [func makeArray<U>(of: U.Type, channelCount: Int) -> [U]](./vimage/pixelbuffer/makearray%28of,channelcount%29.md)
  Returns an array of `width * height * channelCount` values that’s a copy of the buffer’s visible contents.
### Accessing underlying pixel values
- [func withUnsafeBufferPointer<R>((UnsafeBufferPointer<Format.ComponentType>) throws -> R) rethrows -> R](./vimage/pixelbuffer/withunsafebufferpointer%28_%29.md)
  Calls the given closure with a pointer to the buffer’s contiguous storage.
- [func withUnsafeMutableBufferPointer<R>((inout UnsafeMutableBufferPointer<Format.ComponentType>) throws -> R) rethrows -> R](./vimage/pixelbuffer/withunsafemutablebufferpointer%28_%29.md)
  Calls the given closure with a pointer to the buffer’s mutable contiguous storage.
### Accessing underlying vImage buffers
- [func withUnsafePointerToVImageBuffer<R>((UnsafePointer<vImage_Buffer>) throws -> R) rethrows -> R](./vimage/pixelbuffer/withunsafepointertovimagebuffer%28_%29.md)
  Calls the given closure with an unsafe pointer to the underlying vImage buffer.
- [func withUnsafeVImageBuffer<R>((vImage_Buffer) throws -> R) rethrows -> R](./vimage/pixelbuffer/withunsafevimagebuffer%28_%29.md)
  Calls the given closure with the underlying vImage buffer.
- [func withUnsafeVImageBuffers<R>(([vImage_Buffer]) throws -> R) rethrows -> R](./vimage/pixelbuffer/withunsafevimagebuffers%28_%29.md)
  Calls the given closure with the underlying vImage buffers.
### Accessing component pixel buffers
- [func withUnsafePixelBuffer<R>(at: Int, (vImage.PixelBuffer<Format.PlanarPixelFormat>) throws -> R) rethrows -> R](./vimage/pixelbuffer/withunsafepixelbuffer%28at,_%29.md)
  Calls the given closure with the pixel buffer that references the individual plane at the given index.
- [func withUnsafePixelBuffers<R>(([vImage.PixelBuffer<Format.PlanarPixelFormat>]) throws -> R) rethrows -> R](./vimage/pixelbuffer/withunsafepixelbuffers%28_%29.md)
  Calls the given closure with the array of pixel buffers that reference the individual planes.

## See Also

### Pixel buffer essentials
- [Creating vImage pixel buffers](./creating-vimage-pixel-buffers.md)
  Allocate and initialize pixel buffers from raw pixel data, Core Graphics images, and Core Video buffers.
- [Pixel formats](./pixel-formats.md)
  Specify a pixel buffer’s bit depth, number of channels, and data storage format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/working-with-underlying-data)*