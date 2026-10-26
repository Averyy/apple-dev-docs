---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxvlm/qwen35vlmnextndraftmodel"
framework: "mlx-swift-lm/MLXVLM"
---

# Qwen35VLMNextNDraftModel

**Framework**: mlx-swift-lm/MLXVLM  
**Kind**: class  
**Role**: Class

## Declaration

```swift
final class Qwen35VLMNextNDraftModel
```

## Topics

### Initializers
- [init(Qwen35Configuration, preconvertedNorms: Bool)](./qwen35vlmnextndraftmodel/init%28_,preconvertednorms%29-1p4rc.md)
- [init(Qwen35Configuration.TextConfiguration, preconvertedNorms: Bool)](./qwen35vlmnextndraftmodel/init%28_,preconvertednorms%29-7v09e.md)
### Instance Properties
- [let configuration: Qwen35Configuration.TextConfiguration](./qwen35vlmnextndraftmodel/configuration.md)
- [var excludedCheckpointNamespaces: [String]](./qwen35vlmnextndraftmodel/excludedcheckpointnamespaces.md)
- [let maximumBlockSize: Int?](./qwen35vlmnextndraftmodel/maximumblocksize.md)
- [let requiresGreedySampling: Bool](./qwen35vlmnextndraftmodel/requiresgreedysampling.md)
- [let requiresPromptPrefill: Bool](./qwen35vlmnextndraftmodel/requirespromptprefill.md)
- [let requiresSharedTargetKV: Bool](./qwen35vlmnextndraftmodel/requiressharedtargetkv.md)
### Instance Methods
- [func commitDrafterState(target: any LanguageModel, targetHidden: MLXArray, draftTokens: MLXArray, acceptedCount: Int, finalToken: MLXArray, positionDeltas: MLXArray?, state: inout MTPDrafterState, sampler: any LogitSampler)](./qwen35vlmnextndraftmodel/commitdrafterstate%28target,targethidden,drafttokens,acceptedcount,finaltoken,positiondeltas,state,sampler%29.md)
- [func draftBlock(target: any LanguageModel, lastToken: MLXArray, lastHidden: MLXArray, sharedKV: [String : (MLXArray, MLXArray)], positionDeltas: MLXArray?, queryOffset: Int, blockSize: Int, sampler: any LogitSampler) -> MLXArray](./qwen35vlmnextndraftmodel/draftblock%28target,lasttoken,lasthidden,sharedkv,positiondeltas,queryoffset,blocksize,sampler%29.md)
- [func draftBlock(target: any LanguageModel, lastToken: MLXArray, lastHidden: MLXArray, sharedKV: [String : (MLXArray, MLXArray)], positionDeltas: MLXArray?, queryOffset: Int, blockSize: Int, state: inout MTPDrafterState, sampler: any LogitSampler) -> MLXArray](./qwen35vlmnextndraftmodel/draftblock%28target,lasttoken,lasthidden,sharedkv,positiondeltas,queryoffset,blocksize,state,sampler%29.md)
- [func isCompatible(with: any LanguageModel) -> Bool](./qwen35vlmnextndraftmodel/iscompatible%28with%29.md)
- [func makeState(parameters: GenerateParameters?) -> MTPDrafterState](./qwen35vlmnextndraftmodel/makestate%28parameters%29.md)
- [func prepareCheckpoint(ModelCheckpoint) throws -> ModelCheckpoint](./qwen35vlmnextndraftmodel/preparecheckpoint%28_%29.md)
- [func prepareDrafterState(target: any LanguageModel, promptTokens: MLXArray, targetHidden: MLXArray, firstBonus: MLXArray, positionDeltas: MLXArray?, state: inout MTPDrafterState, sampler: any LogitSampler)](./qwen35vlmnextndraftmodel/preparedrafterstate%28target,prompttokens,targethidden,firstbonus,positiondeltas,state,sampler%29.md)
- [func sanitize(weights: [String : MLXArray]) throws -> [String : MLXArray]](./qwen35vlmnextndraftmodel/sanitize%28weights%29.md)
- [func sanitize(weights: [String : MLXArray], metadata: [String : String]) throws -> [String : MLXArray]](./qwen35vlmnextndraftmodel/sanitize%28weights,metadata%29.md)
### Default Implementations
- [ModelConversionMetadataProvider Implementations](./qwen35vlmnextndraftmodel/modelconversionmetadataprovider-implementations.md)

## Relationships

### Inherits From
- MLXNN.Module
### Conforms To
- MLX.Evaluatable
- MLX.IndentedDescription
- MLX.Updatable
- MLXLMCommon.BaseLanguageModel
- MLXLMCommon.MTPDrafterModel
- MLXLMCommon.ModelConversionMetadataProvider
- MLXLMCommon.StatefulMTPDrafterModel
- Swift.Copyable
- Swift.CustomStringConvertible
- Swift.Escapable


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxvlm/qwen35vlmnextndraftmodel)*