---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/reasoningtokencollector/ingest(_:)"
framework: "mlx-swift-lm/MLXLMCommon"
---

# ingest(_:)

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: method  
**Role**: Instance Method

Ingest one generated token: append it to [`reasoningTokenIDs`](./reasoningtokenids.md), advance the detokenizer, and return the routed segments (forward these to the channel). Returns an empty array when the token only advanced an incomplete multibyte character or a partial delimiter held back across the chunk boundary.

## Declaration

```swift
mutating func ingest(_ token: Int) -> [ReasoningEventEmitter.Segment]
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/reasoningtokencollector/ingest(_:))*