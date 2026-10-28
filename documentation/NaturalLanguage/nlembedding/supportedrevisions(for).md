# supportedRevisions(for:)

**Framework**: Natural Language  
**Kind**: method  
**Role**: Type Method

Retrieves all version numbers of a word embedding for the given language.

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
class func supportedRevisions(for language: NLLanguage) -> IndexSet
```

```objc
+ (NSIndexSet *) supportedRevisionsForLanguage:(NLLanguage) language;
```

## Return Value

An index set.

## Parameters

- `language`: A language supported by the Natural Language framework.

## See Also

### Checking for Natural Language support
- [class func currentRevision(for: NLLanguage) -> Int](./currentrevision%28for%29.md)
  Retrieves the current version of a word embedding for the given language.
- [class func currentSentenceEmbeddingRevision(for: NLLanguage) -> Int](./currentsentenceembeddingrevision%28for%29.md)
  Retrieves the current version of a sentence embedding for the given language.
- [class func supportedSentenceEmbeddingRevisions(for: NLLanguage) -> IndexSet](./supportedsentenceembeddingrevisions%28for%29.md)
  Retrieves all version numbers of a sentence embedding for the given language.


---

*[View on Apple Developer](https://developer.apple.com/documentation/naturallanguage/nlembedding/supportedrevisions(for:))*