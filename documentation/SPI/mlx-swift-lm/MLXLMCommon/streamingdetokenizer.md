---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/streamingdetokenizer"
framework: "mlx-swift-lm/MLXLMCommon"
---

# StreamingDetokenizer

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: protocol  
**Role**: Protocol

Decodes one generated sequence. Preserve special tokens for downstream protocol parsing. `next()` returns available text, or nil until more tokens arrive. Custom implementations should emit stable text, holding incomplete bytes or context-dependent suffixes as needed.

## Declaration

```swift
protocol StreamingDetokenizer : IteratorProtocol where Self.Element == String
```

## Topics

### Instance Methods
- [func append(token: Int)](./streamingdetokenizer/append%28token%29.md)
- [func finish() -> String?](./streamingdetokenizer/finish%28%29.md)
  Ends the sequence and returns all remaining text, including any unread output. Call after the last token and before finishing downstream parsers. Repeated calls return nil. Create a new decoder before appending another sequence.

## Relationships

### Inherits From
- Swift.IteratorProtocol
### Conforming Types
- [NaiveStreamingDetokenizer](./naivestreamingdetokenizer.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/streamingdetokenizer)*