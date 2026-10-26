---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/generate(input:cache:state:parameters:context:components:wiredmemoryticket:tools:)"
framework: "mlx-swift-lm/MLXLMCommon"
---

# generate(input:cache:state:parameters:context:components:wiredMemoryTicket:tools:)

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: func  
**Role**: Function

Generates tokens asynchronously using the provided language model input, parameters, and context.

## Declaration

```swift
func generate(input: LMInput, cache: [KVCache]? = nil, state: LMOutput.State? = nil, parameters: GenerateParameters, context: ModelContext, components: GenerationComponents = .init(), wiredMemoryTicket: WiredMemoryTicket? = nil, tools: [[String : any Sendable]]? = nil) throws -> AsyncStream<Generation>
```

#### Return Value

An `AsyncStream` that emits `Generation` values, including generated text chunks (`.chunk`), accepted tool calls (`.toolCall`), rejected tool-call attempts (`.rejectedToolCall`), and completion information (`.info`).

#### Discussion

This function initializes a `TokenIterator` with the given input, model, and generation parameters, and then streams the token generation process via an `AsyncStream`. The resulting stream yields instances of the `Generation` enum, which can represent text chunks, tool calls, or summary completion information.

> ❗ **Important**: If the stream is terminated early (e.g. break from the loop) computation will continue using the model, parameters, KVCache, etc. for some time (typically a few ms).  This is typically OK for one-shot calls, but for “chat session” type calls consider using [`generateTask(promptTokenCount:modelConfiguration:tokenizer:iterator:wiredMemoryTicket:tools:toolCallPolicy:)`](./generatetask%28prompttokencount,modelconfiguration,tokenizer,iterator,wiredmemoryticket,tools,toolcallpolicy%29.md) so that the end of the generation task can be observed.

> **Throws**: An error if the `TokenIterator` initialization fails due to invalid input or model configuration.

##### Example Usage:

```swift
// Define the input, parameters, and context for token generation.
let generateParameters: GenerateParameters
let input: UserInput
let context: ModelContext

let lmInput = try context.processor.prepare(input: input)

// Call the generate function to get an AsyncStream.
let stream = try generate(input: lmInput, parameters: generateParameters, context: context)

// Process the stream asynchronously to handle text chunks and completion info.
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

## Parameters

- `input`: The input for the language model.
- `cache`: Optional [`KVCache`](./kvcache.md)
- `state`: Optional model state saved with `cache`, as [`state`](./promptcachesnapshot/state.md). Pass it whenever `cache` came from a snapshot: models that position from a carried anchor need it to place later tokens correctly.
- `parameters`: The configuration options for token generation.
- `context`: The model context, including the model itself and associated tokenizer.
- `components`: Optional behavioral components, e.g. a custom [`LogitProcessor`](./logitprocessor.md)
- `wiredMemoryTicket`: Optional wired memory ticket for policy-based coordination across concurrent tasks. This is opt-in and only applied on GPU devices that support wired memory control (macOS 15 / iOS 18 / tvOS 18 or newer).
- `tools`: Optional tool schemas used to parse tool-call arguments and authorize function names.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/generate(input:cache:state:parameters:context:components:wiredmemoryticket:tools:))*