---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxllm/bailingmoemodel"
framework: "mlx-swift-lm/MLXLLM"
---

# BailingMoeModel

**Framework**: mlx-swift-lm/MLXLLM  
**Kind**: class  
**Role**: Class

## Declaration

```swift
class BailingMoeModel
```

## Topics

### Initializers
- [init(BailingMoeConfiguration)](./bailingmoemodel/init%28_%29.md)
### Instance Properties
- [let kvHeads: [Int]](./bailingmoemodel/kvheads.md)
- [let model: BailingMoeModelInner](./bailingmoemodel/model.md)
- [let vocabularySize: Int](./bailingmoemodel/vocabularysize.md)
### Instance Methods
- [func callAsFunction(MLXArray, cache: [KVCache]?) -> MLXArray](./bailingmoemodel/callasfunction%28_,cache%29.md)
- [func sanitize(weights: [String : MLXArray]) -> [String : MLXArray]](./bailingmoemodel/sanitize%28weights%29.md)
### Default Implementations
- [BaseLanguageModel Implementations](./bailingmoemodel/baselanguagemodel-implementations.md)
- [ChatConventionsProviding Implementations](./bailingmoemodel/chatconventionsproviding-implementations.md)
- [LLMModel Implementations](./bailingmoemodel/llmmodel-implementations.md)
- [LanguageModel Implementations](./bailingmoemodel/languagemodel-implementations.md)
- [LoRAModel Implementations](./bailingmoemodel/loramodel-implementations.md)

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

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxllm/bailingmoemodel)*