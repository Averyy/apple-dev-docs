---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/glm4toolcallparser"
framework: "mlx-swift-lm/MLXLMCommon"
---

# GLM4ToolCallParser

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: struct  
**Role**: Structure

Parser for the GLM4 tool-call dialects.

## Declaration

```swift
struct GLM4ToolCallParser
```

#### Overview

GLM-4.5 and later frame a call as `<tool_call>func<arg_key>k</arg_key><arg_value>v</arg_value></tool_call>`. GLM-4-0414 writes the function name on its own line followed by a JSON arguments object, with no delimiters at all. `ToolCallProcessor` anchors that markerless dialect on the declared tools before it reaches this parser.

Reference: https://github.com/ml-explore/mlx-lm/blob/main/mlx_lm/tool_parsers/glm47.py

## Topics

### Initializers
- [init()](./glm4toolcallparser/init%28%29.md)
### Instance Properties
- [let endTag: String?](./glm4toolcallparser/endtag.md)
- [let startTag: String?](./glm4toolcallparser/starttag.md)
- [var supportsMarkerlessNamedJSON: Bool](./glm4toolcallparser/supportsmarkerlessnamedjson.md)
### Instance Methods
- [func parse(content: String, tools: [[String : any Sendable]]?) -> ToolCall?](./glm4toolcallparser/parse%28content,tools%29.md)
### Default Implementations
- [ToolCallParser Implementations](./glm4toolcallparser/toolcallparser-implementations.md)

## Relationships

### Conforms To
- Swift.Sendable
- Swift.SendableMetatype
- [ToolCallParser](./toolcallparser.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/glm4toolcallparser)*