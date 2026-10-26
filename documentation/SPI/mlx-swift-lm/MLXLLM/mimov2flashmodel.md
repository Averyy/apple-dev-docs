---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxllm/mimov2flashmodel"
framework: "mlx-swift-lm/MLXLLM"
---

# MiMoV2FlashModel

**Framework**: mlx-swift-lm/MLXLLM  
**Kind**: class  
**Role**: Class

## Declaration

```swift
class MiMoV2FlashModel
```

## Topics

### Initializers
- [init(MiMoV2FlashConfiguration)](./mimov2flashmodel/init%28_%29.md)
### Instance Properties
- [let kvHeads: [Int]](./mimov2flashmodel/kvheads.md)
- [let model: MiMoV2FlashModelInner](./mimov2flashmodel/model.md)
- [let modelType: String](./mimov2flashmodel/modeltype.md)
- [let vocabularySize: Int](./mimov2flashmodel/vocabularysize.md)
### Instance Methods
- [func callAsFunction(MLXArray, cache: [KVCache]?) -> MLXArray](./mimov2flashmodel/callasfunction%28_,cache%29.md)
- [func newCache(parameters: GenerateParameters?) throws -> [KVCache]](./mimov2flashmodel/newcache%28parameters%29.md)
- [func sanitize(weights: [String : MLXArray]) -> [String : MLXArray]](./mimov2flashmodel/sanitize%28weights%29.md)
### Default Implementations
- [BaseLanguageModel Implementations](./mimov2flashmodel/baselanguagemodel-implementations.md)
- [ChatConventionsProviding Implementations](./mimov2flashmodel/chatconventionsproviding-implementations.md)
- [LLMModel Implementations](./mimov2flashmodel/llmmodel-implementations.md)
- [LanguageModel Implementations](./mimov2flashmodel/languagemodel-implementations.md)
- [LoRAModel Implementations](./mimov2flashmodel/loramodel-implementations.md)

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

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxllm/mimov2flashmodel)*