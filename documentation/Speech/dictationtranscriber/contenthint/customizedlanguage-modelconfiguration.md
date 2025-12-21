# customizedLanguage(modelConfiguration:)

**Framework**: Speech  
**Kind**: method

A hint specifying a custom language model applicable to the expected spoken audio content.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
static func customizedLanguage(modelConfiguration: SFSpeechLanguageModel.Configuration) -> DictationTranscriber.ContentHint
```

## See Also

- [static let shortForm: DictationTranscriber.ContentHint](dictationtranscriber/contenthint/shortform.md)
  A processing hint indicating that the audio is only expected to be a minute or so long.
- [static let farField: DictationTranscriber.ContentHint](dictationtranscriber/contenthint/farfield.md)
  A processing hint indicating that the audio should be processed as if it were from a speaker far from the microphone.
- [static let atypicalSpeech: DictationTranscriber.ContentHint](dictationtranscriber/contenthint/atypicalspeech.md)
  A processing hint indicating that the audio is from a speaker with a heavy accent, lisp, or other confounding factor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/dictationtranscriber/contenthint/customizedlanguage(modelconfiguration:))*