# vImage.Size

**Framework**: Accelerate  
**Kind**: struct  
**Role**: Structure

A structure that contains width and height values.

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
struct Size
```

## Topics

### Initializers
- [init(cvPixelBuffer: CVPixelBuffer)](./size/init%28cvpixelbuffer%29.md)
  Creates a size with dimensions specified by a Core Video pixel buffer.
- [init?<T>(exactWidth: T, height: T)](./size/init%28exactwidth,height%29-9nwk0.md)
  Creates a size with dimensions specified as floating-point values.
- [init?<T>(exactWidth: T, height: T)](./size/init%28exactwidth,height%29-4ygbk.md)
  Creates a size with dimensions specified as integer values.
- [init?(exactly: CGSize)](./size/init%28exactly%29.md)
  Creates a size with dimensions specified as a Core Graphics size value.
- [init(width: Int, height: Int)](./size/init%28width,height%29-fzcb.md)
  Creates a size with dimensions specified as integer values.
- [init(width: vImagePixelCount, height: vImagePixelCount)](./size/init%28width,height%29-8ly3k.md)
  Creates a size with dimensions specified as unsigned integer values.
### Instance Properties
- [let height: Int](./size/height.md)
  The height of the size structure.
- [let width: Int](./size/width.md)
  The width of the size structure.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)

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
- [vImage.InterleavedFx2](./interleavedfx2.md)
  A two-channel, 32-bit-per-channel, floating-point interleaved buffer.
- [vImage.InterleavedFx3](./interleavedfx3.md)
  A three-channel, 32-bit-per-channel, floating-point interleaved buffer.
- [vImage.InterleavedFx4](./interleavedfx4.md)
  A four-channel, 32-bit-per-channel, floating-point interleaved buffer.
- [vImage.MultidimensionalLookupTable](./multidimensionallookuptable.md)
  A multidimensional lookup table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimage/size)*