# SpeechTranscriber.ReportingOption

**Framework**: Speech  
**Kind**: enum  
**Role**: Enumeration

Options relating to the transcriber’s result delivery.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
enum ReportingOption
```

## Topics

### Reporting options
- [SpeechTranscriber.ReportingOption.alternativeTranscriptions](./reportingoption/alternativetranscriptions.md)
  Includes alternative transcriptions in addition to the most likely transcription.
- [SpeechTranscriber.ReportingOption.fastResults](./reportingoption/fastresults.md)
  Biases the transcriber towards responsiveness, yielding faster but also less accurate results.
- [SpeechTranscriber.ReportingOption.volatileResults](./reportingoption/volatileresults.md)
  Provides tentative results for an audio range in addition to the finalized result.

## Relationships

### Conforms To
- [CaseIterable](../../Swift/caseiterable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Configuring transcription
- [SpeechTranscriber.ResultAttributeOption](./resultattributeoption.md)
  Options relating to the attributes of the transcription.
- [SpeechTranscriber.TranscriptionOption](./transcriptionoption.md)
  Options relating to the text of the transcription.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/speechtranscriber/reportingoption)*