# export(to:)

**Framework**: Speech  
**Kind**: method

Export the accumulated data to a file.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 1.1+

## Declaration

```swift
func export(to path: URL) async throws
```

#### Discussion

The file produced by this method can be provided to `SFSpeechLanguageModel.prepareCustomLanguageModel` to produce language model and vocabulary files that are then ready to be used in conjunction with the `SFSpeechRecognizer`.

> **Note**: Errors related to creating directories and files, and deleting files

## Parameters

- `path`: A URL where the exported data will be saved.

## See Also

- [func insert(phraseCount: SFCustomLanguageModelData.PhraseCount)](sfcustomlanguagemodeldata/insert(phrasecount:).md)
  Add a sample to the body of training data.
- [func insert(phraseCountGenerator: SFCustomLanguageModelData.PhraseCountGenerator)](sfcustomlanguagemodeldata/insert(phrasecountgenerator:).md)
  Add a stream of samples to the body of training data.
- [func insert(term: SFCustomLanguageModelData.CustomPronunciation)](sfcustomlanguagemodeldata/insert(term:).md)
  Add a custom term to the vocabulary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/sfcustomlanguagemodeldata/export(to:))*