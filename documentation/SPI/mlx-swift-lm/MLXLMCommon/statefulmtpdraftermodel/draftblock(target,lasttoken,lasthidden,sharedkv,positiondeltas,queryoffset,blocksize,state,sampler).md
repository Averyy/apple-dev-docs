---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/statefulmtpdraftermodel/draftblock(target:lasttoken:lasthidden:sharedkv:positiondeltas:queryoffset:blocksize:state:sampler:)"
framework: "mlx-swift-lm/MLXLMCommon"
---

# draftBlock(target:lastToken:lastHidden:sharedKV:positionDeltas:queryOffset:blockSize:state:sampler:)

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Stateful variant of [`draftBlock(target:lastToken:lastHidden:sharedKV:positionDeltas:queryOffset:blockSize:sampler:)`](../mtpdraftermodel/draftblock%28target,lasttoken,lasthidden,sharedkv,positiondeltas,queryoffset,blocksize,sampler%29.md).

## Declaration

```swift
func draftBlock(target: any LanguageModel, lastToken: MLXArray, lastHidden: MLXArray, sharedKV: [String : (MLXArray, MLXArray)], positionDeltas: MLXArray?, queryOffset: Int, blockSize: Int, state: inout MTPDrafterState, sampler: any LogitSampler) -> MLXArray
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/statefulmtpdraftermodel/draftblock(target:lasttoken:lasthidden:sharedkv:positiondeltas:queryoffset:blocksize:state:sampler:))*