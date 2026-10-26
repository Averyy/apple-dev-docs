---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxllm/nanbeigemodel"
framework: "mlx-swift-lm/MLXLLM"
---

# NanbeigeModel

**Framework**: mlx-swift-lm/MLXLLM  
**Kind**: class  
**Role**: Class

## Declaration

```swift
class NanbeigeModel
```

## Topics

### Initializers
- [init(NanbeigeConfiguration)](./nanbeigemodel/init%28_%29.md)
### Instance Properties
- [let model: NanbeigeModelInner](./nanbeigemodel/model.md)
- [let vocabularySize: Int](./nanbeigemodel/vocabularysize.md)
### Instance Methods
- [func callAsFunction(MLXArray, cache: [KVCache]?) -> MLXArray](./nanbeigemodel/callasfunction%28_,cache%29.md)
- [func newCache(parameters: GenerateParameters?) throws -> [KVCache]](./nanbeigemodel/newcache%28parameters%29.md)
- [func sanitize(weights: [String : MLXArray]) -> [String : MLXArray]](./nanbeigemodel/sanitize%28weights%29.md)
### Default Implementations
- [BaseLanguageModel Implementations](./nanbeigemodel/baselanguagemodel-implementations.md)
- [ChatConventionsProviding Implementations](./nanbeigemodel/chatconventionsproviding-implementations.md)
- [LLMModel Implementations](./nanbeigemodel/llmmodel-implementations.md)
- [LanguageModel Implementations](./nanbeigemodel/languagemodel-implementations.md)
- [LoRAModel Implementations](./nanbeigemodel/loramodel-implementations.md)

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
- MLXLMCommon.LanguageModel
- MLXLMCommon.LoRAModel
- Swift.Copyable
- Swift.CustomStringConvertible
- Swift.Escapable


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxllm/nanbeigemodel)*