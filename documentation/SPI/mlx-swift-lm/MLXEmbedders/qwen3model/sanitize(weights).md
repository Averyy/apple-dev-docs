---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxembedders/qwen3model/sanitize(weights:)"
framework: "mlx-swift-lm/MLXEmbedders"
---

# sanitize(weights:)

**Framework**: mlx-swift-lm/MLXEmbedders  
**Kind**: method  
**Role**: Instance Method

Cleans and remaps external weight keys to match the internal module structure.

## Declaration

```swift
func sanitize(weights: [String : MLXArray]) -> [String : MLXArray]
```

## Return Value

A sanitized dictionary with keys correctly prefixed with `model.`.

## Discussion

This is vital when loading weights from formats like Hugging Face `safetensors`.

## Parameters

- `weights`: A dictionary of original weight keys and values.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxembedders/qwen3model/sanitize(weights:))*