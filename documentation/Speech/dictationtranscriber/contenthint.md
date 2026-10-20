# DictationTranscriber.ContentHint

**Framework**: Speech  
**Kind**: struct  
**Role**: Structure

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
- [static let shortForm: DictationTranscriber.ContentHint](./contenthint/shortform.md)
  A processing hint indicating that the audio is only expected to be a minute or so long.
- [static let farField: DictationTranscriber.ContentHint](./contenthint/farfield.md)
  A processing hint indicating that the audio should be processed as if it were from a speaker far from the microphone.
- [static func customizedLanguage(modelConfiguration: SFSpeechLanguageModel.Configuration) -> DictationTranscriber.ContentHint](./contenthint/customizedlanguage%28modelconfiguration%29.md)
  A hint specifying a custom language model applicable to the expected spoken audio content.
- [static let atypicalSpeech: DictationTranscriber.ContentHint](./contenthint/atypicalspeech.md)
  A processing hint indicating that the audio is from a speaker with a heavy accent, lisp, or other confounding factor.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Configuring transcription
- [DictationTranscriber.ReportingOption](./reportingoption.md)
  Options relating to the transcriber’s result delivery.
- [DictationTranscriber.ResultAttributeOption](./resultattributeoption.md)
  Options relating to the attributes of the transcription.
- [DictationTranscriber.TranscriptionOption](./transcriptionoption.md)
  Options relating to the text of the transcription.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/dictationtranscriber/contenthint)*