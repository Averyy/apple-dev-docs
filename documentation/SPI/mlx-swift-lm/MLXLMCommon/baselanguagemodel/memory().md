---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/baselanguagemodel/memory()"
framework: "mlx-swift-lm/MLXLMCommon"
---

# memory()

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: method  
**Role**: Instance Method

Measure the buffers held by the model and its loaded on-demand components.

## Declaration

```swift
func memory() throws -> ModelMemory
```

## Discussion

Models from the model factories are evaluated before they are returned, so this succeeds right after loading.

> **Throws**: An MLX error if a tensor has never been evaluated.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/baselanguagemodel/memory())*