---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/cachelist/metastate"
framework: "mlx-swift-lm/MLXLMCommon"
---

# metaState

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: property  
**Role**: Instance Property

metaState format: [childCount, (className, stateCount, metaStateCount, …metaState)*]

## Declaration

```swift
override var metaState: [String] { get set }
```

## Discussion

Like Python’s CacheList.meta_state which returns [child_class_names, child_meta_states], but flattened for Swift’s [String] format.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/cachelist/metastate)*