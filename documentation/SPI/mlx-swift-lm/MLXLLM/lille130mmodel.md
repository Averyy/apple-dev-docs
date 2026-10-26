---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxllm/lille130mmodel"
framework: "mlx-swift-lm/MLXLLM"
---

# Lille130mModel

**Framework**: mlx-swift-lm/MLXLLM  
**Kind**: class  
**Role**: Class

## Declaration

```swift
final class Lille130mModel
```

## Topics

### Initializers
- [init(Lille130mConfiguration)](./lille130mmodel/init%28_%29.md)
### Instance Properties
- [let kvHeads: [Int]](./lille130mmodel/kvheads.md)
- [var transformer: Lille130mModelInner](./lille130mmodel/transformer.md)
- [let vocabularySize: Int](./lille130mmodel/vocabularysize.md)
### Instance Methods
- [func callAsFunction(MLXArray, cache: [KVCache]?) -> MLXArray](./lille130mmodel/callasfunction%28_,cache%29.md)
- [func sanitize(weights: [String : MLXArray]) -> [String : MLXArray]](./lille130mmodel/sanitize%28weights%29.md)
### Default Implementations
- [BaseLanguageModel Implementations](./lille130mmodel/baselanguagemodel-implementations.md)
- [ChatConventionsProviding Implementations](./lille130mmodel/chatconventionsproviding-implementations.md)
- [LLMModel Implementations](./lille130mmodel/llmmodel-implementations.md)
- [LanguageModel Implementations](./lille130mmodel/languagemodel-implementations.md)
- [LoRAModel Implementations](./lille130mmodel/loramodel-implementations.md)

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

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxllm/lille130mmodel)*