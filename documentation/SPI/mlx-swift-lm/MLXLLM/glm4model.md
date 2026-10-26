---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxllm/glm4model"
framework: "mlx-swift-lm/MLXLLM"
---

# GLM4Model

**Framework**: mlx-swift-lm/MLXLLM  
**Kind**: class  
**Role**: Class

## Declaration

```swift
class GLM4Model
```

## Topics

### Initializers
- [init(GLM4Configuration)](./glm4model/init%28_%29.md)
### Instance Properties
- [let kvHeads: [Int]](./glm4model/kvheads.md)
- [let model: GLM4ModelInner](./glm4model/model.md)
- [let vocabularySize: Int](./glm4model/vocabularysize.md)
### Instance Methods
- [func callAsFunction(MLXArray, cache: [KVCache]?) -> MLXArray](./glm4model/callasfunction%28_,cache%29.md)
- [func sanitize(weights: [String : MLXArray]) -> [String : MLXArray]](./glm4model/sanitize%28weights%29.md)
### Default Implementations
- [BaseLanguageModel Implementations](./glm4model/baselanguagemodel-implementations.md)
- [ChatConventionsProviding Implementations](./glm4model/chatconventionsproviding-implementations.md)
- [LLMModel Implementations](./glm4model/llmmodel-implementations.md)
- [LanguageModel Implementations](./glm4model/languagemodel-implementations.md)
- [LoRAModel Implementations](./glm4model/loramodel-implementations.md)

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
- [class MiMoModel](./mimomodel.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxllm/glm4model)*