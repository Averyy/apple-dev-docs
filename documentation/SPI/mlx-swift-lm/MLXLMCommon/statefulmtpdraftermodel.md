---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/statefulmtpdraftermodel"
framework: "mlx-swift-lm/MLXLMCommon"
---

# StatefulMTPDrafterModel

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: protocol  
**Role**: Protocol

Optional capability for MTP drafters that maintain per-stream state.

## Declaration

```swift
protocol StatefulMTPDrafterModel : MTPDrafterModel
```

#### Overview

This keeps the base [`MTPDrafterModel`](./mtpdraftermodel.md) surface minimal for stateless drafters such as Gemma 4 assistants while giving Qwen-style MTP predictors an iterator-owned state that can carry and trim their private KV cache. The state must not be stored on the model instance because drafter models can be shared across concurrent generation streams.

## Topics

### Instance Methods
- [func commitDrafterState(target: any LanguageModel, targetHidden: MLXArray, draftTokens: MLXArray, acceptedCount: Int, finalToken: MLXArray, positionDeltas: MLXArray?, state: inout MTPDrafterState, sampler: any LogitSampler)](./statefulmtpdraftermodel/commitdrafterstate%28target,targethidden,drafttokens,acceptedcount,finaltoken,positiondeltas,state,sampler%29.md)
  Reconcile tentative proposal writes with the sequence accepted by the target, then seed the next proposal if the architecture supports it.
- [func draftBlock(target: any LanguageModel, lastToken: MLXArray, lastHidden: MLXArray, sharedKV: [String : (MLXArray, MLXArray)], positionDeltas: MLXArray?, queryOffset: Int, blockSize: Int, state: inout MTPDrafterState, sampler: any LogitSampler) -> MLXArray](./statefulmtpdraftermodel/draftblock%28target,lasttoken,lasthidden,sharedkv,positiondeltas,queryoffset,blocksize,state,sampler%29.md)
  Stateful variant of [`draftBlock(target:lastToken:lastHidden:sharedKV:positionDeltas:queryOffset:blockSize:sampler:)`](./mtpdraftermodel/draftblock%28target,lasttoken,lasthidden,sharedkv,positiondeltas,queryoffset,blocksize,sampler%29.md).
- [func makeState(parameters: GenerateParameters?) -> MTPDrafterState](./statefulmtpdraftermodel/makestate%28parameters%29.md)
  Create per-stream state owned and trimmed by the iterator.
- [func prepareDrafterState(target: any LanguageModel, promptTokens: MLXArray, targetHidden: MLXArray, firstBonus: MLXArray, positionDeltas: MLXArray?, state: inout MTPDrafterState, sampler: any LogitSampler)](./statefulmtpdraftermodel/preparedrafterstate%28target,prompttokens,targethidden,firstbonus,positiondeltas,state,sampler%29.md)
  Prefill drafter-owned state from the target’s prompt hidden states.

## Relationships

### Inherits From
- [BaseLanguageModel](./baselanguagemodel.md)
- [MTPDrafterModel](./mtpdraftermodel.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/statefulmtpdraftermodel)*