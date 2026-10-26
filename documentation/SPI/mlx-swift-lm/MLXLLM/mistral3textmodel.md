---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxllm/mistral3textmodel"
framework: "mlx-swift-lm/MLXLLM"
---

# Mistral3TextModel

**Framework**: mlx-swift-lm/MLXLLM  
**Kind**: class  
**Role**: Class

Mistral3Text language model.

## Declaration

```swift
class Mistral3TextModel
```

## Topics

### Initializers
- [init(Mistral3TextConfiguration)](./mistral3textmodel/init%28_%29.md)
### Instance Properties
- [let kvHeads: [Int]](./mistral3textmodel/kvheads.md)
- [let model: Mistral3TextModelInner](./mistral3textmodel/model.md)
- [let vocabularySize: Int](./mistral3textmodel/vocabularysize.md)
### Instance Methods
- [func callAsFunction(MLXArray, cache: [KVCache]?) -> MLXArray](./mistral3textmodel/callasfunction%28_,cache%29.md)
- [func callAsFunction(MLXArray, cache: [KVCache]?, inputEmbeddings: MLXArray?) -> MLXArray](./mistral3textmodel/callasfunction%28_,cache,inputembeddings%29.md)
- [func newCache(parameters: GenerateParameters?) throws -> [KVCache]](./mistral3textmodel/newcache%28parameters%29.md)
  Create appropriate caches for each layer type.
- [func sanitize(weights: [String : MLXArray]) -> [String : MLXArray]](./mistral3textmodel/sanitize%28weights%29.md)
### Default Implementations
- [BaseLanguageModel Implementations](./mistral3textmodel/baselanguagemodel-implementations.md)
- [ChatConventionsProviding Implementations](./mistral3textmodel/chatconventionsproviding-implementations.md)
- [LLMModel Implementations](./mistral3textmodel/llmmodel-implementations.md)
- [LanguageModel Implementations](./mistral3textmodel/languagemodel-implementations.md)
- [LoRAModel Implementations](./mistral3textmodel/loramodel-implementations.md)

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

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxllm/mistral3textmodel)*