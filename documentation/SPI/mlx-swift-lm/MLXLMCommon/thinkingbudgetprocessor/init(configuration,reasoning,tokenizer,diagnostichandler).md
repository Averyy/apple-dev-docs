---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/thinkingbudgetprocessor/init(configuration:reasoning:tokenizer:diagnostichandler:)"
framework: "mlx-swift-lm/MLXLMCommon"
---

# init(configuration:reasoning:tokenizer:diagnosticHandler:)

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: init  
**Role**: Initializer

Creates a processor for direct use with a token iterator.

## Declaration

```swift
init(configuration: ThinkingBudgetConfiguration, reasoning: ReasoningConfig, tokenizer: any Tokenizer, diagnosticHandler: (@Sendable (ThinkingBudgetDiagnostic) -> Void)? = nil) throws
```

## Discussion

Prefer [`applyingThinkingBudget(_:reasoning:tokenizer:diagnosticHandler:)`](../generationcomponents/applyingthinkingbudget%28_,reasoning,tokenizer,diagnostichandler%29.md) for `ChatSession` and the parameter-driven generation APIs. That path also validates that `maxTokens` leaves transition and answer headroom.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/thinkingbudgetprocessor/init(configuration:reasoning:tokenizer:diagnostichandler:))*