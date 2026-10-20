# SFCustomLanguageModelData.PhraseCountGenerator

**Framework**: Speech  
**Kind**: class  
**Role**: Class

Abstract base class defining the interface for classes that generate `PhraseCount` via an iterator.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.1+

## Declaration

```swift
class PhraseCountGenerator
```

## Topics

### Protocol requirements
- [init()](./phrasecountgenerator/init%28%29.md)
- [SFCustomLanguageModelData.PhraseCountGenerator.Iterator](./phrasecountgenerator/iterator.md)

## Relationships

### Inherited By
- [SFCustomLanguageModelData.TemplatePhraseCountGenerator](./templatephrasecountgenerator.md)
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
- [SFCustomLanguageModelData.TemplatePhraseCountGenerator](./templatephrasecountgenerator.md)
  A `PhraseCountGenerator` that produces `PhraseCount` values based on templates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/sfcustomlanguagemodeldata/phrasecountgenerator)*