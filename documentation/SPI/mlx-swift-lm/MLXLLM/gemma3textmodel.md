---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxllm/gemma3textmodel"
framework: "mlx-swift-lm/MLXLLM"
---

# Gemma3TextModel

**Framework**: mlx-swift-lm/MLXLLM  
**Kind**: class  
**Role**: Class

## Declaration

```swift
class Gemma3TextModel
```

## Topics

### Initializers
- [init(Gemma3TextConfiguration)](./gemma3textmodel/init%28_%29.md)
### Instance Properties
- [let config: Gemma3TextConfiguration](./gemma3textmodel/config.md)
- [var model: Gemma3Model](./gemma3textmodel/model.md)
- [var vocabularySize: Int](./gemma3textmodel/vocabularysize.md)
### Instance Methods
- [func callAsFunction(MLXArray, cache: [KVCache]?) -> MLXArray](./gemma3textmodel/callasfunction%28_,cache%29.md)
- [func newCache(parameters: GenerateParameters?) throws -> [KVCache]](./gemma3textmodel/newcache%28parameters%29.md)
- [func prepare(LMInput, cache: [KVCache], state: LMOutput.State?, prefill: PrefillParameters) throws -> PrepareResult](./gemma3textmodel/prepare%28_,cache,state,prefill%29.md)
  Handles prompt processing for sequences
- [func sanitize(weights: [String : MLXArray]) -> [String : MLXArray]](./gemma3textmodel/sanitize%28weights%29.md)
### Default Implementations
- [BaseLanguageModel Implementations](./gemma3textmodel/baselanguagemodel-implementations.md)
- [ChatConventionsProviding Implementations](./gemma3textmodel/chatconventionsproviding-implementations.md)
- [LLMModel Implementations](./gemma3textmodel/llmmodel-implementations.md)
- [LanguageModel Implementations](./gemma3textmodel/languagemodel-implementations.md)
- [LoRAModel Implementations](./gemma3textmodel/loramodel-implementations.md)

## Relationships

### Inherits From
- MLXNN.Module
### Conforms To
- [LLMModel](./llmmodel.md)
- MLX.Evaluatable
- MLX.IndentedDescription
- MLX.Updatable
- MLXLMCommon.BaseLanguageModel
- MLXLMCommon.ChatConventionsProviding
- MLXLMCommon.LanguageModel
- MLXLMCommon.LoRAModel
- Swift.Copyable
- Swift.CustomStringConvertible
- Swift.Escapable


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxllm/gemma3textmodel)*