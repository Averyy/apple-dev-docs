# vImage.Options

**Framework**: Accelerate  
**Kind**: struct

Set flags on vImage operations to specify processing options.

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
struct Options
```

## Topics

### Type Properties
- [static let backgroundColorFill: vImage.Options](vimage/options/backgroundcolorfill.md)
  A flag that uses the background color for missing pixels.
- [static let copyInPlace: vImage.Options](vimage/options/copyinplace.md)
  A flag that copies the value of the edge pixel in the source to the destination.
- [static let doNotClamp: vImage.Options](vimage/options/donotclamp.md)
  A flag that disables clamping in some conversions to floating-point formats.
- [static let doNotTile: vImage.Options](vimage/options/donottile.md)
  A flag that disables vImage internal tiling routines.
- [static let getTempBufferSize: vImage.Options](vimage/options/gettempbuffersize.md)
  A flag that returns the minimum temporary buffer size for the operation, given the parameters provided.
- [static let hdrContent: vImage.Options](vimage/options/hdrcontent.md)
  A flag that uses HDR-aware methods.
- [static let highQualityResampling: vImage.Options](vimage/options/highqualityresampling.md)
  A flag that uses a higher quality, slower resampling filter for geometry operations.
- [static let imageExtend: vImage.Options](vimage/options/imageextend.md)
  A flag that extends the edges of the image infinitely.
- [static let leaveAlphaUnchanged: vImage.Options](vimage/options/leavealphaunchanged.md)
  A flag that restricts the operation to red, green, and blue channels only.
- [static let noAllocate: vImage.Options](vimage/options/noallocate.md)
  A flag that prevents vImage from allocating additional storage.
- [static let noFlags: vImage.Options](vimage/options/noflags.md)
  A flag that sets the behavior to the default.
- [static let printDiagnosticsToConsole: vImage.Options](vimage/options/printdiagnosticstoconsole.md)
  A flag that prints a debug message if the operation fails.
- [static let truncateKernel: vImage.Options](vimage/options/truncatekernel.md)
  A flag that uses only the part of the kernel that overlaps the image.
### Instance Properties
- [var flags: vImage_Flags](vimage/options/flags.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimage/options)*