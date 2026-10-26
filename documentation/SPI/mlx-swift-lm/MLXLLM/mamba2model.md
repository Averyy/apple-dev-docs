---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxllm/mamba2model"
framework: "mlx-swift-lm/MLXLLM"
---

# Mamba2Model

**Framework**: mlx-swift-lm/MLXLLM  
**Kind**: class  
**Role**: Class

## Declaration

```swift
class Mamba2Model
```

## Topics

### Initializers
- [init(Mamba2Configuration)](./mamba2model/init%28_%29.md)
### Instance Properties
- [var loraLayers: [Module]](./mamba2model/loralayers.md)
### Instance Methods
- [func callAsFunction(MLXArray, cache: [KVCache]?) -> MLXArray](./mamba2model/callasfunction%28_,cache%29.md)
- [func newCache(parameters: GenerateParameters?) -> [KVCache]](./mamba2model/newcache%28parameters%29.md)
- [func sanitize(weights: [String : MLXArray]) -> [String : MLXArray]](./mamba2model/sanitize%28weights%29.md)
### Default Implementations
- [BaseLanguageModel Implementations](./mamba2model/baselanguagemodel-implementations.md)
- [ChatConventionsProviding Implementations](./mamba2model/chatconventionsproviding-implementations.md)
- [LLMModel Implementations](./mamba2model/llmmodel-implementations.md)
- [LanguageModel Implementations](./mamba2model/languagemodel-implementations.md)
- [LoRAModel Implementations](./mamba2model/loramodel-implementations.md)

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
- MLXLMCommon.LanguageModel
- MLXLMCommon.LoRAModel
- Swift.CustomStringConvertible


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxllm/mamba2model)*