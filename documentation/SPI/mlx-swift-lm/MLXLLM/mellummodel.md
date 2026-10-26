---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxllm/mellummodel"
framework: "mlx-swift-lm/MLXLLM"
---

# MellumModel

**Framework**: mlx-swift-lm/MLXLLM  
**Kind**: class  
**Role**: Class

## Declaration

```swift
final class MellumModel
```

## Topics

### Initializers
- [init(MellumConfiguration)](./mellummodel/init%28_%29.md)
### Instance Properties
- [let kvHeads: [Int]](./mellummodel/kvheads.md)
- [let model: MellumModelInner](./mellummodel/model.md)
- [let vocabularySize: Int](./mellummodel/vocabularysize.md)
### Instance Methods
- [func callAsFunction(MLXArray, cache: [KVCache]?) -> MLXArray](./mellummodel/callasfunction%28_,cache%29.md)
- [func newCache(parameters: GenerateParameters?) throws -> [KVCache]](./mellummodel/newcache%28parameters%29.md)
- [func nextTokenLogits(LMInput.Text, cache: [KVCache]?, state: LMOutput.State?) -> LMOutput](./mellummodel/nexttokenlogits%28_,cache,state%29.md)
- [func sanitize(weights: [String : MLXArray]) -> [String : MLXArray]](./mellummodel/sanitize%28weights%29.md)
### Default Implementations
- [BaseLanguageModel Implementations](./mellummodel/baselanguagemodel-implementations.md)
- [ChatConventionsProviding Implementations](./mellummodel/chatconventionsproviding-implementations.md)
- [LLMModel Implementations](./mellummodel/llmmodel-implementations.md)
- [LanguageModel Implementations](./mellummodel/languagemodel-implementations.md)
- [LoRAModel Implementations](./mellummodel/loramodel-implementations.md)

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

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxllm/mellummodel)*