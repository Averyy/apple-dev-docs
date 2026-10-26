---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxllm/qwen3nextmodel"
framework: "mlx-swift-lm/MLXLLM"
---

# Qwen3NextModel

**Framework**: mlx-swift-lm/MLXLLM  
**Kind**: class  
**Role**: Class

## Declaration

```swift
class Qwen3NextModel
```

## Topics

### Initializers
- [init(Qwen3NextConfiguration)](./qwen3nextmodel/init%28_%29.md)
### Instance Properties
- [let kvHeads: [Int]](./qwen3nextmodel/kvheads.md)
- [let model: Qwen3NextModelInner](./qwen3nextmodel/model.md)
- [let vocabularySize: Int](./qwen3nextmodel/vocabularysize.md)
### Instance Methods
- [func callAsFunction(MLXArray, cache: [KVCache]?) -> MLXArray](./qwen3nextmodel/callasfunction%28_,cache%29.md)
- [func makeCache() -> [KVCache]](./qwen3nextmodel/makecache%28%29.md)
- [func newCache(parameters: GenerateParameters?) throws -> [KVCache]](./qwen3nextmodel/newcache%28parameters%29.md)
- [func sanitize(weights: [String : MLXArray]) -> [String : MLXArray]](./qwen3nextmodel/sanitize%28weights%29.md)
### Default Implementations
- [BaseLanguageModel Implementations](./qwen3nextmodel/baselanguagemodel-implementations.md)
- [ChatConventionsProviding Implementations](./qwen3nextmodel/chatconventionsproviding-implementations.md)
- [LLMModel Implementations](./qwen3nextmodel/llmmodel-implementations.md)
- [LanguageModel Implementations](./qwen3nextmodel/languagemodel-implementations.md)
- [LoRAModel Implementations](./qwen3nextmodel/loramodel-implementations.md)

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

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxllm/qwen3nextmodel)*