---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/streamingdetokenizer/finish()"
framework: "mlx-swift-lm/MLXLMCommon"
---

# finish()

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Ends the sequence and returns all remaining text, including any unread output. Call after the last token and before finishing downstream parsers. Repeated calls return nil. Create a new decoder before appending another sequence.

## Declaration

```swift
mutating func finish() -> String?
```

## Mentions

- [Using mlx-swift-lm](../using.md)

## Default Implementations

### StreamingDetokenizer Implementations
- [func finish() -> String?](./finish%28%29-6ih6o.md)
  Preserves the legacy behavior for decoders without a final flush operation.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/streamingdetokenizer/finish())*