---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxllm/olmo3model"
framework: "mlx-swift-lm/MLXLLM"
---

# Olmo3Model

**Framework**: mlx-swift-lm/MLXLLM  
**Kind**: class  
**Role**: Class

## Declaration

```swift
class Olmo3Model
```

## Topics

### Initializers
- [init(Olmo3Configuration)](./olmo3model/init%28_%29.md)
### Instance Properties
- [let kvHeads: [Int]](./olmo3model/kvheads.md)
- [let model: Olmo3ModelInner](./olmo3model/model.md)
- [let vocabularySize: Int](./olmo3model/vocabularysize.md)
### Instance Methods
- [func callAsFunction(MLXArray, cache: [KVCache]?) -> MLXArray](./olmo3model/callasfunction%28_,cache%29.md)
- [func newCache(parameters: GenerateParameters?) throws -> [KVCache]](./olmo3model/newcache%28parameters%29.md)
- [func sanitize(weights: [String : MLXArray]) -> [String : MLXArray]](./olmo3model/sanitize%28weights%29.md)
### Default Implementations
- [BaseLanguageModel Implementations](./olmo3model/baselanguagemodel-implementations.md)
- [ChatConventionsProviding Implementations](./olmo3model/chatconventionsproviding-implementations.md)
- [LLMModel Implementations](./olmo3model/llmmodel-implementations.md)
- [LanguageModel Implementations](./olmo3model/languagemodel-implementations.md)
- [LoRAModel Implementations](./olmo3model/loramodel-implementations.md)

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

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxllm/olmo3model)*