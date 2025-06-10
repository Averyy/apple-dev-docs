# SFCustomLanguageModelData.TemplatePhraseCountGenerator

**Framework**: Speech  
**Kind**: class

A `PhraseCountGenerator` that produces `PhraseCount` values based on templates.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 1.1+

## Declaration

```swift
class TemplatePhraseCountGenerator
```

## Topics

### Classes
- [SFCustomLanguageModelData.TemplatePhraseCountGenerator.Iterator](sfcustomlanguagemodeldata/templatephrasecountgenerator/iterator.md)
### Structures
- [SFCustomLanguageModelData.TemplatePhraseCountGenerator.Template](sfcustomlanguagemodeldata/templatephrasecountgenerator/template.md)
### Operators
- [static func == (SFCustomLanguageModelData.TemplatePhraseCountGenerator, SFCustomLanguageModelData.TemplatePhraseCountGenerator) -> Bool](sfcustomlanguagemodeldata/templatephrasecountgenerator/==(_:_:).md)
### Initializers
- [init()](sfcustomlanguagemodeldata/templatephrasecountgenerator/init.md)
- [init(from: any Decoder) throws](sfcustomlanguagemodeldata/templatephrasecountgenerator/init(from:).md)
### Instance Methods
- [func define(className: String, values: [String])](sfcustomlanguagemodeldata/templatephrasecountgenerator/define(classname:values:).md)
  Define a class of tokens to be used in template strings.
- [func hash(into: inout Hasher)](sfcustomlanguagemodeldata/templatephrasecountgenerator/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
- [func insert(template: String, count: Int)](sfcustomlanguagemodeldata/templatephrasecountgenerator/insert(template:count:).md)
  Add a template to be used to generate data samples.
- [func makeAsyncIterator() -> SFCustomLanguageModelData.PhraseCountGenerator.Iterator](sfcustomlanguagemodeldata/templatephrasecountgenerator/makeasynciterator.md)

## Relationships

### Inherits From
- [SFCustomLanguageModelData.PhraseCountGenerator](sfcustomlanguagemodeldata/phrasecountgenerator.md)
### Conforms To
- [AsyncSequence](../Swift/AsyncSequence.md)
- [DataInsertable](datainsertable.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)

## See Also

- [SFCustomLanguageModelData.PhraseCountGenerator](sfcustomlanguagemodeldata/phrasecountgenerator.md)
  Abstract base class defining the interface for classes that generate `PhraseCount` via an iterator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/sfcustomlanguagemodeldata/templatephrasecountgenerator)*