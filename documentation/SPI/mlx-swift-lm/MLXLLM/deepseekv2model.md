---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxllm/deepseekv2model"
framework: "mlx-swift-lm/MLXLLM"
---

# DeepseekV2Model

**Framework**: mlx-swift-lm/MLXLLM  
**Kind**: class  
**Role**: Class

## Declaration

```swift
class DeepseekV2Model
```

## Topics

### Initializers
- [init(DeepseekV2Configuration)](./deepseekv2model/init%28_%29.md)
### Instance Properties
- [var kvHeads: [Int]](./deepseekv2model/kvheads.md)
- [var loraLayers: [Module]](./deepseekv2model/loralayers.md)
- [let model: DeepseekV2ModelInner](./deepseekv2model/model.md)
### Instance Methods
- [func callAsFunction(MLXArray, cache: [KVCache]?) -> MLXArray](./deepseekv2model/callasfunction%28_,cache%29.md)
- [func sanitize(weights: [String : MLXArray]) -> [String : MLXArray]](./deepseekv2model/sanitize%28weights%29.md)
### Default Implementations
- [BaseLanguageModel Implementations](./deepseekv2model/baselanguagemodel-implementations.md)
- [ChatConventionsProviding Implementations](./deepseekv2model/chatconventionsproviding-implementations.md)
- [LLMModel Implementations](./deepseekv2model/llmmodel-implementations.md)
- [LanguageModel Implementations](./deepseekv2model/languagemodel-implementations.md)
- [LoRAModel Implementations](./deepseekv2model/loramodel-implementations.md)

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
- Swift.CustomStringConvertible


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxllm/deepseekv2model)*