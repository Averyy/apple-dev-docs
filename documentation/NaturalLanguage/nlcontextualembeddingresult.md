# NLContextualEmbeddingResult

**Framework**: Natural Language  
**Kind**: class  
**Role**: Class

An object that represents the embedding vector result from applying a contextual embedding to a string.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
class NLContextualEmbeddingResult
```

```objc
@interface NLContextualEmbeddingResult : NSObject
```

## Overview

This object returns embeddings at the subword level, meaning a single word may generate multiple vectors, especially for rare or complex terms. If you need to work with whole-word embeddings or create single representations for entire text inputs, pool or combine subword vectors.

## Topics

### Inspecting the result
- [var language: NLLanguage](./nlcontextualembeddingresult/language.md)
  The language that the framework identified or used when processing the input string.
- [var sequenceLength: Int](./nlcontextualembeddingresult/sequencelength.md)
  The number of embedding vectors the request generates.
- [var string: String](./nlcontextualembeddingresult/string.md)
  A copy of the input string used to generate the embedding vectors.
### Enumerating the vectors
- [func enumerateTokenVectors(in: Range<String.Index>, using: ([Double], Range<String.Index>) -> Bool)](./nlcontextualembeddingresult/enumeratetokenvectors%28in,using%29.md)
  Iterates over the embedding vectors corresponding to the subword tokens within the specified range of the input string.
- [func tokenVector(at: String.Index) -> ([Double], Range<String.Index>)?](./nlcontextualembeddingresult/tokenvector%28at%29.md)
  Gets a token vector at the index you specify.
- [- enumerateTokenVectorsInRange:usingBlock:](./nlcontextualembeddingresult/enumeratetokenvectorsinrange_usingblock_.md)
  Iterates over the embedding vectors corresponding to the subword tokens within the specified range of the input string.
- [- tokenVectorAtIndex:tokenRange:](./nlcontextualembeddingresult/tokenvectoratindex_tokenrange_.md)
  Returns a token vector at the specified character index.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Applying an embedding
- [func embeddingResult(for: String, language: NLLanguage?) throws -> NLContextualEmbeddingResult](./nlcontextualembedding/embeddingresult%28for,language%29.md)
  Applies an embedding to a string and obtains the resulting embedding vectors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/naturallanguage/nlcontextualembeddingresult)*