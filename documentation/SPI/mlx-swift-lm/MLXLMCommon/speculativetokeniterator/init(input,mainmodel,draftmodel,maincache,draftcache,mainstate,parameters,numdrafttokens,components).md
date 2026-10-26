---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/speculativetokeniterator/init(input:mainmodel:draftmodel:maincache:draftcache:mainstate:parameters:numdrafttokens:components:)"
framework: "mlx-swift-lm/MLXLMCommon"
---

# init(input:mainModel:draftModel:mainCache:draftCache:mainState:parameters:numDraftTokens:components:)

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: init  
**Role**: Initializer

Initialize a `SpeculativeTokenIterator` with the given input.

## Declaration

```swift
init(input: LMInput, mainModel: any LanguageModel, draftModel: any LanguageModel, mainCache: [KVCache]? = nil, draftCache: [KVCache]? = nil, mainState: LMOutput.State? = nil, parameters: GenerateParameters, numDraftTokens: Int, components: GenerationComponents = .init()) throws
```

## Parameters

- `input`: Language model input
- `mainModel`: The main (verifier) [`LanguageModel`](../languagemodel.md)
- `draftModel`: The draft [`LanguageModel`](../languagemodel.md) (must share the same tokenizer)
- `mainCache`: Optional [`KVCache`](../kvcache.md) for the main model
- `draftCache`: Optional [`KVCache`](../kvcache.md) for the draft model
- `mainState`: Optional model state that belongs with `mainCache`
- `parameters`: The generation parameters
- `numDraftTokens`: Number of tokens the draft model proposes per round
- `components`: Optional behavioral components, e.g. a custom [`LogitProcessor`](../logitprocessor.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/speculativetokeniterator/init(input:mainmodel:draftmodel:maincache:draftcache:mainstate:parameters:numdrafttokens:components:))*