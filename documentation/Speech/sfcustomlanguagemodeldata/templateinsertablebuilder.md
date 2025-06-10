# SFCustomLanguageModelData.TemplateInsertableBuilder

**Framework**: Speech  
**Kind**: struct

A custom parameter attribute that constructs custom language model data from closures.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 1.1+

## Declaration

```swift
@resultBuilder
struct TemplateInsertableBuilder
```

#### Overview

Phrase counts can be generated manually by providing an exact phrase and weight (e.g. “Play the Albin counter gambit”) or from templates (e.g. “Move my <piece> to <square>”). Templates themselves can be constructed manually, or using the result builder DSL. This type supports the latter.

## Topics

### Type Methods
- [static func buildArray([any TemplateInsertable]) -> any TemplateInsertable](sfcustomlanguagemodeldata/templateinsertablebuilder/buildarray(_:).md)
  Enables support for `for..in` loops.
- [static func buildBlock(any TemplateInsertable...) -> any TemplateInsertable](sfcustomlanguagemodeldata/templateinsertablebuilder/buildblock(_:).md)
  Combines statement blocks into a single product.
- [static func buildEither(first: any TemplateInsertable) -> any TemplateInsertable](sfcustomlanguagemodeldata/templateinsertablebuilder/buildeither(first:).md)
  Enables support for `if-else` and `switch` constructs.
- [static func buildEither(second: any TemplateInsertable) -> any TemplateInsertable](sfcustomlanguagemodeldata/templateinsertablebuilder/buildeither(second:).md)
  Enables support for `if-else` and `switch` constructs.
- [static func buildOptional((any TemplateInsertable)?) -> any TemplateInsertable](sfcustomlanguagemodeldata/templateinsertablebuilder/buildoptional(_:).md)
  Enables support for `if` statements that do not have an `else` clause.

## See Also

- [SFCustomLanguageModelData.CompoundTemplate](sfcustomlanguagemodeldata/compoundtemplate.md)
  A class supporting the custom language model training data result builder. You are not intended to use this directly.
- [SFCustomLanguageModelData.CustomPronunciation](sfcustomlanguagemodeldata/custompronunciation.md)
  A term to be introduced into the speech recognition model’s vocabulary.
- [SFCustomLanguageModelData.DataInsertableBuilder](sfcustomlanguagemodeldata/datainsertablebuilder.md)
  A custom parameter attribute that constructs custom language model data from closures.
- [SFCustomLanguageModelData.PhraseCount](sfcustomlanguagemodeldata/phrasecount.md)
  A phrase used to bias the language model, along with a weight influencing the relative strength of the bias.
- [SFCustomLanguageModelData.PhraseCountsFromTemplates](sfcustomlanguagemodeldata/phrasecountsfromtemplates.md)
  A type that can be used to construct custom language model data by specifying a set of template classes and using the resuilt builder DSL to specify templates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/sfcustomlanguagemodeldata/templateinsertablebuilder)*