---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxllm/phi3model"
framework: "mlx-swift-lm/MLXLLM"
---

# Phi3Model

**Framework**: mlx-swift-lm/MLXLLM  
**Kind**: class  
**Role**: Class

## Declaration

```swift
class Phi3Model
```

## Topics

### Initializers
- [init(Phi3Configuration)](./phi3model/init%28_%29.md)
### Instance Properties
- [let kvHeads: [Int]](./phi3model/kvheads.md)
- [let model: Phi3ModelInner](./phi3model/model.md)
- [let vocabularySize: Int](./phi3model/vocabularysize.md)
### Instance Methods
- [func callAsFunction(MLXArray, cache: [KVCache]?) -> MLXArray](./phi3model/callasfunction%28_,cache%29.md)
- [func sanitize(weights: [String : MLXArray]) -> [String : MLXArray]](./phi3model/sanitize%28weights%29.md)
### Default Implementations
- [BaseLanguageModel Implementations](./phi3model/baselanguagemodel-implementations.md)
- [ChatConventionsProviding Implementations](./phi3model/chatconventionsproviding-implementations.md)
- [LLMModel Implementations](./phi3model/llmmodel-implementations.md)
- [LanguageModel Implementations](./phi3model/languagemodel-implementations.md)
- [LoRAModel Implementations](./phi3model/loramodel-implementations.md)

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
- [class PhiMoEModel](./phimoemodel.md)
- [class Qwen2Model](./qwen2model.md)
- [class Qwen3Model](./qwen3model.md)
- [class Starcoder2Model](./starcoder2model.md)
- [class MiMoModel](./mimomodel.md)
- [class GLM4Model](./glm4model.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxllm/phi3model)*