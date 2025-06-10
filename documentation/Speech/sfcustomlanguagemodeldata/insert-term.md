# insert(term:)

**Framework**: Speech  
**Kind**: method

Add a custom term to the vocabulary.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 1.1+

## Declaration

```swift
func insert(term: SFCustomLanguageModelData.CustomPronunciation)
```

#### Discussion

This class accumulates vocabulary data (in the form of tokens paired with X-SAMPA representations of the spoken forms of those tokens) which will later be processed and then provided to an `SFSpeechRecognizer`, to enable it to recognize words that are typically out-of-vocabulary.

## Parameters

- `term`: A token, paired with an X-SAMPA representation of the token’s pronunciation

## See Also

- [func export(to: URL) async throws](sfcustomlanguagemodeldata/export(to:).md)
  Export the accumulated data to a file.
- [func insert(phraseCount: SFCustomLanguageModelData.PhraseCount)](sfcustomlanguagemodeldata/insert(phrasecount:).md)
  Add a sample to the body of training data.
- [func insert(phraseCountGenerator: SFCustomLanguageModelData.PhraseCountGenerator)](sfcustomlanguagemodeldata/insert(phrasecountgenerator:).md)
  Add a stream of samples to the body of training data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/sfcustomlanguagemodeldata/insert(term:))*