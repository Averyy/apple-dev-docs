---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxvlm/paligemma"
framework: "mlx-swift-lm/MLXVLM"
---

# PaliGemma

**Framework**: mlx-swift-lm/MLXVLM  
**Kind**: class  
**Role**: Class

PaliGemma VLM

## Declaration

```swift
class PaliGemma
```

#### Overview

This is typically created by [`VLMModelFactory`](./vlmmodelfactory.md).

## Topics

### Initializers
- [init(PaliGemmaConfiguration)](./paligemma/init%28_%29.md)
### Instance Properties
- [let config: PaliGemmaConfiguration](./paligemma/config.md)
- [var kvHeads: [Int]](./paligemma/kvheads.md)
- [var loraLayers: [Module]](./paligemma/loralayers.md)
- [var vocabularySize: Int](./paligemma/vocabularysize.md)
### Instance Methods
- [func callAsFunction(MLXArray, cache: [any KVCache]?) -> MLXArray](./paligemma/callasfunction%28_,cache%29.md)
- [func prepare(LMInput, cache: [any KVCache], state: LMOutput.State?, prefill: PrefillParameters) throws -> PrepareResult](./paligemma/prepare%28_,cache,state,prefill%29.md)
- [func sanitize(weights: [String : MLXArray]) -> [String : MLXArray]](./paligemma/sanitize%28weights%29.md)
### Default Implementations
- [BaseLanguageModel Implementations](./paligemma/baselanguagemodel-implementations.md)
- [ChatConventionsProviding Implementations](./paligemma/chatconventionsproviding-implementations.md)
- [LanguageModel Implementations](./paligemma/languagemodel-implementations.md)
- [LoRAModel Implementations](./paligemma/loramodel-implementations.md)

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

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxvlm/paligemma)*