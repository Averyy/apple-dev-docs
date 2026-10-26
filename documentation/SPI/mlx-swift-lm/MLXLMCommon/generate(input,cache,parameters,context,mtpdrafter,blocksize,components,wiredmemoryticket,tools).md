---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/generate(input:cache:parameters:context:mtpdrafter:blocksize:components:wiredmemoryticket:tools:)"
framework: "mlx-swift-lm/MLXLMCommon"
---

# generate(input:cache:parameters:context:mtpDrafter:blockSize:components:wiredMemoryTicket:tools:)

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: func  
**Role**: Function

Generates tokens asynchronously using MTP speculative decoding.

## Declaration

```swift
func generate(input: LMInput, cache: [KVCache]? = nil, parameters: GenerateParameters, context: ModelContext, mtpDrafter: any MTPDrafterModel, blockSize: Int = 4, components: GenerationComponents = .init(), wiredMemoryTicket: WiredMemoryTicket? = nil, tools: [[String : any Sendable]]? = nil) throws -> AsyncStream<Generation>
```

#### Return Value

An `AsyncStream<Generation>` yielding chunks and tool calls.

#### Discussion

Parallel to [`generate(input:cache:state:parameters:context:draftModel:draftCache:numDraftTokens:components:wiredMemoryTicket:tools:)`](./generate%28input,cache,state,parameters,context,draftmodel,draftcache,numdrafttokens,components,wiredmemoryticket,tools%29.md) but for MTP drafters: the drafter shares K/V with the target model and produces a block of `blockSize - 1` candidate tokens per round in a single `draftBlock(...)` call. The drafter shares the target’s tokenizer (via `context.tokenizer`).

> **Throws**: An error if the iterator initialization fails.

## Parameters

- `input`: Language model input for the main (verifier) model.
- `cache`: Optional [`KVCache`](./kvcache.md) for the main model.
- `parameters`: Generation parameters (sampling, max tokens, KV quantization, etc.).
- `context`: Model context for the main (verifier) model.
- `mtpDrafter`: The [`MTPDrafterModel`](./mtpdraftermodel.md). The target is threaded through [`draftBlock(target:lastToken:lastHidden:sharedKV:positionDeltas:queryOffset:blockSize:sampler:)`](./mtpdraftermodel/draftblock%28target,lasttoken,lasthidden,sharedkv,positiondeltas,queryoffset,blocksize,sampler%29.md) per round; drafter instances hold no target-derived state and are safe to share across iterators. Speculative rounds are staged and committed rather than written and rewound, so a sliding-window model speculates for the whole stream rather than only while total context stays inside the window. If the target ever stops emitting drafter state — a KV cache that quantizes mid-stream, say — the iterator logs once, reports [`passthroughReason`](./generatecompletioninfo/passthroughreason.md), and finishes the stream with ordinary single-token generation.
- `blockSize`: Total tokens per round (`blockSize - 1` drafted plus the bonus from the previous verify). Mirrors mlx-vlm’s `draft_block_size`. Default 4 matches mlx-vlm’s example configs.
- `components`: Optional behavioral components, e.g. a custom [`LogitProcessor`](./logitprocessor.md)
- `wiredMemoryTicket`: Optional wired memory ticket.
- `tools`: Optional tool schemas used to parse arguments and authorize function names.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/generate(input:cache:parameters:context:mtpdrafter:blocksize:components:wiredmemoryticket:tools:))*