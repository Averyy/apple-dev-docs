---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/languagemodel"
framework: "mlx-swift-lm/MLXLMCommon"
---

# LanguageModel

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: protocol  
**Role**: Protocol

Interface for all Language Models (e.g. LLM, VLM).

## Declaration

```swift
protocol LanguageModel : BaseLanguageModel, ChatConventionsProviding
```

## Overview

The language model is typically called by the [`TokenIterator`](./tokeniterator.md) and it:

- consumes the [`LMInput`](./lminput.md)
- calls [`prepare(_:cache:state:prefill:)`](./languagemodel/prepare%28_,cache,state,prefill%29.md) to initialize the KVCache and consume the prompt
- calls [`callAsFunction(_:cache:state:)`](./languagemodel/callasfunction%28_,cache,state%29.md) for each token, producing an [`LMOutput`](./lmoutput.md)
- the [`TokenIterator`](./tokeniterator.md) accumulates this information into a [`GenerateResult`](./generateresult.md)

## Topics

### Instance Methods
- [func cacheStatus(parameters: GenerateParameters?) throws -> KVCacheStatus](./languagemodel/cachestatus%28parameters%29.md)
  Authoritative planned status of the cache [`newCache(parameters:)`](./languagemodel/newcache%28parameters%29.md) produces.
- [func callAsFunction(MLXArray, cache: [KVCache]?) -> MLXArray](./languagemodel/callasfunction%28_,cache%29.md)
  Models may implement this simplified interface if they do not produce any [`LMOutput.State`](./lmoutput/state-swift.struct.md)
- [func callAsFunction(LMInput.Text, cache: [KVCache]?, state: LMOutput.State?) -> LMOutput](./languagemodel/callasfunction%28_,cache,state%29.md)
  Primary entry point to produce a step (single token) from the model
- [func fuse(with: ModelAdapter) throws](./languagemodel/fuse%28with%29.md)
  Fuses an adapter permanently into the model.
- [func load(adapter: ModelAdapter) throws](./languagemodel/load%28adapter%29.md)
  Loads an adapter into the model.
- [func newCache(parameters: GenerateParameters?) throws -> [KVCache]](./languagemodel/newcache%28parameters%29.md)
  Create a new array of [`KVCache`](./kvcache.md) appropriate for this model.
- [func nextTokenLogits(LMInput.Text, cache: [KVCache]?, state: LMOutput.State?) -> LMOutput](./languagemodel/nexttokenlogits%28_,cache,state%29.md)
  Evaluate all input positions when only the final position’s logits are needed.
- [func perform<R>(with: ModelAdapter, perform: () throws -> R) throws -> R](./languagemodel/perform%28with,perform%29-5njjk.md)
  Temporarily loads an adapter, performs a synchronous action, then unloads the adapter.
- [func perform<R>(with: ModelAdapter, perform: () async throws -> R) async throws -> R](./languagemodel/perform%28with,perform%29-64w62.md)
  Temporarily loads an adapter, performs an asynchronous action, then unloads the adapter.
- [func prepare() throws](./languagemodel/prepare%28%29.md)
  Build derived state after checkpoint or adapter topology updates and before the model is used for inference.
- [func prepare(LMInput, cache: [KVCache], state: LMOutput.State?, prefill: PrefillParameters) throws -> PrepareResult](./languagemodel/prepare%28_,cache,state,prefill%29.md)
  Prepare the cache state and consume the [`LMInput`](./lminput.md).
- [func prepare(LMInput, cache: [KVCache], state: LMOutput.State?, windowSize: Int?) throws -> PrepareResult](./languagemodel/prepare%28_,cache,state,windowsize%29.md)
- [func unload(adapter: ModelAdapter)](./languagemodel/unload%28adapter%29.md)
  Unloads an adapter from the model.

## Relationships

### Inherits From
- [BaseLanguageModel](./baselanguagemodel.md)
- [ChatConventionsProviding](./chatconventionsproviding.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/languagemodel)*