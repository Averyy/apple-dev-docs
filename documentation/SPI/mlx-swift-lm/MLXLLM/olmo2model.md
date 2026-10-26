---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxllm/olmo2model"
framework: "mlx-swift-lm/MLXLLM"
---

# Olmo2Model

**Framework**: mlx-swift-lm/MLXLLM  
**Kind**: class  
**Role**: Class

## Declaration

```swift
class Olmo2Model
```

## Topics

### Initializers
- [init(Olmo2Configuration)](./olmo2model/init%28_%29.md)
### Instance Properties
- [let kvHeads: [Int]](./olmo2model/kvheads.md)
- [let model: Olmo2ModelInner](./olmo2model/model.md)
- [let vocabularySize: Int](./olmo2model/vocabularysize.md)
### Instance Methods
- [func callAsFunction(MLXArray, cache: [KVCache]?) -> MLXArray](./olmo2model/callasfunction%28_,cache%29.md)
- [func sanitize(weights: [String : MLXArray]) -> [String : MLXArray]](./olmo2model/sanitize%28weights%29.md)
### Default Implementations
- [BaseLanguageModel Implementations](./olmo2model/baselanguagemodel-implementations.md)
- [ChatConventionsProviding Implementations](./olmo2model/chatconventionsproviding-implementations.md)
- [LLMModel Implementations](./olmo2model/llmmodel-implementations.md)
- [LanguageModel Implementations](./olmo2model/languagemodel-implementations.md)
- [LoRAModel Implementations](./olmo2model/loramodel-implementations.md)

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

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxllm/olmo2model)*