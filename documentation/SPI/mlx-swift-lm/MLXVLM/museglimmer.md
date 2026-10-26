---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxvlm/museglimmer"
framework: "mlx-swift-lm/MLXVLM"
---

# MuseGlimmer

**Framework**: mlx-swift-lm/MLXVLM  
**Kind**: class  
**Role**: Class

## Declaration

```swift
class MuseGlimmer
```

## Topics

### Initializers
- [init(MuseGlimmerConfiguration)](./museglimmer/init%28_%29.md)
### Instance Properties
- [let config: MuseGlimmerConfiguration](./museglimmer/config.md)
- [var kvHeads: [Int]](./museglimmer/kvheads.md)
- [var reasoningConfig: ReasoningConfig?](./museglimmer/reasoningconfig.md)
- [var toolCallFormat: ToolCallFormat?](./museglimmer/toolcallformat.md)
- [var vocabularySize: Int](./museglimmer/vocabularysize.md)
### Instance Methods
- [func callAsFunction(MLXArray, cache: [any KVCache]?) -> MLXArray](./museglimmer/callasfunction%28_,cache%29.md)
- [func newCache(parameters: GenerateParameters?) throws -> [any KVCache]](./museglimmer/newcache%28parameters%29.md)
- [func prepare(LMInput, cache: [any KVCache], state: LMOutput.State?, prefill: PrefillParameters) throws -> PrepareResult](./museglimmer/prepare%28_,cache,state,prefill%29.md)
- [func sanitize(weights: [String : MLXArray]) -> [String : MLXArray]](./museglimmer/sanitize%28weights%29.md)
  Key renaming only — a byte-for-byte port of `muse_glimmer.Model.sanitize`.
### Default Implementations
- [BaseLanguageModel Implementations](./museglimmer/baselanguagemodel-implementations.md)
- [LanguageModel Implementations](./museglimmer/languagemodel-implementations.md)
- [LoRAModel Implementations](./museglimmer/loramodel-implementations.md)
- [ModelComponentsProviding Implementations](./museglimmer/modelcomponentsproviding-implementations.md)

## Relationships

### Inherits From
- MLXNN.Module
### Conforms To
- MLX.Evaluatable
- MLX.IndentedDescription
- MLX.Updatable
- MLXLMCommon.BaseLanguageModel
- MLXLMCommon.ChatConventionsProviding
- MLXLMCommon.KVCacheDimensionProvider
- MLXLMCommon.LanguageModel
- MLXLMCommon.LoRAModel
- MLXLMCommon.ModelComponentsProviding
- Swift.Copyable
- Swift.CustomStringConvertible
- Swift.Escapable
- [VLMModel](./vlmmodel.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxvlm/museglimmer)*