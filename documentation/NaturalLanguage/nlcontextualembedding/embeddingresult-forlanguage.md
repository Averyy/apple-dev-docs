# embeddingResult(for:language:)

**Framework**: Natural Language  
**Kind**: method

Applies an embedding to a string and obtains the resulting embedding vectors.

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
func embeddingResult(for string: String, language: NLLanguage?) throws -> NLContextualEmbeddingResult
```

#### Return Value

An embedding result.

#### Discussion

If the language of the string is unknown, the framework infers it from the string you specify.

## Parameters

- `string`: The string to apply an embedding to.
- `language`: The language of the string.

## See Also

- [class NLContextualEmbeddingResult](nlcontextualembeddingresult.md)
  An object that represents the embedding vector result from applying a contextual embedding to a string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/naturallanguage/nlcontextualembedding/embeddingresult(for:language:))*