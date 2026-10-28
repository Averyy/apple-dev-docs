---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/mistraltoolcallparser"
framework: "mlx-swift-lm/MLXLMCommon"
---

# MistralToolCallParser

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: struct  
**Role**: Structure

Parser for Mistral V13 tool call format: `[TOOL_CALLS]name[ARGS]{"json_args"}`

## Declaration

```swift
struct MistralToolCallParser
```

## Overview

This format is used by Mistral3/Ministral-3 2512 models and Devstral 2. The special tokens `[TOOL_CALLS]` (token ID 9) and `[ARGS]` (ID 32) are used as delimiters. Multiple tool calls use repeated `[TOOL_CALLS]` tokens.

Also handles the older V11 format which includes an optional `[CALL_ID]` between the function name and `[ARGS]` (V13 does not use `[CALL_ID]`).

Examples:

- `[TOOL_CALLS]get_weather[ARGS]{"location": "Tokyo"}`
- `[TOOL_CALLS]fn1[ARGS]{...}[TOOL_CALLS]fn2[ARGS]{...}` (multiple calls)

Mistral does not use an end tag — tool calls end at EOS. Since stop tokens are intercepted at the token ID level before detokenization, tool calls are extracted via `ToolCallProcessor.processEOS()` at generation end.

## Topics

### Initializers
- [init()](./mistraltoolcallparser/init%28%29.md)
### Instance Properties
- [let endTag: String?](./mistraltoolcallparser/endtag.md)
- [let startTag: String?](./mistraltoolcallparser/starttag.md)
### Instance Methods
- [func parse(content: String, tools: [[String : any Sendable]]?) -> ToolCall?](./mistraltoolcallparser/parse%28content,tools%29.md)
### Default Implementations
- [ToolCallParser Implementations](./mistraltoolcallparser/toolcallparser-implementations.md)

## Relationships

### Conforms To
- Swift.Sendable
- Swift.SendableMetatype
- [ToolCallParser](./toolcallparser.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/mistraltoolcallparser)*