---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxembedders/distilbertmodel/sanitize(weights:)"
framework: "mlx-swift-lm/MLXEmbedders"
---

# sanitize(weights:)

**Framework**: mlx-swift-lm/MLXEmbedders  
**Kind**: method  
**Role**: Instance Method

Remaps DistilBERT-specific weight keys to the internal MLX architecture.

## Declaration

```swift
override func sanitize(weights: [String : MLXArray]) -> [String : MLXArray]
```

## Return Value

A sanitized dictionary compatible with the `Module` property keys.

## Discussion

DistilBERT weights use different naming patterns than standard BERT (e.g., using `ffn` instead of `intermediate`). This method ensures that weights from models like `distilbert-base-uncased` map correctly to the Swift property names.

## Parameters

- `weights`: A dictionary of keys and tensors from the model file.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxembedders/distilbertmodel/sanitize(weights:))*