---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/reasoningpromptstrategy"
framework: "mlx-swift-lm/MLXLMCommon"
---

# ReasoningPromptStrategy

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: enum  
**Role**: Enumeration

How a model’s “thinking on / off” preference is expressed to its chat template.

## Declaration

```swift
enum ReasoningPromptStrategy
```

## Overview

`MLXLMCommon` deliberately does not depend on `FoundationModels`, so this takes a plain `Bool?` (think on / off / unspecified) rather than a `FoundationModels` reasoning level. The level → `Bool?` mapping lives in the `MLXFoundationModels` layer, mirroring how [`ToolCallFormat`](./toolcallformat.md) carries no `FoundationModels`-typed mirror.

## Topics

### Enumeration Cases
- [ReasoningPromptStrategy.alwaysOn](./reasoningpromptstrategy/alwayson.md)
  The model always reasons and cannot be turned off (e.g. DeepSeek-R1).
- [ReasoningPromptStrategy.none](./reasoningpromptstrategy/none.md)
  The model has no prompt-level thinking control.
- [ReasoningPromptStrategy.templateFlag(key:defaultOn:)](./reasoningpromptstrategy/templateflag%28key,defaulton%29.md)
  Toggleable via a chat-template keyword argument (e.g. Qwen3’s `enable_thinking`). The `key` is the kwarg name; `defaultOn` is the value used when the caller expresses no preference, matching the model’s own template default.
### Instance Methods
- [func additionalContext(forThinkingEnabled: Bool?) throws -> [String : any Sendable]?](./reasoningpromptstrategy/additionalcontext%28forthinkingenabled%29.md)
  Maps a “thinking enabled” preference to the chat-template `additionalContext` it implies.
### Default Implementations
- [Equatable Implementations](./reasoningpromptstrategy/equatable-implementations.md)

## Relationships

### Conforms To
- Swift.Equatable
- Swift.Sendable
- Swift.SendableMetatype


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/reasoningpromptstrategy)*