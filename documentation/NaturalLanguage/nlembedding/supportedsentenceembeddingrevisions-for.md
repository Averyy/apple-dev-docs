# supportedSentenceEmbeddingRevisions(for:)

**Framework**: Natural Language  
**Kind**: method

Retrieves all version numbers of a sentence embedding for the given language.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
class func supportedSentenceEmbeddingRevisions(for language: NLLanguage) -> IndexSet
```

#### Return Value

An index set representing all of the supported version numbers of the sentence embedding.

## Parameters

- `language`: A language supported by the Natural Language framework. For possible values, see  .

## See Also

- [class func currentRevision(for: NLLanguage) -> Int](nlembedding/currentrevision(for:).md)
  Retrieves the current version of a word embedding for the given language.
- [class func supportedRevisions(for: NLLanguage) -> IndexSet](nlembedding/supportedrevisions(for:).md)
  Retrieves all version numbers of a word embedding for the given language.
- [class func currentSentenceEmbeddingRevision(for: NLLanguage) -> Int](nlembedding/currentsentenceembeddingrevision(for:).md)
  Retrieves the current version of a sentence embedding for the given language.


---

*[View on Apple Developer](https://developer.apple.com/documentation/naturallanguage/nlembedding/supportedsentenceembeddingrevisions(for:))*