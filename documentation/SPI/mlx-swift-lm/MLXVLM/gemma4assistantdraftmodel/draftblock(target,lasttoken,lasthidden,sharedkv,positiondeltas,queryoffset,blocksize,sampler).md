---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxvlm/gemma4assistantdraftmodel/draftblock(target:lasttoken:lasthidden:sharedkv:positiondeltas:queryoffset:blocksize:sampler:)"
framework: "mlx-swift-lm/MLXVLM"
---

# draftBlock(target:lastToken:lastHidden:sharedKV:positionDeltas:queryOffset:blockSize:sampler:)

**Framework**: mlx-swift-lm/MLXVLM  
**Kind**: method  
**Role**: Instance Method

Inherited from `MTPDrafterModel.draftBlock(target:lastToken:lastHidden:sharedKV:positionDeltas:queryOffset:blockSize:sampler:)`.

## Declaration

```swift
func draftBlock(target: any LanguageModel, lastToken: MLXArray, lastHidden: MLXArray, sharedKV: [String : (MLXArray, MLXArray)], positionDeltas _: MLXArray?, queryOffset: Int, blockSize: Int, sampler: any LogitSampler) -> MLXArray
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxvlm/gemma4assistantdraftmodel/draftblock(target:lasttoken:lasthidden:sharedkv:positiondeltas:queryoffset:blocksize:sampler:))*