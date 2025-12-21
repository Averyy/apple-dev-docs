# SFCustomLanguageModelData.PhraseCountGenerator

**Framework**: Speech  
**Kind**: class

Abstract base class defining the interface for classes that generate `PhraseCount` via an iterator.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 1.1+

## Declaration

```swift
class PhraseCountGenerator
```

## Topics

### Protocol requirements
- [init()](sfcustomlanguagemodeldata/phrasecountgenerator/init.md)
- [SFCustomLanguageModelData.PhraseCountGenerator.Iterator](sfcustomlanguagemodeldata/phrasecountgenerator/iterator.md)

## Relationships

### Inherited By
- [SFCustomLanguageModelData.TemplatePhraseCountGenerator](sfcustomlanguagemodeldata/templatephrasecountgenerator.md)
### Conforms To
- [AsyncSequence](../Swift/AsyncSequence.md)
- [DataInsertable](datainsertable.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)

## See Also

- [func insert(phraseCountGenerator: SFCustomLanguageModelData.PhraseCountGenerator)](sfcustomlanguagemodeldata/insert(phrasecountgenerator:).md)
  Add a stream of samples to the body of training data.
- [SFCustomLanguageModelData.TemplatePhraseCountGenerator](sfcustomlanguagemodeldata/templatephrasecountgenerator.md)
  A `PhraseCountGenerator` that produces `PhraseCount` values based on templates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/sfcustomlanguagemodeldata/phrasecountgenerator)*