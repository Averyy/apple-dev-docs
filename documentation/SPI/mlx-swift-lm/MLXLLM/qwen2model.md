---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxllm/qwen2model"
framework: "mlx-swift-lm/MLXLLM"
---

# Qwen2Model

**Framework**: mlx-swift-lm/MLXLLM  
**Kind**: class  
**Role**: Class

## Declaration

```swift
class Qwen2Model
```

## Topics

### Initializers
- [init(Qwen2Configuration)](./qwen2model/init%28_%29.md)
### Instance Properties
- [let kvHeads: [Int]](./qwen2model/kvheads.md)
- [let model: Qwen2ModelInner](./qwen2model/model.md)
- [let vocabularySize: Int](./qwen2model/vocabularysize.md)
### Instance Methods
- [func callAsFunction(MLXArray, cache: [KVCache]?) -> MLXArray](./qwen2model/callasfunction%28_,cache%29.md)
- [func sanitize(weights: [String : MLXArray]) -> [String : MLXArray]](./qwen2model/sanitize%28weights%29.md)
### Default Implementations
- [BaseLanguageModel Implementations](./qwen2model/baselanguagemodel-implementations.md)
- [ChatConventionsProviding Implementations](./qwen2model/chatconventionsproviding-implementations.md)
- [LLMModel Implementations](./qwen2model/llmmodel-implementations.md)
- [LanguageModel Implementations](./qwen2model/languagemodel-implementations.md)
- [LoRAModel Implementations](./qwen2model/loramodel-implementations.md)

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
- [class Qwen3Model](./qwen3model.md)
- [class Starcoder2Model](./starcoder2model.md)
- [class MiMoModel](./mimomodel.md)
- [class GLM4Model](./glm4model.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxllm/qwen2model)*