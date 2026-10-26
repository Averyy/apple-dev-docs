---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/tokeniterator/state"
framework: "mlx-swift-lm/MLXLMCommon"
---

# state

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: property  
**Role**: Instance Property

Per-call model state (e.g. M-RoPE rope deltas), seeded from the initializer’s `state`, replaced by prefill, then threaded through every decode step. A caller continuing this cache later (as [`ChatSession`](../chatsession.md) does across turns) reads it back after initialization and seeds the next iterator with it.

## Declaration

```swift
var state: LMOutput.State? { get }
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/tokeniterator/state)*