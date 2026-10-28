---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/reasoningbudgettransition"
framework: "mlx-swift-lm/MLXLMCommon"
---

# ReasoningBudgetTransition

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: struct  
**Role**: Structure

A model-protocol transition used when a reasoning budget is exhausted.

## Declaration

```swift
struct ReasoningBudgetTransition
```

## Overview

The value is model-agnostic: model-family adapters provide the actual text. Models without a validated transition leave [`budgetTransition`](./reasoningconfig/budgettransition.md) unset, while applications can opt in through [`transitionOverride`](./thinkingbudgetconfiguration/transitionoverride.md).

## Topics

### Initializers
- [init(beforeEndDelimiter: String, afterEndDelimiter: String)](./reasoningbudgettransition/init%28beforeenddelimiter,afterenddelimiter%29.md)
### Instance Properties
- [var afterEndDelimiter: String](./reasoningbudgettransition/afterenddelimiter.md)
  Text forced immediately after [`endDelimiter`](./reasoningconfig/enddelimiter.md).
- [var beforeEndDelimiter: String](./reasoningbudgettransition/beforeenddelimiter.md)
  Text forced immediately before [`endDelimiter`](./reasoningconfig/enddelimiter.md).
### Type Properties
- [static let immediate: ReasoningBudgetTransition](./reasoningbudgettransition/immediate.md)
  Close the reasoning span with no additional model-specific text.
### Default Implementations
- [Equatable Implementations](./reasoningbudgettransition/equatable-implementations.md)

## Relationships

### Conforms To
- Swift.Equatable
- Swift.Sendable
- Swift.SendableMetatype


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/reasoningbudgettransition)*