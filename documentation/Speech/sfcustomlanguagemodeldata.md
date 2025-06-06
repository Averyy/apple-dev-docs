# SFCustomLanguageModelData

**Framework**: Speech  
**Kind**: class

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst ?+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.1+
- watchOS 10.0+

## Declaration

```swift
class SFCustomLanguageModelData
```

## Topics

### Initializers
- [init(locale: Locale, identifier: String, version: String)](sfcustomlanguagemodeldata/init(locale:identifier:version:).md)
- [convenience init(locale: Locale, identifier: String, version: String, builder: () -> any DataInsertable)](sfcustomlanguagemodeldata/init(locale:identifier:version:builder:).md)
### Instance Properties
- [let identifier: String](sfcustomlanguagemodeldata/identifier.md)
- [let locale: Locale](sfcustomlanguagemodeldata/locale.md)
- [let version: String](sfcustomlanguagemodeldata/version.md)
### Instance Methods
- [func export(to: URL) async throws](sfcustomlanguagemodeldata/export(to:).md)
- [func insert(phraseCount: SFCustomLanguageModelData.PhraseCount)](sfcustomlanguagemodeldata/insert(phrasecount:).md)
- [func insert(phraseCountGenerator: SFCustomLanguageModelData.PhraseCountGenerator)](sfcustomlanguagemodeldata/insert(phrasecountgenerator:).md)
- [func insert(term: SFCustomLanguageModelData.CustomPronunciation)](sfcustomlanguagemodeldata/insert(term:).md)
### Type Methods
- [static func supportedPhonemes(locale: Locale) -> [String]](sfcustomlanguagemodeldata/supportedphonemes(locale:).md)
### Classes
- [SFCustomLanguageModelData.PhraseCountGenerator](sfcustomlanguagemodeldata/phrasecountgenerator.md)
- [SFCustomLanguageModelData.TemplatePhraseCountGenerator](sfcustomlanguagemodeldata/templatephrasecountgenerator.md)
### Structures
- [SFCustomLanguageModelData.CompoundTemplate](sfcustomlanguagemodeldata/compoundtemplate.md)
- [SFCustomLanguageModelData.CustomPronunciation](sfcustomlanguagemodeldata/custompronunciation.md)
- [SFCustomLanguageModelData.DataInsertableBuilder](sfcustomlanguagemodeldata/datainsertablebuilder.md)
- [SFCustomLanguageModelData.PhraseCount](sfcustomlanguagemodeldata/phrasecount.md)
- [SFCustomLanguageModelData.PhraseCountsFromTemplates](sfcustomlanguagemodeldata/phrasecountsfromtemplates.md)
- [SFCustomLanguageModelData.TemplateInsertableBuilder](sfcustomlanguagemodeldata/templateinsertablebuilder.md)

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)

## See Also

- [class SFSpeechLanguageModel](sfspeechlanguagemodel.md)
- [SFSpeechLanguageModel.Configuration](sfspeechlanguagemodel/configuration.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/sfcustomlanguagemodeldata)*