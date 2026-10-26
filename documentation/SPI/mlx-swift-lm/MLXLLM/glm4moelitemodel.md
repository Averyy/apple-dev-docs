---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxllm/glm4moelitemodel"
framework: "mlx-swift-lm/MLXLLM"
---

# GLM4MoELiteModel

**Framework**: mlx-swift-lm/MLXLLM  
**Kind**: class  
**Role**: Class

## Declaration

```swift
class GLM4MoELiteModel
```

## Topics

### Initializers
- [init(GLM4MoELiteConfiguration)](./glm4moelitemodel/init%28_%29.md)
### Instance Properties
- [let kvHeads: [Int]](./glm4moelitemodel/kvheads.md)
- [let model: GLM4MoELiteModelInner](./glm4moelitemodel/model.md)
- [let vocabularySize: Int](./glm4moelitemodel/vocabularysize.md)
### Instance Methods
- [func callAsFunction(MLXArray, cache: [KVCache]?) -> MLXArray](./glm4moelitemodel/callasfunction%28_,cache%29.md)
- [func sanitize(weights: [String : MLXArray]) -> [String : MLXArray]](./glm4moelitemodel/sanitize%28weights%29.md)
### Default Implementations
- [BaseLanguageModel Implementations](./glm4moelitemodel/baselanguagemodel-implementations.md)
- [ChatConventionsProviding Implementations](./glm4moelitemodel/chatconventionsproviding-implementations.md)
- [LLMModel Implementations](./glm4moelitemodel/llmmodel-implementations.md)
- [LanguageModel Implementations](./glm4moelitemodel/languagemodel-implementations.md)
- [LoRAModel Implementations](./glm4moelitemodel/loramodel-implementations.md)

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

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxllm/glm4moelitemodel)*