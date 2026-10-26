---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxllm/hunyuanmodel"
framework: "mlx-swift-lm/MLXLLM"
---

# HunyuanModel

**Framework**: mlx-swift-lm/MLXLLM  
**Kind**: class  
**Role**: Class

## Declaration

```swift
class HunyuanModel
```

## Topics

### Initializers
- [init(HunyuanConfiguration)](./hunyuanmodel/init%28_%29.md)
### Instance Properties
- [let kvHeads: [Int]](./hunyuanmodel/kvheads.md)
- [let model: HunyuanModelInner](./hunyuanmodel/model.md)
- [let vocabularySize: Int](./hunyuanmodel/vocabularysize.md)
### Instance Methods
- [func callAsFunction(MLXArray, cache: [KVCache]?) -> MLXArray](./hunyuanmodel/callasfunction%28_,cache%29.md)
- [func sanitize(weights: [String : MLXArray]) -> [String : MLXArray]](./hunyuanmodel/sanitize%28weights%29.md)
### Default Implementations
- [BaseLanguageModel Implementations](./hunyuanmodel/baselanguagemodel-implementations.md)
- [ChatConventionsProviding Implementations](./hunyuanmodel/chatconventionsproviding-implementations.md)
- [LLMModel Implementations](./hunyuanmodel/llmmodel-implementations.md)
- [LanguageModel Implementations](./hunyuanmodel/languagemodel-implementations.md)
- [LoRAModel Implementations](./hunyuanmodel/loramodel-implementations.md)

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

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxllm/hunyuanmodel)*