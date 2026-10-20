# init(contentsOf:)

**Framework**: Natural Language  
**Kind**: init  
**Role**: Initializer

Creates a word embedding from a model file.

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
convenience init(contentsOf url: URL) throws
```

```objc
+ (instancetype) embeddingWithContentsOfURL:(NSURL *) url error:(NSError **) error;
```

#### Discussion

Use this initializer to create a word embedding from an `.mlmodel` file saved by Create ML’s [`MLWordEmbedding`](../../CreateML/mlwordembedding.md).

## Parameters

- `url`: The location of the .`mlmodel` file that contains a word embedding.

## See Also

### Creating a word embedding
- [class func wordEmbedding(for: NLLanguage) -> NLEmbedding?](./wordembedding%28for%29.md)
  Retrieves a word embedding for a given language.
- [class func wordEmbedding(for: NLLanguage, revision: Int) -> NLEmbedding?](./wordembedding%28for,revision%29.md)
  Retrieves a word embedding for a given language and revision.


---

*[View on Apple Developer](https://developer.apple.com/documentation/naturallanguage/nlembedding/init(contentsof:))*