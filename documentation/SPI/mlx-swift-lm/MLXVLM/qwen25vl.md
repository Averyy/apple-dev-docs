---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxvlm/qwen25vl"
framework: "mlx-swift-lm/MLXVLM"
---

# Qwen25VL

**Framework**: mlx-swift-lm/MLXVLM  
**Kind**: class  
**Role**: Class

Qwen2.5VL VLM

## Declaration

```swift
class Qwen25VL
```

#### Overview

This is typically created by [`VLMModelFactory`](./vlmmodelfactory.md).

## Topics

### Initializers
- [init(Qwen25VLConfiguration)](./qwen25vl/init%28_%29.md)
### Instance Properties
- [let config: Qwen25VLConfiguration](./qwen25vl/config.md)
- [var kvHeads: [Int]](./qwen25vl/kvheads.md)
- [var loraLayers: [Module]](./qwen25vl/loralayers.md)
- [var vocabularySize: Int](./qwen25vl/vocabularysize.md)
### Instance Methods
- [func callAsFunction(LMInput.Text, cache: [any KVCache]?, state: LMOutput.State?) -> LMOutput](./qwen25vl/callasfunction%28_,cache,state%29.md)
- [func prepare(LMInput, cache: [any KVCache], state: LMOutput.State?, prefill: PrefillParameters) throws -> PrepareResult](./qwen25vl/prepare%28_,cache,state,prefill%29.md)
- [func sanitize(weights: [String : MLXArray]) -> [String : MLXArray]](./qwen25vl/sanitize%28weights%29.md)
### Default Implementations
- [BaseLanguageModel Implementations](./qwen25vl/baselanguagemodel-implementations.md)
- [ChatConventionsProviding Implementations](./qwen25vl/chatconventionsproviding-implementations.md)
- [LanguageModel Implementations](./qwen25vl/languagemodel-implementations.md)
- [LoRAModel Implementations](./qwen25vl/loramodel-implementations.md)
- [PreparedInputSplitting Implementations](./qwen25vl/preparedinputsplitting-implementations.md)

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

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxvlm/qwen25vl)*