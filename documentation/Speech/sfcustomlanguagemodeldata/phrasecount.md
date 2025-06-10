# SFCustomLanguageModelData.PhraseCount

**Framework**: Speech  
**Kind**: struct

A phrase used to bias the language model, along with a weight influencing the relative strength of the bias.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 1.1+

## Declaration

```swift
struct PhraseCount
```

## Topics

### Initializers
- [init(phrase: String, count: Int)](sfcustomlanguagemodeldata/phrasecount/init(phrase:count:).md)
### Instance Properties
- [let count: Int](sfcustomlanguagemodeldata/phrasecount/count.md)
- [let phrase: String](sfcustomlanguagemodeldata/phrasecount/phrase.md)

## Relationships

### Conforms To
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [DataInsertable](datainsertable.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [SFCustomLanguageModelData.CompoundTemplate](sfcustomlanguagemodeldata/compoundtemplate.md)
  A class supporting the custom language model training data result builder. You are not intended to use this directly.
- [SFCustomLanguageModelData.CustomPronunciation](sfcustomlanguagemodeldata/custompronunciation.md)
  A term to be introduced into the speech recognition model’s vocabulary.
- [SFCustomLanguageModelData.DataInsertableBuilder](sfcustomlanguagemodeldata/datainsertablebuilder.md)
  A custom parameter attribute that constructs custom language model data from closures.
- [SFCustomLanguageModelData.PhraseCountsFromTemplates](sfcustomlanguagemodeldata/phrasecountsfromtemplates.md)
  A type that can be used to construct custom language model data by specifying a set of template classes and using the resuilt builder DSL to specify templates.
- [SFCustomLanguageModelData.TemplateInsertableBuilder](sfcustomlanguagemodeldata/templateinsertablebuilder.md)
  A custom parameter attribute that constructs custom language model data from closures.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/sfcustomlanguagemodeldata/phrasecount)*