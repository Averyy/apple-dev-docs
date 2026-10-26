---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/chatsession/observe(to:using:)"
framework: "mlx-swift-lm/MLXLMCommon"
---

# observe(to:using:)

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: method  
**Role**: Instance Method

Stream transformed details after appending structured messages.

## Declaration

```swift
func observe<T>(to messages: consuming [Chat.Message], using transformer: T) -> AsyncThrowingStream<T.Handler.Output, Error> where T : GenerationTransformer
```

#### Discussion

The transformer applies only to this request. The session retains its transcript and KV cache, including across automatic tool restarts.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/chatsession/observe(to:using:))*