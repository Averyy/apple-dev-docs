# DictationTranscriber.ReportingOption.volatileResults

**Framework**: Speech  
**Kind**: case

Provides tentative results for an audio range in addition to the finalized result.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
case volatileResults
```

#### Discussion

The transcriber will deliver several results for an audio range as it refines the transcription.

## See Also

- [DictationTranscriber.ReportingOption.alternativeTranscriptions](dictationtranscriber/reportingoption/alternativetranscriptions.md)
  Includes alternative transcriptions in addition to the most likely transcription.
- [DictationTranscriber.ReportingOption.frequentFinalization](dictationtranscriber/reportingoption/frequentfinalization.md)
  Biases the transcriber towards responsiveness, resulting in more frequent but also less accurate finalized results.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/dictationtranscriber/reportingoption/volatileresults)*