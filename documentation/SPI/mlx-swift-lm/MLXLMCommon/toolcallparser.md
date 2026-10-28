---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/toolcallparser"
framework: "mlx-swift-lm/MLXLMCommon"
---

# ToolCallParser

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: protocol  
**Role**: Protocol

Protocol for parsing tool call content from model output.

## Declaration

```swift
protocol ToolCallParser : Sendable
```

## Mentions

- [Developing mlx-swift-lm](./developing.md)

## Overview

Different models use different formats for tool calls. This protocol provides a common interface for parsing tool calls from model output text.

Reference: https://github.com/ml-explore/mlx-lm/tree/main/mlx_lm/tool_parsers

## Topics

### Instance Properties
- [var endTag: String?](./toolcallparser/endtag.md)
  The end tag that indicates a tool call has ended. Returns `nil` for inline formats that don’t use wrapper tags.
- [var startTag: String?](./toolcallparser/starttag.md)
  The start tag that indicates a tool call is beginning. Returns `nil` for inline formats that don’t use wrapper tags.
- [var supportsBareJSON: Bool](./toolcallparser/supportsbarejson.md)
  Whether an unframed JSON object is native call syntax for this parser.
- [var supportsMarkerlessNamedJSON: Bool](./toolcallparser/supportsmarkerlessnamedjson.md)
  Whether a declared tool name that begins a line, followed by a JSON arguments object, is native call syntax for this parser.
### Instance Methods
- [func parse(content: String, tools: [[String : any Sendable]]?) -> ToolCall?](./toolcallparser/parse%28content,tools%29.md)
  Parse the content into a `ToolCall`.
- [func parseEOS(String, tools: [[String : any Sendable]]?) -> [ToolCall]](./toolcallparser/parseeos%28_,tools%29.md)
  Parse remaining buffered content at end-of-sequence.

## Relationships

### Inherits From
- Swift.Sendable
- Swift.SendableMetatype
### Conforming Types
- [ATEMToolCallParser](./atemtoolcallparser.md)
- [GLM4ToolCallParser](./glm4toolcallparser.md)
- [GemmaFunctionParser](./gemmafunctionparser.md)
- [JSONToolCallParser](./jsontoolcallparser.md)
- [KimiK2ToolCallParser](./kimik2toolcallparser.md)
- [Llama3ToolCallParser](./llama3toolcallparser.md)
- [MiniMaxM2ToolCallParser](./minimaxm2toolcallparser.md)
- [MistralToolCallParser](./mistraltoolcallparser.md)
- [PythonicToolCallParser](./pythonictoolcallparser.md)
- [Qwen35ToolCallParser](./qwen35toolcallparser.md)
- [XMLFunctionParser](./xmlfunctionparser.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/toolcallparser)*