---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/tokeniterator"
framework: "mlx-swift-lm/MLXLMCommon"
---

# TokenIterator

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: struct  
**Role**: Structure

Generator of tokens.

## Declaration

```swift
struct TokenIterator
```

## Mentions

- [Observing token log probabilities](./generation-observability.md)

#### Overview

This is typically used via a call to [`generate(input:cache:state:parameters:context:components:wiredMemoryTicket:tools:)`](./generate%28input,cache,state,parameters,context,components,wiredmemoryticket,tools%29.md) returning `AsyncStream<Generation>`.

To use it directly:

```swift
let generateParameters: GenerateParameters
let input: LMInput
let model: LanguageModel

let iterator = try TokenIterator(input: input, model: model, parameters: generateParameters)

for token in iterator {
    ...
}
```

Tokens are integers that can be passed through a `Tokenizer` or [`StreamingDetokenizer`](./streamingdetokenizer.md) to produce Strings.

Port of `generate_step()` from https://github.com/ml-explore/mlx-examples/blob/main/llms/mlx_lm/utils.py

Note: this uses `asyncEval()` and there may be an async evaluation running after a call to `next()`.

## Topics

### Initializers
- [init(input: LMInput, model: any LanguageModel, cache: [KVCache]?, state: LMOutput.State?, parameters: GenerateParameters, components: GenerationComponents) throws](./tokeniterator/init%28input,model,cache,state,parameters,components%29.md)
  Initialize a `TokenIterator` with the given input.
- [init(input: LMInput, model: any LanguageModel, cache: [KVCache]?, state: LMOutput.State?, processor: LogitProcessor?, sampler: LogitSampler, prefill: PrefillParameters, maxTokens: Int?) throws](./tokeniterator/init%28input,model,cache,state,processor,sampler,prefill,maxtokens%29.md)
  Initialize a `TokenIterator` with the given input and logit handling.
- [init(input: LMInput, model: any LanguageModel, cache: [KVCache]?, state: LMOutput.State?, processor: LogitProcessor?, sampler: LogitSampler, prefillStepSize: Int?, maxTokens: Int?) throws](./tokeniterator/init%28input,model,cache,state,processor,sampler,prefillstepsize,maxtokens%29.md)
- [init(prompt: MLXArray, model: any LanguageModel, cache: [KVCache]?, parameters: GenerateParameters, components: GenerationComponents) throws](./tokeniterator/init%28prompt,model,cache,parameters,components%29.md)
  Initialize a `TokenIterator` with the given tokens. Note: this has been replaced with [`init(input:model:cache:state:parameters:components:)`](./tokeniterator/init%28input,model,cache,state,parameters,components%29.md).
### Instance Properties
- [var evictedTokenCount: Int](./tokeniterator/evictedtokencount.md)
- [var lastLogProbabilities: DeferredTokenLogProbabilities?](./tokeniterator/lastlogprobabilities.md)
  Log probabilities for the token returned by the most recent [`next()`](./tokeniterator/next%28%29.md) call.
- [let maxTokens: Int?](./tokeniterator/maxtokens.md)
- [var promptPrefillTime: TimeInterval](./tokeniterator/promptprefilltime.md)
- [var reasoningTokenCount: Int?](./tokeniterator/reasoningtokencount.md)
- [var state: LMOutput.State?](./tokeniterator/state.md)
  Per-call model state (e.g. M-RoPE rope deltas), seeded from the initializer’s `state`, replaced by prefill, then threaded through every decode step. A caller continuing this cache later (as [`ChatSession`](./chatsession.md) does across turns) reads it back after initialization and seeds the next iterator with it.
- [var tokenCount: Int](./tokeniterator/tokencount.md)
### Instance Methods
- [func next() -> Int?](./tokeniterator/next%28%29.md)
- [func recordEmittedToken(Int)](./tokeniterator/recordemittedtoken%28_%29.md)
### Default Implementations
- [Sequence Implementations](./tokeniterator/sequence-implementations.md)
- [TokenIteratorProtocol Implementations](./tokeniterator/tokeniteratorprotocol-implementations.md)

## Relationships

### Conforms To
- Swift.IteratorProtocol
- Swift.Sequence
- [TokenIteratorProtocol](./tokeniteratorprotocol.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/tokeniterator)*