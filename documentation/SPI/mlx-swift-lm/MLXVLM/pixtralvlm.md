---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxvlm/pixtralvlm"
framework: "mlx-swift-lm/MLXVLM"
---

# PixtralVLM

**Framework**: mlx-swift-lm/MLXVLM  
**Kind**: class  
**Role**: Class

## Declaration

```swift
class PixtralVLM
```

## Topics

### Initializers
- [init(PixtralConfiguration)](./pixtralvlm/init%28_%29.md)
### Instance Properties
- [let config: PixtralConfiguration](./pixtralvlm/config.md)
- [var kvHeads: [Int]](./pixtralvlm/kvheads.md)
- [var vocabularySize: Int](./pixtralvlm/vocabularysize.md)
### Instance Methods
- [func callAsFunction(MLXArray, cache: [KVCache]?) -> MLXArray](./pixtralvlm/callasfunction%28_,cache%29.md)
- [func newCache(parameters: GenerateParameters?) throws -> [KVCache]](./pixtralvlm/newcache%28parameters%29.md)
- [func prepare(LMInput, cache: [KVCache], state: LMOutput.State?, prefill: PrefillParameters) throws -> PrepareResult](./pixtralvlm/prepare%28_,cache,state,prefill%29.md)
- [func sanitize(weights: [String : MLXArray]) -> [String : MLXArray]](./pixtralvlm/sanitize%28weights%29.md)
### Default Implementations
- [BaseLanguageModel Implementations](./pixtralvlm/baselanguagemodel-implementations.md)
- [ChatConventionsProviding Implementations](./pixtralvlm/chatconventionsproviding-implementations.md)
- [LanguageModel Implementations](./pixtralvlm/languagemodel-implementations.md)
- [LoRAModel Implementations](./pixtralvlm/loramodel-implementations.md)

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

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxvlm/pixtralvlm)*