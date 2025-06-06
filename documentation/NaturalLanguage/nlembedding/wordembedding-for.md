# wordEmbedding(for:)

**Framework**: Natural Language  
**Kind**: method

Retrieves a word embedding for a given language.

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
class func wordEmbedding(for language: NLLanguage) -> NLEmbedding?
```

## Mentions

- [Finding similarities between pieces of text](finding-similarities-between-pieces-of-text.md)

#### Return Value

An [`NLEmbedding`](nlembedding.md) if available, otherwise `nil`.

## Parameters

- `language`: The language of the word embedding, such as  .

## See Also

- [class func wordEmbedding(for: NLLanguage, revision: Int) -> NLEmbedding?](nlembedding/wordembedding(for:revision:).md)
  Retrieves a word embedding for a given language and revision.
- [convenience init(contentsOf: URL) throws](nlembedding/init(contentsof:).md)
  Creates a word embedding from a model file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/naturallanguage/nlembedding/wordembedding(for:))*