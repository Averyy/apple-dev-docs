# contains(_:)

**Framework**: Natural Language  
**Kind**: method

Requests a Boolean value that indicates whether the term is in the vocabulary.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
func contains(_ string: String) -> Bool
```

#### Return Value

`true` if the term is in the word embedding’s vocabulary, otherwise `false`.

## Parameters

- `string`: The term to search for in the word embedding.

## See Also

- [var dimension: Int](nlembedding/dimension.md)
  The number of dimensions in the vocabulary’s vector space.
- [var vocabularySize: Int](nlembedding/vocabularysize.md)
  The number of words in the vocabulary.
- [var language: NLLanguage?](nlembedding/language.md)
  The language of the text in the word embedding.
- [func vector(for: String) -> [Double]?](nlembedding/vector(for:).md)
  Requests the vector for the given term.
- [var revision: Int](nlembedding/revision.md)
  The revision of the word embedding.


---

*[View on Apple Developer](https://developer.apple.com/documentation/naturallanguage/nlembedding/contains(_:))*