---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxllm/baichuanm1model"
framework: "mlx-swift-lm/MLXLLM"
---

# BaichuanM1Model

**Framework**: mlx-swift-lm/MLXLLM  
**Kind**: class  
**Role**: Class

## Declaration

```swift
class BaichuanM1Model
```

## Topics

### Initializers
- [init(BaichuanM1Configuration)](./baichuanm1model/init%28_%29.md)
### Instance Properties
- [let kvHeads: [Int]](./baichuanm1model/kvheads.md)
- [let model: BaichuanM1ModelInner](./baichuanm1model/model.md)
- [let vocabularySize: Int](./baichuanm1model/vocabularysize.md)
### Instance Methods
- [func callAsFunction(MLXArray, cache: [KVCache]?) -> MLXArray](./baichuanm1model/callasfunction%28_,cache%29.md)
- [func newCache(parameters: GenerateParameters?) throws -> [KVCache]](./baichuanm1model/newcache%28parameters%29.md)
- [func sanitize(weights: [String : MLXArray]) -> [String : MLXArray]](./baichuanm1model/sanitize%28weights%29.md)
### Default Implementations
- [BaseLanguageModel Implementations](./baichuanm1model/baselanguagemodel-implementations.md)
- [ChatConventionsProviding Implementations](./baichuanm1model/chatconventionsproviding-implementations.md)
- [LLMModel Implementations](./baichuanm1model/llmmodel-implementations.md)
- [LanguageModel Implementations](./baichuanm1model/languagemodel-implementations.md)
- [LoRAModel Implementations](./baichuanm1model/loramodel-implementations.md)

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

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxllm/baichuanm1model)*