# imageExtend

**Framework**: Accelerate  
**Kind**: property

A flag that extends the edges of the image infinitely.

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
static let imageExtend: vImage.Options
```

## See Also

- [var kvImageEdgeExtend: Int](kvimageedgeextend.md)
  A flag that extends the edges of the image infinitely.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimage/options/imageextend)*