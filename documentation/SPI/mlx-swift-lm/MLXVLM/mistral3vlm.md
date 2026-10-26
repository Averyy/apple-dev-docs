---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxvlm/mistral3vlm"
framework: "mlx-swift-lm/MLXVLM"
---

# Mistral3VLM

**Framework**: mlx-swift-lm/MLXVLM  
**Kind**: class  
**Role**: Class

## Declaration

```swift
class Mistral3VLM
```

## Topics

### Initializers
- [init(Mistral3VLMConfiguration)](./mistral3vlm/init%28_%29.md)
### Instance Properties
- [let config: Mistral3VLMConfiguration](./mistral3vlm/config.md)
- [var kvHeads: [Int]](./mistral3vlm/kvheads.md)
- [var vocabularySize: Int](./mistral3vlm/vocabularysize.md)
### Instance Methods
- [func callAsFunction(MLXArray, cache: [KVCache]?) -> MLXArray](./mistral3vlm/callasfunction%28_,cache%29.md)
- [func newCache(parameters: GenerateParameters?) throws -> [KVCache]](./mistral3vlm/newcache%28parameters%29.md)
- [func prepare(LMInput, cache: [KVCache], state: LMOutput.State?, prefill: PrefillParameters) throws -> PrepareResult](./mistral3vlm/prepare%28_,cache,state,prefill%29.md)
- [func sanitize(weights: [String : MLXArray]) -> [String : MLXArray]](./mistral3vlm/sanitize%28weights%29.md)
### Default Implementations
- [BaseLanguageModel Implementations](./mistral3vlm/baselanguagemodel-implementations.md)
- [ChatConventionsProviding Implementations](./mistral3vlm/chatconventionsproviding-implementations.md)
- [LanguageModel Implementations](./mistral3vlm/languagemodel-implementations.md)
- [LoRAModel Implementations](./mistral3vlm/loramodel-implementations.md)

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

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxvlm/mistral3vlm)*