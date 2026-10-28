---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxvlm/lfm2vl"
framework: "mlx-swift-lm/MLXVLM"
---

# LFM2VL

**Framework**: mlx-swift-lm/MLXVLM  
**Kind**: class  
**Role**: Class

LFM2 VL VLM

## Declaration

```swift
class LFM2VL
```

## Overview

This is typically created by [`VLMModelFactory`](./vlmmodelfactory.md).

## Topics

### Initializers
- [init(LFM2VLConfiguration)](./lfm2vl/init%28_%29.md)
### Instance Properties
- [let config: LFM2VLConfiguration](./lfm2vl/config.md)
- [var kvHeads: [Int]](./lfm2vl/kvheads.md)
- [var loraLayers: [Module]](./lfm2vl/loralayers.md)
- [var vocabularySize: Int](./lfm2vl/vocabularysize.md)
### Instance Methods
- [func callAsFunction(MLXArray, cache: [any KVCache]?) -> MLXArray](./lfm2vl/callasfunction%28_,cache%29.md)
- [func newCache(parameters: GenerateParameters?) throws -> [KVCache]](./lfm2vl/newcache%28parameters%29.md)
- [func prepare(LMInput, cache: [any KVCache], state: LMOutput.State?, prefill: PrefillParameters) throws -> PrepareResult](./lfm2vl/prepare%28_,cache,state,prefill%29.md)
- [func sanitize(weights: [String : MLXArray]) -> [String : MLXArray]](./lfm2vl/sanitize%28weights%29.md)
### Default Implementations
- [BaseLanguageModel Implementations](./lfm2vl/baselanguagemodel-implementations.md)
- [ChatConventionsProviding Implementations](./lfm2vl/chatconventionsproviding-implementations.md)
- [LanguageModel Implementations](./lfm2vl/languagemodel-implementations.md)
- [LoRAModel Implementations](./lfm2vl/loramodel-implementations.md)

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

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxvlm/lfm2vl)*