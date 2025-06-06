# NLContextualEmbeddingKey

**Framework**: Natural Language  
**Kind**: struct

Contextual embedding keys.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.0+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
struct NLContextualEmbeddingKey
```

## Topics

### Getting embedding keys
- [static let languages: NLContextualEmbeddingKey](nlcontextualembeddingkey/languages.md)
  A key that identifies the languages in a contextual embedding.
- [static let revision: NLContextualEmbeddingKey](nlcontextualembeddingkey/revision.md)
  A key that identifies the revision for a contextual embedding.
- [static let scripts: NLContextualEmbeddingKey](nlcontextualembeddingkey/scripts.md)
  A key that identifies the scripts in a contextual embedding.
### Creating embedding keys
- [init(String)](nlcontextualembeddingkey/init(_:).md)
  Creates an embedding key with the given string.
- [init(rawValue: String)](nlcontextualembeddingkey/init(rawvalue:).md)
  Creates an embedding key with the given string as its raw value.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [class NLContextualEmbedding](nlcontextualembedding.md)
  A model that computes sequences of embedding vectors for natural language utterances.
- [struct NLScript](nlscript.md)
  The writing scripts that the Natural Language framework supports.


---

*[View on Apple Developer](https://developer.apple.com/documentation/naturallanguage/nlcontextualembeddingkey)*