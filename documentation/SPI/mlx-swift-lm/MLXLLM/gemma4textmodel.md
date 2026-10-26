---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxllm/gemma4textmodel"
framework: "mlx-swift-lm/MLXLLM"
---

# Gemma4TextModel

**Framework**: mlx-swift-lm/MLXLLM  
**Kind**: class  
**Role**: Class

## Declaration

```swift
class Gemma4TextModel
```

## Topics

### Initializers
- [init(Gemma4TextConfiguration)](./gemma4textmodel/init%28_%29.md)
### Instance Properties
- [let kvHeads: [Int]](./gemma4textmodel/kvheads.md)
- [let vocabularySize: Int](./gemma4textmodel/vocabularysize.md)
### Instance Methods
- [func callAsFunction(MLXArray, cache: [KVCache]?) -> MLXArray](./gemma4textmodel/callasfunction%28_,cache%29.md)
- [func newCache(parameters: GenerateParameters?) throws -> [any KVCache]](./gemma4textmodel/newcache%28parameters%29.md)
- [func sanitize(weights: [String : MLXArray]) -> [String : MLXArray]](./gemma4textmodel/sanitize%28weights%29.md)
### Default Implementations
- [BaseLanguageModel Implementations](./gemma4textmodel/baselanguagemodel-implementations.md)
- [ChatConventionsProviding Implementations](./gemma4textmodel/chatconventionsproviding-implementations.md)
- [LLMModel Implementations](./gemma4textmodel/llmmodel-implementations.md)
- [LanguageModel Implementations](./gemma4textmodel/languagemodel-implementations.md)
- [LoRAModel Implementations](./gemma4textmodel/loramodel-implementations.md)

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

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxllm/gemma4textmodel)*