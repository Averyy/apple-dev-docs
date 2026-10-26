---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxllm/ernie45model"
framework: "mlx-swift-lm/MLXLLM"
---

# Ernie45Model

**Framework**: mlx-swift-lm/MLXLLM  
**Kind**: class  
**Role**: Class

## Declaration

```swift
class Ernie45Model
```

## Topics

### Initializers
- [init(Ernie45Configuration)](./ernie45model/init%28_%29.md)
### Instance Properties
- [let kvHeads: [Int]](./ernie45model/kvheads.md)
- [let model: Ernie45ModelInner](./ernie45model/model.md)
- [let vocabularySize: Int](./ernie45model/vocabularysize.md)
### Instance Methods
- [func callAsFunction(MLXArray, cache: [KVCache]?) -> MLXArray](./ernie45model/callasfunction%28_,cache%29.md)
- [func sanitize(weights: [String : MLXArray]) -> [String : MLXArray]](./ernie45model/sanitize%28weights%29.md)
### Default Implementations
- [BaseLanguageModel Implementations](./ernie45model/baselanguagemodel-implementations.md)
- [ChatConventionsProviding Implementations](./ernie45model/chatconventionsproviding-implementations.md)
- [LLMModel Implementations](./ernie45model/llmmodel-implementations.md)
- [LanguageModel Implementations](./ernie45model/languagemodel-implementations.md)
- [LoRAModel Implementations](./ernie45model/loramodel-implementations.md)

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

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxllm/ernie45model)*