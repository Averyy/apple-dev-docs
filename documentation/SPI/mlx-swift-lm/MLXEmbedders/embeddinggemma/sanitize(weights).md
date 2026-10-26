---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxembedders/embeddinggemma/sanitize(weights:)"
framework: "mlx-swift-lm/MLXEmbedders"
---

# sanitize(weights:)

**Framework**: mlx-swift-lm/MLXEmbedders  
**Kind**: method  
**Role**: Instance Method

Preprocesses the weights, handling key remapping and vocabulary truncation.

## Declaration

```swift
func sanitize(weights: [String : MLXArray]) -> [String : MLXArray]
```

#### Return Value

A sanitized dictionary of weights compatible with the model structure.

## Parameters

- `weights`: The original dictionary of weights.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxembedders/embeddinggemma/sanitize(weights:))*