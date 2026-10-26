---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxllm/heliummodel"
framework: "mlx-swift-lm/MLXLLM"
---

# HeliumModel

**Framework**: mlx-swift-lm/MLXLLM  
**Kind**: class  
**Role**: Class

## Declaration

```swift
class HeliumModel
```

## Topics

### Initializers
- [init(HeliumConfiguration)](./heliummodel/init%28_%29.md)
### Instance Properties
- [let kvHeads: [Int]](./heliummodel/kvheads.md)
- [let model: HeliumModelInner](./heliummodel/model.md)
- [let vocabularySize: Int](./heliummodel/vocabularysize.md)
### Instance Methods
- [func callAsFunction(MLXArray, cache: [KVCache]?) -> MLXArray](./heliummodel/callasfunction%28_,cache%29.md)
- [func sanitize(weights: [String : MLXArray]) -> [String : MLXArray]](./heliummodel/sanitize%28weights%29.md)
### Default Implementations
- [BaseLanguageModel Implementations](./heliummodel/baselanguagemodel-implementations.md)
- [ChatConventionsProviding Implementations](./heliummodel/chatconventionsproviding-implementations.md)
- [LLMModel Implementations](./heliummodel/llmmodel-implementations.md)
- [LanguageModel Implementations](./heliummodel/languagemodel-implementations.md)
- [LoRAModel Implementations](./heliummodel/loramodel-implementations.md)

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

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxllm/heliummodel)*