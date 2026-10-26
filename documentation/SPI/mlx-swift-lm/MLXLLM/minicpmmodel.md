---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxllm/minicpmmodel"
framework: "mlx-swift-lm/MLXLLM"
---

# MiniCPMModel

**Framework**: mlx-swift-lm/MLXLLM  
**Kind**: class  
**Role**: Class

## Declaration

```swift
final class MiniCPMModel
```

## Topics

### Initializers
- [init(MiniCPMConfiguration)](./minicpmmodel/init%28_%29.md)
### Instance Properties
- [let kvHeads: [Int]](./minicpmmodel/kvheads.md)
- [let model: MiniCPMModelInner](./minicpmmodel/model.md)
- [let vocabularySize: Int](./minicpmmodel/vocabularysize.md)
### Instance Methods
- [func callAsFunction(MLXArray, cache: [KVCache]?) -> MLXArray](./minicpmmodel/callasfunction%28_,cache%29.md)
- [func sanitize(weights: [String : MLXArray]) -> [String : MLXArray]](./minicpmmodel/sanitize%28weights%29.md)
### Default Implementations
- [BaseLanguageModel Implementations](./minicpmmodel/baselanguagemodel-implementations.md)
- [ChatConventionsProviding Implementations](./minicpmmodel/chatconventionsproviding-implementations.md)
- [LLMModel Implementations](./minicpmmodel/llmmodel-implementations.md)
- [LanguageModel Implementations](./minicpmmodel/languagemodel-implementations.md)
- [LoRAModel Implementations](./minicpmmodel/loramodel-implementations.md)

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

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxllm/minicpmmodel)*