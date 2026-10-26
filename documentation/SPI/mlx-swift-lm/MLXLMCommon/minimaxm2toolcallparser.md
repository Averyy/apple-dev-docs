---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/minimaxm2toolcallparser"
framework: "mlx-swift-lm/MLXLMCommon"
---

# MiniMaxM2ToolCallParser

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: struct  
**Role**: Structure

Parser for MiniMax M2 format: v Reference: https://github.com/ml-explore/mlx-lm/blob/main/mlx_lm/tool_parsers/minimax_m2.py

## Declaration

```swift
struct MiniMaxM2ToolCallParser
```

## Topics

### Initializers
- [init()](./minimaxm2toolcallparser/init%28%29.md)
### Instance Properties
- [let endTag: String?](./minimaxm2toolcallparser/endtag.md)
- [let startTag: String?](./minimaxm2toolcallparser/starttag.md)
### Instance Methods
- [func parse(content: String, tools: [[String : any Sendable]]?) -> ToolCall?](./minimaxm2toolcallparser/parse%28content,tools%29.md)
### Default Implementations
- [ToolCallParser Implementations](./minimaxm2toolcallparser/toolcallparser-implementations.md)

## Relationships

### Conforms To
- Swift.Sendable
- Swift.SendableMetatype
- [ToolCallParser](./toolcallparser.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/minimaxm2toolcallparser)*