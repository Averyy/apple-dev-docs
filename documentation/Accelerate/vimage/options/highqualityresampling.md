# highQualityResampling

**Framework**: Accelerate  
**Kind**: property  
**Role**: Type Property

A flag that uses a higher quality, slower resampling filter for geometry operations.

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
static let highQualityResampling: vImage.Options
```

## See Also

### Related Documentation
- [var kvImageHighQualityResampling: Int](../../kvimagehighqualityresampling.md)
  A flag that uses a higher-quality, slower resampling filter for geometry operations.
### Type Properties
- [static let backgroundColorFill: vImage.Options](./backgroundcolorfill.md)
  A flag that uses the background color for missing pixels.
- [static let copyInPlace: vImage.Options](./copyinplace.md)
  A flag that copies the value of the edge pixel in the source to the destination.
- [static let doNotClamp: vImage.Options](./donotclamp.md)
  A flag that disables clamping in some conversions to floating-point formats.
- [static let doNotTile: vImage.Options](./donottile.md)
  A flag that disables vImage internal tiling routines.
- [static let getTempBufferSize: vImage.Options](./gettempbuffersize.md)
  A flag that returns the minimum temporary buffer size for the operation, given the parameters provided.
- [static let hdrContent: vImage.Options](./hdrcontent.md)
  A flag that uses HDR-aware methods.
- [static let imageExtend: vImage.Options](./imageextend.md)
  A flag that extends the edges of the image infinitely.
- [static let leaveAlphaUnchanged: vImage.Options](./leavealphaunchanged.md)
  A flag that restricts the operation to red, green, and blue channels only.
- [static let noAllocate: vImage.Options](./noallocate.md)
  A flag that prevents vImage from allocating additional storage.
- [static let noFlags: vImage.Options](./noflags.md)
  A flag that sets the behavior to the default.
- [static let printDiagnosticsToConsole: vImage.Options](./printdiagnosticstoconsole.md)
  A flag that prints a debug message if the operation fails.
- [static let truncateKernel: vImage.Options](./truncatekernel.md)
  A flag that uses only the part of the kernel that overlaps the image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimage/options/highqualityresampling)*