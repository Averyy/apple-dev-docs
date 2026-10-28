---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/reasoningeventemitter/process(_:)"
framework: "mlx-swift-lm/MLXLMCommon"
---

# process(_:)

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: method  
**Role**: Instance Method

Ingests one decoded chunk and returns the segments it resolves to.

## Declaration

```swift
mutating func process(_ chunk: String) -> [Segment]
```

## Discussion

May return zero segments (e.g. the chunk only advanced a partial delimiter), or several (e.g. a chunk containing a full `<think>…</think>`).


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/reasoningeventemitter/process(_:))*