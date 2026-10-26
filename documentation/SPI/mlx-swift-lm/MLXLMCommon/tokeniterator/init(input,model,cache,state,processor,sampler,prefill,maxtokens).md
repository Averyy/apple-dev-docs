---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/tokeniterator/init(input:model:cache:state:processor:sampler:prefill:maxtokens:)"
framework: "mlx-swift-lm/MLXLMCommon"
---

# init(input:model:cache:state:processor:sampler:prefill:maxTokens:)

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: init  
**Role**: Initializer

Initialize a `TokenIterator` with the given input and logit handling.

## Declaration

```swift
init(input: LMInput, model: any LanguageModel, cache: [KVCache]? = nil, state: LMOutput.State? = nil, processor: LogitProcessor?, sampler: LogitSampler, prefill: PrefillParameters = .init(), maxTokens: Int? = nil) throws
```

## Parameters

- `input`: Language model input
- `model`: The [`LanguageModel`](../languagemodel.md)
- `cache`: Optional [`KVCache`](../kvcache.md)
- `state`: Optional per-call model state carried over from earlier evaluation against `cache` (e.g. by a caller resuming a session)
- `processor`: The logit processor
- `sampler`: The logit sampler
- `prefill`: Prefill parameters (step size, chunking, progress)
- `maxTokens`: Maximum number of tokens to generate


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/tokeniterator/init(input:model:cache:state:processor:sampler:prefill:maxtokens:))*