---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxllm/falconh1model"
framework: "mlx-swift-lm/MLXLLM"
---

# FalconH1Model

**Framework**: mlx-swift-lm/MLXLLM  
**Kind**: class  
**Role**: Class

## Declaration

```swift
class FalconH1Model
```

## Topics

### Initializers
- [init(FalconH1Configuration)](./falconh1model/init%28_%29.md)
### Instance Properties
- [let kvHeads: [Int]](./falconh1model/kvheads.md)
- [let model: FalconH1ModelInner](./falconh1model/model.md)
- [let vocabularySize: Int](./falconh1model/vocabularysize.md)
### Instance Methods
- [func callAsFunction(MLXArray, cache: [KVCache]?) -> MLXArray](./falconh1model/callasfunction%28_,cache%29.md)
- [func callAsFunction(MLXArray, cache: [KVCache]?, logitsToKeep: Int?) -> MLXArray](./falconh1model/callasfunction%28_,cache,logitstokeep%29.md)
  Compute logits for the input tokens.
- [func callAsFunction(LMInput.Text, cache: [KVCache]?, state: LMOutput.State?) -> LMOutput](./falconh1model/callasfunction%28_,cache,state%29.md)
- [func makeCache() -> [CacheList]](./falconh1model/makecache%28%29.md)
- [func newCache(parameters: GenerateParameters?) throws -> [any KVCache]](./falconh1model/newcache%28parameters%29.md)
- [func sanitize(weights: [String : MLXArray]) -> [String : MLXArray]](./falconh1model/sanitize%28weights%29.md)
- [func sanitize(weights: [String : MLXArray], metadata: [String : String]) -> [String : MLXArray]](./falconh1model/sanitize%28weights,metadata%29.md)
### Default Implementations
- [BaseLanguageModel Implementations](./falconh1model/baselanguagemodel-implementations.md)
- [ChatConventionsProviding Implementations](./falconh1model/chatconventionsproviding-implementations.md)
- [LLMModel Implementations](./falconh1model/llmmodel-implementations.md)
- [LanguageModel Implementations](./falconh1model/languagemodel-implementations.md)
- [LoRAModel Implementations](./falconh1model/loramodel-implementations.md)
- [ModelConversionMetadataProvider Implementations](./falconh1model/modelconversionmetadataprovider-implementations.md)

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
- MLXLMCommon.ModelConversionMetadataProvider
- Swift.Copyable
- Swift.CustomStringConvertible
- Swift.Escapable


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxllm/falconh1model)*