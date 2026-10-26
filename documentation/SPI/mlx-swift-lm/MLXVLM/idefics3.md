---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxvlm/idefics3"
framework: "mlx-swift-lm/MLXVLM"
---

# Idefics3

**Framework**: mlx-swift-lm/MLXVLM  
**Kind**: class  
**Role**: Class

## Declaration

```swift
class Idefics3
```

## Topics

### Initializers
- [init(Idefics3Configuration)](./idefics3/init%28_%29.md)
### Instance Properties
- [let config: Idefics3Configuration](./idefics3/config.md)
- [var headDim: MLX.IntOrPair](./idefics3/headdim.md)
- [var kvHeads: [Int]](./idefics3/kvheads.md)
- [var loraLayers: [Module]](./idefics3/loralayers.md)
- [var vocabularySize: Int](./idefics3/vocabularysize.md)
### Instance Methods
- [func callAsFunction(MLXArray, cache: [any KVCache]?) -> MLXArray](./idefics3/callasfunction%28_,cache%29.md)
- [func prepare(LMInput, cache: [any KVCache], state: LMOutput.State?, prefill: PrefillParameters) throws -> PrepareResult](./idefics3/prepare%28_,cache,state,prefill%29.md)
- [func sanitize(weights: [String : MLXArray]) -> [String : MLXArray]](./idefics3/sanitize%28weights%29.md)
### Default Implementations
- [BaseLanguageModel Implementations](./idefics3/baselanguagemodel-implementations.md)
- [ChatConventionsProviding Implementations](./idefics3/chatconventionsproviding-implementations.md)
- [LanguageModel Implementations](./idefics3/languagemodel-implementations.md)
- [LoRAModel Implementations](./idefics3/loramodel-implementations.md)

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

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxvlm/idefics3)*