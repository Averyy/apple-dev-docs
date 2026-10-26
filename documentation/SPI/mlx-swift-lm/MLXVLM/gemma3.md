---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxvlm/gemma3"
framework: "mlx-swift-lm/MLXVLM"
---

# Gemma3

**Framework**: mlx-swift-lm/MLXVLM  
**Kind**: class  
**Role**: Class

## Declaration

```swift
class Gemma3
```

## Topics

### Initializers
- [init(Gemma3Configuration)](./gemma3/init%28_%29.md)
### Instance Properties
- [let config: Gemma3Configuration](./gemma3/config.md)
- [var kvHeads: [Int]](./gemma3/kvheads.md)
- [var vocabularySize: Int](./gemma3/vocabularysize.md)
### Instance Methods
- [func callAsFunction(MLXArray, cache: [any KVCache]?) -> MLXArray](./gemma3/callasfunction%28_,cache%29.md)
- [func newCache(parameters: GenerateParameters?) throws -> [any KVCache]](./gemma3/newcache%28parameters%29.md)
  Create cache with proper types for each layer
- [func prepare(LMInput, cache: [any KVCache], state: LMOutput.State?, prefill: PrefillParameters) throws -> PrepareResult](./gemma3/prepare%28_,cache,state,prefill%29.md)
- [func sanitize(weights: [String : MLXArray]) -> [String : MLXArray]](./gemma3/sanitize%28weights%29.md)
### Default Implementations
- [BaseLanguageModel Implementations](./gemma3/baselanguagemodel-implementations.md)
- [ChatConventionsProviding Implementations](./gemma3/chatconventionsproviding-implementations.md)
- [LanguageModel Implementations](./gemma3/languagemodel-implementations.md)
- [LoRAModel Implementations](./gemma3/loramodel-implementations.md)

## Relationships

### Inherits From
- MLXNN.Module
### Conforms To
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
- [VLMModel](./vlmmodel.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxvlm/gemma3)*