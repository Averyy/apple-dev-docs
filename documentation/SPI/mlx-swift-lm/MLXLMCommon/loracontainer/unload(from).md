---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/loracontainer/unload(from:)"
framework: "mlx-swift-lm/MLXLMCommon"
---

# unload(from:)

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: method  
**Role**: Instance Method

Removes adapter layers (LoRA or DoRA) and restores the model to its original form.

## Declaration

```swift
func unload(from model: LanguageModel)
```

## Discussion

This method reverts each adapted layer to its original linear layer, if possible.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/loracontainer/unload(from:))*