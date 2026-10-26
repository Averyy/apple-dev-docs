---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxvlm/qwen35"
framework: "mlx-swift-lm/MLXVLM"
---

# Qwen35

**Framework**: mlx-swift-lm/MLXVLM  
**Kind**: class  
**Role**: Class

## Declaration

```swift
class Qwen35
```

## Topics

### Initializers
- [init(Qwen35Configuration)](./qwen35/init%28_%29.md)
### Instance Properties
- [let config: Qwen35Configuration](./qwen35/config.md)
- [var loraLayers: [Module]](./qwen35/loralayers.md)
- [var vocabularySize: Int](./qwen35/vocabularysize.md)
### Instance Methods
- [func callAsFunction(LMInput.Text, cache: [any KVCache]?, state: LMOutput.State?) -> LMOutput](./qwen35/callasfunction%28_,cache,state%29.md)
- [func newCache(parameters: GenerateParameters?) throws -> [KVCache]](./qwen35/newcache%28parameters%29.md)
- [func prepare() throws](./qwen35/prepare%28%29.md)
- [func prepare(LMInput, cache: [any KVCache], state: LMOutput.State?, prefill: PrefillParameters) throws -> PrepareResult](./qwen35/prepare%28_,cache,state,prefill%29.md)
- [func prepareCheckpoint(ModelCheckpoint) throws -> ModelCheckpoint](./qwen35/preparecheckpoint%28_%29.md)
- [func sanitize(weights: [String : MLXArray]) throws -> [String : MLXArray]](./qwen35/sanitize%28weights%29.md)
- [func sanitize(weights: [String : MLXArray], metadata: [String : String]) throws -> [String : MLXArray]](./qwen35/sanitize%28weights,metadata%29.md)
### Default Implementations
- [BaseLanguageModel Implementations](./qwen35/baselanguagemodel-implementations.md)
- [ChatConventionsProviding Implementations](./qwen35/chatconventionsproviding-implementations.md)
- [LanguageModel Implementations](./qwen35/languagemodel-implementations.md)
- [LoRAModel Implementations](./qwen35/loramodel-implementations.md)
- [ModelComponentsProviding Implementations](./qwen35/modelcomponentsproviding-implementations.md)
- [SpeculativeCacheRewindModel Implementations](./qwen35/speculativecacherewindmodel-implementations.md)

## Relationships

### Inherits From
- MLXNN.Module
### Inherited By
- [Qwen35MoE](./qwen35moe.md)
### Conforms To
- MLX.Evaluatable
- MLX.IndentedDescription
- MLX.Updatable
- MLXLMCommon.BaseLanguageModel
- MLXLMCommon.ChatConventionsProviding
- MLXLMCommon.LanguageModel
- MLXLMCommon.LoRAModel
- MLXLMCommon.ModelComponentsProviding
- MLXLMCommon.SpeculativeCacheRewindModel
- Swift.Copyable
- Swift.CustomStringConvertible
- Swift.Escapable
- [VLMModel](./vlmmodel.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxvlm/qwen35)*