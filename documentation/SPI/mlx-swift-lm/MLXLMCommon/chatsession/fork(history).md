---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/chatsession/fork(history:)"
framework: "mlx-swift-lm/MLXLMCommon"
---

# fork(history:)

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: method  
**Role**: Instance Method

Create a session that starts from a copy of this session’s cache.

## Declaration

```swift
nonisolated(nonsending)
func fork(history: [Chat.Message]? = nil) async -> ChatSession
```

## Return Value

A session that owns a copy of this session’s cache

## Discussion

Each session continues without affecting the other. Copying is cheap: they share the cache’s arrays until one of them writes. Once either loads the draft model for speculative decoding, both use it.

Without `history`, the new session continues this conversation, which branches it. With `history`, it holds that conversation instead. Its first response keeps only the part of the cache that its prompt starts with, and prefills the rest of the prompt. Conversations that share instructions and tools therefore prefill them once:

```swift
let session = ChatSession(model, instructions: instructions, tools: tools)
_ = try await session.respond(to: "What time is it?")

let next = await session.fork(history: [])
_ = try await next.respond(to: "What is the weather like?")
```

A transcript with images, videos or audios, in either session, starts from an empty cache: their placeholder tokens are the same for different media, so they cannot prove the cached prefix matches.

The new session copies this session’s configuration, which can be changed before it responds. A response in progress finishes before the cache is copied.

## Parameters

- `history`: The conversation the new session holds, or `nil` to continue this one


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/chatsession/fork(history:))*