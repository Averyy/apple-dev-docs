# SpeechDetector.Result

**Framework**: Speech  
**Kind**: struct

A result from the speech detector. Please note, these must be enabled via [`init(detectionOptions:reportResults:)`](speechdetector/init(detectionoptions:reportresults:).md) and currently only support error handling from the VAD model.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
struct Result
```

## Topics

### Getting detection results
- [let speechDetected: Bool](speechdetector/result/speechdetected.md)
### Getting audio range
- [var range: CMTimeRange](speechmoduleresult/range.md)
  The audio input range that this result applies to.
### Getting finalization state
- [var isFinal: Bool](speechmoduleresult/isfinal.md)
  Whether this result is final at the time it is produced.
- [var resultsFinalizationTime: CMTime](speechmoduleresult/resultsfinalizationtime.md)
  The audio input time up to which results from this module have been finalized (after this result). The module’s results are final up to but not including this time.

## Relationships

### Conforms To
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [SpeechModuleResult](speechmoduleresult.md)

## See Also

- [var results: some Sendable & AsyncSequence<SpeechDetector.Result, any Error>](speechdetector/results.md)
  The asynchronous sequence of speech detection results.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/speechdetector/result)*