---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/generatecompletioninfo/cachedprompttokencount"
framework: "mlx-swift-lm/MLXLMCommon"
---

# cachedPromptTokenCount

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: property  
**Role**: Instance Property

The number of prompt tokens served by a reused KV-cache prefix instead of being prefilled, or `0` when the whole prompt was prefilled.

## Declaration

```swift
var cachedPromptTokenCount: Int { get }
```

## Discussion

Only a cache-owning caller can know this: the generation loop receives an already narrowed prompt and has no notion of a prompt cache. [`ChatSession`](../chatsession.md) attributes it from its cache reuse decision.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/generatecompletioninfo/cachedprompttokencount)*