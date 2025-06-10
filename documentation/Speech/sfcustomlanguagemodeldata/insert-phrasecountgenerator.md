# insert(phraseCountGenerator:)

**Framework**: Speech  
**Kind**: method

Add a stream of samples to the body of training data.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 1.1+

## Declaration

```swift
func insert(phraseCountGenerator: SFCustomLanguageModelData.PhraseCountGenerator)
```

#### Discussion

This class accumulates text data that will later be used to train a language model, which can be provided to an `SFSpeechRecognizer` to improve performance on certain phrases.

## Parameters

- `phraseCountGenerator`: A generator of phrase counts

## See Also

- [func export(to: URL) async throws](sfcustomlanguagemodeldata/export(to:).md)
  Export the accumulated data to a file.
- [func insert(phraseCount: SFCustomLanguageModelData.PhraseCount)](sfcustomlanguagemodeldata/insert(phrasecount:).md)
  Add a sample to the body of training data.
- [func insert(term: SFCustomLanguageModelData.CustomPronunciation)](sfcustomlanguagemodeldata/insert(term:).md)
  Add a custom term to the vocabulary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/sfcustomlanguagemodeldata/insert(phrasecountgenerator:))*