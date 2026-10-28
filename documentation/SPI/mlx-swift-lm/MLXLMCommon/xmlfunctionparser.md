---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/xmlfunctionparser"
framework: "mlx-swift-lm/MLXLMCommon"
---

# XMLFunctionParser

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: struct  
**Role**: Structure

Parser for XML function format: <function=name><parameter=key>value Reference: https://github.com/ml-explore/mlx-lm/blob/main/mlx_lm/tool_parsers/qwen3_coder.py

## Declaration

```swift
struct XMLFunctionParser
```

## Overview

Structure is validated with the shared `QwenXMLPayloadScanner`, the same grammar used by [`Qwen35ToolCallParser`](./qwen35toolcallparser.md) and by cross-dialect recovery. A payload becomes a call only when it is canonical in full:

- the function close is the *structural* close rather than the first textual `</function>`, so a parameter value may contain that literal verbatim;
- every `<parameter=` must close with `</parameter>`;
- nothing but whitespace may follow the payload inside its frame.

A malformed payload yields `nil` instead of a partially populated call. This matters most at end of stream, where a truncated frame must be rejected rather than executed with silently missing arguments — structural validity must never depend on whether the caller’s schema declares `required`.

## Topics

### Initializers
- [init(startTag: String, endTag: String)](./xmlfunctionparser/init%28starttag,endtag%29.md)
### Instance Properties
- [let endTag: String?](./xmlfunctionparser/endtag.md)
- [let startTag: String?](./xmlfunctionparser/starttag.md)
### Instance Methods
- [func parse(content: String, tools: [[String : any Sendable]]?) -> ToolCall?](./xmlfunctionparser/parse%28content,tools%29.md)
### Default Implementations
- [ToolCallParser Implementations](./xmlfunctionparser/toolcallparser-implementations.md)

## Relationships

### Conforms To
- Swift.Sendable
- Swift.SendableMetatype
- [ToolCallParser](./toolcallparser.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/xmlfunctionparser)*