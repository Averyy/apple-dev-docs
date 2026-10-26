---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxllm/falconh1model/callasfunction(_:cache:logitstokeep:)"
framework: "mlx-swift-lm/MLXLLM"
---

# callAsFunction(_:cache:logitsToKeep:)

**Framework**: mlx-swift-lm/MLXLLM  
**Kind**: method  
**Role**: Instance Method

Compute logits for the input tokens.

## Declaration

```swift
func callAsFunction(_ inputs: MLXArray, cache: [KVCache]? = nil, logitsToKeep: Int?) -> MLXArray
```

## Parameters

- `inputs`: Token ids, shape `[batch, sequence]`
- `cache`: Optional per-layer cache
- `logitsToKeep`: Number of trailing positions for which to compute logits. `nil` falls back to the `num_logits_to_keep` configuration value. A non-positive value keeps all positions (useful for perplexity / training evaluation).


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxllm/falconh1model/callasfunction(_:cache:logitstokeep:))*