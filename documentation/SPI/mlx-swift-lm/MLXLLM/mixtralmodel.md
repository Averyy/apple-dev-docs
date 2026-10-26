---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxllm/mixtralmodel"
framework: "mlx-swift-lm/MLXLLM"
---

# MixtralModel

**Framework**: mlx-swift-lm/MLXLLM  
**Kind**: class  
**Role**: Class

## Declaration

```swift
class MixtralModel
```

## Topics

### Initializers
- [init(MixtralConfiguration)](./mixtralmodel/init%28_%29.md)
### Instance Properties
- [let kvHeads: [Int]](./mixtralmodel/kvheads.md)
- [let model: MixtralModelInner](./mixtralmodel/model.md)
- [let vocabularySize: Int](./mixtralmodel/vocabularysize.md)
### Instance Methods
- [func callAsFunction(MLXArray, cache: [KVCache]?) -> MLXArray](./mixtralmodel/callasfunction%28_,cache%29.md)
- [func sanitize(weights: [String : MLXArray]) -> [String : MLXArray]](./mixtralmodel/sanitize%28weights%29.md)
### Default Implementations
- [BaseLanguageModel Implementations](./mixtralmodel/baselanguagemodel-implementations.md)
- [ChatConventionsProviding Implementations](./mixtralmodel/chatconventionsproviding-implementations.md)
- [LLMModel Implementations](./mixtralmodel/llmmodel-implementations.md)
- [LanguageModel Implementations](./mixtralmodel/languagemodel-implementations.md)
- [LoRAModel Implementations](./mixtralmodel/loramodel-implementations.md)

## Relationships

### Inherits From
- MLXNN.Module
### Conforms To
- [LLMModel](./llmmodel.md)
- MLX.Evaluatable
- MLX.IndentedDescription
- MLX.Updatable
- MLXLMCommon.BaseLanguageModel
- MLXLMCommon.ChatConventionsProviding
- MLXLMCommon.KVCacheDimensionProvider
- MLXLMCommon.LanguageModel
- MLXLMCommon.LoRAModel
- Swift.Copyable
- Swift.CustomStringConvertible
- Swift.Escapable


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxllm/mixtralmodel)*