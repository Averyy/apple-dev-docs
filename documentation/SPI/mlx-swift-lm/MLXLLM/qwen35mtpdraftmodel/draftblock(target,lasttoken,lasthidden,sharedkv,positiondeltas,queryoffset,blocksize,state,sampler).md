---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxllm/qwen35mtpdraftmodel/draftblock(target:lasttoken:lasthidden:sharedkv:positiondeltas:queryoffset:blocksize:state:sampler:)"
framework: "mlx-swift-lm/MLXLLM"
---

# draftBlock(target:lastToken:lastHidden:sharedKV:positionDeltas:queryOffset:blockSize:state:sampler:)

**Framework**: mlx-swift-lm/MLXLLM  
**Kind**: method  
**Role**: Instance Method

Inherited from `StatefulMTPDrafterModel.draftBlock(target:lastToken:lastHidden:sharedKV:positionDeltas:queryOffset:blockSize:state:sampler:)`.

## Declaration

```swift
func draftBlock(target: any LanguageModel, lastToken: MLXArray, lastHidden: MLXArray, sharedKV _: [String : (MLXArray, MLXArray)], positionDeltas _: MLXArray?, queryOffset: Int, blockSize: Int, state: inout MTPDrafterState, sampler: any LogitSampler) -> MLXArray
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxllm/qwen35mtpdraftmodel/draftblock(target:lasttoken:lasthidden:sharedkv:positiondeltas:queryoffset:blocksize:state:sampler:))*