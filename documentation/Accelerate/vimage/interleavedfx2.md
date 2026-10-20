# vImage.InterleavedFx2

**Framework**: Accelerate  
**Kind**: struct  
**Role**: Structure

A two-channel, 32-bit-per-channel, floating-point interleaved buffer.

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
struct InterleavedFx2
```

## Topics

### Type Methods
- [static func makePixel(Pixel_16F16F) -> Pixel_FF](./interleavedfx2/makepixel%28_%29.md)
  Returns a 32-bit floating-point pixel value from a 16-bit floating-point pixel value.

## Relationships

### Conforms To
- [PixelFormat](../pixelformat.md)
- [SinglePlanePixelFormat](../singleplanepixelformat.md)
- [StaticPixelFormat](../staticpixelformat.md)

## See Also

### Type Aliases
- [typealias StructuringElement](./structuringelement.md)
  A 2D matrix that represents a morphology kernel.
- [vImage.ConvolutionKernel](./convolutionkernel.md)
  Constants that describe 1D convolution kernels.
- [vImage.ConvolutionKernel2D](./convolutionkernel2d.md)
  A 2D matrix that represents a convolution kernel.
- [vImage.DynamicPixelFormat](./dynamicpixelformat.md)
  A buffer that contains pixels with a data type that’s unknown at compile time.
- [vImage.Interleaved16Fx2](./interleaved16fx2.md)
  A two-channel, 16-bit-per-channel, floating-point interleaved buffer.
- [vImage.Interleaved16Fx4](./interleaved16fx4.md)
  A four-channel, 16-bit-per-channel, floating-point interleaved buffer.
- [vImage.Interleaved16Ux2](./interleaved16ux2.md)
  A two-channel, 16-bit-per-channel, unsigned-integer interleaved buffer.
- [vImage.Interleaved16Ux4](./interleaved16ux4.md)
  A four-channel, 16-bit-per-channel, unsigned-integer interleaved buffer.
- [vImage.Interleaved8x2](./interleaved8x2.md)
  A two-channel, 8-bit-per-channel interleaved buffer.
- [vImage.Interleaved8x3](./interleaved8x3.md)
  A three-channel, 8-bit-per-channel interleaved buffer.
- [vImage.Interleaved8x4](./interleaved8x4.md)
  A four-channel, 8-bit-per-channel interleaved buffer.
- [vImage.InterleavedFx3](./interleavedfx3.md)
  A three-channel, 32-bit-per-channel, floating-point interleaved buffer.
- [vImage.InterleavedFx4](./interleavedfx4.md)
  A four-channel, 32-bit-per-channel, floating-point interleaved buffer.
- [vImage.MultidimensionalLookupTable](./multidimensionallookuptable.md)
  A multidimensional lookup table.
- [vImage.Options](./options.md)
  Set flags on vImage operations to specify processing options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimage/interleavedfx2)*