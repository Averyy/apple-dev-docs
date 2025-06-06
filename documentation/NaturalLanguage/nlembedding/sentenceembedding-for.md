# sentenceEmbedding(for:)

**Framework**: Natural Language  
**Kind**: method

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

## Mentions

- [Finding similarities between pieces of text](finding-similarities-between-pieces-of-text.md)

#### Return Value

An [`NLEmbedding`](nlembedding.md) if available, otherwise `nil`.

## Parameters

- `language`: The language of the sentence embedding, such as  . For possible values, see  .

## See Also

- [class func sentenceEmbedding(for: NLLanguage, revision: Int) -> NLEmbedding?](nlembedding/sentenceembedding(for:revision:).md)
  Retrieves a sentence embedding for a given language and revision.


---

*[View on Apple Developer](https://developer.apple.com/documentation/naturallanguage/nlembedding/sentenceembedding(for:))*