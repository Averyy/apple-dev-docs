---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/llama3toolcallparser"
framework: "mlx-swift-lm/MLXLMCommon"
---

# Llama3ToolCallParser

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: struct  
**Role**: Structure

Parser for Llama 3 tool calls. Llama 3 often outputs inline JSON without standard start/end tags, or preceded by `<|python_tag|>`. It may also output native python function calls like `get_weather(location="San Francisco")`.

## Declaration

```swift
struct Llama3ToolCallParser
```

## Topics

### Initializers
- [init()](./llama3toolcallparser/init%28%29.md)
### Instance Properties
- [let endTag: String?](./llama3toolcallparser/endtag.md)
- [let startTag: String?](./llama3toolcallparser/starttag.md)
- [let supportsBareJSON: Bool](./llama3toolcallparser/supportsbarejson.md)
### Instance Methods
- [func parse(content: String, tools: [[String : any Sendable]]?) -> ToolCall?](./llama3toolcallparser/parse%28content,tools%29.md)
- [func parseEOS(String, tools: [[String : any Sendable]]?) -> [ToolCall]](./llama3toolcallparser/parseeos%28_,tools%29.md)
### Default Implementations
- [ToolCallParser Implementations](./llama3toolcallparser/toolcallparser-implementations.md)

## Relationships

### Conforms To
- Swift.Sendable
- Swift.SendableMetatype
- [ToolCallParser](./toolcallparser.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/llama3toolcallparser)*