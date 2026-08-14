# SFCustomLanguageModelData.PhraseCount

**Framework**: Speech  
**Kind**: struct

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
- [init(phrase: String, count: Int)](sfcustomlanguagemodeldata/phrasecount/init(phrase:count:).md)
### Inspecting the weighted phrase
- [let count: Int](sfcustomlanguagemodeldata/phrasecount/count.md)
- [let phrase: String](sfcustomlanguagemodeldata/phrasecount/phrase.md)

## Relationships

### Conforms To
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [DataInsertable](datainsertable.md)
- [Decodable](../swift/decodable.md)
- [Encodable](../swift/encodable.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [func insert(phraseCount: SFCustomLanguageModelData.PhraseCount)](sfcustomlanguagemodeldata/insert(phrasecount:).md)
  Add a sample to the body of training data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/sfcustomlanguagemodeldata/phrasecount)*