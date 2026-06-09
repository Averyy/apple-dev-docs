# results

**Framework**: Speech  
**Kind**: property

The asynchronous sequence of speech detection results.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
final var results: some Sendable & AsyncSequence<SpeechDetector.Result, any Error> { get }
```

#### Discussion

This sequence may throw an error, but will otherwise remain empty.

Accessing this property does not create a new sequence.

## See Also

- [SpeechDetector.Result](speechdetector/result.md)
  A result from the speech detector. Please note, these must be enabled via [`init(detectionOptions:reportResults:)`](speechdetector/init(detectionoptions:reportresults:).md) and currently only support error handling from the VAD model.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/speechdetector/results)*