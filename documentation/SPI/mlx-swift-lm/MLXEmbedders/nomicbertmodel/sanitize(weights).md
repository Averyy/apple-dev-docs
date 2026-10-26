---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxembedders/nomicbertmodel/sanitize(weights:)"
framework: "mlx-swift-lm/MLXEmbedders"
---

# sanitize(weights:)

**Framework**: mlx-swift-lm/MLXEmbedders  
**Kind**: method  
**Role**: Instance Method

Remaps weight keys from external formats (e.g., Hugging Face) to this model’s internal structure.

## Declaration

```swift
func sanitize(weights: [String : MLXArray]) -> [String : MLXArray]
```

#### Return Value

A new dictionary with keys renamed to match this Swift class structure.

#### Discussion

This is critical when loading `.safetensors` or PyTorch checkpoints, as variable names often differ.

## Parameters

- `weights`: A dictionary of loaded weights.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxembedders/nomicbertmodel/sanitize(weights:))*