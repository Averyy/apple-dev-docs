---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/generatetokens(input:cache:parameters:context:mtpdrafter:blocksize:components:wiredmemoryticket:)"
framework: "mlx-swift-lm/MLXLMCommon"
---

# generateTokens(input:cache:parameters:context:mtpDrafter:blockSize:components:wiredMemoryTicket:)

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: func  
**Role**: Function

Generates raw token IDs asynchronously using MTP speculative decoding.

## Declaration

```swift
func generateTokens(input: LMInput, cache: [KVCache]? = nil, parameters: GenerateParameters, context: ModelContext, mtpDrafter: any MTPDrafterModel, blockSize: Int = 4, components: GenerationComponents = .init(), wiredMemoryTicket: WiredMemoryTicket? = nil) throws -> AsyncStream<TokenGeneration>
```

## Discussion

Parallels [`generateTokens(input:cache:state:parameters:context:draftModel:draftCache:numDraftTokens:components:wiredMemoryTicket:)`](./generatetokens%28input,cache,state,parameters,context,draftmodel,draftcache,numdrafttokens,components,wiredmemoryticket%29.md) but for MTP drafters. Yields raw token IDs instead of decoded text or tool calls.

Speculative rounds are staged and committed rather than written and rewound, so a sliding-window model speculates for the whole stream rather than only while total context stays inside the window. If the target ever stops emitting drafter state — a KV cache that quantizes mid-stream, say — the iterator logs once, reports [`passthroughReason`](./generatecompletioninfo/passthroughreason.md) on the emitted `.info` event, and finishes the stream with ordinary single-token generation.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/generatetokens(input:cache:parameters:context:mtpdrafter:blocksize:components:wiredmemoryticket:))*