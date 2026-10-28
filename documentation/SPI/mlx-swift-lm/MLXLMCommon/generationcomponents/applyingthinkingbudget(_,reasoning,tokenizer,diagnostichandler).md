---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/generationcomponents/applyingthinkingbudget(_:reasoning:tokenizer:diagnostichandler:)"
framework: "mlx-swift-lm/MLXLMCommon"
---

# applyingThinkingBudget(_:reasoning:tokenizer:diagnosticHandler:)

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: method  
**Role**: Instance Method

Return a copy that enforces a reasoning-token budget for every generation.

## Declaration

```swift
func applyingThinkingBudget(_ configuration: ThinkingBudgetConfiguration, reasoning: ReasoningConfig, tokenizer: any Tokenizer, diagnosticHandler: (@Sendable (ThinkingBudgetDiagnostic) -> Void)? = nil) throws -> GenerationComponents
```

## Discussion

The reasoning protocol must declare a [`ReasoningBudgetTransition`](../reasoningbudgettransition.md), or the caller must supply one via [`transitionOverride`](../thinkingbudgetconfiguration/transitionoverride.md). Unknown protocols fail during setup rather than receiving a guessed `</think>` sequence. The configured generation limit must include enough headroom for a Unicode boundary completion, the longest possible protocol transition, and the answer.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/generationcomponents/applyingthinkingbudget(_:reasoning:tokenizer:diagnostichandler:))*