---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/loracontainer/load(into:)"
framework: "mlx-swift-lm/MLXLMCommon"
---

# load(into:)

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: method  
**Role**: Instance Method

Applies adapter modules (LoRA or DoRA) to the given model.

## Declaration

```swift
func load(into model: LanguageModel) throws
```

## Discussion

This method replaces target layers in the model with corresponding adapter layers based on the configuration. It also loads adapter-specific weights into the model. Replacement layers preserve the model’s current training or evaluation mode. Models placed in a [`ModelContext`](../modelcontext.md) are in evaluation mode by default.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/loracontainer/load(into:))*