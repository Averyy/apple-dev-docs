# insert(phraseCount:)

**Framework**: Speech  
**Kind**: method

Add a sample to the body of training data.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 1.1+

## Declaration

```swift
func insert(phraseCount: SFCustomLanguageModelData.PhraseCount)
```

#### Discussion

This class accumulates text data that will later be used to train a language model, which can be provided to an `SFSpeechRecognizer` to improve performance on certain phrases.

## Parameters

- `phraseCount`: A sample of text on which to train your custom language model

## See Also

- [func export(to: URL) async throws](sfcustomlanguagemodeldata/export(to:).md)
  Export the accumulated data to a file.
- [func insert(phraseCountGenerator: SFCustomLanguageModelData.PhraseCountGenerator)](sfcustomlanguagemodeldata/insert(phrasecountgenerator:).md)
  Add a stream of samples to the body of training data.
- [func insert(term: SFCustomLanguageModelData.CustomPronunciation)](sfcustomlanguagemodeldata/insert(term:).md)
  Add a custom term to the vocabulary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/sfcustomlanguagemodeldata/insert(phrasecount:))*