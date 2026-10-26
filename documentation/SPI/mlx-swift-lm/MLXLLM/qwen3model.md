---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxllm/qwen3model"
framework: "mlx-swift-lm/MLXLLM"
---

# Qwen3Model

**Framework**: mlx-swift-lm/MLXLLM  
**Kind**: class  
**Role**: Class

## Declaration

```swift
class Qwen3Model
```

## Topics

### Initializers
- [init(Qwen3Configuration)](./qwen3model/init%28_%29.md)
### Instance Properties
- [let kvHeads: [Int]](./qwen3model/kvheads.md)
- [let model: Qwen3ModelInner](./qwen3model/model.md)
- [let vocabularySize: Int](./qwen3model/vocabularysize.md)
### Instance Methods
- [func callAsFunction(MLXArray, cache: [KVCache]?) -> MLXArray](./qwen3model/callasfunction%28_,cache%29.md)
- [func nextTokenLogits(LMInput.Text, cache: [KVCache]?, state: LMOutput.State?) -> LMOutput](./qwen3model/nexttokenlogits%28_,cache,state%29.md)
- [func sanitize(weights: [String : MLXArray]) -> [String : MLXArray]](./qwen3model/sanitize%28weights%29.md)
### Default Implementations
- [BaseLanguageModel Implementations](./qwen3model/baselanguagemodel-implementations.md)
- [ChatConventionsProviding Implementations](./qwen3model/chatconventionsproviding-implementations.md)
- [LLMModel Implementations](./qwen3model/llmmodel-implementations.md)
- [LanguageModel Implementations](./qwen3model/languagemodel-implementations.md)
- [LoRAModel Implementations](./qwen3model/loramodel-implementations.md)

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
- [class Starcoder2Model](./starcoder2model.md)
- [class MiMoModel](./mimomodel.md)
- [class GLM4Model](./glm4model.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxllm/qwen3model)*