---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/reasoningconfig"
framework: "mlx-swift-lm/MLXLMCommon"
---

# ReasoningConfig

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: struct  
**Role**: Structure

Describes a model’s reasoning (chain-of-thought) protocol: the delimiters that bracket its thinking in the decoded generation stream, and how thinking is toggled at prompt time.

## Declaration

```swift
struct ReasoningConfig
```

## Overview

Rides on [`ModelConfiguration`](./modelconfiguration.md) (and therefore [`ResolvedModelConfiguration`](./resolvedmodelconfiguration.md)) so it reaches generation-time code via `ModelContext.configuration`, exactly like [`ToolCallFormat`](./toolcallformat.md).

## Topics

### Initializers
- [init(startDelimiter: String, endDelimiter: String, promptStrategy: ReasoningPromptStrategy, isSpecialToken: Bool, implicitEndDelimiters: [String], budgetTransition: ReasoningBudgetTransition?)](./reasoningconfig/init%28startdelimiter,enddelimiter,promptstrategy,isspecialtoken,implicitenddelimiters,budgettransition%29.md)
### Instance Properties
- [var budgetTransition: ReasoningBudgetTransition?](./reasoningconfig/budgettransition.md)
  How this model safely transitions to its answer when a reasoning budget is exhausted, or `nil` when hard budget enforcement is unsupported.
- [var endDelimiter: String](./reasoningconfig/enddelimiter.md)
  The marker that closes a reasoning span (e.g. `</think>`).
- [var implicitEndDelimiters: [String]](./reasoningconfig/implicitenddelimiters.md)
  Markers that implicitly leave reasoning without emitting [`endDelimiter`](./reasoningconfig/enddelimiter.md).
- [var isSpecialToken: Bool](./reasoningconfig/isspecialtoken.md)
  Diagnostic only: whether [`startDelimiter`](./reasoningconfig/startdelimiter.md) is a registered special token for this model’s tokenizer. Budget enforcement compiles every boundary with the active tokenizer and does not rely on this hint.
- [var promptStrategy: ReasoningPromptStrategy](./reasoningconfig/promptstrategy.md)
  How a thinking on / off preference is expressed to the chat template.
- [var startDelimiter: String](./reasoningconfig/startdelimiter.md)
  The marker that opens a reasoning span (e.g. `<think>`).
### Type Properties
- [static let alwaysOnThinking: ReasoningConfig](./reasoningconfig/alwaysonthinking.md)
  Always-on `<think>`/`</think>` with no prompt-level off switch (DeepSeek-R1 and its distills). The protocol does not claim a known-safe hard-budget transition; applications may opt into one explicitly after validating it for their exact model and tokenizer.
- [static let thinkTagsWithEnableThinking: ReasoningConfig](./reasoningconfig/thinktagswithenablethinking.md)
  Generic `<think>`/`</think>` protocol toggled by the `enable_thinking` chat-template flag (default on).
### Default Implementations
- [Equatable Implementations](./reasoningconfig/equatable-implementations.md)

## Relationships

### Conforms To
- Swift.Equatable
- Swift.Sendable
- Swift.SendableMetatype


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/reasoningconfig)*