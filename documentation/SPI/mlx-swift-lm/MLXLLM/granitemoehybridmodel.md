---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxllm/granitemoehybridmodel"
framework: "mlx-swift-lm/MLXLLM"
---

# GraniteMoeHybridModel

**Framework**: mlx-swift-lm/MLXLLM  
**Kind**: class  
**Role**: Class

## Declaration

```swift
class GraniteMoeHybridModel
```

## Topics

### Initializers
- [init(GraniteMoeHybridConfiguration)](./granitemoehybridmodel/init%28_%29.md)
### Instance Properties
- [let kvHeads: [Int]](./granitemoehybridmodel/kvheads.md)
- [var loraLayers: [Module]](./granitemoehybridmodel/loralayers.md)
- [let model: GraniteMoeHybridModelInner](./granitemoehybridmodel/model.md)
- [let vocabularySize: Int](./granitemoehybridmodel/vocabularysize.md)
### Instance Methods
- [func callAsFunction(MLXArray, cache: [KVCache]?) -> MLXArray](./granitemoehybridmodel/callasfunction%28_,cache%29.md)
- [func newCache(parameters: GenerateParameters?) throws -> [KVCache]](./granitemoehybridmodel/newcache%28parameters%29.md)
- [func sanitize(weights: [String : MLXArray]) -> [String : MLXArray]](./granitemoehybridmodel/sanitize%28weights%29.md)
### Default Implementations
- [BaseLanguageModel Implementations](./granitemoehybridmodel/baselanguagemodel-implementations.md)
- [ChatConventionsProviding Implementations](./granitemoehybridmodel/chatconventionsproviding-implementations.md)
- [LLMModel Implementations](./granitemoehybridmodel/llmmodel-implementations.md)
- [LanguageModel Implementations](./granitemoehybridmodel/languagemodel-implementations.md)
- [LoRAModel Implementations](./granitemoehybridmodel/loramodel-implementations.md)

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

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxllm/granitemoehybridmodel)*