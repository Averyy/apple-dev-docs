---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxllm/smollm3model"
framework: "mlx-swift-lm/MLXLLM"
---

# SmolLM3Model

**Framework**: mlx-swift-lm/MLXLLM  
**Kind**: class  
**Role**: Class

## Declaration

```swift
class SmolLM3Model
```

## Topics

### Initializers
- [init(SmolLM3Configuration)](./smollm3model/init%28_%29.md)
### Instance Properties
- [let kvHeads: [Int]](./smollm3model/kvheads.md)
- [let model: SmolLM3ModelInner](./smollm3model/model.md)
- [let vocabularySize: Int](./smollm3model/vocabularysize.md)
### Instance Methods
- [func callAsFunction(MLXArray, cache: [KVCache]?) -> MLXArray](./smollm3model/callasfunction%28_,cache%29.md)
- [func sanitize(weights: [String : MLXArray]) -> [String : MLXArray]](./smollm3model/sanitize%28weights%29.md)
### Default Implementations
- [BaseLanguageModel Implementations](./smollm3model/baselanguagemodel-implementations.md)
- [ChatConventionsProviding Implementations](./smollm3model/chatconventionsproviding-implementations.md)
- [LLMModel Implementations](./smollm3model/llmmodel-implementations.md)
- [LanguageModel Implementations](./smollm3model/languagemodel-implementations.md)
- [LoRAModel Implementations](./smollm3model/loramodel-implementations.md)

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

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxllm/smollm3model)*