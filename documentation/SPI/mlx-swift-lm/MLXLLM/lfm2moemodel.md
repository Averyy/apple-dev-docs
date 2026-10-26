---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxllm/lfm2moemodel"
framework: "mlx-swift-lm/MLXLLM"
---

# LFM2MoEModel

**Framework**: mlx-swift-lm/MLXLLM  
**Kind**: class  
**Role**: Class

## Declaration

```swift
class LFM2MoEModel
```

## Topics

### Initializers
- [init(LFM2MoEConfiguration)](./lfm2moemodel/init%28_%29.md)
### Instance Properties
- [let kvHeads: [Int]](./lfm2moemodel/kvheads.md)
- [let model: LFM2MoEModelInner](./lfm2moemodel/model.md)
- [let vocabularySize: Int](./lfm2moemodel/vocabularysize.md)
### Instance Methods
- [func callAsFunction(MLXArray, cache: [KVCache]?) -> MLXArray](./lfm2moemodel/callasfunction%28_,cache%29.md)
- [func newCache(parameters: GenerateParameters?) throws -> [KVCache]](./lfm2moemodel/newcache%28parameters%29.md)
- [func sanitize(weights: [String : MLXArray]) -> [String : MLXArray]](./lfm2moemodel/sanitize%28weights%29.md)
### Default Implementations
- [BaseLanguageModel Implementations](./lfm2moemodel/baselanguagemodel-implementations.md)
- [ChatConventionsProviding Implementations](./lfm2moemodel/chatconventionsproviding-implementations.md)
- [LLMModel Implementations](./lfm2moemodel/llmmodel-implementations.md)
- [LanguageModel Implementations](./lfm2moemodel/languagemodel-implementations.md)
- [LoRAModel Implementations](./lfm2moemodel/loramodel-implementations.md)

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

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxllm/lfm2moemodel)*