---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/chatsession/respond(to:role:images:videos:audios:)"
framework: "mlx-swift-lm/MLXLMCommon"
---

# respond(to:role:images:videos:audios:)

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: method  
**Role**: Instance Method

Produces a response to a prompt.

## Declaration

```swift
func respond(to prompt: String, role: Chat.Message.Role = .user, images: consuming [UserInput.Image], videos: consuming [UserInput.Video], audios: consuming [UserInput.Audio]) async throws -> String
```

## Return Value

The model’s response

## Parameters

- `prompt`: The user prompt
- `role`: The message role (defaults to `.user`)
- `images`: List of images (for use with VLMs)
- `videos`: List of videos (for use with VLMs)
- `audios`: List of audios (for use with VLMs)


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/chatsession/respond(to:role:images:videos:audios:))*