---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/thinkingbudgetconfiguration"
framework: "mlx-swift-lm/MLXLMCommon"
---

# ThinkingBudgetConfiguration

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: struct  
**Role**: Structure

A hard upper bound for model-selected reasoning tokens.

## Declaration

```swift
struct ThinkingBudgetConfiguration
```

#### Overview

Protocol tokens used to enter or leave reasoning are not charged to the budget. If a byte-fallback token ends mid-scalar, generation may consume the minimum additional tokens needed to complete valid Unicode before forcing the transition. Forced transition tokens still count toward [`maxTokens`](./generateparameters/maxtokens.md); callers must leave room for the transition and the final answer in their overall generation limit.

## Topics

### Initializers
- [init(maximumTokenCount: Int, minimumAnswerTokenCount: Int, transitionOverride: ReasoningBudgetTransition?) throws](./thinkingbudgetconfiguration/init%28maximumtokencount,minimumanswertokencount,transitionoverride%29.md)
### Instance Properties
- [let maximumTokenCount: Int](./thinkingbudgetconfiguration/maximumtokencount.md)
  Maximum number of model-selected tokens allowed inside a reasoning span. Zero closes a prompt-primed reasoning span before it generates content.
- [let minimumAnswerTokenCount: Int](./thinkingbudgetconfiguration/minimumanswertokencount.md)
  Tokens reserved for the final answer after the worst-case transition.
- [let transitionOverride: ReasoningBudgetTransition?](./thinkingbudgetconfiguration/transitionoverride.md)
  Replaces the model’s [`budgetTransition`](./reasoningconfig/budgettransition.md).
### Default Implementations
- [Equatable Implementations](./thinkingbudgetconfiguration/equatable-implementations.md)

## Relationships

### Conforms To
- Swift.Equatable
- Swift.Sendable
- Swift.SendableMetatype


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/thinkingbudgetconfiguration)*