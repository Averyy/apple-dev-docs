---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxllm/llamamodel"
framework: "mlx-swift-lm/MLXLLM"
---

# LlamaModel

**Framework**: mlx-swift-lm/MLXLLM  
**Kind**: class  
**Role**: Class

Model for Llama and Mistral model types.

## Declaration

```swift
class LlamaModel
```

## Topics

### Initializers
- [init(LlamaConfiguration)](./llamamodel/init%28_%29.md)
### Instance Properties
- [let kvHeads: [Int]](./llamamodel/kvheads.md)
- [let model: LlamaModelInner](./llamamodel/model.md)
- [let vocabularySize: Int](./llamamodel/vocabularysize.md)
### Instance Methods
- [func callAsFunction(MLXArray, cache: [KVCache]?) -> MLXArray](./llamamodel/callasfunction%28_,cache%29.md)
- [func messageGenerator(tokenizer: any Tokenizer) -> any MessageGenerator](./llamamodel/messagegenerator%28tokenizer%29.md)
- [func sanitize(weights: [String : MLXArray]) -> [String : MLXArray]](./llamamodel/sanitize%28weights%29.md)
### Default Implementations
- [BaseLanguageModel Implementations](./llamamodel/baselanguagemodel-implementations.md)
- [ChatConventionsProviding Implementations](./llamamodel/chatconventionsproviding-implementations.md)
- [LLMModel Implementations](./llamamodel/llmmodel-implementations.md)
- [LanguageModel Implementations](./llamamodel/languagemodel-implementations.md)
- [LoRAModel Implementations](./llamamodel/loramodel-implementations.md)

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

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxllm/llamamodel)*