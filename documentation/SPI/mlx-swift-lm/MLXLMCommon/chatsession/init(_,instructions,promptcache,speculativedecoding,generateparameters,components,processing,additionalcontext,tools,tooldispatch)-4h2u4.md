---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/chatsession/init(_:instructions:promptcache:speculativedecoding:generateparameters:components:processing:additionalcontext:tools:tooldispatch:)-4h2u4"
framework: "mlx-swift-lm/MLXLMCommon"
---

# init(_:instructions:promptCache:speculativeDecoding:generateParameters:components:processing:additionalContext:tools:toolDispatch:)

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: init  
**Role**: Initializer

Initialize the `ChatSession` with a prompt cache and the model state that belongs with it.

## Declaration

```swift
convenience init(_ model: ModelContainer, instructions: String? = nil, promptCache: consuming PromptCacheSnapshot, speculativeDecoding: SpeculativeDecodingConfig? = nil, generateParameters: GenerateParameters = .init(), components: GenerationComponents = .init(), processing: UserInput.Processing = .init(resize: CGSize(width: 512, height: 512)), additionalContext: [String : any Sendable]? = nil, tools: [ToolSpec]? = nil, toolDispatch: (@Sendable (ToolCall) async throws -> String)? = nil)
```

#### Discussion

This is the preferred way to start a session from a saved cache: the snapshot keeps the KV arrays and the model state together, so neither can be dropped. Read one from disk with [`loadPromptCacheSnapshot(url:)`](../loadpromptcachesnapshot%28url%29.md), or build one in process with [`init(cache:metadata:state:)`](../promptcachesnapshot/init%28cache,metadata,state%29.md).

Models that do not carry model state simply ignore it, so this works for any model.

> ❗ **Important**: A snapshot carries the cache and model state, not the structured chat transcript, so this initializer uses fragment-based continuation. A later image-bearing turn continues warm from the cached prefix rather than rebuilding and re-rendering earlier messages. Positions stay correct, but the prompt differs — and on vision encoders that attend across image boundaries (Qwen2-VL today) so do the new image’s features, since it is encoded alone rather than beside the cached one. Use a history initializer when later turns must re-render the full conversation.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/chatsession/init(_:instructions:promptcache:speculativedecoding:generateparameters:components:processing:additionalcontext:tools:tooldispatch:)-4h2u4)*