---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/reasoningpromptstrategy/additionalcontext(forthinkingenabled:)"
framework: "mlx-swift-lm/MLXLMCommon"
---

# additionalContext(forThinkingEnabled:)

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: method  
**Role**: Instance Method

Maps a “thinking enabled” preference to the chat-template `additionalContext` it implies.

## Declaration

```swift
func additionalContext(forThinkingEnabled thinkingEnabled: Bool?) throws -> [String : any Sendable]?
```

## Return Value

The `additionalContext` to merge into the rendered prompt, or `nil` when no context needs to be injected.

## Discussion

> **Throws**: [`ReasoningError.cannotDisableReasoning`](../reasoningerror/cannotdisablereasoning.md) when `false` is requested on a non-suppressible strategy ([`ReasoningPromptStrategy.alwaysOn`](./alwayson.md) or [`ReasoningPromptStrategy.none`](./none.md)).

## Parameters

- `thinkingEnabled`: `true` / `false` to force thinking on / off, `nil` when the caller expressed no preference.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/reasoningpromptstrategy/additionalcontext(forthinkingenabled:))*