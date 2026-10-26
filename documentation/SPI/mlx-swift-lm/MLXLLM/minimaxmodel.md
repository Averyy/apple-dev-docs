---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxllm/minimaxmodel"
framework: "mlx-swift-lm/MLXLLM"
---

# MiniMaxModel

**Framework**: mlx-swift-lm/MLXLLM  
**Kind**: class  
**Role**: Class

## Declaration

```swift
class MiniMaxModel
```

## Topics

### Initializers
- [init(MiniMaxConfiguration)](./minimaxmodel/init%28_%29.md)
### Instance Properties
- [let kvHeads: [Int]](./minimaxmodel/kvheads.md)
- [let model: MiniMaxModelInner](./minimaxmodel/model.md)
- [let vocabularySize: Int](./minimaxmodel/vocabularysize.md)
### Instance Methods
- [func callAsFunction(MLXArray, cache: [KVCache]?) -> MLXArray](./minimaxmodel/callasfunction%28_,cache%29.md)
- [func sanitize(weights: [String : MLXArray]) -> [String : MLXArray]](./minimaxmodel/sanitize%28weights%29.md)
### Default Implementations
- [BaseLanguageModel Implementations](./minimaxmodel/baselanguagemodel-implementations.md)
- [ChatConventionsProviding Implementations](./minimaxmodel/chatconventionsproviding-implementations.md)
- [LLMModel Implementations](./minimaxmodel/llmmodel-implementations.md)
- [LanguageModel Implementations](./minimaxmodel/languagemodel-implementations.md)
- [LoRAModel Implementations](./minimaxmodel/loramodel-implementations.md)

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

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxllm/minimaxmodel)*