---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxvlm/gemma4"
framework: "mlx-swift-lm/MLXVLM"
---

# Gemma4

**Framework**: mlx-swift-lm/MLXVLM  
**Kind**: class  
**Role**: Class

## Declaration

```swift
final class Gemma4
```

## Topics

### Initializers
- [init(Gemma4Configuration)](./gemma4/init%28_%29.md)
### Instance Properties
- [let config: Gemma4Configuration](./gemma4/config.md)
- [var kvHeads: [Int]](./gemma4/kvheads.md)
- [var loraLayers: [Module]](./gemma4/loralayers.md)
- [var suppressedTokenIds: Set<Int>](./gemma4/suppressedtokenids.md)
  Multimodal placeholder token IDs that must never be sampled as text. Seeded from the model configuration; the model factory merges `suppress_tokens` from `generation_config.json` on top. See `SuppressedTokensProviding` in MLXLMCommon.
- [var vocabularySize: Int](./gemma4/vocabularysize.md)
### Instance Methods
- [func callAsFunction(MLXArray, cache: [any KVCache]?) -> MLXArray](./gemma4/callasfunction%28_,cache%29.md)
- [func callAsFunction(LMInput.Text, cache: [any KVCache]?, state: LMOutput.State?) -> LMOutput](./gemma4/callasfunction%28_,cache,state%29.md)
  MTP-aware `LanguageModel` entry point. Reads `mtpEmitFlagKey` from the incoming `state` and threads it through to `Gemma4TextLanguageModel`; the returned `LMOutput` carries `mtpLastHiddenStatesKey` and `mtpSharedKVStatesKey` populated when the flag is set, empty otherwise. Overrides the protocol-extension default at `LanguageModel` which would discard `state`.
- [func newCache(parameters: GenerateParameters?) throws -> [any KVCache]](./gemma4/newcache%28parameters%29.md)
- [func prepare(LMInput, cache: [any KVCache], state: LMOutput.State?, prefill: PrefillParameters) throws -> PrepareResult](./gemma4/prepare%28_,cache,state,prefill%29.md)
- [func sanitize(weights: [String : MLXArray]) -> [String : MLXArray]](./gemma4/sanitize%28weights%29.md)
### Default Implementations
- [BaseLanguageModel Implementations](./gemma4/baselanguagemodel-implementations.md)
- [ChatConventionsProviding Implementations](./gemma4/chatconventionsproviding-implementations.md)
- [LanguageModel Implementations](./gemma4/languagemodel-implementations.md)
- [LoRAModel Implementations](./gemma4/loramodel-implementations.md)

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
- MLXLMCommon.SuppressedTokensProviding
- Swift.CustomStringConvertible
- [VLMModel](./vlmmodel.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxvlm/gemma4)*