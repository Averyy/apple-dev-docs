---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxllm/granitemodel"
framework: "mlx-swift-lm/MLXLLM"
---

# GraniteModel

**Framework**: mlx-swift-lm/MLXLLM  
**Kind**: class  
**Role**: Class

## Declaration

```swift
class GraniteModel
```

## Topics

### Initializers
- [init(GraniteConfiguration)](./granitemodel/init%28_%29.md)
### Instance Properties
- [let kvHeads: [Int]](./granitemodel/kvheads.md)
- [let model: GraniteModelInner](./granitemodel/model.md)
- [let vocabularySize: Int](./granitemodel/vocabularysize.md)
### Instance Methods
- [func callAsFunction(MLXArray, cache: [KVCache]?) -> MLXArray](./granitemodel/callasfunction%28_,cache%29.md)
- [func sanitize(weights: [String : MLXArray]) -> [String : MLXArray]](./granitemodel/sanitize%28weights%29.md)
### Default Implementations
- [BaseLanguageModel Implementations](./granitemodel/baselanguagemodel-implementations.md)
- [ChatConventionsProviding Implementations](./granitemodel/chatconventionsproviding-implementations.md)
- [LLMModel Implementations](./granitemodel/llmmodel-implementations.md)
- [LanguageModel Implementations](./granitemodel/languagemodel-implementations.md)
- [LoRAModel Implementations](./granitemodel/loramodel-implementations.md)

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

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxllm/granitemodel)*