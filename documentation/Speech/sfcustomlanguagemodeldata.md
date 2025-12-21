# SFCustomLanguageModelData

**Framework**: Speech  
**Kind**: class

An object that generates and exports custom language model training data.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 1.1+

## Declaration

```swift
class SFCustomLanguageModelData
```

## Topics

### Creating a model data container
- [convenience init(locale: Locale, identifier: String, version: String, builder: () -> any DataInsertable)](sfcustomlanguagemodeldata/init(locale:identifier:version:builder:).md)
  Constructs a data container using a builder
- [init(locale: Locale, identifier: String, version: String)](sfcustomlanguagemodeldata/init(locale:identifier:version:).md)
  Constructs an empty data container.
- [SFCustomLanguageModelData.DataInsertableBuilder](sfcustomlanguagemodeldata/datainsertablebuilder.md)
  A custom parameter attribute that constructs custom language model data from closures.
### Adding terms
- [func insert(term: SFCustomLanguageModelData.CustomPronunciation)](sfcustomlanguagemodeldata/insert(term:).md)
  Add a custom term to the vocabulary.
- [static func supportedPhonemes(locale: Locale) -> [String]](sfcustomlanguagemodeldata/supportedphonemes(locale:).md)
  List the supported subset of X-SAMPA pronunciations supported by this locale for the Speech framework.
- [SFCustomLanguageModelData.CustomPronunciation](sfcustomlanguagemodeldata/custompronunciation.md)
  A term to be introduced into the speech recognition model’s vocabulary.
### Adding phrases
- [func insert(phraseCount: SFCustomLanguageModelData.PhraseCount)](sfcustomlanguagemodeldata/insert(phrasecount:).md)
  Add a sample to the body of training data.
- [SFCustomLanguageModelData.PhraseCount](sfcustomlanguagemodeldata/phrasecount.md)
  A phrase used to bias the language model, along with a weight influencing the relative strength of the bias.
### Adding parameterized sample data within a result builder
- [SFCustomLanguageModelData.PhraseCountsFromTemplates](sfcustomlanguagemodeldata/phrasecountsfromtemplates.md)
  A type that can be used to construct custom language model data by specifying a set of template classes and using the result builder DSL to specify templates.
- [SFCustomLanguageModelData.TemplateInsertableBuilder](sfcustomlanguagemodeldata/templateinsertablebuilder.md)
  A custom parameter attribute that constructs custom language model data from closures.
### Adding parameterized sample data with a generator
- [func insert(phraseCountGenerator: SFCustomLanguageModelData.PhraseCountGenerator)](sfcustomlanguagemodeldata/insert(phrasecountgenerator:).md)
  Add a stream of samples to the body of training data.
- [SFCustomLanguageModelData.TemplatePhraseCountGenerator](sfcustomlanguagemodeldata/templatephrasecountgenerator.md)
  A `PhraseCountGenerator` that produces `PhraseCount` values based on templates.
- [SFCustomLanguageModelData.PhraseCountGenerator](sfcustomlanguagemodeldata/phrasecountgenerator.md)
  Abstract base class defining the interface for classes that generate `PhraseCount` via an iterator.
### Exporting model data
- [func export(to: URL) async throws](sfcustomlanguagemodeldata/export(to:).md)
  Export the accumulated data to a file.
### Inspecting model data
- [let identifier: String](sfcustomlanguagemodeldata/identifier.md)
- [let locale: Locale](sfcustomlanguagemodeldata/locale.md)
- [let version: String](sfcustomlanguagemodeldata/version.md)
### Result builder support
- [SFCustomLanguageModelData.CompoundTemplate](sfcustomlanguagemodeldata/compoundtemplate.md)
  A class supporting the custom language model training data result builder. You are not intended to use this directly.
- [protocol DataInsertable](datainsertable.md)
  A protocol supporting the custom language model training data result builder.
- [protocol TemplateInsertable](templateinsertable.md)
  A protocol supporting the custom language model training data result builder.

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)

## See Also

- [class AnalysisContext](analysiscontext.md)
  Contextual information that may be shared among analyzers.
- [class SFSpeechLanguageModel](sfspeechlanguagemodel.md)
  A language model built from custom training data.
- [SFSpeechLanguageModel.Configuration](sfspeechlanguagemodel/configuration.md)
  An object describing the location of a custom language model and specialized vocabulary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/sfcustomlanguagemodeldata)*