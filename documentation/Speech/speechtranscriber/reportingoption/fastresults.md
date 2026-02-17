# SpeechTranscriber.ReportingOption.fastResults

**Framework**: Speech  
**Kind**: case

Biases the transcriber towards responsiveness, yielding faster but also less accurate results.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
case fastResults
```

#### Discussion

If included, the transcriber reduces result latency by using a smaller “context window”.

## See Also

- [SpeechTranscriber.ReportingOption.alternativeTranscriptions](speechtranscriber/reportingoption/alternativetranscriptions.md)
  Includes alternative transcriptions in addition to the most likely transcription.
- [SpeechTranscriber.ReportingOption.volatileResults](speechtranscriber/reportingoption/volatileresults.md)
  Provides tentative results for an audio range in addition to the finalized result.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/speechtranscriber/reportingoption/fastresults)*