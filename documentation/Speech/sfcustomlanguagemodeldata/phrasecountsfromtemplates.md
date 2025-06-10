# SFCustomLanguageModelData.PhraseCountsFromTemplates

**Framework**: Speech  
**Kind**: struct

A type that can be used to construct custom language model data by specifying a set of template classes and using the resuilt builder DSL to specify templates.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 1.1+

## Declaration

```swift
struct PhraseCountsFromTemplates
```

## Topics

### Initializers
- [init(classes: [String : [String]], builder: () -> any TemplateInsertable)](sfcustomlanguagemodeldata/phrasecountsfromtemplates/init(classes:builder:).md)

## Relationships

### Conforms To
- [DataInsertable](datainsertable.md)

## See Also

- [SFCustomLanguageModelData.CompoundTemplate](sfcustomlanguagemodeldata/compoundtemplate.md)
  A class supporting the custom language model training data result builder. You are not intended to use this directly.
- [SFCustomLanguageModelData.CustomPronunciation](sfcustomlanguagemodeldata/custompronunciation.md)
  A term to be introduced into the speech recognition model’s vocabulary.
- [SFCustomLanguageModelData.DataInsertableBuilder](sfcustomlanguagemodeldata/datainsertablebuilder.md)
  A custom parameter attribute that constructs custom language model data from closures.
- [SFCustomLanguageModelData.PhraseCount](sfcustomlanguagemodeldata/phrasecount.md)
  A phrase used to bias the language model, along with a weight influencing the relative strength of the bias.
- [SFCustomLanguageModelData.TemplateInsertableBuilder](sfcustomlanguagemodeldata/templateinsertablebuilder.md)
  A custom parameter attribute that constructs custom language model data from closures.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/sfcustomlanguagemodeldata/phrasecountsfromtemplates)*