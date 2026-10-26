---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxvlm/gemma4unified/suppressedtokenids"
framework: "mlx-swift-lm/MLXVLM"
---

# suppressedTokenIds

**Framework**: mlx-swift-lm/MLXVLM  
**Kind**: property  
**Role**: Instance Property

Multimodal placeholder token IDs that must never be sampled as text. Seeded from the model configuration; the model factory merges `suppress_tokens` from `generation_config.json` on top. See `SuppressedTokensProviding` in MLXLMCommon.

## Declaration

```swift
var suppressedTokenIds: Set<Int>
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxvlm/gemma4unified/suppressedtokenids)*