---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/generate(input:cache:state:parameters:context:draftmodel:draftcache:numdrafttokens:components:wiredmemoryticket:tools:)"
framework: "mlx-swift-lm/MLXLMCommon"
---

# generate(input:cache:state:parameters:context:draftModel:draftCache:numDraftTokens:components:wiredMemoryTicket:tools:)

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: func  
**Role**: Function

Generates text and tool calls asynchronously using speculative decoding with a draft model.

## Declaration

```swift
func generate(input: LMInput, cache: [KVCache]? = nil, state: LMOutput.State? = nil, parameters: GenerateParameters, context: ModelContext, draftModel: any LanguageModel, draftCache: [KVCache]? = nil, numDraftTokens: Int = 2, components: GenerationComponents = .init(), wiredMemoryTicket: WiredMemoryTicket? = nil, tools: [[String : any Sendable]]? = nil) throws -> AsyncStream<Generation>
```

## Return Value

An `AsyncStream` that emits text, accepted or rejected tool calls, and completion information as `Generation` values.

## Discussion

This function uses a smaller draft model to propose tokens that are verified in batch by the main model, potentially accelerating generation. The resulting stream yields decoded text chunks, tool calls, and completion information. It has the same output as the non-speculative [`generate(input:cache:state:parameters:context:components:wiredMemoryTicket:tools:)`](./generate%28input,cache,state,parameters,context,components,wiredmemoryticket,tools%29.md).

Both models must share the same tokenizer.

### Example Usage:

```swift
let generateParameters: GenerateParameters
let input: UserInput
let mainContext: ModelContext
let draftModel: LanguageModel

let lmInput = try mainContext.processor.prepare(input: input)

let stream = try generate(
    input: lmInput, parameters: generateParameters,
    context: mainContext, draftModel: draftModel)

for await generation in stream {
    switch generation {
    case .chunk(let text):
        print("Generated text: \(text)")
    case .info(let info):
        print("Finished: \(info.tokensPerSecond) tokens/s.")
    case .toolCall(let call):
        print("Tool call: \(call.function.name)")
    case .rejectedToolCall(let rejection):
        print("Rejected tool call: \(rejection.reason)")
    }
}
```

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
- `tools`: Optional tool schemas used to parse arguments and authorize function names.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/generate(input:cache:state:parameters:context:draftmodel:draftcache:numdrafttokens:components:wiredmemoryticket:tools:))*