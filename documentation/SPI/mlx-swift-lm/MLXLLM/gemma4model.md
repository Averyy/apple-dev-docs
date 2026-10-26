---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxllm/gemma4model"
framework: "mlx-swift-lm/MLXLLM"
---

# Gemma4Model

**Framework**: mlx-swift-lm/MLXLLM  
**Kind**: class  
**Role**: Class

## Declaration

```swift
class Gemma4Model
```

## Topics

### Initializers
- [init(Gemma4Configuration)](./gemma4model/init%28_%29.md)
### Instance Properties
- [var kvHeads: [Int]](./gemma4model/kvheads.md)
- [var vocabularySize: Int](./gemma4model/vocabularysize.md)
### Instance Methods
- [func callAsFunction(MLXArray, cache: [KVCache]?) -> MLXArray](./gemma4model/callasfunction%28_,cache%29.md)
- [func newCache(parameters: GenerateParameters?) throws -> [any KVCache]](./gemma4model/newcache%28parameters%29.md)
- [func sanitize(weights: [String : MLXArray]) -> [String : MLXArray]](./gemma4model/sanitize%28weights%29.md)
### Default Implementations
- [BaseLanguageModel Implementations](./gemma4model/baselanguagemodel-implementations.md)
- [ChatConventionsProviding Implementations](./gemma4model/chatconventionsproviding-implementations.md)
- [LLMModel Implementations](./gemma4model/llmmodel-implementations.md)
- [LanguageModel Implementations](./gemma4model/languagemodel-implementations.md)
- [LoRAModel Implementations](./gemma4model/loramodel-implementations.md)

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

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxllm/gemma4model)*