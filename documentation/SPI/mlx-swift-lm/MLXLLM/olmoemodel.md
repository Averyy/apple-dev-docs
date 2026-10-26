---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxllm/olmoemodel"
framework: "mlx-swift-lm/MLXLLM"
---

# OlmoEModel

**Framework**: mlx-swift-lm/MLXLLM  
**Kind**: class  
**Role**: Class

## Declaration

```swift
class OlmoEModel
```

## Topics

### Initializers
- [init(OlmoEConfiguration)](./olmoemodel/init%28_%29.md)
### Instance Properties
- [let kvHeads: [Int]](./olmoemodel/kvheads.md)
- [let model: OlmoEModelInner](./olmoemodel/model.md)
- [let vocabularySize: Int](./olmoemodel/vocabularysize.md)
### Instance Methods
- [func callAsFunction(MLXArray, cache: [KVCache]?) -> MLXArray](./olmoemodel/callasfunction%28_,cache%29.md)
- [func sanitize(weights: [String : MLXArray]) -> [String : MLXArray]](./olmoemodel/sanitize%28weights%29.md)
### Default Implementations
- [BaseLanguageModel Implementations](./olmoemodel/baselanguagemodel-implementations.md)
- [ChatConventionsProviding Implementations](./olmoemodel/chatconventionsproviding-implementations.md)
- [LLMModel Implementations](./olmoemodel/llmmodel-implementations.md)
- [LanguageModel Implementations](./olmoemodel/languagemodel-implementations.md)
- [LoRAModel Implementations](./olmoemodel/loramodel-implementations.md)

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

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxllm/olmoemodel)*