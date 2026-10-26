---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxvlm/qwen3vlmoe"
framework: "mlx-swift-lm/MLXVLM"
---

# Qwen3VLMoE

**Framework**: mlx-swift-lm/MLXVLM  
**Kind**: class  
**Role**: Class

## Declaration

```swift
final class Qwen3VLMoE
```

## Topics

### Initializers
- [init(Qwen3VLMoEConfiguration)](./qwen3vlmoe/init%28_%29.md)
### Instance Properties
- [let config: Qwen3VLMoEConfiguration](./qwen3vlmoe/config.md)
- [var kvHeads: [Int]](./qwen3vlmoe/kvheads.md)
- [var loraLayers: [Module]](./qwen3vlmoe/loralayers.md)
- [var vocabularySize: Int](./qwen3vlmoe/vocabularysize.md)
### Instance Methods
- [func callAsFunction(LMInput.Text, cache: [any KVCache]?, state: LMOutput.State?) -> LMOutput](./qwen3vlmoe/callasfunction%28_,cache,state%29.md)
- [func prepare(LMInput, cache: [any KVCache], state: LMOutput.State?, prefill: PrefillParameters) throws -> PrepareResult](./qwen3vlmoe/prepare%28_,cache,state,prefill%29.md)
- [func sanitize(weights: [String : MLXArray]) -> [String : MLXArray]](./qwen3vlmoe/sanitize%28weights%29.md)
### Default Implementations
- [BaseLanguageModel Implementations](./qwen3vlmoe/baselanguagemodel-implementations.md)
- [ChatConventionsProviding Implementations](./qwen3vlmoe/chatconventionsproviding-implementations.md)
- [LanguageModel Implementations](./qwen3vlmoe/languagemodel-implementations.md)
- [LoRAModel Implementations](./qwen3vlmoe/loramodel-implementations.md)

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
- Swift.CustomStringConvertible
- [VLMModel](./vlmmodel.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxvlm/qwen3vlmoe)*