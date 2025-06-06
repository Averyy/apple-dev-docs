# AVVideoFrameAnalysisType

**Framework**: AVKit  
**Kind**: struct

Constants that define the types of analysis a player view controller may perform on a paused video frame.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 1.0+

## Declaration

```swift
struct AVVideoFrameAnalysisType
```

## Topics

### Analysis types
- [static var `default`: AVVideoFrameAnalysisType](avvideoframeanalysistype/default.md)
  The default types of analysis to perform.
- [static var text: AVVideoFrameAnalysisType](avvideoframeanalysistype/text.md)
  A type that finds text in a paused video frame.
- [static var subject: AVVideoFrameAnalysisType](avvideoframeanalysistype/subject.md)
  A type that finds a subject that a user can copy out of frame.
- [static var visualSearch: AVVideoFrameAnalysisType](avvideoframeanalysistype/visualsearch.md)
  A type that identifies objects, landmarks, art, and so on.
- [static var machineReadableCode: AVVideoFrameAnalysisType](avvideoframeanalysistype/machinereadablecode.md)
  A type that recognizes machine-readable codes, such as QR codes.
### Initializers
- [init(rawValue: UInt)](avvideoframeanalysistype/init(rawvalue:).md)
  Creates a type from a string value.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [var allowsVideoFrameAnalysis: Bool](avplayerview/allowsvideoframeanalysis.md)
  A Boolean value that indicates whether to perform video frame analysis.
- [var videoFrameAnalysisTypes: AVVideoFrameAnalysisType](avplayerview/videoframeanalysistypes.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avvideoframeanalysistype)*