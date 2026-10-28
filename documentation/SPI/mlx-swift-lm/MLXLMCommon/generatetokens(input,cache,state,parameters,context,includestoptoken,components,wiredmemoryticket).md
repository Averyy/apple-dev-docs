---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/generatetokens(input:cache:state:parameters:context:includestoptoken:components:wiredmemoryticket:)"
framework: "mlx-swift-lm/MLXLMCommon"
---

# generateTokens(input:cache:state:parameters:context:includeStopToken:components:wiredMemoryTicket:)

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: func  
**Role**: Function

Generates raw token IDs asynchronously using the provided language model input, parameters, and context.

## Declaration

```swift
func generateTokens(input: LMInput, cache: [KVCache]? = nil, state: LMOutput.State? = nil, parameters: GenerateParameters, context: ModelContext, includeStopToken: Bool = false, components: GenerationComponents = .init(), wiredMemoryTicket: WiredMemoryTicket? = nil) throws -> AsyncStream<TokenGeneration>
```

## Return Value

An `AsyncStream` that emits `TokenGeneration` values.

## Discussion

This is similar to `generate(input:cache:state:parameters:context:)`, but yields raw token IDs instead of decoded text/tool calls. This is useful for downstream parsers that need access to token IDs directly.

## Parameters

- `input`: The input for the language model.
- `cache`: Optional [`KVCache`](./kvcache.md)
- `state`: Optional model state saved with `cache`, as [`state`](./promptcachesnapshot/state.md). Pass it whenever `cache` came from a snapshot: models that position from a carried anchor need it to place later tokens correctly.
- `parameters`: The configuration options for token generation.
- `context`: The model context, including the model itself and associated tokenizer.
- `includeStopToken`: When true, the terminating EOS/unknown token is yielded before finishing
- `components`: Optional behavioral components, e.g. a custom [`LogitProcessor`](./logitprocessor.md)
- `wiredMemoryTicket`: Optional wired memory ticket for policy-based coordination across concurrent tasks. This is opt-in and only applied on GPU devices that support wired memory control (macOS 15 / iOS 18 / tvOS 18 or newer).


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/generatetokens(input:cache:state:parameters:context:includestoptoken:components:wiredmemoryticket:))*