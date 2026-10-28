---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/reasoningtokencollector/shouldstopafterreasoning"
framework: "mlx-swift-lm/MLXLMCommon"
---

# shouldStopAfterReasoning

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: property  
**Role**: Instance Property

Whether a reasoning span has closed — the Phase 1 → Phase 2 boundary.

## Declaration

```swift
var shouldStopAfterReasoning: Bool { get }
```

## Discussion

Latches on the FIRST close (a later stray `<think>` re-opens the emitter, but the caller has already stopped). Crucially this detects an empty `<think></think>` that opens and closes within a single decoded chunk, which sampling [`isInsideReasoning`](./isinsidereasoning.md) after `ingest` cannot.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/reasoningtokencollector/shouldstopafterreasoning)*