---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxllm/gptossmodel"
framework: "mlx-swift-lm/MLXLLM"
---

# GPTOSSModel

**Framework**: mlx-swift-lm/MLXLLM  
**Kind**: class  
**Role**: Class

## Declaration

```swift
class GPTOSSModel
```

## Topics

### Initializers
- [init(GPTOSSConfiguration)](./gptossmodel/init%28_%29.md)
### Instance Properties
- [let kvHeads: [Int]](./gptossmodel/kvheads.md)
- [let model: GPTOSSModelInner](./gptossmodel/model.md)
- [let modelType: String](./gptossmodel/modeltype.md)
- [let vocabularySize: Int](./gptossmodel/vocabularysize.md)
### Instance Methods
- [func callAsFunction(MLXArray, cache: [KVCache]?) -> MLXArray](./gptossmodel/callasfunction%28_,cache%29.md)
- [func messageGenerator(tokenizer: any Tokenizer) -> any MessageGenerator](./gptossmodel/messagegenerator%28tokenizer%29.md)
- [func newCache(parameters: GenerateParameters?) throws -> [any KVCache]](./gptossmodel/newcache%28parameters%29.md)
- [func sanitize(weights: [String : MLXArray]) -> [String : MLXArray]](./gptossmodel/sanitize%28weights%29.md)
### Default Implementations
- [BaseLanguageModel Implementations](./gptossmodel/baselanguagemodel-implementations.md)
- [ChatConventionsProviding Implementations](./gptossmodel/chatconventionsproviding-implementations.md)
- [LLMModel Implementations](./gptossmodel/llmmodel-implementations.md)
- [LanguageModel Implementations](./gptossmodel/languagemodel-implementations.md)
- [LoRAModel Implementations](./gptossmodel/loramodel-implementations.md)

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


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxllm/gptossmodel)*