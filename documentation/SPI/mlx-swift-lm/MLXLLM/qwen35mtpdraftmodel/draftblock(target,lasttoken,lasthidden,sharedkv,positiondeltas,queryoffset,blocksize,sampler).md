---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxllm/qwen35mtpdraftmodel/draftblock(target:lasttoken:lasthidden:sharedkv:positiondeltas:queryoffset:blocksize:sampler:)"
framework: "mlx-swift-lm/MLXLLM"
---

# draftBlock(target:lastToken:lastHidden:sharedKV:positionDeltas:queryOffset:blockSize:sampler:)

**Framework**: mlx-swift-lm/MLXLLM  
**Kind**: method  
**Role**: Instance Method

Inherited from `MTPDrafterModel.draftBlock(target:lastToken:lastHidden:sharedKV:positionDeltas:queryOffset:blockSize:sampler:)`.

## Declaration

```swift
func draftBlock(target: any LanguageModel, lastToken: MLXArray, lastHidden: MLXArray, sharedKV: [String : (MLXArray, MLXArray)], positionDeltas: MLXArray?, queryOffset: Int, blockSize: Int, sampler: any LogitSampler) -> MLXArray
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxllm/qwen35mtpdraftmodel/draftblock(target:lasttoken:lasthidden:sharedkv:positiondeltas:queryoffset:blocksize:sampler:))*