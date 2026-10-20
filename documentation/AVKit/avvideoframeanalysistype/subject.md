# subject

**Framework**: AVKit  
**Kind**: property  
**Role**: Type Property

A type that finds a subject that a user can copy out of frame.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 1.0+

## Declaration

```swift
static var subject: AVVideoFrameAnalysisType { get }
```

```c
AVVideoFrameAnalysisTypeSubject
```

## See Also

### Analysis types
- [static var `default`: AVVideoFrameAnalysisType](./default.md)
  The default types of analysis to perform.
- [static var text: AVVideoFrameAnalysisType](./text.md)
  A type that finds text in a paused video frame.
- [static var visualSearch: AVVideoFrameAnalysisType](./visualsearch.md)
  A type that identifies objects, landmarks, art, and so on.
- [static var machineReadableCode: AVVideoFrameAnalysisType](./machinereadablecode.md)
  A type that recognizes machine-readable codes, such as QR codes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avvideoframeanalysistype/subject)*