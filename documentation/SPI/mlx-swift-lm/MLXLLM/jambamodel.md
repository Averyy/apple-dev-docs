---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxllm/jambamodel"
framework: "mlx-swift-lm/MLXLLM"
---

# JambaModel

**Framework**: mlx-swift-lm/MLXLLM  
**Kind**: class  
**Role**: Class

## Declaration

```swift
class JambaModel
```

## Topics

### Initializers
- [init(JambaConfiguration)](./jambamodel/init%28_%29.md)
### Instance Properties
- [let kvHeads: [Int]](./jambamodel/kvheads.md)
- [var layers: [Module]](./jambamodel/layers.md)
- [let model: JambaModelInner](./jambamodel/model.md)
### Instance Methods
- [func callAsFunction(MLXArray, cache: [KVCache]?) -> MLXArray](./jambamodel/callasfunction%28_,cache%29.md)
- [func makeCache() -> [KVCache]](./jambamodel/makecache%28%29.md)
- [func newCache(parameters: GenerateParameters?) throws -> [KVCache]](./jambamodel/newcache%28parameters%29.md)
- [func sanitize(weights: [String : MLXArray]) -> [String : MLXArray]](./jambamodel/sanitize%28weights%29.md)
### Default Implementations
- [BaseLanguageModel Implementations](./jambamodel/baselanguagemodel-implementations.md)
- [ChatConventionsProviding Implementations](./jambamodel/chatconventionsproviding-implementations.md)
- [LLMModel Implementations](./jambamodel/llmmodel-implementations.md)
- [LanguageModel Implementations](./jambamodel/languagemodel-implementations.md)
- [LoRAModel Implementations](./jambamodel/loramodel-implementations.md)

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

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxllm/jambamodel)*