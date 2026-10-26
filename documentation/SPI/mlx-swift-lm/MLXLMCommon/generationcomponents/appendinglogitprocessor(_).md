---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/generationcomponents/appendinglogitprocessor(_:)"
framework: "mlx-swift-lm/MLXLMCommon"
---

# appendingLogitProcessor(_:)

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: method  
**Role**: Instance Method

Return a copy with another custom [`LogitProcessor`](../logitprocessor.md) appended.

## Declaration

```swift
func appendingLogitProcessor(_ factory: @escaping @Sendable () -> any LogitProcessor) -> GenerationComponents
```

#### Discussion

Processors are applied in insertion order. The returned component keeps factories—not processor instances—so every generation receives a fresh stateful chain. This is the generic composition primitive used by higher-level features such as [`applyingThinkingBudget(_:reasoning:tokenizer:diagnosticHandler:)`](./applyingthinkingbudget%28_,reasoning,tokenizer,diagnostichandler%29.md).


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/generationcomponents/appendinglogitprocessor(_:))*