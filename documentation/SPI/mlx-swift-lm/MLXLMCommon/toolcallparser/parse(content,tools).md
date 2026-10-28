---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/toolcallparser/parse(content:tools:)"
framework: "mlx-swift-lm/MLXLMCommon"
---

# parse(content:tools:)

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Parse the content into a `ToolCall`.

## Declaration

```swift
func parse(content: String, tools: [[String : any Sendable]]?) -> ToolCall?
```

## Return Value

A `ToolCall` if parsing succeeds, `nil` otherwise

## Parameters

- `content`: The text content to parse (may include tags)
- `tools`: Optional tool schemas for type-aware parsing


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/toolcallparser/parse(content:tools:))*