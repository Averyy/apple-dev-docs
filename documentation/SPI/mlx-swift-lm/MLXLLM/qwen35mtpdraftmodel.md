---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxllm/qwen35mtpdraftmodel"
framework: "mlx-swift-lm/MLXLLM"
---

# Qwen35MTPDraftModel

**Framework**: mlx-swift-lm/MLXLLM  
**Kind**: class  
**Role**: Class

## Declaration

```swift
final class Qwen35MTPDraftModel
```

## Topics

### Initializers
- [init(Qwen35TextConfiguration, preconvertedNorms: Bool)](./qwen35mtpdraftmodel/init%28_,preconvertednorms%29-3umuh.md)
- [init(Qwen35Configuration, preconvertedNorms: Bool)](./qwen35mtpdraftmodel/init%28_,preconvertednorms%29-90vee.md)
### Instance Properties
- [let configuration: Qwen35TextConfiguration](./qwen35mtpdraftmodel/configuration.md)
- [var excludedCheckpointNamespaces: [String]](./qwen35mtpdraftmodel/excludedcheckpointnamespaces.md)
- [let maximumBlockSize: Int?](./qwen35mtpdraftmodel/maximumblocksize.md)
- [let requiresGreedySampling: Bool](./qwen35mtpdraftmodel/requiresgreedysampling.md)
- [let requiresPromptPrefill: Bool](./qwen35mtpdraftmodel/requirespromptprefill.md)
- [let requiresSharedTargetKV: Bool](./qwen35mtpdraftmodel/requiressharedtargetkv.md)
### Instance Methods
- [func commitDrafterState(target: any LanguageModel, targetHidden: MLXArray, draftTokens: MLXArray, acceptedCount: Int, finalToken: MLXArray, positionDeltas: MLXArray?, state: inout MTPDrafterState, sampler: any LogitSampler)](./qwen35mtpdraftmodel/commitdrafterstate%28target,targethidden,drafttokens,acceptedcount,finaltoken,positiondeltas,state,sampler%29.md)
- [func draftBlock(target: any LanguageModel, lastToken: MLXArray, lastHidden: MLXArray, sharedKV: [String : (MLXArray, MLXArray)], positionDeltas: MLXArray?, queryOffset: Int, blockSize: Int, sampler: any LogitSampler) -> MLXArray](./qwen35mtpdraftmodel/draftblock%28target,lasttoken,lasthidden,sharedkv,positiondeltas,queryoffset,blocksize,sampler%29.md)
- [func draftBlock(target: any LanguageModel, lastToken: MLXArray, lastHidden: MLXArray, sharedKV: [String : (MLXArray, MLXArray)], positionDeltas: MLXArray?, queryOffset: Int, blockSize: Int, state: inout MTPDrafterState, sampler: any LogitSampler) -> MLXArray](./qwen35mtpdraftmodel/draftblock%28target,lasttoken,lasthidden,sharedkv,positiondeltas,queryoffset,blocksize,state,sampler%29.md)
- [func isCompatible(with: any LanguageModel) -> Bool](./qwen35mtpdraftmodel/iscompatible%28with%29.md)
- [func makeState(parameters: GenerateParameters?) -> MTPDrafterState](./qwen35mtpdraftmodel/makestate%28parameters%29.md)
- [func prepareCheckpoint(ModelCheckpoint) throws -> ModelCheckpoint](./qwen35mtpdraftmodel/preparecheckpoint%28_%29.md)
- [func prepareDrafterState(target: any LanguageModel, promptTokens: MLXArray, targetHidden: MLXArray, firstBonus: MLXArray, positionDeltas: MLXArray?, state: inout MTPDrafterState, sampler: any LogitSampler)](./qwen35mtpdraftmodel/preparedrafterstate%28target,prompttokens,targethidden,firstbonus,positiondeltas,state,sampler%29.md)
- [func sanitize(weights: [String : MLXArray]) throws -> [String : MLXArray]](./qwen35mtpdraftmodel/sanitize%28weights%29.md)
- [func sanitize(weights: [String : MLXArray], metadata: [String : String]) throws -> [String : MLXArray]](./qwen35mtpdraftmodel/sanitize%28weights,metadata%29.md)
### Default Implementations
- [ModelConversionMetadataProvider Implementations](./qwen35mtpdraftmodel/modelconversionmetadataprovider-implementations.md)

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

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxllm/qwen35mtpdraftmodel)*