---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxllm/openelmmodel"
framework: "mlx-swift-lm/MLXLLM"
---

# OpenELMModel

**Framework**: mlx-swift-lm/MLXLLM  
**Kind**: class  
**Role**: Class

## Declaration

```swift
class OpenELMModel
```

## Topics

### Initializers
- [init(OpenElmConfiguration)](./openelmmodel/init%28_%29.md)
### Instance Properties
- [let kvHeads: [Int]](./openelmmodel/kvheads.md)
- [let transformer: OpenELMModelInner](./openelmmodel/transformer.md)
- [let vocabularySize: Int](./openelmmodel/vocabularysize.md)
### Instance Methods
- [func callAsFunction(MLXArray, cache: [KVCache]?) -> MLXArray](./openelmmodel/callasfunction%28_,cache%29.md)
### Default Implementations
- [BaseLanguageModel Implementations](./openelmmodel/baselanguagemodel-implementations.md)
- [ChatConventionsProviding Implementations](./openelmmodel/chatconventionsproviding-implementations.md)
- [LLMModel Implementations](./openelmmodel/llmmodel-implementations.md)
- [LanguageModel Implementations](./openelmmodel/languagemodel-implementations.md)
- [LoRAModel Implementations](./openelmmodel/loramodel-implementations.md)

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
- [class PhiModel](./phimodel.md)
- [class Phi3Model](./phi3model.md)
- [class PhiMoEModel](./phimoemodel.md)
- [class Qwen2Model](./qwen2model.md)
- [class Qwen3Model](./qwen3model.md)
- [class Starcoder2Model](./starcoder2model.md)
- [class MiMoModel](./mimomodel.md)
- [class GLM4Model](./glm4model.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxllm/openelmmodel)*