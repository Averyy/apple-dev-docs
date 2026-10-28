---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/thinkingbudgetconfiguration/transitionoverride"
framework: "mlx-swift-lm/MLXLMCommon"
---

# transitionOverride

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: property  
**Role**: Instance Property

Replaces the model’s [`budgetTransition`](../reasoningconfig/budgettransition.md).

## Declaration

```swift
let transitionOverride: ReasoningBudgetTransition?
```

## Discussion

Most reasoning protocols ship with no declared transition, because sharing `<think>`/`</think>` with Qwen3 does not mean a family was trained to answer from a truncated reasoning span. Supplying a transition here is how an application opts a model in anyway, after validating the behavior for its exact weights and tokenizer.

[`immediate`](../reasoningbudgettransition/immediate.md) is the conservative choice: it closes the span with the model’s own end delimiter and adds nothing else.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/thinkingbudgetconfiguration/transitionoverride)*