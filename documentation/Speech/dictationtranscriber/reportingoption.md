# DictationTranscriber.ReportingOption

**Framework**: Speech  
**Kind**: enum  
**Role**: Enumeration

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
- [DictationTranscriber.ReportingOption.alternativeTranscriptions](./reportingoption/alternativetranscriptions.md)
  Includes alternative transcriptions in addition to the most likely transcription.
- [DictationTranscriber.ReportingOption.frequentFinalization](./reportingoption/frequentfinalization.md)
  Biases the transcriber towards responsiveness, resulting in more frequent but also less accurate finalized results.
- [DictationTranscriber.ReportingOption.volatileResults](./reportingoption/volatileresults.md)
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
- [DictationTranscriber.ContentHint](./contenthint.md)
  Expected characteristics of the spoken audio content and its delivery.
- [DictationTranscriber.ResultAttributeOption](./resultattributeoption.md)
  Options relating to the attributes of the transcription.
- [DictationTranscriber.TranscriptionOption](./transcriptionoption.md)
  Options relating to the text of the transcription.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/dictationtranscriber/reportingoption)*