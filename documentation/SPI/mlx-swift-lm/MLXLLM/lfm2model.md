---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxllm/lfm2model"
framework: "mlx-swift-lm/MLXLLM"
---

# LFM2Model

**Framework**: mlx-swift-lm/MLXLLM  
**Kind**: class  
**Role**: Class

## Declaration

```swift
class LFM2Model
```

## Topics

### Initializers
- [init(LFM2Configuration)](./lfm2model/init%28_%29.md)
### Instance Properties
- [let kvHeads: [Int]](./lfm2model/kvheads.md)
- [let model: LFM2ModelInner](./lfm2model/model.md)
- [let vocabularySize: Int](./lfm2model/vocabularysize.md)
### Instance Methods
- [func callAsFunction(MLXArray, cache: [KVCache]?) -> MLXArray](./lfm2model/callasfunction%28_,cache%29.md)
- [func newCache(parameters: GenerateParameters?) throws -> [KVCache]](./lfm2model/newcache%28parameters%29.md)
- [func sanitize(weights: [String : MLXArray]) -> [String : MLXArray]](./lfm2model/sanitize%28weights%29.md)
### Default Implementations
- [BaseLanguageModel Implementations](./lfm2model/baselanguagemodel-implementations.md)
- [ChatConventionsProviding Implementations](./lfm2model/chatconventionsproviding-implementations.md)
- [LLMModel Implementations](./lfm2model/llmmodel-implementations.md)
- [LanguageModel Implementations](./lfm2model/languagemodel-implementations.md)
- [LoRAModel Implementations](./lfm2model/loramodel-implementations.md)

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

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxllm/lfm2model)*