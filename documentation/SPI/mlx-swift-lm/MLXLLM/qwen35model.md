---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxllm/qwen35model"
framework: "mlx-swift-lm/MLXLLM"
---

# Qwen35Model

**Framework**: mlx-swift-lm/MLXLLM  
**Kind**: class  
**Role**: Class

## Declaration

```swift
class Qwen35Model
```

## Topics

### Initializers
- [init(Qwen35Configuration)](./qwen35model/init%28_%29.md)
### Instance Properties
- [var configuration: Qwen35TextConfiguration](./qwen35model/configuration.md)
  The text backbone’s geometry.
- [let kvHeads: [Int]](./qwen35model/kvheads.md)
- [let vocabularySize: Int](./qwen35model/vocabularysize.md)
### Instance Methods
- [func callAsFunction(MLXArray, cache: [KVCache]?) -> MLXArray](./qwen35model/callasfunction%28_,cache%29.md)
- [func callAsFunction(LMInput.Text, cache: [KVCache]?, state: LMOutput.State?) -> LMOutput](./qwen35model/callasfunction%28_,cache,state%29.md)
- [func newCache(parameters: GenerateParameters?) throws -> [KVCache]](./qwen35model/newcache%28parameters%29.md)
- [func nextTokenLogits(LMInput.Text, cache: [KVCache]?, state: LMOutput.State?) -> LMOutput](./qwen35model/nexttokenlogits%28_,cache,state%29.md)
- [func prepare() throws](./qwen35model/prepare%28%29.md)
- [func prepareCheckpoint(ModelCheckpoint) throws -> ModelCheckpoint](./qwen35model/preparecheckpoint%28_%29.md)
- [func sanitize(weights: [String : MLXArray]) throws -> [String : MLXArray]](./qwen35model/sanitize%28weights%29.md)
### Default Implementations
- [BaseLanguageModel Implementations](./qwen35model/baselanguagemodel-implementations.md)
- [ChatConventionsProviding Implementations](./qwen35model/chatconventionsproviding-implementations.md)
- [LLMModel Implementations](./qwen35model/llmmodel-implementations.md)
- [LanguageModel Implementations](./qwen35model/languagemodel-implementations.md)
- [LoRAModel Implementations](./qwen35model/loramodel-implementations.md)
- [SpeculativeCacheRewindModel Implementations](./qwen35model/speculativecacherewindmodel-implementations.md)

## Relationships

### Inherits From
- MLXNN.Module
### Inherited By
- [Qwen35MoEModel](./qwen35moemodel.md)
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
- MLXLMCommon.SpeculativeCacheRewindModel
- Swift.Copyable
- Swift.CustomStringConvertible
- Swift.Escapable


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxllm/qwen35model)*