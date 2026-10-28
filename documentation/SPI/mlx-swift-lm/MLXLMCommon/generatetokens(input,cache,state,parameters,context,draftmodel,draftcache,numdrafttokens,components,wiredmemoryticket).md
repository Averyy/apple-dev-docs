---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/generatetokens(input:cache:state:parameters:context:draftmodel:draftcache:numdrafttokens:components:wiredmemoryticket:)"
framework: "mlx-swift-lm/MLXLMCommon"
---

# generateTokens(input:cache:state:parameters:context:draftModel:draftCache:numDraftTokens:components:wiredMemoryTicket:)

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: func  
**Role**: Function

Generates raw token IDs asynchronously using speculative decoding with a draft model.

## Declaration

```swift
func generateTokens(input: LMInput, cache: [KVCache]? = nil, state: LMOutput.State? = nil, parameters: GenerateParameters, context: ModelContext, draftModel: any LanguageModel, draftCache: [KVCache]? = nil, numDraftTokens: Int = 2, components: GenerationComponents = .init(), wiredMemoryTicket: WiredMemoryTicket? = nil) throws -> AsyncStream<TokenGeneration>
```

## Return Value

An `AsyncStream` that emits `TokenGeneration` values.

## Discussion

This is similar to `generate(input:cache:state:parameters:context:draftModel:draftCache:numDraftTokens:components:wiredMemoryTicket:)`, but yields raw token IDs instead of decoded text/tool calls.

Both models must share the same tokenizer.

> **Throws**: An error if the iterator initialization fails.

## Parameters

- `input`: The input for the language model.
- `cache`: Optional [`KVCache`](./kvcache.md) for the main model.
- `state`: Optional model state saved with `cache`, as [`state`](./promptcachesnapshot/state.md). Pass it whenever `cache` came from a snapshot: models that position from a carried anchor need it to place later tokens correctly.
- `parameters`: The configuration options for token generation.
- `context`: The model context for the main (verifier) model.
- `draftModel`: The draft [`LanguageModel`](./languagemodel.md) for speculative token proposals.
- `draftCache`: Optional [`KVCache`](./kvcache.md) for the draft model.
- `numDraftTokens`: Number of tokens the draft model proposes per round (default: 2).
- `components`: Optional behavioral components, e.g. a custom [`LogitProcessor`](./logitprocessor.md)
- `wiredMemoryTicket`: Optional wired memory ticket for policy-based coordination.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/generatetokens(input:cache:state:parameters:context:draftmodel:draftcache:numdrafttokens:components:wiredmemoryticket:))*