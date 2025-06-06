# PhotogrammetrySession.Limits

**Framework**: RealityKit  
**Kind**: struct

Data structure to observe hardware limits for reconstruction.  Note that these are specific to the device on which the `PhotogrammetrySession` is run.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+

## Declaration

```swift
struct Limits
```

## Topics

### Instance Properties
- [var maximumInputImageDimension: Int](photogrammetrysession/limits-swift.struct/maximuminputimagedimension.md)
  The maximum allowed dimension (either height or width) of input images that can be ingested by the reconstruction session. If images larger than this are provided, they will be ignored and an `.invalidSample` message will be output.
- [var maximumNumberOfInputImages: Int](photogrammetrysession/limits-swift.struct/maximumnumberofinputimages.md)
  Returns the maximum number of input images or samples that the session can use for reconstruction. If more than this number are provided, any in excess of the limit will be ignored and an `.invalidSample` message for the sample will be output.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/photogrammetrysession/limits-swift.struct)*