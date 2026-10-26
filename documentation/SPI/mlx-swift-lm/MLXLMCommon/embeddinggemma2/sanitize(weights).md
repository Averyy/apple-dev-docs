---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/embeddinggemma2/sanitize(weights:)"
framework: "mlx-swift-lm/MLXLMCommon"
---

# sanitize(weights:)

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: method  
**Role**: Instance Method

Keeps the text model and the encoders this configuration loads. PyTorch checkpoints store convolution kernels channels-first; they move to the channels-last layout of MLX.

## Declaration

```swift
func sanitize(weights: [String : MLXArray]) throws -> [String : MLXArray]
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/embeddinggemma2/sanitize(weights:))*