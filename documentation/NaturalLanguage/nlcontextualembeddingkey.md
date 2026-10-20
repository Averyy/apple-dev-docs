# NLContextualEmbeddingKey

**Framework**: Natural Language  
**Kind**: struct  
**Role**: Structure

This class defines properties that you can filter or search for contextual embeddings.

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

```c
typedef NSString * NLContextualEmbeddingKey;
```

#### Overview

The keys within this class provide filtering criteria that you can specify within your model. For example, you can use a defined key like [`scripts`](./nlcontextualembeddingkey/scripts.md) and search for models that use a specfic script like `Latin`.

## Topics

### Getting embedding keys
- [static let languages: NLContextualEmbeddingKey](./nlcontextualembeddingkey/languages.md)
  A key that identifies the supported languages in a contextual embedding.
- [static let revision: NLContextualEmbeddingKey](./nlcontextualembeddingkey/revision.md)
  A key that identifies the version number the contextual embedding uses.
- [static let scripts: NLContextualEmbeddingKey](./nlcontextualembeddingkey/scripts.md)
  A key that identifies the writing system that the language uses in a contextual embedding.
### Creating embedding keys
- [init(String)](./nlcontextualembeddingkey/init%28_%29.md)
  Creates an embedding key with the given string.
- [init(rawValue: String)](./nlcontextualembeddingkey/init%28rawvalue%29.md)
  Creates an embedding key with the given string as its raw value.

## Relationships

### Conforms To
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Contextual embedding
- [class NLContextualEmbedding](./nlcontextualembedding.md)
  A model that computes sequences of embedding vectors for natural language utterances.
- [struct NLScript](./nlscript.md)
  The writing scripts that the Natural Language framework supports.


---

*[View on Apple Developer](https://developer.apple.com/documentation/naturallanguage/nlcontextualembeddingkey)*