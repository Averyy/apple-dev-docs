---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxllm/qwen35textmodel"
framework: "mlx-swift-lm/MLXLLM"
---

# Qwen35TextModel

**Framework**: mlx-swift-lm/MLXLLM  
**Kind**: class  
**Role**: Class

## Declaration

```swift
class Qwen35TextModel
```

## Topics

### Initializers
- [init(Qwen35TextConfiguration)](./qwen35textmodel/init%28_%29.md)
### Instance Properties
- [let kvHeads: [Int]](./qwen35textmodel/kvheads.md)
- [let model: Qwen35TextModelInner](./qwen35textmodel/model.md)
- [let vocabularySize: Int](./qwen35textmodel/vocabularysize.md)
### Instance Methods
- [func callAsFunction(MLXArray, cache: [KVCache]?) -> MLXArray](./qwen35textmodel/callasfunction%28_,cache%29.md)
- [func callAsFunction(LMInput.Text, cache: [KVCache]?, state: LMOutput.State?) -> LMOutput](./qwen35textmodel/callasfunction%28_,cache,state%29.md)
- [func newCache(parameters: GenerateParameters?) throws -> [KVCache]](./qwen35textmodel/newcache%28parameters%29.md)
- [func nextTokenLogits(LMInput.Text, cache: [KVCache]?, state: LMOutput.State?) -> LMOutput](./qwen35textmodel/nexttokenlogits%28_,cache,state%29.md)
- [func prepare() throws](./qwen35textmodel/prepare%28%29.md)
- [func prepareCheckpoint(ModelCheckpoint) throws -> ModelCheckpoint](./qwen35textmodel/preparecheckpoint%28_%29.md)
- [func sanitize(weights: [String : MLXArray]) -> [String : MLXArray]](./qwen35textmodel/sanitize%28weights%29.md)
### Default Implementations
- [BaseLanguageModel Implementations](./qwen35textmodel/baselanguagemodel-implementations.md)
- [ChatConventionsProviding Implementations](./qwen35textmodel/chatconventionsproviding-implementations.md)
- [LLMModel Implementations](./qwen35textmodel/llmmodel-implementations.md)
- [LanguageModel Implementations](./qwen35textmodel/languagemodel-implementations.md)
- [LoRAModel Implementations](./qwen35textmodel/loramodel-implementations.md)
- [SpeculativeCacheRewindModel Implementations](./qwen35textmodel/speculativecacherewindmodel-implementations.md)

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
- MLXLMCommon.SpeculativeCacheRewindModel
- Swift.Copyable
- Swift.CustomStringConvertible
- Swift.Escapable


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxllm/qwen35textmodel)*