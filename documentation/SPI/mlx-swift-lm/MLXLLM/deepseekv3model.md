---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxllm/deepseekv3model"
framework: "mlx-swift-lm/MLXLLM"
---

# DeepseekV3Model

**Framework**: mlx-swift-lm/MLXLLM  
**Kind**: class  
**Role**: Class

## Declaration

```swift
class DeepseekV3Model
```

## Topics

### Initializers
- [init(DeepseekV3Configuration)](./deepseekv3model/init%28_%29.md)
### Instance Properties
- [var kvHeads: [Int]](./deepseekv3model/kvheads.md)
- [var loraLayers: [Module]](./deepseekv3model/loralayers.md)
- [var model: DeepseekV3ModelInner](./deepseekv3model/model.md)
### Instance Methods
- [func callAsFunction(MLXArray, cache: [KVCache]?) -> MLXArray](./deepseekv3model/callasfunction%28_,cache%29.md)
- [func sanitize(weights: [String : MLXArray]) -> [String : MLXArray]](./deepseekv3model/sanitize%28weights%29.md)
### Default Implementations
- [BaseLanguageModel Implementations](./deepseekv3model/baselanguagemodel-implementations.md)
- [ChatConventionsProviding Implementations](./deepseekv3model/chatconventionsproviding-implementations.md)
- [LLMModel Implementations](./deepseekv3model/llmmodel-implementations.md)
- [LanguageModel Implementations](./deepseekv3model/languagemodel-implementations.md)
- [LoRAModel Implementations](./deepseekv3model/loramodel-implementations.md)

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

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxllm/deepseekv3model)*