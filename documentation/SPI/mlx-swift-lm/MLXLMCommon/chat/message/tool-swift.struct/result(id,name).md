---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/chat/message/tool-swift.struct/result(id:name:)"
framework: "mlx-swift-lm/MLXLMCommon"
---

# result(id:name:)

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: method  
**Role**: Type Method

Identifies the assistant tool call answered by a tool message.

## Declaration

```swift
static func result(id: String, name: String? = nil) -> Chat.Message.Tool
```

## Discussion

Some chat templates correlate results by `tool_call_id`, while others (including Onyx) render the function `name` directly.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/chat/message/tool-swift.struct/result(id:name:))*