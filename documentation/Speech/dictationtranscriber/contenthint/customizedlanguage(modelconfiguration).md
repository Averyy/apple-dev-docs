# customizedLanguage(modelConfiguration:)

**Framework**: Speech  
**Kind**: method  
**Role**: Type Method

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

### Content hints
- [static let shortForm: DictationTranscriber.ContentHint](./shortform.md)
  A processing hint indicating that the audio is only expected to be a minute or so long.
- [static let farField: DictationTranscriber.ContentHint](./farfield.md)
  A processing hint indicating that the audio should be processed as if it were from a speaker far from the microphone.
- [static let atypicalSpeech: DictationTranscriber.ContentHint](./atypicalspeech.md)
  A processing hint indicating that the audio is from a speaker with a heavy accent, lisp, or other confounding factor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/dictationtranscriber/contenthint/customizedlanguage(modelconfiguration:))*