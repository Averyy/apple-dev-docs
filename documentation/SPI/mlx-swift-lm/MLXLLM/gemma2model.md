---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxllm/gemma2model"
framework: "mlx-swift-lm/MLXLLM"
---

# Gemma2Model

**Framework**: mlx-swift-lm/MLXLLM  
**Kind**: class  
**Role**: Class

## Declaration

```swift
class Gemma2Model
```

## Topics

### Initializers
- [init(Gemma2Configuration)](./gemma2model/init%28_%29.md)
### Instance Properties
- [let kvHeads: [Int]](./gemma2model/kvheads.md)
- [let model: Gemma2ModelInner](./gemma2model/model.md)
- [let vocabularySize: Int](./gemma2model/vocabularysize.md)
### Instance Methods
- [func callAsFunction(MLXArray, cache: [KVCache]?) -> MLXArray](./gemma2model/callasfunction%28_,cache%29.md)
- [func messageGenerator(tokenizer: any Tokenizer) -> any MessageGenerator](./gemma2model/messagegenerator%28tokenizer%29.md)
### Default Implementations
- [BaseLanguageModel Implementations](./gemma2model/baselanguagemodel-implementations.md)
- [ChatConventionsProviding Implementations](./gemma2model/chatconventionsproviding-implementations.md)
- [LLMModel Implementations](./gemma2model/llmmodel-implementations.md)
- [LanguageModel Implementations](./gemma2model/languagemodel-implementations.md)
- [LoRAModel Implementations](./gemma2model/loramodel-implementations.md)

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
- [class MiMoModel](./mimomodel.md)
- [class GLM4Model](./glm4model.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxllm/gemma2model)*