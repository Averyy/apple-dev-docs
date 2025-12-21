# DictationTranscriber.ContentHint

**Framework**: Speech  
**Kind**: struct

Expected characteristics of the spoken audio content and its delivery.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
struct ContentHint
```

#### Overview

These hints optimize transcription, but do not preclude spoken audio with different characteristics.

## Topics

### Content hints
- [static let shortForm: DictationTranscriber.ContentHint](dictationtranscriber/contenthint/shortform.md)
  A processing hint indicating that the audio is only expected to be a minute or so long.
- [static let farField: DictationTranscriber.ContentHint](dictationtranscriber/contenthint/farfield.md)
  A processing hint indicating that the audio should be processed as if it were from a speaker far from the microphone.
- [static func customizedLanguage(modelConfiguration: SFSpeechLanguageModel.Configuration) -> DictationTranscriber.ContentHint](dictationtranscriber/contenthint/customizedlanguage(modelconfiguration:).md)
  A hint specifying a custom language model applicable to the expected spoken audio content.
- [static let atypicalSpeech: DictationTranscriber.ContentHint](dictationtranscriber/contenthint/atypicalspeech.md)
  A processing hint indicating that the audio is from a speaker with a heavy accent, lisp, or other confounding factor.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [DictationTranscriber.ReportingOption](dictationtranscriber/reportingoption.md)
  Options relating to the transcriber’s result delivery.
- [DictationTranscriber.ResultAttributeOption](dictationtranscriber/resultattributeoption.md)
  Options relating to the attributes of the transcription.
- [DictationTranscriber.TranscriptionOption](dictationtranscriber/transcriptionoption.md)
  Options relating to the text of the transcription.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/dictationtranscriber/contenthint)*