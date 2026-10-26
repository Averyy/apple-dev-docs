---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/chatsession/respond(to:)"
framework: "mlx-swift-lm/MLXLMCommon"
---

# respond(to:)

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: method  
**Role**: Instance Method

Produces a response after appending a batch of structured chat messages.

## Declaration

```swift
func respond(to messages: consuming [Chat.Message]) async throws -> String
```

#### Return Value

The model’s response

#### Discussion

Use this to continue an existing session with non-user roles, such as one or more tool results, while preserving the session’s KV cache.

> ❗ **Important**: Initializing a new session from history must prefill that history once. Reuse the same session with this method for subsequent tool or agent turns to avoid repeatedly pre-filling the accumulated transcript.

## Parameters

- `messages`: Chat messages to append before generation


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/chatsession/respond(to:))*