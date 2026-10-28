---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/chatsession/streamdetails(to:role:images:videos:audios:)"
framework: "mlx-swift-lm/MLXLMCommon"
---

# streamDetails(to:role:images:videos:audios:)

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: method  
**Role**: Instance Method

Produces a streaming response to a prompt as `Generation`.

## Declaration

```swift
func streamDetails(to prompt: String, role: Chat.Message.Role = .user, images: consuming [UserInput.Image] = [], videos: consuming [UserInput.Video] = [], audios: consuming [UserInput.Audio] = []) -> AsyncThrowingStream<Generation, Error>
```

## Return Value

A stream of `Generation` from the model

## Discussion

Rejected calls are emitted as [`Generation.rejectedToolCall(_:)`](../generation/rejectedtoolcall%28_%29.md). When automatic tool dispatch is configured, the stream instead throws [`RejectedToolCallError`](../rejectedtoolcallerror.md) before dispatching any call from that turn.

## Parameters

- `prompt`: The user prompt
- `role`: The message role (defaults to `.user`)
- `images`: List of images (for use with VLMs)
- `videos`: List of videos (for use with VLMs)
- `audios`: List of audios (for use with VLMs)


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/chatsession/streamdetails(to:role:images:videos:audios:))*