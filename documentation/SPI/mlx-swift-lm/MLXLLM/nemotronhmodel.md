---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxllm/nemotronhmodel"
framework: "mlx-swift-lm/MLXLLM"
---

# NemotronHModel

**Framework**: mlx-swift-lm/MLXLLM  
**Kind**: class  
**Role**: Class

## Declaration

```swift
class NemotronHModel
```

## Topics

### Initializers
- [init(NemotronHConfiguration)](./nemotronhmodel/init%28_%29.md)
### Instance Properties
- [var castPredicate: ((String) -> Bool)?](./nemotronhmodel/castpredicate.md)
  Predicate for casting: some parameters should stay in float32
- [let kvHeads: [Int]](./nemotronhmodel/kvheads.md)
- [var loraLayers: [Module]](./nemotronhmodel/loralayers.md)
- [let vocabularySize: Int](./nemotronhmodel/vocabularysize.md)
### Instance Methods
- [func callAsFunction(MLXArray, cache: [KVCache]?) -> MLXArray](./nemotronhmodel/callasfunction%28_,cache%29.md)
- [func newCache(parameters: GenerateParameters?) throws -> [KVCache]](./nemotronhmodel/newcache%28parameters%29.md)
- [func sanitize(weights: [String : MLXArray]) -> [String : MLXArray]](./nemotronhmodel/sanitize%28weights%29.md)
### Default Implementations
- [BaseLanguageModel Implementations](./nemotronhmodel/baselanguagemodel-implementations.md)
- [ChatConventionsProviding Implementations](./nemotronhmodel/chatconventionsproviding-implementations.md)
- [LLMModel Implementations](./nemotronhmodel/llmmodel-implementations.md)
- [LanguageModel Implementations](./nemotronhmodel/languagemodel-implementations.md)
- [LoRAModel Implementations](./nemotronhmodel/loramodel-implementations.md)

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
- Swift.CustomStringConvertible


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxllm/nemotronhmodel)*