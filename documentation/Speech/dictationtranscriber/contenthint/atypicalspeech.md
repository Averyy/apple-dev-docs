# atypicalSpeech

**Framework**: Speech  
**Kind**: property  
**Role**: Type Property

A processing hint indicating that the audio is from a speaker with a heavy accent, lisp, or other confounding factor.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
static let atypicalSpeech: DictationTranscriber.ContentHint
```

## See Also

### Content hints
- [static let shortForm: DictationTranscriber.ContentHint](./shortform.md)
  A processing hint indicating that the audio is only expected to be a minute or so long.
- [static let farField: DictationTranscriber.ContentHint](./farfield.md)
  A processing hint indicating that the audio should be processed as if it were from a speaker far from the microphone.
- [static func customizedLanguage(modelConfiguration: SFSpeechLanguageModel.Configuration) -> DictationTranscriber.ContentHint](./customizedlanguage%28modelconfiguration%29.md)
  A hint specifying a custom language model applicable to the expected spoken audio content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/dictationtranscriber/contenthint/atypicalspeech)*