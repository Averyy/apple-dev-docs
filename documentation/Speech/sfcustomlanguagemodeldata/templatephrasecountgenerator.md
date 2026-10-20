# SFCustomLanguageModelData.TemplatePhraseCountGenerator

**Framework**: Speech  
**Kind**: class  
**Role**: Class

A `PhraseCountGenerator` that produces `PhraseCount` values based on templates.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.1+

## Declaration

```swift
class TemplatePhraseCountGenerator
```

## Topics

### Defining template tokens
- [func define(className: String, values: [String])](./templatephrasecountgenerator/define%28classname,values%29.md)
  Define a class of tokens to be used in template strings.
### Adding a template
- [func insert(template: String, count: Int)](./templatephrasecountgenerator/insert%28template,count%29.md)
  Add a template to be used to generate data samples.
- [SFCustomLanguageModelData.TemplatePhraseCountGenerator.Template](./templatephrasecountgenerator/template.md)
### Classes
- [SFCustomLanguageModelData.TemplatePhraseCountGenerator.Iterator](./templatephrasecountgenerator/iterator.md)
### Operators
- [static func == (SFCustomLanguageModelData.TemplatePhraseCountGenerator, SFCustomLanguageModelData.TemplatePhraseCountGenerator) -> Bool](./templatephrasecountgenerator/eqeq%28_,_%29.md)
### Initializers
- [init()](./templatephrasecountgenerator/init%28%29.md)
- [init(from: any Decoder) throws](./templatephrasecountgenerator/init%28from%29.md)
### Instance Methods
- [func hash(into: inout Hasher)](./templatephrasecountgenerator/hash%28into%29.md)
  Hashes the essential components of this value by feeding them into the given hasher.
- [func makeAsyncIterator() -> SFCustomLanguageModelData.PhraseCountGenerator.Iterator](./templatephrasecountgenerator/makeasynciterator%28%29.md)

## Relationships

### Inherits From
- [SFCustomLanguageModelData.PhraseCountGenerator](./phrasecountgenerator.md)
### Conforms To
- [AsyncSequence](../../Swift/asyncsequence.md)
- [DataInsertable](../datainsertable.md)
- [Decodable](../../Swift/decodable.md)
- [Encodable](../../Swift/encodable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)

## See Also

### Adding parameterized sample data with a generator
- [func insert(phraseCountGenerator: SFCustomLanguageModelData.PhraseCountGenerator)](./insert%28phrasecountgenerator%29.md)
  Add a stream of samples to the body of training data.
- [SFCustomLanguageModelData.PhraseCountGenerator](./phrasecountgenerator.md)
  Abstract base class defining the interface for classes that generate `PhraseCount` via an iterator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/sfcustomlanguagemodeldata/templatephrasecountgenerator)*