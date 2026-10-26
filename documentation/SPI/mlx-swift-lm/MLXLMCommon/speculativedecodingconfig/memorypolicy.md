---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/speculativedecodingconfig/memorypolicy"
framework: "mlx-swift-lm/MLXLMCommon"
---

# memoryPolicy

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: property  
**Role**: Instance Property

Optional memory policy used to decide whether auxiliary-model speculation should run. Pass `.recommendedWorkingSet` to fall back to regular generation when the combined main and draft model parameters exceed the recommended working set.

## Declaration

```swift
let memoryPolicy: SpeculativeDecodingMemoryPolicy?
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/speculativedecodingconfig/memorypolicy)*