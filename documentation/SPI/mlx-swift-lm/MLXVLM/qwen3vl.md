---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxvlm/qwen3vl"
framework: "mlx-swift-lm/MLXVLM"
---

# Qwen3VL

**Framework**: mlx-swift-lm/MLXVLM  
**Kind**: class  
**Role**: Class

## Declaration

```swift
final class Qwen3VL
```

## Topics

### Initializers
- [init(Qwen3VLConfiguration)](./qwen3vl/init%28_%29.md)
### Instance Properties
- [let config: Qwen3VLConfiguration](./qwen3vl/config.md)
- [var kvHeads: [Int]](./qwen3vl/kvheads.md)
- [var loraLayers: [Module]](./qwen3vl/loralayers.md)
- [var vocabularySize: Int](./qwen3vl/vocabularysize.md)
### Instance Methods
- [func callAsFunction(LMInput.Text, cache: [any KVCache]?, state: LMOutput.State?) -> LMOutput](./qwen3vl/callasfunction%28_,cache,state%29.md)
- [func prepare(LMInput, cache: [any KVCache], state: LMOutput.State?, prefill: PrefillParameters) throws -> PrepareResult](./qwen3vl/prepare%28_,cache,state,prefill%29.md)
- [func sanitize(weights: [String : MLXArray]) -> [String : MLXArray]](./qwen3vl/sanitize%28weights%29.md)
### Default Implementations
- [BaseLanguageModel Implementations](./qwen3vl/baselanguagemodel-implementations.md)
- [ChatConventionsProviding Implementations](./qwen3vl/chatconventionsproviding-implementations.md)
- [LanguageModel Implementations](./qwen3vl/languagemodel-implementations.md)
- [LoRAModel Implementations](./qwen3vl/loramodel-implementations.md)
- [PreparedInputSplitting Implementations](./qwen3vl/preparedinputsplitting-implementations.md)

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
- MLXLMCommon.PreparedInputSplitting
- Swift.Copyable
- Swift.CustomStringConvertible
- Swift.Escapable
- [VLMModel](./vlmmodel.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxvlm/qwen3vl)*