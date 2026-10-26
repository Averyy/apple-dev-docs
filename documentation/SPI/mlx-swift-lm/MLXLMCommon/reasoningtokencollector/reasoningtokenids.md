---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/reasoningtokencollector/reasoningtokenids"
framework: "mlx-swift-lm/MLXLMCommon"
---

# reasoningTokenIDs

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: property  
**Role**: Instance Property

Every token ingested so far, in order. Phase 2 prefills the model’s prompt + these to continue from the completed reasoning span.

## Declaration

```swift
var reasoningTokenIDs: [Int] { get }
```

#### Discussion

Because the caller stops ingesting once [`shouldStopAfterReasoning`](./shouldstopafterreasoning.md) is true, this ends at the closing-delimiter token. The *opening* delimiter is included when the model generates it (non-primed families, e.g. Qwen3); for primed families (e.g. DeepSeek-R1) the opening `<think>` lives in the prompt instead, so it is already part of the Phase-2 prefix.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/reasoningtokencollector/reasoningtokenids)*