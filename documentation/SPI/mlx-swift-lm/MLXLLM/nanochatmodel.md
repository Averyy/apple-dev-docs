---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxllm/nanochatmodel"
framework: "mlx-swift-lm/MLXLLM"
---

# NanoChatModel

**Framework**: mlx-swift-lm/MLXLLM  
**Kind**: class  
**Role**: Class

## Declaration

```swift
final class NanoChatModel
```

## Topics

### Initializers
- [init(NanoChatConfiguration)](./nanochatmodel/init%28_%29.md)
### Instance Properties
- [let kvHeads: [Int]](./nanochatmodel/kvheads.md)
- [let modelType: String](./nanochatmodel/modeltype.md)
- [var transformer: NanoChatModelInner](./nanochatmodel/transformer.md)
- [let vocabularySize: Int](./nanochatmodel/vocabularysize.md)
### Instance Methods
- [func callAsFunction(MLXArray, cache: [KVCache]?) -> MLXArray](./nanochatmodel/callasfunction%28_,cache%29.md)
### Default Implementations
- [BaseLanguageModel Implementations](./nanochatmodel/baselanguagemodel-implementations.md)
- [ChatConventionsProviding Implementations](./nanochatmodel/chatconventionsproviding-implementations.md)
- [LLMModel Implementations](./nanochatmodel/llmmodel-implementations.md)
- [LanguageModel Implementations](./nanochatmodel/languagemodel-implementations.md)
- [LoRAModel Implementations](./nanochatmodel/loramodel-implementations.md)

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

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxllm/nanochatmodel)*