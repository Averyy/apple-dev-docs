---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/kimik2toolcallparser"
framework: "mlx-swift-lm/MLXLMCommon"
---

# KimiK2ToolCallParser

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: struct  
**Role**: Structure

Parser for Kimi K2 format: functions.name:0<|tool_call_argument_begin|>{JSON} Reference: https://github.com/ml-explore/mlx-lm/blob/main/mlx_lm/tool_parsers/kimi_k2.py

## Declaration

```swift
struct KimiK2ToolCallParser
```

## Topics

### Initializers
- [init()](./kimik2toolcallparser/init%28%29.md)
### Instance Properties
- [let endTag: String?](./kimik2toolcallparser/endtag.md)
- [let startTag: String?](./kimik2toolcallparser/starttag.md)
### Instance Methods
- [func parse(content: String, tools: [[String : any Sendable]]?) -> ToolCall?](./kimik2toolcallparser/parse%28content,tools%29.md)
### Default Implementations
- [ToolCallParser Implementations](./kimik2toolcallparser/toolcallparser-implementations.md)

## Relationships

### Conforms To
- Swift.Sendable
- Swift.SendableMetatype
- [ToolCallParser](./toolcallparser.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/kimik2toolcallparser)*