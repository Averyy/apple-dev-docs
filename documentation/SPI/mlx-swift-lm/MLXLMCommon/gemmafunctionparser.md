---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/gemmafunctionparser"
framework: "mlx-swift-lm/MLXLMCommon"
---

# GemmaFunctionParser

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: struct  
**Role**: Structure

Parser for Gemma format: call:name{key:value,k:str} Reference: https://github.com/ml-explore/mlx-lm/blob/main/mlx_lm/tool_parsers/function_gemma.py

## Declaration

```swift
struct GemmaFunctionParser
```

## Topics

### Initializers
- [init(startTag: String, endTag: String, escapeMarker: String)](./gemmafunctionparser/init%28starttag,endtag,escapemarker%29.md)
### Instance Properties
- [let endTag: String?](./gemmafunctionparser/endtag.md)
- [let escapeMarker: String?](./gemmafunctionparser/escapemarker.md)
- [let startTag: String?](./gemmafunctionparser/starttag.md)
### Instance Methods
- [func parse(content: String, tools: [[String : any Sendable]]?) -> ToolCall?](./gemmafunctionparser/parse%28content,tools%29.md)
### Default Implementations
- [ToolCallParser Implementations](./gemmafunctionparser/toolcallparser-implementations.md)

## Relationships

### Conforms To
- Swift.Sendable
- Swift.SendableMetatype
- [ToolCallParser](./toolcallparser.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/gemmafunctionparser)*