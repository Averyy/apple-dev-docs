# SFCustomLanguageModelData.TemplatePhraseCountGenerator

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
class TemplatePhraseCountGenerator
```

## Topics

### Initializers
- [init()](sfcustomlanguagemodeldata/templatephrasecountgenerator/init.md)
- [init(from: any Decoder) throws](sfcustomlanguagemodeldata/templatephrasecountgenerator/init(from:).md)
### Instance Methods
- [func define(className: String, values: [String])](sfcustomlanguagemodeldata/templatephrasecountgenerator/define(classname:values:).md)
- [func hash(into: inout Hasher)](sfcustomlanguagemodeldata/templatephrasecountgenerator/hash(into:).md)
- [func insert(template: String, count: Int)](sfcustomlanguagemodeldata/templatephrasecountgenerator/insert(template:count:).md)
- [func makeAsyncIterator() -> SFCustomLanguageModelData.PhraseCountGenerator.Iterator](sfcustomlanguagemodeldata/templatephrasecountgenerator/makeasynciterator.md)
### Operator Functions
- [static func == (SFCustomLanguageModelData.TemplatePhraseCountGenerator, SFCustomLanguageModelData.TemplatePhraseCountGenerator) -> Bool](sfcustomlanguagemodeldata/templatephrasecountgenerator/==(_:_:).md)
### Classes
- [SFCustomLanguageModelData.TemplatePhraseCountGenerator.Iterator](sfcustomlanguagemodeldata/templatephrasecountgenerator/iterator.md)
### Structures
- [SFCustomLanguageModelData.TemplatePhraseCountGenerator.Template](sfcustomlanguagemodeldata/templatephrasecountgenerator/template.md)

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/sfcustomlanguagemodeldata/templatephrasecountgenerator)*