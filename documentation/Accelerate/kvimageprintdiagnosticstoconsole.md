# kvImagePrintDiagnosticsToConsole

**Framework**: Accelerate  
**Kind**: var

A flag that prints a debug message if the operation fails.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var kvImagePrintDiagnosticsToConsole: Int { get }
```

## See Also

- [vImage.Options](vimage/options.md)
  Set flags on vImage operations to specify processing options.
- [var kvImageNoFlags: Int](kvimagenoflags.md)
  A flag that sets the behavior to the default.
- [var kvImageLeaveAlphaUnchanged: Int](kvimageleavealphaunchanged.md)
  A flag that restricts the operation to red, green, and blue channels only.
- [var kvImageDoNotTile: Int](kvimagedonottile.md)
  A flag that disables vImage internal tiling routines.
- [var kvImageHighQualityResampling: Int](kvimagehighqualityresampling.md)
  A flag that uses a higher-quality, slower resampling filter for geometry operations.
- [var kvImageGetTempBufferSize: Int](kvimagegettempbuffersize.md)
  A flag that returns the minimum temporary buffer size for the operation, given the parameters provided.
- [var kvImageNoAllocate: Int](kvimagenoallocate.md)
  A flag that prevents vImage from allocating additional storage.
- [var kvImageHDRContent: Int](kvimagehdrcontent.md)
  A flag that uses HDR-aware methods.
- [var kvImageDoNotClamp: Int](kvimagedonotclamp.md)
  A flag that disables clamping in some conversions to floating-point formats.
- [var kvImageUseFP16Accumulator: Int](kvimageusefp16accumulator.md)
  A flag that specifies vImage uses faster but lower-precision internal arithmetic for floating-point 16-bit operations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/kvimageprintdiagnosticstoconsole)*