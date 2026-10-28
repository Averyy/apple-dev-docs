# sentenceEmbedding(for:)

**Framework**: Natural Language  
**Kind**: method  
**Role**: Type Method

Retrieves a sentence embedding for a given language.

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
class func sentenceEmbedding(for language: NLLanguage) -> NLEmbedding?
```

```objc
+ (NLEmbedding *) sentenceEmbeddingForLanguage:(NLLanguage) language;
```

## Mentions

- [Finding similarities between pieces of text](../finding-similarities-between-pieces-of-text.md)

## Return Value

An [`NLEmbedding`](../nlembedding.md) if available, otherwise `nil`.

## Parameters

- `language`: The language of the sentence embedding, such as [`french`](../nllanguage/french.md). For possible values, see [`NLLanguage`](../nllanguage.md).

## See Also

### Creating a sentence embedding
- [class func sentenceEmbedding(for: NLLanguage, revision: Int) -> NLEmbedding?](./sentenceembedding%28for,revision%29.md)
  Retrieves a sentence embedding for a given language and revision.


---

*[View on Apple Developer](https://developer.apple.com/documentation/naturallanguage/nlembedding/sentenceembedding(for:))*