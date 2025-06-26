# vImage.PixelBuffer

**Framework**: Accelerate  
**Kind**: struct

An image buffer that stores an image’s pixel data, dimensions, bit depth, and number of channels.

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
struct PixelBuffer<Format> where Format : PixelFormat
```

## Mentions

- [Enhancing image contrast with histogram manipulation](enhancing-image-contrast-with-histogram-manipulation.md)
- [Applying vImage operations to regions of interest](applying-vimage-operations-to-regions-of-interest.md)
- [Building a basic image conversion workflow](building-a-basic-image-conversion-workflow.md)
- [Converting chroma-subsampled images](converting-chroma-subsampled-images.md)
- [Optimizing image-processing performance](optimizing-image-processing-performance.md)
- [Converting bitmap data between Core Graphics images and vImage buffers](converting-bitmap-data-between-core-graphics-images-and-vimage-buffers.md)
- [Applying color transforms to images with a multidimensional lookup table](applying-color-transforms-to-images-with-a-multidimensional-lookup-table.md)

#### Overview

Use a [`vImage.PixelBuffer`](vimage/pixelbuffer.md) to represent an image from a [`CGImage`](https://developer.apple.com/documentation/CoreGraphics/CGImage) instance, a [`CVPixelBuffer`](https://developer.apple.com/documentation/CoreVideo/CVPixelBuffer) structure, or a collection of raw pixel values. Pixel buffers are typed by their bits per channel and number of channels. For example, [`vImage.Interleaved8x4`](vimage/interleaved8x4.md) indicates a 4-channel, 8-bit-per-channel pixel buffer that contains image data such as RGBA or CMYK.

Pixel buffers expose methods that are available for the buffer’s pixel format. For example, the fast box convolution functions are only available for one- and four-channel 8-bit per channel buffers:

```swift
 let src = vImage.PixelBuffer<vImage.Interleaved8x4>(cgImage: cgImage,
                                                     cgImageFormat: &cgImageFormat)
 let dest = vImage.PixelBuffer<vImage.Interleaved8x4>(src.size)

 src.boxConvolve(kernelSize: vImage.Size(width: 64, height: 64),
                 edgeMode: .truncateKernel,
                 destination: dest)
```

Typed pixel buffers provide a simple API to convert between pixel formats. For example, the following code converts 8-bit unsigned integer pixels to 32-bit floating point pixels:

```swift
 let src = vImage.PixelBuffer<vImage.Interleaved8x4>(cgImage: cgImage,
                                                     cgImageFormat: &cgImageFormat)
 let dest = vImage.PixelBuffer<vImage.InterleavedFx4>(size: src.size)

 src.convert(to: dest)
```

vImage pixel buffers manage their memory, therefore, you don’t need to call [`deallocate()`](https://developer.apple.com/documentation/Swift/UnsafeMutableRawPointer/deallocate()) when you’re finished with the buffer.

## Topics

### Pixel buffer essentials
- [Creating vImage pixel buffers](creating-vimage-pixel-buffers.md)
  Allocate and initialize pixel buffers from raw pixel data, Core Graphics images, and Core Video buffers.
- [Pixel formats](pixel-formats.md)
  Specify a pixel buffer’s bit depth, number of channels, and data storage format.
- [Working with underlying data](working-with-underlying-data.md)
  Access a pixel buffer’s underlying pixel data.
### Inspecting a pixel buffer
- [var width: Int](vimage/pixelbuffer/width.md)
  The width of the pixel buffer.
- [var height: Int](vimage/pixelbuffer/height.md)
  The height of the pixel buffer.
- [var size: vImage.Size](vimage/pixelbuffer/size.md)
  The size of the pixel buffer.
- [var channelCount: Int](vimage/pixelbuffer/channelcount.md)
  Returns the number of channels.
- [var rowStride: Int](vimage/pixelbuffer/rowstride.md)
  The width, in pixels, of the underlying memory, including any additional row byte padding.
- [var byteCountPerPixel: Int](vimage/pixelbuffer/bytecountperpixel.md)
  Returns the number of bytes per pixel.
- [var count: Int](vimage/pixelbuffer/count.md)
  The total number of pixels multiplied by the number of channels in the buffer, including any row padding.
- [var array: [Format.ComponentType]](vimage/pixelbuffer/array.md)
  An array of `width * height * channelCount` values that’s a copy of the buffer’s visible contents.
### Pixel buffer methods
- [func copy(to: vImage.PixelBuffer<Format>)](vimage/pixelbuffer/copy(to:).md)
  Copies the contents of the pixel buffer to another pixel buffer.
- [func copy(to: CVPixelBuffer, cvImageFormat: vImageCVImageFormat, cgImageFormat: vImage_CGImageFormat) throws](vimage/pixelbuffer/copy(to:cvimageformat:cgimageformat:).md)
  Copies the contents of a pixel buffer to a Core Video pixel buffer.
- [func makeCGImage(cgImageFormat: vImage_CGImageFormat) -> CGImage?](vimage/pixelbuffer/makecgimage(cgimageformat:).md)
  Returns a Core Graphics image from the pixel buffer’s contents.
- [func withCVPixelBuffer(readOnly: Bool, body: (CVPixelBuffer) -> Void)](vimage/pixelbuffer/withcvpixelbuffer(readonly:body:).md)
  Calls the given closure with a locked 32-bit BGRA Core Video Pixel Buffer.
### Pixel buffer operations
- [Applying geometric operations to pixel buffers](applying-geometric-operations-to-pixel-buffers.md)
  Reflect, shear, rotate, scale, and apply affine transforms to image data.
- [Applying color transforms to pixel buffers](applying-color-transforms-to-pixel-buffers.md)
  Adjust the colors of an image by applying gamma, polynomials, or multidimensional lookup.
- [Blending and compositing pixel buffers](blending-and-compositing-pixel-buffers.md)
  Composite two pixel buffers to create a single image.
- [Convolving and applying morphology](convolving-and-applying-morphology.md)
  Apply convolution, dilation, or erosion to a pixel buffer.
- [Thresholding and clipping pixel buffer values](thresholding-and-clipping-pixel-buffer-values.md)
  Limit the values in a pixel buffer to a threshold or a range.
- [Calculating and transforming histograms](calculating-and-transforming-histograms.md)
  Enhance and adjust the contrast of an image with histogram equalization, contrast stretching, and specification.
- [Converting pixel buffers](converting-pixel-buffers.md)
  Convert pixel buffer data between different bit-depths.
- [Interleaving and deinterleaving pixel buffers](interleaving-and-deinterleaving-pixel-buffers.md)
  Convert pixel buffer data between interleaved and planar formats.
- [Cropping and working with regions of interest](cropping-and-working-with-regions-of-interest.md)
  Crop images and apply operations to regions of interest.
- [Applying channel operations](applying-channel-operations.md)
  Extract, flatten, permute, and overwrite the individual color channels of a pixel buffer.
- [Applying arithmetic operations](applying-arithmetic-operations.md)
  Multiply the pixel values of a buffer by scalar values or matrices.
### Instance Properties
- [var bytesPerRow: Int](vimage/pixelbuffer/bytesperrow.md)
  The width, in bytes, of the underlying memory including any additional row byte padding.
### Instance Methods
- [func applyLookup([Pixel_16U], destination: vImage.PixelBuffer<vImage.Planar16U>)](vimage/pixelbuffer/applylookup(_:destination:)-3yi7i.md)
- [func applyLookup([Pixel_8], destination: vImage.PixelBuffer<vImage.Planar8>)](vimage/pixelbuffer/applylookup(_:destination:)-6498m.md)
- [func applyLookup([Pixel_F], destination: vImage.PixelBuffer<vImage.PlanarF>)](vimage/pixelbuffer/applylookup(_:destination:)-715aw.md)
- [func applyMorphology(operation: vImage.MorphologyOperation<Format.ComponentType>, destination: vImage.PixelBuffer<Format>)](vimage/pixelbuffer/applymorphology(operation:destination:)-1aqer.md)
  Applies a morphology operation to the buffer.
- [func applyMorphology(operation: vImage.MorphologyOperation<Format.ComponentType>, destination: vImage.PixelBuffer<Format>)](vimage/pixelbuffer/applymorphology(operation:destination:)-5al25.md)
  Applies a morphology operation to the buffer.
- [func convolve(with: vImage.ConvolutionKernel2D<Float>, bias: Float?, edgeMode: vImage.EdgeMode<Pixel_8888>, destination: vImage.PixelBuffer<Format>)](vimage/pixelbuffer/convolve(with:bias:edgemode:destination:)-7no5n.md)
- [func separableConvolve(horizontalKernel: [Float], verticalKernel: [Float], bias: Float, edgeMode: vImage.EdgeMode<Pixel_8888>, destination: vImage.PixelBuffer<Format>)](vimage/pixelbuffer/separableconvolve(horizontalkernel:verticalkernel:bias:edgemode:destination:)-15dhm.md)
- [func withBNNSTensor<R>((BNNSTensor) throws -> R) rethrows -> R](vimage/pixelbuffer/withbnnstensor(_:).md)
  Calls the given closure with a pointer to a BNNS tensor that shares memory with the pixel buffer.
### Default Implementations
- [AccelerateBuffer Implementations](vimage/pixelbuffer/acceleratebuffer-implementations.md)
- [AccelerateMatrixBuffer Implementations](vimage/pixelbuffer/acceleratematrixbuffer-implementations.md)
- [AccelerateMutableMatrixBuffer Implementations](vimage/pixelbuffer/acceleratemutablematrixbuffer-implementations.md)

## Relationships

### Conforms To
- [AccelerateBuffer](acceleratebuffer.md)
- [AccelerateMatrixBuffer](acceleratematrixbuffer.md)
- [AccelerateMutableBuffer](acceleratemutablebuffer.md)
- [AccelerateMutableMatrixBuffer](acceleratemutablematrixbuffer.md)
- [Copyable](../Swift/Copyable.md)

## See Also

- [Using vImage pixel buffers to generate video effects](using-vimage-pixel-buffers-to-generate-video-effects.md)
  Render real-time video effects with the vImage Pixel Buffer.
- [Applying tone curve adjustments to images](applying-tone-curve-adjustments-to-images.md)
  Use the vImage library’s polynomial transform to apply tone curve adjustments to images.
- [Adjusting the brightness and contrast of an image](adjusting-the-brightness-and-contrast-of-an-image.md)
  Use a gamma function to apply a linear or exponential curve.
- [Adjusting the hue of an image](adjusting-the-hue-of-an-image.md)
  Convert an image to L*a*b* color space and apply hue adjustment.
- [Sharing texture data between the Model I/O framework and the vImage library](sharing-texture-data-between-the-model-io-framework-and-the-vimage-library.md)
  Use Model I/O and vImage to composite a photograph over a computer-generated sky.
- [Calculating the dominant colors in an image](calculating-the-dominant-colors-in-an-image.md)
  Find the main colors in an image by implementing k-means clustering using the Accelerate framework.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimage/pixelbuffer)*