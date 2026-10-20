# SFCustomLanguageModelData.PhraseCount

**Framework**: Speech  
**Kind**: struct  
**Role**: Structure

A phrase used to bias the language model, along with a weight influencing the relative strength of the bias.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.1+

## Declaration

```swift
struct PhraseCount
```

## Topics

### Creating a weighted phrase
- [init(phrase: String, count: Int)](./phrasecount/init%28phrase,count%29.md)
### Inspecting the weighted phrase
- [let count: Int](./phrasecount/count.md)
- [let phrase: String](./phrasecount/phrase.md)

## Relationships

### Conforms To
- [CustomStringConvertible](../../Swift/customstringconvertible.md)
- [DataInsertable](../datainsertable.md)
- [Decodable](../../Swift/decodable.md)
- [Encodable](../../Swift/encodable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Adding phrases
- [func insert(phraseCount: SFCustomLanguageModelData.PhraseCount)](./insert%28phrasecount%29.md)
  Add a sample to the body of training data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/sfcustomlanguagemodeldata/phrasecount)*