---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxembedders/bertmodel/sanitize(weights:)"
framework: "mlx-swift-lm/MLXEmbedders"
---

# sanitize(weights:)

**Framework**: mlx-swift-lm/MLXEmbedders  
**Kind**: method  
**Role**: Instance Method

Maps external weight names (e.g., from Hugging Face) to this class’s internal structure.

## Declaration

```swift
func sanitize(weights: [String : MLXArray]) -> [String : MLXArray]
```

## Discussion

This is essential for loading pre-trained weights, as it renames keys like `attention.output.dense` to `attention.out_proj`.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxembedders/bertmodel/sanitize(weights:))*