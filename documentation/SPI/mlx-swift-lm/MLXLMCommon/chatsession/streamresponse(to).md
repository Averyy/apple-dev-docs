---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/chatsession/streamresponse(to:)"
framework: "mlx-swift-lm/MLXLMCommon"
---

# streamResponse(to:)

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: method  
**Role**: Instance Method

Produces a streaming response after appending a batch of structured chat messages.

## Declaration

```swift
func streamResponse(to messages: consuming [Chat.Message]) -> AsyncThrowingStream<String, Error>
```

## Return Value

A stream of string chunks from the model

## Discussion

Use this to continue an existing session with non-user roles, such as one or more tool results, while preserving the session’s KV cache.

> **Throws**: [`RejectedToolCallError`](../rejectedtoolcallerror.md) if the model emits a rejected tool call, or an error produced during generation.

## Parameters

- `messages`: Chat messages to append before generation


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/chatsession/streamresponse(to:))*