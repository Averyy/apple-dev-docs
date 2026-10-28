---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/qwenreasoningprotocol/qwen3"
framework: "mlx-swift-lm/MLXLMCommon"
---

# qwen3

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: property  
**Role**: Type Property

The original hybrid Qwen3 protocol and its published budget transition.

## Declaration

```swift
static let qwen3: ReasoningConfig
```

## Discussion

The exact leading space after the two newlines is part of Qwen’s `early_stopping_text`. Keeping this adapter family-specific prevents a later Qwen-derived model from inheriting the transition merely because it happens to use the same delimiters.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/qwenreasoningprotocol/qwen3)*