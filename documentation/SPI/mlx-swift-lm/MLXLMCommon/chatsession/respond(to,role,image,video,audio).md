---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/chatsession/respond(to:role:image:video:audio:)"
framework: "mlx-swift-lm/MLXLMCommon"
---

# respond(to:role:image:video:audio:)

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: method  
**Role**: Instance Method

Produces a response to a prompt.

## Declaration

```swift
func respond(to prompt: String, role: Chat.Message.Role = .user, image: consuming UserInput.Image? = nil, video: consuming UserInput.Video? = nil, audio: consuming UserInput.Audio? = nil) async throws -> String
```

## Return Value

The model’s response

## Parameters

- `prompt`: The user prompt
- `role`: The message role (defaults to `.user`)
- `image`: Optional image (for use with VLMs)
- `video`: Optional video (for use with VLMs)
- `audio`: Optional audio (for use with VLMs)


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/chatsession/respond(to:role:image:video:audio:))*