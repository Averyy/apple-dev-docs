---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxllm/afmoemodel"
framework: "mlx-swift-lm/MLXLLM"
---

# AfMoEModel

**Framework**: mlx-swift-lm/MLXLLM  
**Kind**: class  
**Role**: Class

## Declaration

```swift
class AfMoEModel
```

## Topics

### Initializers
- [init(AfMoEConfiguration)](./afmoemodel/init%28_%29.md)
### Instance Properties
- [let kvHeads: [Int]](./afmoemodel/kvheads.md)
- [let vocabularySize: Int](./afmoemodel/vocabularysize.md)
### Instance Methods
- [func callAsFunction(MLXArray, cache: [KVCache]?) -> MLXArray](./afmoemodel/callasfunction%28_,cache%29.md)
- [func newCache(parameters: GenerateParameters?) throws -> [KVCache]](./afmoemodel/newcache%28parameters%29.md)
- [func sanitize(weights: [String : MLXArray]) -> [String : MLXArray]](./afmoemodel/sanitize%28weights%29.md)
### Default Implementations
- [BaseLanguageModel Implementations](./afmoemodel/baselanguagemodel-implementations.md)
- [ChatConventionsProviding Implementations](./afmoemodel/chatconventionsproviding-implementations.md)
- [LLMModel Implementations](./afmoemodel/llmmodel-implementations.md)
- [LanguageModel Implementations](./afmoemodel/languagemodel-implementations.md)
- [LoRAModel Implementations](./afmoemodel/loramodel-implementations.md)

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

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxllm/afmoemodel)*