---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxvlm/gemma4assistantdraftmodel"
framework: "mlx-swift-lm/MLXVLM"
---

# Gemma4AssistantDraftModel

**Framework**: mlx-swift-lm/MLXVLM  
**Kind**: class  
**Role**: Class

The Gemma 4 MTP drafter — a 4-layer Q-only assistant that cross-attends to the target model’s last full-attention and last sliding-attention K/V to propose K-1 tokens per round.

## Declaration

```swift
final class Gemma4AssistantDraftModel
```

## Overview

Mirrors mlx-vlm’s `Gemma4AssistantDraftModel` at `mlx_vlm/speculative/drafters/gemma4_assistant/gemma4_assistant.py` (SHA d49d428). Conforms to `MTPDrafterModel`; consumed by `MTPSpeculativeTokenIterator` (Phase B).

## Topics

### Initializers
- [init(Gemma4AssistantConfiguration)](./gemma4assistantdraftmodel/init%28_%29.md)
### Instance Properties
- [let config: Gemma4AssistantConfiguration](./gemma4assistantdraftmodel/config.md)
- [var lmHead: Linear?](./gemma4assistantdraftmodel/lmhead.md)
- [var maskedEmbedding: Gemma4AssistantMaskedEmbedder?](./gemma4assistantdraftmodel/maskedembedding.md)
- [var model: Gemma4AssistantDraftInner](./gemma4assistantdraftmodel/model.md)
- [var postProjection: Linear](./gemma4assistantdraftmodel/postprojection.md)
- [var preProjection: Linear](./gemma4assistantdraftmodel/preprojection.md)
### Instance Methods
- [func draftBlock(target: any LanguageModel, lastToken: MLXArray, lastHidden: MLXArray, sharedKV: [String : (MLXArray, MLXArray)], positionDeltas: MLXArray?, queryOffset: Int, blockSize: Int, sampler: any LogitSampler) -> MLXArray](./gemma4assistantdraftmodel/draftblock%28target,lasttoken,lasthidden,sharedkv,positiondeltas,queryoffset,blocksize,sampler%29.md)
- [func isCompatible(with: any LanguageModel) -> Bool](./gemma4assistantdraftmodel/iscompatible%28with%29.md)
- [func sanitize(weights: [String : MLXArray]) -> [String : MLXArray]](./gemma4assistantdraftmodel/sanitize%28weights%29.md)
### Default Implementations
- [BaseLanguageModel Implementations](./gemma4assistantdraftmodel/baselanguagemodel-implementations.md)
- [MTPDrafterModel Implementations](./gemma4assistantdraftmodel/mtpdraftermodel-implementations.md)

## Relationships

### Inherits From
- MLXNN.Module
### Conforms To
- MLX.Evaluatable
- MLX.IndentedDescription
- MLX.Updatable
- MLXLMCommon.BaseLanguageModel
- MLXLMCommon.MTPDrafterModel
- Swift.CustomStringConvertible


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxvlm/gemma4assistantdraftmodel)*