---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/chatsession"
framework: "mlx-swift-lm/MLXLMCommon"
---

# ChatSession

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: class  
**Role**: Class

Simplified API for multi-turn conversations with LLMs and VLMs.

## Declaration

```swift
final class ChatSession
```

## Mentions

- [Observing token log probabilities](./generation-observability.md)
- [KV Cache Quantization](./kv-cache-quantization.md)

#### Overview

For example:

```swift
let modelContainer = try await loadModelContainer(id: "mlx-community/Qwen3-4B-4bit")
let session = ChatSession(modelContainer)
print(try await session.respond(to: "What are two things to see in San Francisco?"))
print(try await session.respond(to: "How about a great place to eat?"))
```

To enable speculative decoding for faster generation, pass a `SpeculativeDecodingConfig`:

```swift
let draft = try await LLMModelFactory.shared.loadContainer(configuration: draftConfig)
let session = ChatSession(
    modelContainer,
    speculativeDecoding: SpeculativeDecodingConfig(draftModel: draft)
)
```

> **Note**: `ChatSession` is not thread-safe. Each session should be used from a single task/thread at a time. The underlying `ModelContainer` handles thread safety for model operations.

> **Note**: A session retains its structured transcript, including referenced media, until [`clear()`](./chatsession/clear%28%29.md) is called. Long-running VLM sessions should clear or replace the session when that retained context is no longer needed.

## Topics

### Initializers
- [init(ModelContainer, instructions: String?, cache: consuming [KVCache], state: LMOutput.State?, speculativeDecoding: SpeculativeDecodingConfig?, generateParameters: GenerateParameters, components: GenerationComponents, processing: UserInput.Processing, additionalContext: [String : any Sendable]?, tools: [ToolSpec]?, toolDispatch: (@Sendable (ToolCall) async throws -> String)?)](./chatsession/init%28_,instructions,cache,state,speculativedecoding,generateparameters,components,processing,additionalcontext,tools,tooldispatch%29-5mrio.md)
  Initialize the `ChatSession` with a pre-built KV cache.
- [init(ModelContext, instructions: String?, cache: consuming [KVCache], state: LMOutput.State?, speculativeDecoding: SpeculativeDecodingConfig?, generateParameters: GenerateParameters, components: GenerationComponents, processing: UserInput.Processing, additionalContext: [String : any Sendable]?, tools: [ToolSpec]?, toolDispatch: (@Sendable (ToolCall) async throws -> String)?)](./chatsession/init%28_,instructions,cache,state,speculativedecoding,generateparameters,components,processing,additionalcontext,tools,tooldispatch%29-9a7za.md)
  Initialize the `ChatSession` with a pre-built KV cache.
- [init(ModelContext, instructions: String?, history: [Chat.Message], speculativeDecoding: SpeculativeDecodingConfig?, generateParameters: GenerateParameters, components: GenerationComponents, processing: UserInput.Processing, additionalContext: [String : any Sendable]?, tools: [ToolSpec]?, toolDispatch: (@Sendable (ToolCall) async throws -> String)?)](./chatsession/init%28_,instructions,history,speculativedecoding,generateparameters,components,processing,additionalcontext,tools,tooldispatch%29-5cb5s.md)
  Initialize the `ChatSession` with an existing message history.
- [init(ModelContainer, instructions: String?, history: consuming [Chat.Message], speculativeDecoding: SpeculativeDecodingConfig?, generateParameters: GenerateParameters, components: GenerationComponents, processing: UserInput.Processing, additionalContext: [String : any Sendable]?, tools: [ToolSpec]?, toolDispatch: (@Sendable (ToolCall) async throws -> String)?)](./chatsession/init%28_,instructions,history,speculativedecoding,generateparameters,components,processing,additionalcontext,tools,tooldispatch%29-6yr11.md)
  Initialize the `ChatSession` with an existing message history.
- [init(ModelContainer, instructions: String?, promptCache: consuming PromptCacheSnapshot, speculativeDecoding: SpeculativeDecodingConfig?, generateParameters: GenerateParameters, components: GenerationComponents, processing: UserInput.Processing, additionalContext: [String : any Sendable]?, tools: [ToolSpec]?, toolDispatch: (@Sendable (ToolCall) async throws -> String)?)](./chatsession/init%28_,instructions,promptcache,speculativedecoding,generateparameters,components,processing,additionalcontext,tools,tooldispatch%29-4h2u4.md)
  Initialize the `ChatSession` with a prompt cache and the model state that belongs with it.
- [init(ModelContext, instructions: String?, promptCache: consuming PromptCacheSnapshot, speculativeDecoding: SpeculativeDecodingConfig?, generateParameters: GenerateParameters, components: GenerationComponents, processing: UserInput.Processing, additionalContext: [String : any Sendable]?, tools: [ToolSpec]?, toolDispatch: (@Sendable (ToolCall) async throws -> String)?)](./chatsession/init%28_,instructions,promptcache,speculativedecoding,generateparameters,components,processing,additionalcontext,tools,tooldispatch%29-7of4u.md)
  Initialize the `ChatSession` with a prompt cache and the model state that belongs with it.
- [init(ModelContext, instructions: String?, speculativeDecoding: SpeculativeDecodingConfig?, generateParameters: GenerateParameters, components: GenerationComponents, processing: UserInput.Processing, additionalContext: [String : any Sendable]?, tools: [ToolSpec]?, toolDispatch: (@Sendable (ToolCall) async throws -> String)?)](./chatsession/init%28_,instructions,speculativedecoding,generateparameters,components,processing,additionalcontext,tools,tooldispatch%29-3toqu.md)
  Initialize the `ChatSession`.
- [init(ModelContainer, instructions: String?, speculativeDecoding: SpeculativeDecodingConfig?, generateParameters: GenerateParameters, components: GenerationComponents, processing: UserInput.Processing, additionalContext: [String : any Sendable]?, tools: [ToolSpec]?, toolDispatch: (@Sendable (ToolCall) async throws -> String)?)](./chatsession/init%28_,instructions,speculativedecoding,generateparameters,components,processing,additionalcontext,tools,tooldispatch%29-943t6.md)
  Initialize the `ChatSession`.
### Instance Properties
- [var additionalContext: [String : any Sendable]?](./chatsession/additionalcontext.md)
- [var components: GenerationComponents](./chatsession/components.md)
  Optional behavioral components (e.g. a custom [`LogitProcessor`](./logitprocessor.md)) applied on each generation. The `logitProcessorFactory` is invoked fresh for every [`respond(to:role:images:videos:audios:)`](./chatsession/respond%28to,role,images,videos,audios%29.md) so stateful processors do not leak state across turns.
- [var generateParameters: GenerateParameters](./chatsession/generateparameters.md)
- [var instructions: String?](./chatsession/instructions.md)
- [var processing: UserInput.Processing](./chatsession/processing.md)
- [let speculativeDecoding: SpeculativeDecodingConfig?](./chatsession/speculativedecoding.md)
  Speculative decoding configuration, nil if disabled.
- [var toolDispatch: (@Sendable (ToolCall) async throws -> String)?](./chatsession/tooldispatch.md)
  Optional automatic dispatcher for accepted tool calls.
- [var tools: [ToolSpec]?](./chatsession/tools.md)
### Instance Methods
- [func cacheStatus() async throws -> KVCacheStatus](./chatsession/cachestatus%28%29.md)
  Unified KV / recurrent-cache status for this session.
- [func clear() async](./chatsession/clear%28%29.md)
  Clear the session history and cache, preserving system instructions.
- [func fork(history: [Chat.Message]?) async -> ChatSession](./chatsession/fork%28history%29.md)
  Create a session that starts from a copy of this session’s cache.
- [func kvCacheRuntimeReport() async throws -> KVCacheRuntimeReport?](./chatsession/kvcacheruntimereport%28%29.md)
  Return the legacy runtime-only view of the configured KV-cache strategy.
- [func observe<T>(to: String, role: Chat.Message.Role, images: consuming [UserInput.Image], videos: consuming [UserInput.Video], audios: consuming [UserInput.Audio], using: T) -> AsyncThrowingStream<T.Handler.Output, Error>](./chatsession/observe%28to,role,images,videos,audios,using%29.md)
  Stream details through a fresh composed handler for each generation pass.
- [func observe<T>(to: consuming [Chat.Message], using: T) -> AsyncThrowingStream<T.Handler.Output, Error>](./chatsession/observe%28to,using%29.md)
  Stream transformed details after appending structured messages.
- [func respond(to: consuming [Chat.Message]) async throws -> String](./chatsession/respond%28to%29.md)
  Produces a response after appending a batch of structured chat messages.
- [func respond(to: String, role: Chat.Message.Role, image: consuming UserInput.Image?, video: consuming UserInput.Video?, audio: consuming UserInput.Audio?) async throws -> String](./chatsession/respond%28to,role,image,video,audio%29.md)
  Produces a response to a prompt.
- [func respond(to: String, role: Chat.Message.Role, images: consuming [UserInput.Image], videos: consuming [UserInput.Video], audios: consuming [UserInput.Audio]) async throws -> String](./chatsession/respond%28to,role,images,videos,audios%29.md)
  Produces a response to a prompt.
- [func saveCache(to: URL) async throws](./chatsession/savecache%28to%29.md)
  Saves the current KV cache to disk.
- [func streamDetails(to: consuming [Chat.Message]) -> AsyncThrowingStream<Generation, Error>](./chatsession/streamdetails%28to%29.md)
  Produces a streaming response after appending a batch of structured chat messages as `Generation`.
- [func streamDetails(to: String, role: Chat.Message.Role, images: consuming [UserInput.Image], videos: consuming [UserInput.Video], audios: consuming [UserInput.Audio]) -> AsyncThrowingStream<Generation, Error>](./chatsession/streamdetails%28to,role,images,videos,audios%29.md)
  Produces a streaming response to a prompt as `Generation`.
- [func streamResponse(to: consuming [Chat.Message]) -> AsyncThrowingStream<String, Error>](./chatsession/streamresponse%28to%29.md)
  Produces a streaming response after appending a batch of structured chat messages.
- [func streamResponse(to: String, image: consuming UserInput.Image?, video: consuming UserInput.Video?, audio: consuming UserInput.Audio?) -> AsyncThrowingStream<String, Error>](./chatsession/streamresponse%28to,image,video,audio%29.md)
  Produces a streaming response to a prompt.
- [func streamResponse(to: String, role: Chat.Message.Role, images: consuming [UserInput.Image], videos: consuming [UserInput.Video], audios: consuming [UserInput.Audio]) -> AsyncThrowingStream<String, Error>](./chatsession/streamresponse%28to,role,images,videos,audios%29.md)
  Produces a streaming response to a prompt as Strings.
- [func synchronize() async](./chatsession/synchronize%28%29.md)
  Wait for exclusive access to the KVCache.
### Enumerations
- [ChatSession.ObservationError](./chatsession/observationerror.md)
  Errors from a generation observation request.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/chatsession)*