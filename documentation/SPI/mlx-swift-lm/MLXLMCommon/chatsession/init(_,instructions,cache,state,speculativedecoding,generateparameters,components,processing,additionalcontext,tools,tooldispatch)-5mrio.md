---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/chatsession/init(_:instructions:cache:state:speculativedecoding:generateparameters:components:processing:additionalcontext:tools:tooldispatch:)-5mrio"
framework: "mlx-swift-lm/MLXLMCommon"
---

# init(_:instructions:cache:state:speculativeDecoding:generateParameters:components:processing:additionalContext:tools:toolDispatch:)

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: init  
**Role**: Initializer

Initialize the `ChatSession` with a pre-built KV cache.

## Declaration

```swift
init(_ model: ModelContainer, instructions: String? = nil, cache: consuming [KVCache], state: LMOutput.State? = nil, speculativeDecoding: SpeculativeDecodingConfig? = nil, generateParameters: GenerateParameters = .init(), components: GenerationComponents = .init(), processing: UserInput.Processing = .init(resize: CGSize(width: 512, height: 512)), additionalContext: [String : any Sendable]? = nil, tools: [ToolSpec]? = nil, toolDispatch: (@Sendable (ToolCall) async throws -> String)? = nil)
```

## Discussion

This enables prefix caching: build a KV cache from a long shared context (e.g. a system prompt and document) once, save it via [`saveCache(to:)`](./savecache%28to%29.md), and restore it across multiple sessions to avoid re-prefilling the same tokens each time.

> ❗ **Important**: If the cache was built from a session that already included system instructions, do not pass the same `instructions` here — they would be re-tokenized on each call to [`respond(to:role:images:videos:audios:)`](./respond%28to,role,images,videos,audios%29.md) without matching KV state, producing incoherent output.

> ❗ **Important**: Prefer the initializer that takes a `promptCache`. A cache and the model state that belongs with it must travel together: passing `cache: snapshot.cache` while dropping `snapshot.state` compiles, but positions later tokens as if the cached prefix contained no images. Models that carry a position anchor throw [`ContinuationStateError`](../continuationstateerror.md) rather than continue without it.

> ❗ **Important**: A raw cache does not carry the structured chat transcript. This initializer therefore preserves fragment-based continuation behavior. Use a history initializer when later turns must re-render the full conversation.

## Parameters

- `model`: The [`ModelContainer`](../modelcontainer.md)
- `instructions`: Optional system instructions for the session — leave `nil` if the cache already encodes a system prompt
- `cache`: A non-empty `[KVCache]`, matching the given model — from [`loadPromptCacheSnapshot(url:)`](../loadpromptcachesnapshot%28url%29.md) if it was saved to disk
- `state`: The model state captured with that cache; pass `snapshot.state` whenever the cache came from a snapshot
- `speculativeDecoding`: Optional speculative decoding configuration for faster generation
- `generateParameters`: Parameters that control generation
- `components`: Optional behavioral components, e.g. a custom [`LogitProcessor`](../logitprocessor.md)
- `processing`: Media processing configuration for images/videos
- `additionalContext`: Optional model-specific context
- `tools`: Optional tool specifications
- `toolDispatch`: Optional tool dispatch – required for toolcalls if streaming strings rather than details


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/chatsession/init(_:instructions:cache:state:speculativedecoding:generateparameters:components:processing:additionalcontext:tools:tooldispatch:)-5mrio)*