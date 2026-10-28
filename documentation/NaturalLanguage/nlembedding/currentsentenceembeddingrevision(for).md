# currentSentenceEmbeddingRevision(for:)

**Framework**: Natural Language  
**Kind**: method  
**Role**: Type Method

Retrieves the current version of a sentence embedding for the given language.

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
class func currentSentenceEmbeddingRevision(for language: NLLanguage) -> Int
```

```objc
+ (NSUInteger) currentSentenceEmbeddingRevisionForLanguage:(NLLanguage) language;
```

## Return Value

An integer representing the current version number of a sentence embedding.

## Parameters

- `language`: A language supported by the Natural Language framework. For possible values, see [`NLLanguage`](../nllanguage.md).

## See Also

### Checking for Natural Language support
- [class func currentRevision(for: NLLanguage) -> Int](./currentrevision%28for%29.md)
  Retrieves the current version of a word embedding for the given language.
- [class func supportedRevisions(for: NLLanguage) -> IndexSet](./supportedrevisions%28for%29.md)
  Retrieves all version numbers of a word embedding for the given language.
- [class func supportedSentenceEmbeddingRevisions(for: NLLanguage) -> IndexSet](./supportedsentenceembeddingrevisions%28for%29.md)
  Retrieves all version numbers of a sentence embedding for the given language.


---

*[View on Apple Developer](https://developer.apple.com/documentation/naturallanguage/nlembedding/currentsentenceembeddingrevision(for:))*