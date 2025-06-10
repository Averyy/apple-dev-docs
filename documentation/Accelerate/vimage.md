# vImage

**Framework**: Accelerate  
**Kind**: enum

An enumeration that acts as a namespace for Swift overlays to vImage.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst ?+
- macOS 10.15+
- tvOS 13.0+
- visionOS ?+
- watchOS 6.0+

## Declaration

```swift
enum vImage
```

## Topics

### Type Aliases
- [typealias StructuringElement](vimage/structuringelement.md)
  A 2D matrix that represents a morphology kernel.
- [vImage.ConvolutionKernel](vimage/convolutionkernel.md)
  Constants that describe 1D convolution kernels.
- [vImage.ConvolutionKernel2D](vimage/convolutionkernel2d.md)
  A 2D matrix that represents a convolution kernel.
- [vImage.DynamicPixelFormat](vimage/dynamicpixelformat.md)
  A buffer that contains pixels with a data type that’s unknown at compile time.
- [vImage.Interleaved16Fx2](vimage/interleaved16fx2.md)
  A two-channel, 16-bit-per-channel, floating-point interleaved buffer.
- [vImage.Interleaved16Fx4](vimage/interleaved16fx4.md)
  A four-channel, 16-bit-per-channel, floating-point interleaved buffer.
- [vImage.Interleaved16Ux2](vimage/interleaved16ux2.md)
  A two-channel, 16-bit-per-channel, unsigned-integer interleaved buffer.
- [vImage.Interleaved16Ux4](vimage/interleaved16ux4.md)
  A four-channel, 16-bit-per-channel, unsigned-integer interleaved buffer.
- [vImage.Interleaved8x2](vimage/interleaved8x2.md)
  A two-channel, 8-bit-per-channel interleaved buffer.
- [vImage.Interleaved8x3](vimage/interleaved8x3.md)
  A three-channel, 8-bit-per-channel interleaved buffer.
- [vImage.Interleaved8x4](vimage/interleaved8x4.md)
  A four-channel, 8-bit-per-channel interleaved buffer.
- [vImage.InterleavedFx2](vimage/interleavedfx2.md)
  A two-channel, 32-bit-per-channel, floating-point interleaved buffer.
- [vImage.InterleavedFx3](vimage/interleavedfx3.md)
  A three-channel, 32-bit-per-channel, floating-point interleaved buffer.
- [vImage.InterleavedFx4](vimage/interleavedfx4.md)
  A four-channel, 32-bit-per-channel, floating-point interleaved buffer.
- [vImage.MultidimensionalLookupTable](vimage/multidimensionallookuptable.md)
  A multidimensional lookup table.
- [vImage.Options](vimage/options.md)
  Set flags on vImage operations to specify processing options.
- [vImage.PixelBuffer](vimage/pixelbuffer.md)
  An image buffer that stores an image’s pixel data, dimensions, bit depth, and number of channels.
- [vImage.Planar16F](vimage/planar16f.md)
  A single-channel, 16-bit-per-channel, floating-point buffer.
- [vImage.Planar16U](vimage/planar16u.md)
  A single-channel, 16-bit-per-channel, unsigned-integer buffer.
- [vImage.Planar8](vimage/planar8.md)
  A single-channel, 8-bit-per-channel, unsigned-integer buffer.
- [vImage.Planar8x2](vimage/planar8x2.md)
  A pixel buffer that contains two homogeneous 8-bit planes, for example, CbCr.
- [vImage.Planar8x3](vimage/planar8x3.md)
  A pixel buffer that contains three homogeneous 8-bit planes, for example, RGB.
- [vImage.Planar8x4](vimage/planar8x4.md)
  A pixel buffer that contains four homogeneous 8-bit planes, for example, RGBA or CMYK.
- [vImage.PlanarF](vimage/planarf.md)
  A single-channel, 32-bit-per-channel, floating-point buffer.
- [vImage.PlanarFx2](vimage/planarfx2.md)
  A pixel buffer that contains two homogeneous 32-bit, floating-point planes, for example, CbCr.
- [vImage.PlanarFx3](vimage/planarfx3.md)
  A pixel buffer that contains three homogeneous 32-bit, floating-point planes, for example, RGB.
- [vImage.PlanarFx4](vimage/planarfx4.md)
  A pixel buffer that contains four homogeneous 32-bit, floating-point planes, for example, RGBA or CMYK.
- [vImage.Size](vimage/size.md)
  A structure that contains width and height values.
### Enumerations
- [vImage.BlendMode](vimage/blendmode.md)
  Constants that specify an alpha blending mode.
- [vImage.BufferType](vimage/buffertype.md)
  Codes that represent vImage buffer types.
- [vImage.ChannelOrdering](vimage/channelordering.md)
  Constants that specify the channel ordering of a pixel buffer.
- [vImage.CompositeMode](vimage/compositemode.md)
  Constants that specify whether the format of layers is premultiplied or nonpremultiplied.
- [vImage.EdgeMode](vimage/edgemode.md)
  Constants that specify edge modes for convolution operations.
- [vImage.Error](vimage/error.md)
  An error that occurs during a vImage operation.
- [vImage.FloodFillConnectivity](vimage/floodfillconnectivity.md)
- [vImage.Gamma](vimage/gamma.md)
  Describes either a used-defined or constant gamma.
- [vImage.MorphologyOperation](vimage/morphologyoperation.md)
  Describes which morphology operation to perform.
- [vImage.ReflectionAxis](vimage/reflectionaxis.md)
  The axis to reflect an image.
- [vImage.Rotation](vimage/rotation.md)
  The angle to rotate an image.
- [vImage.ShearDirection](vimage/sheardirection.md)
  The shear direction.
### Protocols
- [protocol InitializableFromCGImage](initializablefromcgimage.md)
  A pixel format that supports initialization from a Core Graphics image.
- [protocol MultiplePlanePixelFormat](multipleplanepixelformat.md)
  A pixel format that contains multiple homogeneous planes represented by multiple underlying vImage buffers.
- [protocol PixelFormat](pixelformat.md)
  A pixel buffer pixel format.
- [protocol SinglePlanePixelFormat](singleplanepixelformat.md)
  A pixel format that contains a single underlying vImage buffer.
- [protocol StaticPixelFormat](staticpixelformat.md)
  A pixel format that’s known at compile time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimage)*