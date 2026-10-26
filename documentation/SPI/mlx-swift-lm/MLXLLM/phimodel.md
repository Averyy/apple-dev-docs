---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxllm/phimodel"
framework: "mlx-swift-lm/MLXLLM"
---

# PhiModel

**Framework**: mlx-swift-lm/MLXLLM  
**Kind**: class  
**Role**: Class

## Declaration

```swift
class PhiModel
```

## Topics

### Initializers
- [init(PhiConfiguration)](./phimodel/init%28_%29.md)
### Instance Properties
- [let kvHeads: [Int]](./phimodel/kvheads.md)
- [let model: PhiModelInner](./phimodel/model.md)
- [let vocabularySize: Int](./phimodel/vocabularysize.md)
### Instance Methods
- [func callAsFunction(MLXArray, cache: [KVCache]?) -> MLXArray](./phimodel/callasfunction%28_,cache%29.md)
### Default Implementations
- [BaseLanguageModel Implementations](./phimodel/baselanguagemodel-implementations.md)
- [ChatConventionsProviding Implementations](./phimodel/chatconventionsproviding-implementations.md)
- [LLMModel Implementations](./phimodel/llmmodel-implementations.md)
- [LanguageModel Implementations](./phimodel/languagemodel-implementations.md)
- [LoRAModel Implementations](./phimodel/loramodel-implementations.md)

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
- [class Phi3Model](./phi3model.md)
- [class PhiMoEModel](./phimoemodel.md)
- [class Qwen2Model](./qwen2model.md)
- [class Qwen3Model](./qwen3model.md)
- [class Starcoder2Model](./starcoder2model.md)
- [class MiMoModel](./mimomodel.md)
- [class GLM4Model](./glm4model.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxllm/phimodel)*