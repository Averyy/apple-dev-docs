---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxvlm/museglimmer/sanitize(weights:)"
framework: "mlx-swift-lm/MLXVLM"
---

# sanitize(weights:)

**Framework**: mlx-swift-lm/MLXVLM  
**Kind**: method  
**Role**: Instance Method

Key renaming only — a byte-for-byte port of `muse_glimmer.Model.sanitize`.

## Declaration

```swift
func sanitize(weights: [String : MLXArray]) -> [String : MLXArray]
```

## Discussion

The `mlx-community` repos are already published in the target layout, so this is a no-op there; the prefix rewrites cover the original `transformers` checkpoint. Notably there are no transposes: the patch embedder is a `Linear`, not a convolution.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxvlm/museglimmer/sanitize(weights:))*