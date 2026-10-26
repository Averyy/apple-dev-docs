---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/chatsession/streamresponse(to:image:video:audio:)"
framework: "mlx-swift-lm/MLXLMCommon"
---

# streamResponse(to:image:video:audio:)

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: method  
**Role**: Instance Method

Produces a streaming response to a prompt.

## Declaration

```swift
func streamResponse(to prompt: String, image: consuming UserInput.Image? = nil, video: consuming UserInput.Video? = nil, audio: consuming UserInput.Audio? = nil) -> AsyncThrowingStream<String, Error>
```

#### Return Value

A stream of string chunks from the model

## Parameters

- `prompt`: The user prompt
- `image`: Optional image (for use with VLMs)
- `video`: Optional video (for use with VLMs)
- `audio`: Optional audio (for use with VLMs)


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/chatsession/streamresponse(to:image:video:audio:))*