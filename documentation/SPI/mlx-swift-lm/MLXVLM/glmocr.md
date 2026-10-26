---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxvlm/glmocr"
framework: "mlx-swift-lm/MLXVLM"
---

# GlmOcr

**Framework**: mlx-swift-lm/MLXVLM  
**Kind**: class  
**Role**: Class

GlmOcr VLM

## Declaration

```swift
class GlmOcr
```

## Topics

### Initializers
- [init(GlmOcrConfiguration)](./glmocr/init%28_%29.md)
### Instance Properties
- [let config: GlmOcrConfiguration](./glmocr/config.md)
- [var kvHeads: [Int]](./glmocr/kvheads.md)
- [var loraLayers: [Module]](./glmocr/loralayers.md)
- [var vocabularySize: Int](./glmocr/vocabularysize.md)
### Instance Methods
- [func callAsFunction(LMInput.Text, cache: [any KVCache]?, state: LMOutput.State?) -> LMOutput](./glmocr/callasfunction%28_,cache,state%29.md)
- [func prepare(LMInput, cache: [any KVCache], state: LMOutput.State?, prefill: PrefillParameters) throws -> PrepareResult](./glmocr/prepare%28_,cache,state,prefill%29.md)
- [func sanitize(weights: [String : MLXArray]) -> [String : MLXArray]](./glmocr/sanitize%28weights%29.md)
### Default Implementations
- [BaseLanguageModel Implementations](./glmocr/baselanguagemodel-implementations.md)
- [ChatConventionsProviding Implementations](./glmocr/chatconventionsproviding-implementations.md)
- [LanguageModel Implementations](./glmocr/languagemodel-implementations.md)
- [LoRAModel Implementations](./glmocr/loramodel-implementations.md)

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

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxvlm/glmocr)*