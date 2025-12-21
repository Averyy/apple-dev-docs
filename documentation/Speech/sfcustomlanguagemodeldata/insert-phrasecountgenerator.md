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

- [SFCustomLanguageModelData.TemplatePhraseCountGenerator](sfcustomlanguagemodeldata/templatephrasecountgenerator.md)
  A `PhraseCountGenerator` that produces `PhraseCount` values based on templates.
- [SFCustomLanguageModelData.PhraseCountGenerator](sfcustomlanguagemodeldata/phrasecountgenerator.md)
  Abstract base class defining the interface for classes that generate `PhraseCount` via an iterator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/sfcustomlanguagemodeldata/insert(phrasecountgenerator:))*