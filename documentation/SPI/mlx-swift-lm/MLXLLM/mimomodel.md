---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxllm/mimomodel"
framework: "mlx-swift-lm/MLXLLM"
---

# MiMoModel

**Framework**: mlx-swift-lm/MLXLLM  
**Kind**: class  
**Role**: Class

## Declaration

```swift
class MiMoModel
```

## Topics

### Initializers
- [init(MiMoConfiguration)](./mimomodel/init%28_%29.md)
### Instance Properties
- [let kvHeads: [Int]](./mimomodel/kvheads.md)
- [let model: MiMoModelInner](./mimomodel/model.md)
- [let vocabularySize: Int](./mimomodel/vocabularysize.md)
### Instance Methods
- [func callAsFunction(MLXArray, cache: [KVCache]?) -> MLXArray](./mimomodel/callasfunction%28_,cache%29.md)
- [func sanitize(weights: [String : MLXArray]) -> [String : MLXArray]](./mimomodel/sanitize%28weights%29.md)
### Default Implementations
- [BaseLanguageModel Implementations](./mimomodel/baselanguagemodel-implementations.md)
- [ChatConventionsProviding Implementations](./mimomodel/chatconventionsproviding-implementations.md)
- [LLMModel Implementations](./mimomodel/llmmodel-implementations.md)
- [LanguageModel Implementations](./mimomodel/languagemodel-implementations.md)
- [LoRAModel Implementations](./mimomodel/loramodel-implementations.md)

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
- MLXLMCommon.KVCacheDimensionProvider
- MLXLMCommon.LanguageModel
- MLXLMCommon.LoRAModel
- Swift.Copyable
- Swift.CustomStringConvertible
- Swift.Escapable

## See Also

### Models
- [class CohereModel](./coheremodel.md)
- [class GemmaModel](./gemmamodel.md)
- [class Gemma2Model](./gemma2model.md)
- [class InternLM2Model](./internlm2model.md)
- [class LlamaModel](./llamamodel.md)
  Model for Llama and Mistral model types.
- [class OpenELMModel](./openelmmodel.md)
- [class PhiModel](./phimodel.md)
- [class Phi3Model](./phi3model.md)
- [class PhiMoEModel](./phimoemodel.md)
- [class Qwen2Model](./qwen2model.md)
- [class Qwen3Model](./qwen3model.md)
- [class Starcoder2Model](./starcoder2model.md)
- [class GLM4Model](./glm4model.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxllm/mimomodel)*