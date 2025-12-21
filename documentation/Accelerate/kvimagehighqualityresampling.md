# kvImageHighQualityResampling

**Framework**: Accelerate  
**Kind**: var

A flag that uses a higher-quality, slower resampling filter for geometry operations.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.3+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var kvImageHighQualityResampling: Int { get }
```

## Mentions

- [Applying geometric transforms to images](applying-geometric-transforms-to-images.md)
- [Building a Basic Image-Processing Workflow](building-a-basic-image-processing-workflow.md)
- [Resampling in vImage](resampling-in-vimage.md)

#### Discussion

vImage uses Lanczos interpolation for resampling.

Lanczos interpolation provides excellent results for geometric operations on images, preserves details, and reduces aliasing artifacts compared to other resampling techniques.

By default, vImage uses the Lanczos-3 algorithm for resampling. Set this flag to switch to the higher-quality Lanczos-5 algorithm.

## See Also

- [vImage.Options](vimage/options.md)
  Set flags on vImage operations to specify processing options.
- [var kvImageNoFlags: Int](kvimagenoflags.md)
  A flag that sets the behavior to the default.
- [var kvImageLeaveAlphaUnchanged: Int](kvimageleavealphaunchanged.md)
  A flag that restricts the operation to red, green, and blue channels only.
- [var kvImageDoNotTile: Int](kvimagedonottile.md)
  A flag that disables vImage internal tiling routines.
- [var kvImageGetTempBufferSize: Int](kvimagegettempbuffersize.md)
  A flag that returns the minimum temporary buffer size for the operation, given the parameters provided.
- [var kvImagePrintDiagnosticsToConsole: Int](kvimageprintdiagnosticstoconsole.md)
  A flag that prints a debug message if the operation fails.
- [var kvImageNoAllocate: Int](kvimagenoallocate.md)
  A flag that prevents vImage from allocating additional storage.
- [var kvImageHDRContent: Int](kvimagehdrcontent.md)
  A flag that uses HDR-aware methods.
- [var kvImageDoNotClamp: Int](kvimagedonotclamp.md)
  A flag that disables clamping in some conversions to floating-point formats.
- [var kvImageUseFP16Accumulator: Int](kvimageusefp16accumulator.md)
  A flag that specifies vImage uses faster but lower-precision internal arithmetic for floating-point 16-bit operations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/kvimagehighqualityresampling)*