---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxllm/gemma3ntextmodel"
framework: "mlx-swift-lm/MLXLLM"
---

# Gemma3nTextModel

**Framework**: mlx-swift-lm/MLXLLM  
**Kind**: class  
**Role**: Class

## Declaration

```swift
class Gemma3nTextModel
```

## Topics

### Initializers
- [init(config: Gemma3nTextConfiguration)](./gemma3ntextmodel/init%28config%29.md)
### Instance Properties
- [var languageModel: Gemma3nLanguageModel](./gemma3ntextmodel/languagemodel.md)
### Instance Methods
- [func callAsFunction(MLXArray, cache: [KVCache]?) -> MLXArray](./gemma3ntextmodel/callasfunction%28_,cache%29.md)
- [func callAsFunction(MLXArray?, inputsEmbeds: MLXArray?, mask: MLXFast.ScaledDotProductAttentionMaskMode?, cache: [KVCache]?) -> MLXArray](./gemma3ntextmodel/callasfunction%28_,inputsembeds,mask,cache%29.md)
- [func newCache(parameters: GenerateParameters?) throws -> [any KVCache]](./gemma3ntextmodel/newcache%28parameters%29.md)
- [func prepare(LMInput, cache: [KVCache], state: LMOutput.State?, prefill: PrefillParameters) throws -> PrepareResult](./gemma3ntextmodel/prepare%28_,cache,state,prefill%29.md)
  Handles prompt processing for sequences
- [func prepareCheckpoint(ModelCheckpoint) throws -> ModelCheckpoint](./gemma3ntextmodel/preparecheckpoint%28_%29.md)
- [func sanitize(weights: [String : MLXArray]) throws -> [String : MLXArray]](./gemma3ntextmodel/sanitize%28weights%29.md)
### Default Implementations
- [BaseLanguageModel Implementations](./gemma3ntextmodel/baselanguagemodel-implementations.md)
- [ChatConventionsProviding Implementations](./gemma3ntextmodel/chatconventionsproviding-implementations.md)
- [LLMModel Implementations](./gemma3ntextmodel/llmmodel-implementations.md)
- [LanguageModel Implementations](./gemma3ntextmodel/languagemodel-implementations.md)
- [LoRAModel Implementations](./gemma3ntextmodel/loramodel-implementations.md)

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

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxllm/gemma3ntextmodel)*