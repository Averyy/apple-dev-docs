---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/tokeniterator/init(input:model:cache:state:parameters:components:)"
framework: "mlx-swift-lm/MLXLMCommon"
---

# init(input:model:cache:state:parameters:components:)

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: init  
**Role**: Initializer

Initialize a `TokenIterator` with the given input.

## Declaration

```swift
init(input: LMInput, model: any LanguageModel, cache: [KVCache]? = nil, state: LMOutput.State? = nil, parameters: GenerateParameters, components: GenerationComponents = .init()) throws
```

#### Discussion

If more control is needed over the generation, [`init(input:model:cache:state:processor:sampler:prefill:maxTokens:)`](./init%28input,model,cache,state,processor,sampler,prefill,maxtokens%29.md) allows a caller to specify [`LogitProcessor`](../logitprocessor.md) and [`LogitSampler`](../logitsampler.md) directly.

## Parameters

- `input`: Language model input
- `model`: The [`LanguageModel`](../languagemodel.md)
- `cache`: Optional [`KVCache`](../kvcache.md)
- `state`: Optional per-call model state carried over from earlier evaluation against `cache` (e.g. by a caller resuming a session)
- `parameters`: The generation parameters
- `components`: Optional behavioral components, e.g. a custom [`LogitProcessor`](../logitprocessor.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/tokeniterator/init(input:model:cache:state:parameters:components:))*