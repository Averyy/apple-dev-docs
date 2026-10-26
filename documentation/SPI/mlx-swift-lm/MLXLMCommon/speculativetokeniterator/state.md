---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/speculativetokeniterator/state"
framework: "mlx-swift-lm/MLXLMCommon"
---

# state

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: property  
**Role**: Instance Property

Model state carried by the main model, as [`state`](../tokeniterator/state.md).

## Declaration

```swift
var state: LMOutput.State? { get }
```

#### Discussion

Seeded from `mainState` and updated by prefill and each verification pass. Read it from the same iterator value you generate with: this is a struct, so a copy would not observe later mutations.

> **Note**: A rejected proposal trims KV rows, so only state a decode step does not rewrite survives speculation. The vision models’ M-RoPE anchors qualify — they position from the cache offset, which the same trim rewinds.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/speculativetokeniterator/state)*