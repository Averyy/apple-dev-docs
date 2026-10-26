---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxllm/apertusmodel"
framework: "mlx-swift-lm/MLXLLM"
---

# ApertusModel

**Framework**: mlx-swift-lm/MLXLLM  
**Kind**: class  
**Role**: Class

## Declaration

```swift
class ApertusModel
```

## Topics

### Initializers
- [init(ApertusConfiguration)](./apertusmodel/init%28_%29.md)
### Instance Properties
- [let kvHeads: [Int]](./apertusmodel/kvheads.md)
- [var lmHead: Linear?](./apertusmodel/lmhead.md)
- [let vocabularySize: Int](./apertusmodel/vocabularysize.md)
### Instance Methods
- [func callAsFunction(MLXArray, cache: [KVCache]?) -> MLXArray](./apertusmodel/callasfunction%28_,cache%29.md)
- [func messageGenerator(tokenizer: any Tokenizer) -> any MessageGenerator](./apertusmodel/messagegenerator%28tokenizer%29.md)
- [func sanitize(weights: [String : MLXArray]) -> [String : MLXArray]](./apertusmodel/sanitize%28weights%29.md)
### Default Implementations
- [BaseLanguageModel Implementations](./apertusmodel/baselanguagemodel-implementations.md)
- [ChatConventionsProviding Implementations](./apertusmodel/chatconventionsproviding-implementations.md)
- [LLMModel Implementations](./apertusmodel/llmmodel-implementations.md)
- [LanguageModel Implementations](./apertusmodel/languagemodel-implementations.md)
- [LoRAModel Implementations](./apertusmodel/loramodel-implementations.md)

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

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxllm/apertusmodel)*