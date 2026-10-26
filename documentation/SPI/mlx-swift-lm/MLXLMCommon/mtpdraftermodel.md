---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/mtpdraftermodel"
framework: "mlx-swift-lm/MLXLMCommon"
---

# MTPDrafterModel

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: protocol  
**Role**: Protocol

Protocol for Multi-Token Prediction (MTP) speculative drafter models.

## Declaration

```swift
protocol MTPDrafterModel : BaseLanguageModel
```

#### Overview

Mirrors `EmbeddingModel`’s relationship to `BaseLanguageModel`: this protocol refines `BaseLanguageModel` with drafter-specific surface, so implementations inherit weight loading and `sanitize` hooks while defining their own forward signature.

MTP drafters do **not** conform to `LanguageModel` — their I/O contract is different: a drafter consumes the target’s last hidden state and per layer-type shared K/V, produces a block of K-1 candidate tokens in a single call, and does not store transient round-state on the model object. The `MTPSpeculativeTokenIterator` extracts the shared K/V from the target’s `LMOutput.state` and threads it to the drafter as a method argument.

Conforming types are expected to be stateless with respect to the target model: every per-round input — including the target itself — flows through `draftBlock(...)` as a method parameter. This makes drafter instances safe to share across iterators without per-iterator mutable state on the model instance. Drafters that need their own per-stream state additionally conform to [`StatefulMTPDrafterModel`](./statefulmtpdraftermodel.md).

## Topics

### Instance Properties
- [var maximumBlockSize: Int?](./mtpdraftermodel/maximumblocksize.md)
  Largest total verification block the drafter can produce efficiently. `nil` means the caller may choose any block size.
- [var requiresGreedySampling: Bool](./mtpdraftermodel/requiresgreedysampling.md)
  Whether this drafter is currently supported only for greedy decoding. This keeps stochastic generation on the ordinary target path until a probability-ratio acceptance sampler is available.
- [var requiresPromptPrefill: Bool](./mtpdraftermodel/requirespromptprefill.md)
  Whether the drafter must be prefilled over the shifted prompt before its first proposal. Qwen’s private decoder cache requires this.
- [var requiresSharedTargetKV: Bool](./mtpdraftermodel/requiressharedtargetkv.md)
  Whether this drafter consumes target-emitted shared K/V. Qwen owns a private full-attention cache and therefore only needs target hidden states; Gemma-style assistants consume the shared target K/V directly.
### Instance Methods
- [func draftBlock(target: any LanguageModel, lastToken: MLXArray, lastHidden: MLXArray, sharedKV: [String : (MLXArray, MLXArray)], positionDeltas: MLXArray?, queryOffset: Int, blockSize: Int, sampler: any LogitSampler) -> MLXArray](./mtpdraftermodel/draftblock%28target,lasttoken,lasthidden,sharedkv,positiondeltas,queryoffset,blocksize,sampler%29.md)
  K-step drafting from a constant position.
- [func isCompatible(with: any LanguageModel) -> Bool](./mtpdraftermodel/iscompatible%28with%29.md)
  Whether the drafter can consume hidden states and model-owned values from this target architecture.

## Relationships

### Inherits From
- [BaseLanguageModel](./baselanguagemodel.md)
### Inherited By
- [StatefulMTPDrafterModel](./statefulmtpdraftermodel.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/mtpdraftermodel)*