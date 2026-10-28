---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/chatsession/observe(to:role:images:videos:audios:using:)"
framework: "mlx-swift-lm/MLXLMCommon"
---

# observe(to:role:images:videos:audios:using:)

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: method  
**Role**: Instance Method

Stream details through a fresh composed handler for each generation pass.

## Declaration

```swift
func observe<T>(to prompt: String, role: Chat.Message.Role = .user, images: consuming [UserInput.Image] = [], videos: consuming [UserInput.Video] = [], audios: consuming [UserInput.Audio] = [], using transformer: T) -> AsyncThrowingStream<T.Handler.Output, Error> where T : GenerationTransformer
```

## Discussion

The transformer configures a copy of the session’s parameters for this request, including automatic tool restarts. Its output must forward all base generation events so the session can maintain its transcript and cache. Log-probability reporting with active speculative decoding throws [`ChatSession.ObservationError.unsupportedSpeculativeDecoding`](./observationerror/unsupportedspeculativedecoding.md).


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/chatsession/observe(to:role:images:videos:audios:using:))*