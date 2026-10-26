---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/chatsession/tooldispatch"
framework: "mlx-swift-lm/MLXLMCommon"
---

# toolDispatch

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: property  
**Role**: Instance Property

Optional automatic dispatcher for accepted tool calls.

## Declaration

```swift
var toolDispatch: (@Sendable (ToolCall) async throws -> String)?
```

#### Discussion

Automatic dispatch is fail-closed: only calls naming a function declared in [`tools`](./tools.md) can reach this callback. If `tools` is `nil` or empty, every tool-call-shaped model output is rejected without invoking the callback.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/chatsession/tooldispatch)*