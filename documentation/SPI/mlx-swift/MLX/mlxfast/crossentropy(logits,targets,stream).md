---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxfast/crossentropy(logits:targets:stream:)"
framework: "mlx-swift/MLX"
---

# crossEntropy(logits:targets:stream:)

**Framework**: mlx-swift/MLX  
**Kind**: method  
**Role**: Type Method

Cross entropy loss with class indices as targets.

## Declaration

```swift
static func crossEntropy(logits: MLXArray, targets: MLXArray, stream: StreamOrDevice = .default) -> MLXArray
```

## Parameters

- `logits`: The unnormalized logits. The loss is computed over the last axis.
- `targets`: Class indices. The shape should match the shape of `logits` with the last axis removed. The indices must be in `0 ..< logits.dim(-1)`.
- `stream`: Stream or device to evaluate on


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxfast/crossentropy(logits:targets:stream:))*