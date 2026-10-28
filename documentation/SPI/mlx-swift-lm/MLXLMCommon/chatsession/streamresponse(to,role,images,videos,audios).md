---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/chatsession/streamresponse(to:role:images:videos:audios:)"
framework: "mlx-swift-lm/MLXLMCommon"
---

# streamResponse(to:role:images:videos:audios:)

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: method  
**Role**: Instance Method

Produces a streaming response to a prompt as Strings.

## Declaration

```swift
func streamResponse(to prompt: String, role: Chat.Message.Role = .user, images: consuming [UserInput.Image] = [], videos: consuming [UserInput.Video] = [], audios: consuming [UserInput.Audio] = []) -> AsyncThrowingStream<String, Error>
```

## Return Value

A stream of string chunks from the model

## Discussion

> **Throws**: [`RejectedToolCallError`](../rejectedtoolcallerror.md) if the model emits a rejected tool call, or an error produced during generation.

## Parameters

- `prompt`: The user prompt
- `role`: The message role (defaults to `.user`)
- `images`: List of images (for use with VLMs)
- `videos`: List of videos (for use with VLMs)
- `audios`: List of audios (for use with VLMs)


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/chatsession/streamresponse(to:role:images:videos:audios:))*