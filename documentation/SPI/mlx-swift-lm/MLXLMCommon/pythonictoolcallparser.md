---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/pythonictoolcallparser"
framework: "mlx-swift-lm/MLXLMCommon"
---

# PythonicToolCallParser

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: struct  
**Role**: Structure

Parser for Pythonic tool call format: [function_name(arg1=‘value1’, arg2=‘value2’)] Used by LFM2.5 and similar models that output tool calls in Python function call syntax. Reference: LiquidAI LFM2.5 chat template format

## Declaration

```swift
struct PythonicToolCallParser
```

## Topics

### Initializers
- [init(startTag: String?, endTag: String?)](./pythonictoolcallparser/init%28starttag,endtag%29.md)
### Instance Properties
- [let endTag: String?](./pythonictoolcallparser/endtag.md)
- [let startTag: String?](./pythonictoolcallparser/starttag.md)
### Instance Methods
- [func parse(content: String, tools: [[String : any Sendable]]?) -> ToolCall?](./pythonictoolcallparser/parse%28content,tools%29.md)
- [func parseEOS(String, tools: [[String : any Sendable]]?) -> [ToolCall]](./pythonictoolcallparser/parseeos%28_,tools%29.md)
### Default Implementations
- [ToolCallParser Implementations](./pythonictoolcallparser/toolcallparser-implementations.md)

## Relationships

### Conforms To
- Swift.Sendable
- Swift.SendableMetatype
- [ToolCallParser](./toolcallparser.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/pythonictoolcallparser)*