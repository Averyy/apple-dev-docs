---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxllm/glm4moemodel"
framework: "mlx-swift-lm/MLXLLM"
---

# GLM4MoEModel

**Framework**: mlx-swift-lm/MLXLLM  
**Kind**: class  
**Role**: Class

## Declaration

```swift
class GLM4MoEModel
```

## Topics

### Initializers
- [init(GLM4MoEConfiguration)](./glm4moemodel/init%28_%29.md)
### Instance Properties
- [let kvHeads: [Int]](./glm4moemodel/kvheads.md)
- [let model: GLM4MoEModelInner](./glm4moemodel/model.md)
- [let vocabularySize: Int](./glm4moemodel/vocabularysize.md)
### Instance Methods
- [func callAsFunction(MLXArray, cache: [KVCache]?) -> MLXArray](./glm4moemodel/callasfunction%28_,cache%29.md)
- [func sanitize(weights: [String : MLXArray]) -> [String : MLXArray]](./glm4moemodel/sanitize%28weights%29.md)
### Default Implementations
- [BaseLanguageModel Implementations](./glm4moemodel/baselanguagemodel-implementations.md)
- [ChatConventionsProviding Implementations](./glm4moemodel/chatconventionsproviding-implementations.md)
- [LLMModel Implementations](./glm4moemodel/llmmodel-implementations.md)
- [LanguageModel Implementations](./glm4moemodel/languagemodel-implementations.md)
- [LoRAModel Implementations](./glm4moemodel/loramodel-implementations.md)

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

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxllm/glm4moemodel)*