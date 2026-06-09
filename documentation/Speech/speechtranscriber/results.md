# results

**Framework**: Speech  
**Kind**: property

The asynchronous sequence of transcription results.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
final var results: some Sendable & AsyncSequence<SpeechTranscriber.Result, any Error> { get }
```

#### Discussion

Accessing this property does not create a new sequence.

## See Also

- [SpeechTranscriber.Result](speechtranscriber/result.md)
  A phrase or passage of transcribed speech. The phrases are sent in order.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/speechtranscriber/results)*