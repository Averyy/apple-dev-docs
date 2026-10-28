# wordEmbedding(for:revision:)

**Framework**: Natural Language  
**Kind**: method  
**Role**: Type Method

Retrieves a word embedding for a given language and revision.

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
class func wordEmbedding(for language: NLLanguage, revision: Int) -> NLEmbedding?
```

```objc
+ (NLEmbedding *) wordEmbeddingForLanguage:(NLLanguage) language revision:(NSUInteger) revision;
```

## Return Value

An [`NLEmbedding`](../nlembedding.md) if available, otherwise `nil`.

## Parameters

- `language`: The language of the word embedding, such as [`french`](../nllanguage/french.md).
- `revision`: The revision of the word embedding.

## See Also

### Creating a word embedding
- [class func wordEmbedding(for: NLLanguage) -> NLEmbedding?](./wordembedding%28for%29.md)
  Retrieves a word embedding for a given language.
- [convenience init(contentsOf: URL) throws](./init%28contentsof%29.md)
  Creates a word embedding from a model file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/naturallanguage/nlembedding/wordembedding(for:revision:))*