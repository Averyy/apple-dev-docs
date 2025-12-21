# SpeechTranscriber.ReportingOption

**Framework**: Speech  
**Kind**: enum

Options relating to the transcriber’s result delivery.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
enum ReportingOption
```

## Topics

### Reporting options
- [SpeechTranscriber.ReportingOption.alternativeTranscriptions](speechtranscriber/reportingoption/alternativetranscriptions.md)
  Includes alternative transcriptions in addition to the most likely transcription.
- [SpeechTranscriber.ReportingOption.fastResults](speechtranscriber/reportingoption/fastresults.md)
  Biases the transcriber towards responsiveness, yielding faster but also less accurate results.
- [SpeechTranscriber.ReportingOption.volatileResults](speechtranscriber/reportingoption/volatileresults.md)
  Provides tentative results for an audio range in addition to the finalized result.

## Relationships

### Conforms To
- [CaseIterable](../Swift/CaseIterable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [SpeechTranscriber.ResultAttributeOption](speechtranscriber/resultattributeoption.md)
  Options relating to the attributes of the transcription.
- [SpeechTranscriber.TranscriptionOption](speechtranscriber/transcriptionoption.md)
  Options relating to the text of the transcription.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/speechtranscriber/reportingoption)*