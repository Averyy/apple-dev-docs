# language

**Framework**: Natural Language  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (copy, readonly, nullable) NLLanguage language;
```

## See Also

### Inspecting the vocabulary of an embedding
- [var dimension: Int](./dimension.md)
  The number of dimensions in the vocabulary’s vector space.
- [var vocabularySize: Int](./vocabularysize.md)
  The number of words in the vocabulary.
- [func contains(String) -> Bool](./contains%28_%29.md)
  Requests a Boolean value that indicates whether the term is in the vocabulary.
- [func vector(for: String) -> [Double]?](./vector%28for%29.md)
  Requests the vector for the given term.
- [var revision: Int](./revision.md)
  The revision of the word embedding.
- [- vectorForString:](./vectorforstring_.md)
  Requests the vector for the given term.
- [- getVector:forString:](./getvector_forstring_.md)
  Copies a vector into the given a pointer to a float array.


---

*[View on Apple Developer](https://developer.apple.com/documentation/naturallanguage/nlembedding/language)*