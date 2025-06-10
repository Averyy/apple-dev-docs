# DictationTranscriber.ContentHint

**Framework**: Speech  
**Kind**: struct

Expected characteristics of the spoken audio content and its delivery.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
struct ContentHint
```

#### Overview

These hints optimize transcription, but do not preclude spoken audio with different characteristics.

## Topics

### Type Properties
- [static let atypicalSpeech: DictationTranscriber.ContentHint](dictationtranscriber/contenthint/atypicalspeech.md)
  A processing hint indicating that the audio is from a speaker with a heavy accent, lisp, or other confounding factor.
- [static let farField: DictationTranscriber.ContentHint](dictationtranscriber/contenthint/farfield.md)
  A processing hint indicating that the audio should be processed as if it were from a speaker far from the microphone.
- [static let shortForm: DictationTranscriber.ContentHint](dictationtranscriber/contenthint/shortform.md)
  A processing hint indicating that the audio is only expected to be a minute or so long.
### Type Methods
- [static func customizedLanguage(modelConfiguration: SFSpeechLanguageModel.Configuration) -> DictationTranscriber.ContentHint](dictationtranscriber/contenthint/customizedlanguage(modelconfiguration:).md)
  A hint specifying a custom language model applicable to the expected spoken audio content.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [DictationTranscriber.Preset](dictationtranscriber/preset.md)
  Predefined transcriber configurations.
- [DictationTranscriber.Result](dictationtranscriber/result.md)
  A phrase or passage of transcribed speech. The phrases are sent in order.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/dictationtranscriber/contenthint)*