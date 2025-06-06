# language

**Framework**: Natural Language  
**Kind**: property

The language of the text in the word embedding.

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
var language: NLLanguage? { get }
```

## See Also

- [var dimension: Int](nlembedding/dimension.md)
  The number of dimensions in the vocabulary’s vector space.
- [var vocabularySize: Int](nlembedding/vocabularysize.md)
  The number of words in the vocabulary.
- [func contains(String) -> Bool](nlembedding/contains(_:).md)
  Requests a Boolean value that indicates whether the term is in the vocabulary.
- [func vector(for: String) -> [Double]?](nlembedding/vector(for:).md)
  Requests the vector for the given term.
- [var revision: Int](nlembedding/revision.md)
  The revision of the word embedding.


---

*[View on Apple Developer](https://developer.apple.com/documentation/naturallanguage/nlembedding/language)*