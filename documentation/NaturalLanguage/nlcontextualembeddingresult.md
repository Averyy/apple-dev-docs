# NLContextualEmbeddingResult

**Framework**: Natural Language  
**Kind**: class

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

## Topics

### Inspecting the result
- [var language: NLLanguage](nlcontextualembeddingresult/language.md)
  The resulting language.
- [var sequenceLength: Int](nlcontextualembeddingresult/sequencelength.md)
  The number of embedding vectors the request generates.
- [var string: String](nlcontextualembeddingresult/string.md)
  The string value.
### Enumerating the vectors
- [func enumerateTokenVectors(in: Range<String.Index>, using: ([Double], Range<String.Index>) -> Bool)](nlcontextualembeddingresult/enumeratetokenvectors(in:using:).md)
  Iterates over the embedding vectors for the range you specify.
- [func tokenVector(at: String.Index) -> ([Double], Range<String.Index>)?](nlcontextualembeddingresult/tokenvector(at:).md)
  Gets a token vector at the index you specify.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [func embeddingResult(for: String, language: NLLanguage?) throws -> NLContextualEmbeddingResult](nlcontextualembedding/embeddingresult(for:language:).md)
  Applies an embedding to a string and obtains the resulting embedding vectors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/naturallanguage/nlcontextualembeddingresult)*