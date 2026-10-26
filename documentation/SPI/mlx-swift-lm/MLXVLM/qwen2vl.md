---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxvlm/qwen2vl"
framework: "mlx-swift-lm/MLXVLM"
---

# Qwen2VL

**Framework**: mlx-swift-lm/MLXVLM  
**Kind**: class  
**Role**: Class

Qwen2VL VLM

## Declaration

```swift
class Qwen2VL
```

#### Overview

This is typically created by [`VLMModelFactory`](./vlmmodelfactory.md).

## Topics

### Initializers
- [init(Qwen2VLConfiguration)](./qwen2vl/init%28_%29.md)
### Instance Properties
- [let config: Qwen2VLConfiguration](./qwen2vl/config.md)
- [var kvHeads: [Int]](./qwen2vl/kvheads.md)
- [var loraLayers: [Module]](./qwen2vl/loralayers.md)
- [var vocabularySize: Int](./qwen2vl/vocabularysize.md)
### Instance Methods
- [func callAsFunction(LMInput.Text, cache: [any KVCache]?, state: LMOutput.State?) -> LMOutput](./qwen2vl/callasfunction%28_,cache,state%29.md)
- [func prepare(LMInput, cache: [any KVCache], state: LMOutput.State?, prefill: PrefillParameters) throws -> PrepareResult](./qwen2vl/prepare%28_,cache,state,prefill%29.md)
- [func sanitize(weights: [String : MLXArray]) -> [String : MLXArray]](./qwen2vl/sanitize%28weights%29.md)
### Default Implementations
- [BaseLanguageModel Implementations](./qwen2vl/baselanguagemodel-implementations.md)
- [ChatConventionsProviding Implementations](./qwen2vl/chatconventionsproviding-implementations.md)
- [LanguageModel Implementations](./qwen2vl/languagemodel-implementations.md)
- [LoRAModel Implementations](./qwen2vl/loramodel-implementations.md)

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

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxvlm/qwen2vl)*