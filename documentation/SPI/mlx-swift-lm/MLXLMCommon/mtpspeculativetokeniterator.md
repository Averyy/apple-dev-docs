---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/mtpspeculativetokeniterator"
framework: "mlx-swift-lm/MLXLMCommon"
---

# MTPSpeculativeTokenIterator

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: struct  
**Role**: Structure

Generator of tokens using MTP (Multi-Token Prediction) speculative decoding.

## Declaration

```swift
struct MTPSpeculativeTokenIterator
```

## Overview

Parallels [`SpeculativeTokenIterator`](./speculativetokeniterator.md) but for Gemma 4 - style drafters that share K/V with the target model and produce K - 1 candidate tokens per round in a single [`draftBlock(target:lastToken:lastHidden:sharedKV:positionDeltas:queryOffset:blockSize:sampler:)`](./mtpdraftermodel/draftblock%28target,lasttoken,lasthidden,sharedkv,positiondeltas,queryoffset,blocksize,sampler%29.md) call (rather than K sequential single-token calls). Every per-round input — `lastToken`, `lastHidden`, `sharedKV`, `positionIds` — is threaded as a method argument, with the target’s last hidden state and per-`layer_type` shared K/V extracted from the [`LMOutput.State`](./lmoutput/state-swift.struct.md) emitted by the target on the previous main-model call. If the drafter needs its own KV cache (Qwen MTP), that cache is owned by this iterator, prefilled over the shifted prompt, and reconciled against accepted target tokens after every verify pass; it is never stored on the shared drafter model.

The iterator pre-populates each main-model call’s incoming `state` with [`mtpEmitFlagKey`](./mtpemitflagkey.md) set to `true`, opting the target into populating [`mtpLastHiddenStatesKey`](./mtplasthiddenstateskey.md) and [`mtpSharedKVStatesKey`](./mtpsharedkvstateskey.md) on its returned [`state`](./lmoutput/state-swift.property.md). If the target ever returns nil or partial state (for example when a shared-KV drafter can no longer read regular K/V), the iterator transparently switches into a single-token “passthrough” mode for the remainder of generation — a mid-generation capability loss never crashes or corrupts the stream.

Port of `_speculative_walk` from mlx-vlm/generate.py at SHA `d49d428`, with no-mutation-during-eval idioms (state is threaded through method args; drafter holds no target-derived state — the target and optional per-stream drafter cache are passed as parameters to `draftBlock(...)` so drafter instances are safe to share across iterators).

## Topics

### Initializers
- [init(input: LMInput, mainModel: any LanguageModel, drafter: any MTPDrafterModel, mainCache: [KVCache]?, parameters: GenerateParameters, blockSize: Int, components: GenerationComponents) throws](./mtpspeculativetokeniterator/init%28input,mainmodel,drafter,maincache,parameters,blocksize,components%29.md)
### Instance Properties
- [var acceptedCount: Int](./mtpspeculativetokeniterator/acceptedcount.md)
- [let blockSize: Int](./mtpspeculativetokeniterator/blocksize.md)
  Total tokens proposed per round (`blockSize - 1` drafted, plus the bonus token from the previous verify). Mirrors mlx-vlm’s `draft_block_size` parameter.
- [var evictedTokenCount: Int](./mtpspeculativetokeniterator/evictedtokencount.md)
- [let maxTokens: Int?](./mtpspeculativetokeniterator/maxtokens.md)
- [var passthroughReason: String?](./mtpspeculativetokeniterator/passthroughreason.md)
- [var promptPrefillTime: TimeInterval](./mtpspeculativetokeniterator/promptprefilltime.md)
- [var proposedCount: Int](./mtpspeculativetokeniterator/proposedcount.md)
- [var reasoningTokenCount: Int?](./mtpspeculativetokeniterator/reasoningtokencount.md)
- [var speculativeDecodingTelemetry: SpeculativeDecodingTelemetry?](./mtpspeculativetokeniterator/speculativedecodingtelemetry.md)
- [var tokenCount: Int](./mtpspeculativetokeniterator/tokencount.md)
### Instance Methods
- [func discardGeneratedToken()](./mtpspeculativetokeniterator/discardgeneratedtoken%28%29.md)
- [func next() -> Int?](./mtpspeculativetokeniterator/next%28%29.md)
- [func recordEmittedToken(Int)](./mtpspeculativetokeniterator/recordemittedtoken%28_%29.md)
### Default Implementations
- [MTPStatsCollecting Implementations](./mtpspeculativetokeniterator/mtpstatscollecting-implementations.md)
- [Sequence Implementations](./mtpspeculativetokeniterator/sequence-implementations.md)
- [TokenIteratorProtocol Implementations](./mtpspeculativetokeniterator/tokeniteratorprotocol-implementations.md)

## Relationships

### Conforms To
- [MTPStatsCollecting](./mtpstatscollecting.md)
- Swift.Copyable
- Swift.Escapable
- Swift.IteratorProtocol
- Swift.Sequence
- [TokenIteratorProtocol](./tokeniteratorprotocol.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/mtpspeculativetokeniterator)*