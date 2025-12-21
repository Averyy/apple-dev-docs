# DictationTranscriber.ReportingOption

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
- [DictationTranscriber.ReportingOption.alternativeTranscriptions](dictationtranscriber/reportingoption/alternativetranscriptions.md)
  Includes alternative transcriptions in addition to the most likely transcription.
- [DictationTranscriber.ReportingOption.frequentFinalization](dictationtranscriber/reportingoption/frequentfinalization.md)
  Biases the transcriber towards responsiveness, resulting in more frequent but also less accurate finalized results.
- [DictationTranscriber.ReportingOption.volatileResults](dictationtranscriber/reportingoption/volatileresults.md)
  Provides tentative results for an audio range in addition to the finalized result.

## Relationships

### Conforms To
- [CaseIterable](../Swift/CaseIterable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [DictationTranscriber.ContentHint](dictationtranscriber/contenthint.md)
  Expected characteristics of the spoken audio content and its delivery.
- [DictationTranscriber.ResultAttributeOption](dictationtranscriber/resultattributeoption.md)
  Options relating to the attributes of the transcription.
- [DictationTranscriber.TranscriptionOption](dictationtranscriber/transcriptionoption.md)
  Options relating to the text of the transcription.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/dictationtranscriber/reportingoption)*