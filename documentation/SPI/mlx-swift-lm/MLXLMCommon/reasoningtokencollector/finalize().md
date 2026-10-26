---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/reasoningtokencollector/finalize()"
framework: "mlx-swift-lm/MLXLMCommon"
---

# finalize()

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: method  
**Role**: Instance Method

Flush any held-back text at end of generation. If the stream ended mid-reasoning (no close ever arrived), the leftover routes as `.reasoning`.

## Declaration

```swift
mutating func finalize() -> [ReasoningEventEmitter.Segment]
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/reasoningtokencollector/finalize())*