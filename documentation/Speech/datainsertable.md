# DataInsertable

**Framework**: Speech  
**Kind**: protocol

A protocol supporting the custom language model training data result builder.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 1.1+

## Declaration

```swift
protocol DataInsertable
```

## Topics

### Instance Methods
- [func insert(data: SFCustomLanguageModelData)](datainsertable/insert(data:).md)

## Relationships

### Conforming Types
- [SFCustomLanguageModelData.CustomPronunciation](sfcustomlanguagemodeldata/custompronunciation.md)
- [SFCustomLanguageModelData.PhraseCount](sfcustomlanguagemodeldata/phrasecount.md)
- [SFCustomLanguageModelData.PhraseCountGenerator](sfcustomlanguagemodeldata/phrasecountgenerator.md)
- [SFCustomLanguageModelData.PhraseCountsFromTemplates](sfcustomlanguagemodeldata/phrasecountsfromtemplates.md)
- [SFCustomLanguageModelData.TemplatePhraseCountGenerator](sfcustomlanguagemodeldata/templatephrasecountgenerator.md)

## See Also

- [class AnalysisContext](analysiscontext.md)
  Contextual information that may be shared among analyzers.
- [class SFCustomLanguageModelData](sfcustomlanguagemodeldata.md)
  An object that generates and exports custom language model training data.
- [class SFSpeechLanguageModel](sfspeechlanguagemodel.md)
  A language model built from custom training data.
- [SFSpeechLanguageModel.Configuration](sfspeechlanguagemodel/configuration.md)
  An object describing the location of a custom language model and specialized vocabulary.
- [protocol TemplateInsertable](templateinsertable.md)
  A protocol supporting the custom language model training data result builder.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/datainsertable)*