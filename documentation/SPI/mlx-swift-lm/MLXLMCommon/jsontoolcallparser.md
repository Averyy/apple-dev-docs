---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/jsontoolcallparser"
framework: "mlx-swift-lm/MLXLMCommon"
---

# JSONToolCallParser

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: struct  
**Role**: Structure

Parser for JSON format: {“name”: “…”, “arguments”: {…}} Reference: https://github.com/ml-explore/mlx-lm/blob/main/mlx_lm/tool_parsers/default.py

## Declaration

```swift
struct JSONToolCallParser
```

## Topics

### Initializers
- [init(startTag: String, endTag: String, supportsBareJSON: Bool)](./jsontoolcallparser/init%28starttag,endtag,supportsbarejson%29.md)
### Instance Properties
- [let endTag: String?](./jsontoolcallparser/endtag.md)
- [let startTag: String?](./jsontoolcallparser/starttag.md)
- [let supportsBareJSON: Bool](./jsontoolcallparser/supportsbarejson.md)
### Instance Methods
- [func parse(content: String, tools: [[String : any Sendable]]?) -> ToolCall?](./jsontoolcallparser/parse%28content,tools%29.md)
### Default Implementations
- [ToolCallParser Implementations](./jsontoolcallparser/toolcallparser-implementations.md)

## Relationships

### Conforms To
- Swift.Sendable
- Swift.SendableMetatype
- [ToolCallParser](./toolcallparser.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/jsontoolcallparser)*