# kvImageNoAllocate

**Framework**: Accelerate  
**Kind**: var

A flag that prevents vImage from allocating additional storage.

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
var kvImageNoAllocate: Int { get }
```

#### Discussion

When you set this flag, vImage uses the memory provided to the buffer rather than allocating new memory. For example, instead of overwriting a buffer’s [`data`](vimage_buffer/data.md) property with a newly allocated pointer to memory, vImage uses the memory pointed to by the [`data`](vimage_buffer/data.md) property directly. In other cases, it may cause the function to assume ownership of a buffer, rather than allocating a copy. You are responsible for making sure the buffer that you allocate is large enough to hold the image. Most vImage functions do not allocate memory and assume that the buffer’s data is already allocated, and, in the case of source image buffers, contain valid pixel data.

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
- [var kvImagePrintDiagnosticsToConsole: Int](kvimageprintdiagnosticstoconsole.md)
  A flag that prints a debug message if the operation fails.
- [var kvImageHDRContent: Int](kvimagehdrcontent.md)
  A flag that uses HDR-aware methods.
- [var kvImageDoNotClamp: Int](kvimagedonotclamp.md)
  A flag that disables clamping in some conversions to floating-point formats.
- [var kvImageUseFP16Accumulator: Int](kvimageusefp16accumulator.md)
  A flag that specifies vImage uses faster but lower-precision internal arithmetic for floating-point 16-bit operations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/kvimagenoallocate)*