# SFCustomLanguageModelData.CustomPronunciation

**Framework**: Speech  
**Kind**: struct

A term to be introduced into the speech recognition model’s vocabulary.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 1.1+

## Declaration

```swift
struct CustomPronunciation
```

#### Overview

Attempts to add terms that are already in the model’s vocabulary will be ignored. Pronunciations that use X-SAMPA symbols that are not supported will be ignored; see [`supportedPhonemes(locale:)`](sfcustomlanguagemodeldata/supportedphonemes(locale:).md) for the set of supported symbols.

## Topics

### Initializers
- [init(grapheme: String, phonemes: [String])](sfcustomlanguagemodeldata/custompronunciation/init(grapheme:phonemes:).md)
### Instance Properties
- [let grapheme: String](sfcustomlanguagemodeldata/custompronunciation/grapheme.md)
  The written representation of the term, the way it is expected to appear in transcriptions.
- [let phonemes: [String]](sfcustomlanguagemodeldata/custompronunciation/phonemes.md)
  Zero or more phonetic representations of the term, given as X-SAMPA strings.

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
- [SFCustomLanguageModelData.DataInsertableBuilder](sfcustomlanguagemodeldata/datainsertablebuilder.md)
  A custom parameter attribute that constructs custom language model data from closures.
- [SFCustomLanguageModelData.PhraseCount](sfcustomlanguagemodeldata/phrasecount.md)
  A phrase used to bias the language model, along with a weight influencing the relative strength of the bias.
- [SFCustomLanguageModelData.PhraseCountsFromTemplates](sfcustomlanguagemodeldata/phrasecountsfromtemplates.md)
  A type that can be used to construct custom language model data by specifying a set of template classes and using the resuilt builder DSL to specify templates.
- [SFCustomLanguageModelData.TemplateInsertableBuilder](sfcustomlanguagemodeldata/templateinsertablebuilder.md)
  A custom parameter attribute that constructs custom language model data from closures.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/sfcustomlanguagemodeldata/custompronunciation)*