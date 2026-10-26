---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxvlm/fastvlm"
framework: "mlx-swift-lm/MLXVLM"
---

# FastVLM

**Framework**: mlx-swift-lm/MLXVLM  
**Kind**: class  
**Role**: Class

## Declaration

```swift
class FastVLM
```

## Topics

### Initializers
- [init(FastVLMConfiguration)](./fastvlm/init%28_%29.md)
### Instance Properties
- [let config: FastVLMConfiguration](./fastvlm/config.md)
- [var kvHeads: [Int]](./fastvlm/kvheads.md)
- [var loraLayers: [Module]](./fastvlm/loralayers.md)
### Instance Methods
- [func callAsFunction(MLXArray, cache: [any KVCache]?) -> MLXArray](./fastvlm/callasfunction%28_,cache%29.md)
- [func prepare(LMInput, cache: [any KVCache], state: LMOutput.State?, prefill: PrefillParameters) throws -> PrepareResult](./fastvlm/prepare%28_,cache,state,prefill%29.md)
- [func sanitize(weights: [String : MLXArray]) -> [String : MLXArray]](./fastvlm/sanitize%28weights%29.md)
### Default Implementations
- [BaseLanguageModel Implementations](./fastvlm/baselanguagemodel-implementations.md)
- [ChatConventionsProviding Implementations](./fastvlm/chatconventionsproviding-implementations.md)
- [LanguageModel Implementations](./fastvlm/languagemodel-implementations.md)
- [LoRAModel Implementations](./fastvlm/loramodel-implementations.md)

## Relationships

### Inherits From
- MLXNN.Module
### Conforms To
- MLX.Evaluatable
- MLX.IndentedDescription
- MLX.Updatable
- MLXLMCommon.BaseLanguageModel
- MLXLMCommon.ChatConventionsProviding
- MLXLMCommon.KVCacheDimensionProvider
- MLXLMCommon.LanguageModel
- MLXLMCommon.LoRAModel
- Swift.CustomStringConvertible
- [VLMModel](./vlmmodel.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxvlm/fastvlm)*