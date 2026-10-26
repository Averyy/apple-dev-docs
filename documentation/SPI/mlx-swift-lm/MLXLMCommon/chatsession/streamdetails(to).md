---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/chatsession/streamdetails(to:)"
framework: "mlx-swift-lm/MLXLMCommon"
---

# streamDetails(to:)

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: method  
**Role**: Instance Method

Produces a streaming response after appending a batch of structured chat messages as `Generation`.

## Declaration

```swift
func streamDetails(to messages: consuming [Chat.Message]) -> AsyncThrowingStream<Generation, Error>
```

#### Return Value

A stream of `Generation` from the model

#### Discussion

Use this to continue an existing session with non-user roles, such as one or more tool results, while preserving the session’s KV cache.

Rejected calls are emitted as [`Generation.rejectedToolCall(_:)`](../generation/rejectedtoolcall%28_%29.md). When automatic tool dispatch is configured, the stream instead throws [`RejectedToolCallError`](../rejectedtoolcallerror.md) before dispatching any call from that turn.

## Parameters

- `messages`: Chat messages to append before generation


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/chatsession/streamdetails(to:))*