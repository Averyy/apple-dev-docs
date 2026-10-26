---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxllm/nemotronlabsdiffusionmodel/bidirectionallogits(_:cache:)"
framework: "mlx-swift-lm/MLXLLM"
---

# bidirectionalLogits(_:cache:)

**Framework**: mlx-swift-lm/MLXLLM  
**Kind**: method  
**Role**: Instance Method

Bidirectional forward over only the block, attending to a causally prefilled KV cache (the prompt + previously committed blocks). The cache is updated with the block’s K/V — callers must `trim` the cache by `inputs.dim(1)` after the forward to discard speculative entries.

## Declaration

```swift
func bidirectionalLogits(_ inputs: MLXArray, cache: [KVCache]) -> MLXArray
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxllm/nemotronlabsdiffusionmodel/bidirectionallogits(_:cache:))*