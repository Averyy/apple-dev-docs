---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxllm/qwen3moemodel"
framework: "mlx-swift-lm/MLXLLM"
---

# Qwen3MoEModel

**Framework**: mlx-swift-lm/MLXLLM  
**Kind**: class  
**Role**: Class

## Declaration

```swift
class Qwen3MoEModel
```

## Topics

### Initializers
- [init(Qwen3MoEConfiguration)](./qwen3moemodel/init%28_%29.md)
### Instance Properties
- [let kvHeads: [Int]](./qwen3moemodel/kvheads.md)
- [let model: Qwen3MoEModelInner](./qwen3moemodel/model.md)
- [let vocabularySize: Int](./qwen3moemodel/vocabularysize.md)
### Instance Methods
- [func callAsFunction(MLXArray, cache: [KVCache]?) -> MLXArray](./qwen3moemodel/callasfunction%28_,cache%29.md)
- [func sanitize(weights: [String : MLXArray]) -> [String : MLXArray]](./qwen3moemodel/sanitize%28weights%29.md)
### Default Implementations
- [BaseLanguageModel Implementations](./qwen3moemodel/baselanguagemodel-implementations.md)
- [ChatConventionsProviding Implementations](./qwen3moemodel/chatconventionsproviding-implementations.md)
- [LLMModel Implementations](./qwen3moemodel/llmmodel-implementations.md)
- [LanguageModel Implementations](./qwen3moemodel/languagemodel-implementations.md)
- [LoRAModel Implementations](./qwen3moemodel/loramodel-implementations.md)

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

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxllm/qwen3moemodel)*