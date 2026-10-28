---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/rotatequantizedlinear/callasfunction(_:)"
framework: "mlx-swift-lm/MLXLMCommon"
---

# callAsFunction(_:)

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: method  
**Role**: Instance Method

Forward pass: applies pairwise Givens rotation then quantized matmul.

## Declaration

```swift
override func callAsFunction(_ x: MLXArray) -> MLXArray
```

## Discussion

Computes `y = quantizedMM(rotate(x), W)` where the rotation fuses channel scaling and Givens rotations in a single Metal kernel. No mutable state is read or written by this method.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/rotatequantizedlinear/callasfunction(_:))*