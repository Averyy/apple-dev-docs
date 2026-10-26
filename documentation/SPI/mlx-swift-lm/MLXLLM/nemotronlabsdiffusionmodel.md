---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxllm/nemotronlabsdiffusionmodel"
framework: "mlx-swift-lm/MLXLLM"
---

# NemotronLabsDiffusionModel

**Framework**: mlx-swift-lm/MLXLLM  
**Kind**: class  
**Role**: Class

`nvidia/Nemotron-Labs-Diffusion-3B` and family.

## Declaration

```swift
class NemotronLabsDiffusionModel
```

#### Overview

AR generation works through the standard `LLMModel` pipeline. Diffusion and linear-spec modes are exposed via dedicated methods.

## Topics

### Initializers
- [init(NemotronLabsDiffusionConfiguration)](./nemotronlabsdiffusionmodel/init%28_%29.md)
### Instance Properties
- [let encoder: NemotronLabsDiffusionEncoder](./nemotronlabsdiffusionmodel/encoder.md)
- [let kvHeads: [Int]](./nemotronlabsdiffusionmodel/kvheads.md)
- [let vocabularySize: Int](./nemotronlabsdiffusionmodel/vocabularysize.md)
### Instance Methods
- [func arGenerate(promptIds: [Int], maxNewTokens: Int, eosTokenId: Int?) -> (tokens: [Int], nfe: Int)](./nemotronlabsdiffusionmodel/argenerate%28promptids,maxnewtokens,eostokenid%29.md)
  Pure autoregressive generation (causal attention).
- [func bidirectionalLogits(MLXArray) -> MLXArray](./nemotronlabsdiffusionmodel/bidirectionallogits%28_%29.md)
  Bidirectional forward pass, returning logits. Used for diffusion drafting.
- [func bidirectionalLogits(MLXArray, cache: [KVCache]) -> MLXArray](./nemotronlabsdiffusionmodel/bidirectionallogits%28_,cache%29.md)
  Bidirectional forward over only the block, attending to a causally prefilled KV cache (the prompt + previously committed blocks). The cache is updated with the block’s K/V — callers must `trim` the cache by `inputs.dim(1)` after the forward to discard speculative entries.
- [func callAsFunction(MLXArray, cache: [KVCache]?) -> MLXArray](./nemotronlabsdiffusionmodel/callasfunction%28_,cache%29.md)
  AR forward pass used by the `LLMModel` pipeline (causal attention).
- [func diffusionGenerate(promptIds: [Int], maxNewTokens: Int, blockLength: Int, threshold: Float?, eosTokenId: Int?, onStep: ((_ tokens: [Int], _ nfe: Int) -> Void)?) -> (tokens: [Int], nfe: Int)](./nemotronlabsdiffusionmodel/diffusiongenerate%28promptids,maxnewtokens,blocklength,threshold,eostokenid,onstep%29.md)
  Block-wise diffusion (parallel) decoding.
- [func invalidateLoRACache()](./nemotronlabsdiffusionmodel/invalidateloracache%28%29.md)
  Reset the cached LoRA-layer list. Call after attaching, fusing, or removing an adapter so the next toggle re-discovers layers.
- [func linearSpecGenerate(promptIds: [Int], maxNewTokens: Int, blockLength: Int, threshold: Float, eosTokenId: Int?, onAccept: ((_ tokens: [Int], _ nfe: Int) -> Void)?) -> (tokens: [Int], nfe: Int)](./nemotronlabsdiffusionmodel/linearspecgenerate%28promptids,maxnewtokens,blocklength,threshold,eostokenid,onaccept%29.md)
  Linear speculative decoding: bidirectional drafter + AR verifier with a shared KV cache. Mirrors `linear_spec_generate(...)`.
- [func sanitize(weights: [String : MLXArray]) -> [String : MLXArray]](./nemotronlabsdiffusionmodel/sanitize%28weights%29.md)
### Default Implementations
- [BaseLanguageModel Implementations](./nemotronlabsdiffusionmodel/baselanguagemodel-implementations.md)
- [ChatConventionsProviding Implementations](./nemotronlabsdiffusionmodel/chatconventionsproviding-implementations.md)
- [LLMModel Implementations](./nemotronlabsdiffusionmodel/llmmodel-implementations.md)
- [LanguageModel Implementations](./nemotronlabsdiffusionmodel/languagemodel-implementations.md)
- [LoRAModel Implementations](./nemotronlabsdiffusionmodel/loramodel-implementations.md)

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

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxllm/nemotronlabsdiffusionmodel)*