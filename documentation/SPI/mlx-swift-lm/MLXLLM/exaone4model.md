---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxllm/exaone4model"
framework: "mlx-swift-lm/MLXLLM"
---

# Exaone4Model

**Framework**: mlx-swift-lm/MLXLLM  
**Kind**: class  
**Role**: Class

## Declaration

```swift
class Exaone4Model
```

## Topics

### Initializers
- [init(Exaone4Configuration)](./exaone4model/init%28_%29.md)
### Instance Properties
- [let kvHeads: [Int]](./exaone4model/kvheads.md)
- [let model: Exaone4ModelInner](./exaone4model/model.md)
- [let vocabularySize: Int](./exaone4model/vocabularysize.md)
### Instance Methods
- [func callAsFunction(MLXArray, cache: [KVCache]?) -> MLXArray](./exaone4model/callasfunction%28_,cache%29.md)
- [func newCache(parameters: GenerateParameters?) throws -> [KVCache]](./exaone4model/newcache%28parameters%29.md)
- [func sanitize(weights: [String : MLXArray]) -> [String : MLXArray]](./exaone4model/sanitize%28weights%29.md)
### Default Implementations
- [BaseLanguageModel Implementations](./exaone4model/baselanguagemodel-implementations.md)
- [ChatConventionsProviding Implementations](./exaone4model/chatconventionsproviding-implementations.md)
- [LLMModel Implementations](./exaone4model/llmmodel-implementations.md)
- [LanguageModel Implementations](./exaone4model/languagemodel-implementations.md)
- [LoRAModel Implementations](./exaone4model/loramodel-implementations.md)

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

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxllm/exaone4model)*