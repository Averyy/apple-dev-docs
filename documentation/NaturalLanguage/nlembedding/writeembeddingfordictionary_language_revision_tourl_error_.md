# writeEmbeddingForDictionary:language:revision:toURL:error:

**Framework**: Natural Language  
**Kind**: method  
**Role**: Type Method

Exports the word embedding contained within a Core ML model file at the given URL.

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
+ (BOOL) writeEmbeddingForDictionary:(NSDictionary<NSString *,NSArray<NSNumber *> *> *) dictionary language:(NLLanguage) language revision:(NSUInteger) revision toURL:(NSURL *) url error:(NSError **) error;
```

## Parameters

- `dictionary`: A dictionary of terms, and their vectors, which are represented by an array of doubles.
- `language`: The language of the text in the word embedding.
- `revision`: The revision of the word embedding.
- `url`: The location in the file system to write the file to.


---

*[View on Apple Developer](https://developer.apple.com/documentation/naturallanguage/nlembedding/writeembeddingfordictionary:language:revision:tourl:error:)*