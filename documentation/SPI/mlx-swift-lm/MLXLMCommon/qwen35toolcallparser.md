---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/qwen35toolcallparser"
framework: "mlx-swift-lm/MLXLMCommon"
---

# Qwen35ToolCallParser

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: struct  
**Role**: Structure

Parser for Qwen 3.5’s two observed tool-call payload dialects.

## Declaration

```swift
struct Qwen35ToolCallParser
```

## Overview

Qwen 3.5’s chat template requests the XML function dialect, but the model can occasionally emit the Qwen/Hermes JSON dialect used by earlier Qwen releases. Both payloads are framed by `<tool_call>` tags. Dialect selection is structural and deterministic: XML must begin with `<function=`, while JSON must begin with `{`. Malformed or ambiguous payloads are never repaired into executable calls.

## Topics

### Initializers
- [init(startTag: String, endTag: String)](./qwen35toolcallparser/init%28starttag,endtag%29.md)
### Instance Properties
- [let endTag: String?](./qwen35toolcallparser/endtag.md)
- [let startTag: String?](./qwen35toolcallparser/starttag.md)
### Instance Methods
- [func parse(content: String, tools: [[String : any Sendable]]?) -> ToolCall?](./qwen35toolcallparser/parse%28content,tools%29.md)
### Default Implementations
- [ToolCallParser Implementations](./qwen35toolcallparser/toolcallparser-implementations.md)

## Relationships

### Conforms To
- Swift.Sendable
- Swift.SendableMetatype
- [ToolCallParser](./toolcallparser.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/qwen35toolcallparser)*