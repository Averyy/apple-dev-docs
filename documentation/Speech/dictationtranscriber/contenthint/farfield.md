# farField

**Framework**: Speech  
**Kind**: property

A processing hint indicating that the audio should be processed as if it were from a speaker far from the microphone.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
static let farField: DictationTranscriber.ContentHint
```

## See Also

- [static let shortForm: DictationTranscriber.ContentHint](dictationtranscriber/contenthint/shortform.md)
  A processing hint indicating that the audio is only expected to be a minute or so long.
- [static func customizedLanguage(modelConfiguration: SFSpeechLanguageModel.Configuration) -> DictationTranscriber.ContentHint](dictationtranscriber/contenthint/customizedlanguage(modelconfiguration:).md)
  A hint specifying a custom language model applicable to the expected spoken audio content.
- [static let atypicalSpeech: DictationTranscriber.ContentHint](dictationtranscriber/contenthint/atypicalspeech.md)
  A processing hint indicating that the audio is from a speaker with a heavy accent, lisp, or other confounding factor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/dictationtranscriber/contenthint/farfield)*