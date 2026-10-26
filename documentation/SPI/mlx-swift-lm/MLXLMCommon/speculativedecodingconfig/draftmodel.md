---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/speculativedecodingconfig/draftmodel"
framework: "mlx-swift-lm/MLXLMCommon"
---

# draftModel

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: property  
**Role**: Instance Property

The lightweight model used to propose candidate tokens, when it was provided eagerly.

## Declaration

```swift
var draftModel: ModelContainer? { get }
```

#### Discussion

Configurations initialized with a loader closure return `nil` because the draft model is loaded asynchronously by [`ChatSession`](../chatsession.md) only when speculation is admitted by the memory policy.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/speculativedecodingconfig/draftmodel)*