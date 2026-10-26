---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxllm/bitnetmodel"
framework: "mlx-swift-lm/MLXLLM"
---

# BitnetModel

**Framework**: mlx-swift-lm/MLXLLM  
**Kind**: class  
**Role**: Class

## Declaration

```swift
class BitnetModel
```

## Topics

### Initializers
- [init(BitnetConfiguration)](./bitnetmodel/init%28_%29.md)
### Instance Properties
- [let kvHeads: [Int]](./bitnetmodel/kvheads.md)
- [let model: BitnetModelInner](./bitnetmodel/model.md)
- [let vocabularySize: Int](./bitnetmodel/vocabularysize.md)
### Instance Methods
- [func callAsFunction(MLXArray, cache: [KVCache]?) -> MLXArray](./bitnetmodel/callasfunction%28_,cache%29.md)
- [func sanitize(weights: [String : MLXArray]) -> [String : MLXArray]](./bitnetmodel/sanitize%28weights%29.md)
### Default Implementations
- [BaseLanguageModel Implementations](./bitnetmodel/baselanguagemodel-implementations.md)
- [ChatConventionsProviding Implementations](./bitnetmodel/chatconventionsproviding-implementations.md)
- [LLMModel Implementations](./bitnetmodel/llmmodel-implementations.md)
- [LanguageModel Implementations](./bitnetmodel/languagemodel-implementations.md)
- [LoRAModel Implementations](./bitnetmodel/loramodel-implementations.md)

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

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxllm/bitnetmodel)*