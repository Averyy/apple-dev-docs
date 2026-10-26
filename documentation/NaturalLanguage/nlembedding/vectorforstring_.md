# vectorForString:

**Framework**: Natural Language  
**Kind**: method  
**Role**: Instance Method

Requests the vector for the given term.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```objc
- (NSArray<NSNumber *> *) vectorForString:(NSString *) string;
```

#### Return Value

A vector represented as an array of doubles if present in the word embedding, otherwise `nil`.

## Parameters

- `string`: The term to find in the word embedding.

## See Also

### Inspecting the vocabulary of an embedding
- [var dimension: Int](./dimension.md)
  The number of dimensions in the vocabulary’s vector space.
- [var vocabularySize: Int](./vocabularysize.md)
  The number of words in the vocabulary.
- [var language: NLLanguage?](./language.md)
  The language of the text in the word embedding.
- [func contains(String) -> Bool](./contains%28_%29.md)
  Requests a Boolean value that indicates whether the term is in the vocabulary.
- [- getVector:forString:](./getvector_forstring_.md)
  Copies a vector into the given a pointer to a float array.
- [var revision: Int](./revision.md)
  The revision of the word embedding.


---

*[View on Apple Developer](https://developer.apple.com/documentation/naturallanguage/nlembedding/vectorforstring:)*