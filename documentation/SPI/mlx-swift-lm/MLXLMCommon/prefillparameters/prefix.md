---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/prefillparameters/prefix"
framework: "mlx-swift-lm/MLXLMCommon"
---

# prefix

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: property  
**Role**: Instance Property

Called once, before the first prefill forward, with the positions the cache already holds.

## Declaration

```swift
var prefix: (@Sendable (_ positions: Int) -> Void)?
```

#### Discussion

A prefill resumes on a reused prefix whenever the cache already represents the prompt’s leading positions, as [`ChatSession`](../chatsession.md) arranges between turns, and [`progress`](./progress.md) counts only what the prefill adds on top. This reports the other half, so a consumer tracking how full a cache is while a prompt is prefilled holds `prefix + processed`; a cold cache reports `0`. The figure is the one the turn’s [`cachedPromptTokenCount`](../generatecompletioninfo/cachedprompttokencount.md) confirms once it ends.

The closure is retained like [`progress`](./progress.md).


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/prefillparameters/prefix)*