---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/reasoningeventemitter/finalize()"
framework: "mlx-swift-lm/MLXLMCommon"
---

# finalize()

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: method  
**Role**: Instance Method

Flushes any held-back text at end of generation.

## Declaration

```swift
mutating func finalize() -> [Segment]
```

#### Discussion

If the stream ends mid-reasoning (no closing delimiter ever arrived — e.g. a primed model that hit `maxTokens`), the leftover is emitted as `.reasoning`.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/reasoningeventemitter/finalize())*