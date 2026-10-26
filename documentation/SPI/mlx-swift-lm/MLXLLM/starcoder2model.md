---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxllm/starcoder2model"
framework: "mlx-swift-lm/MLXLLM"
---

# Starcoder2Model

**Framework**: mlx-swift-lm/MLXLLM  
**Kind**: class  
**Role**: Class

## Declaration

```swift
class Starcoder2Model
```

## Topics

### Initializers
- [init(Starcoder2Configuration)](./starcoder2model/init%28_%29.md)
### Instance Properties
- [let kvHeads: [Int]](./starcoder2model/kvheads.md)
- [let model: Starcoder2ModelInner](./starcoder2model/model.md)
- [let tieWordEmbeddings: Bool](./starcoder2model/tiewordembeddings.md)
- [let vocabularySize: Int](./starcoder2model/vocabularysize.md)
### Instance Methods
- [func callAsFunction(MLXArray, cache: [KVCache]?) -> MLXArray](./starcoder2model/callasfunction%28_,cache%29.md)
- [func sanitize(weights: [String : MLXArray]) -> [String : MLXArray]](./starcoder2model/sanitize%28weights%29.md)
### Default Implementations
- [BaseLanguageModel Implementations](./starcoder2model/baselanguagemodel-implementations.md)
- [ChatConventionsProviding Implementations](./starcoder2model/chatconventionsproviding-implementations.md)
- [LLMModel Implementations](./starcoder2model/llmmodel-implementations.md)
- [LanguageModel Implementations](./starcoder2model/languagemodel-implementations.md)
- [LoRAModel Implementations](./starcoder2model/loramodel-implementations.md)

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
- [class MiMoModel](./mimomodel.md)
- [class GLM4Model](./glm4model.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxllm/starcoder2model)*