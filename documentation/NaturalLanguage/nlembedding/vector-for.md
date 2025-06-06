# vector(for:)

**Framework**: Natural Language  
**Kind**: method

Requests the vector for the given term.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
@nonobjc
func vector(for string: String) -> [Double]?
```

## Mentions

- [Finding similarities between pieces of text](finding-similarities-between-pieces-of-text.md)

#### Return Value

A vector represented as an array of doubles if present in the word embedding, otherwise `nil`.

## Parameters

- `string`: The term to find in the word embedding.

## See Also

- [var dimension: Int](nlembedding/dimension.md)
  The number of dimensions in the vocabulary’s vector space.
- [var vocabularySize: Int](nlembedding/vocabularysize.md)
  The number of words in the vocabulary.
- [var language: NLLanguage?](nlembedding/language.md)
  The language of the text in the word embedding.
- [func contains(String) -> Bool](nlembedding/contains(_:).md)
  Requests a Boolean value that indicates whether the term is in the vocabulary.
- [var revision: Int](nlembedding/revision.md)
  The revision of the word embedding.


---

*[View on Apple Developer](https://developer.apple.com/documentation/naturallanguage/nlembedding/vector(for:))*