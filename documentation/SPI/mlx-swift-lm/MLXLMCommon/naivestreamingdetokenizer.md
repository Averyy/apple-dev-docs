---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/naivestreamingdetokenizer"
framework: "mlx-swift-lm/MLXLMCommon"
---

# NaiveStreamingDetokenizer

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: struct  
**Role**: Structure

## Declaration

```swift
struct NaiveStreamingDetokenizer
```

## Mentions

- [Using mlx-swift-lm](./using.md)

## Topics

### Initializers
- [init(tokenizer: any Tokenizer)](./naivestreamingdetokenizer/init%28tokenizer%29.md)
### Instance Methods
- [func append(token: Int)](./naivestreamingdetokenizer/append%28token%29.md)
- [func finish() -> String?](./naivestreamingdetokenizer/finish%28%29.md)
  Flushes remaining text, including replacement characters for incomplete bytes. Repeated calls return nil. Create a new detokenizer for the next sequence.
- [func next() -> String?](./naivestreamingdetokenizer/next%28%29.md)
### Default Implementations
- [StreamingDetokenizer Implementations](./naivestreamingdetokenizer/streamingdetokenizer-implementations.md)

## Relationships

### Conforms To
- [StreamingDetokenizer](./streamingdetokenizer.md)
- Swift.IteratorProtocol


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/naivestreamingdetokenizer)*