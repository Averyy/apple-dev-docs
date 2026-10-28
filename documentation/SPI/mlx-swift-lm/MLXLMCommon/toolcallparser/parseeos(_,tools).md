---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/toolcallparser/parseeos(_:tools:)"
framework: "mlx-swift-lm/MLXLMCommon"
---

# parseEOS(_:tools:)

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Parse remaining buffered content at end-of-sequence.

## Declaration

```swift
func parseEOS(_ toolCallBuffer: String, tools: [[String : any Sendable]]?) -> [ToolCall]
```

## Discussion

Called when generation ends to extract any tool calls still in the buffer. The default implementation splits on `startTag` (if present) and parses each segment individually.

## Default Implementations

### ToolCallParser Implementations
- [func parseEOS(String, tools: [[String : any Sendable]]?) -> [ToolCall]](./parseeos%28_,tools%29-2jck5.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/toolcallparser/parseeos(_:tools:))*