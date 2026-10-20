# vImage.ConvolutionKernel2D

**Framework**: Accelerate  
**Kind**: struct  
**Role**: Structure

A 2D matrix that represents a convolution kernel.

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
struct ConvolutionKernel2D<ComponentType>
```

## Topics

### Initializers
- [init(values: [ComponentType], size: vImage.Size)](./convolutionkernel2d/init%28values,size%29.md)
  Returns a new convolution kernel structure with the size you specify.
- [init(values: [ComponentType], width: Int, height: Int)](./convolutionkernel2d/init%28values,width,height%29.md)
  Returns a new convolution kernel structure with the width and height you specify.
### Instance Properties
- [let width: vImagePixelCount](./convolutionkernel2d/width.md)
  The width of the kernel that must be a positive, odd number.
- [let height: vImagePixelCount](./convolutionkernel2d/height.md)
  The height of the kernel that must be a positive, odd number.
- [let values: [ComponentType]](./convolutionkernel2d/values.md)
  The kernel weights or structuring element values that must contain `height * width` elements.

## See Also

### Type Aliases
- [typealias StructuringElement](./structuringelement.md)
  A 2D matrix that represents a morphology kernel.
- [vImage.ConvolutionKernel](./convolutionkernel.md)
  Constants that describe 1D convolution kernels.
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
- [vImage.InterleavedFx2](./interleavedfx2.md)
  A two-channel, 32-bit-per-channel, floating-point interleaved buffer.
- [vImage.InterleavedFx3](./interleavedfx3.md)
  A three-channel, 32-bit-per-channel, floating-point interleaved buffer.
- [vImage.InterleavedFx4](./interleavedfx4.md)
  A four-channel, 32-bit-per-channel, floating-point interleaved buffer.
- [vImage.MultidimensionalLookupTable](./multidimensionallookuptable.md)
  A multidimensional lookup table.
- [vImage.Options](./options.md)
  Set flags on vImage operations to specify processing options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimage/convolutionkernel2d)*