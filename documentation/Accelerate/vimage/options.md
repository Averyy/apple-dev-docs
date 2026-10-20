# vImage.Options

**Framework**: Accelerate  
**Kind**: struct  
**Role**: Structure

Set flags on vImage operations to specify processing options.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS
- watchOS 6.0+

## Declaration

```swift
struct Options
```

## Topics

### Type Properties
- [static let backgroundColorFill: vImage.Options](./options/backgroundcolorfill.md)
  A flag that uses the background color for missing pixels.
- [static let copyInPlace: vImage.Options](./options/copyinplace.md)
  A flag that copies the value of the edge pixel in the source to the destination.
- [static let doNotClamp: vImage.Options](./options/donotclamp.md)
  A flag that disables clamping in some conversions to floating-point formats.
- [static let doNotTile: vImage.Options](./options/donottile.md)
  A flag that disables vImage internal tiling routines.
- [static let getTempBufferSize: vImage.Options](./options/gettempbuffersize.md)
  A flag that returns the minimum temporary buffer size for the operation, given the parameters provided.
- [static let hdrContent: vImage.Options](./options/hdrcontent.md)
  A flag that uses HDR-aware methods.
- [static let highQualityResampling: vImage.Options](./options/highqualityresampling.md)
  A flag that uses a higher quality, slower resampling filter for geometry operations.
- [static let imageExtend: vImage.Options](./options/imageextend.md)
  A flag that extends the edges of the image infinitely.
- [static let leaveAlphaUnchanged: vImage.Options](./options/leavealphaunchanged.md)
  A flag that restricts the operation to red, green, and blue channels only.
- [static let noAllocate: vImage.Options](./options/noallocate.md)
  A flag that prevents vImage from allocating additional storage.
- [static let noFlags: vImage.Options](./options/noflags.md)
  A flag that sets the behavior to the default.
- [static let printDiagnosticsToConsole: vImage.Options](./options/printdiagnosticstoconsole.md)
  A flag that prints a debug message if the operation fails.
- [static let truncateKernel: vImage.Options](./options/truncatekernel.md)
  A flag that uses only the part of the kernel that overlaps the image.
### Instance Properties
- [var flags: vImage_Flags](./options/flags.md)

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../../Swift/optionset.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [SetAlgebra](../../Swift/setalgebra.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimage/options)*