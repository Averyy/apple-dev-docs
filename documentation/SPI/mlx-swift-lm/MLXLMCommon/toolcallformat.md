---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/toolcallformat"
framework: "mlx-swift-lm/MLXLMCommon"
---

# ToolCallFormat

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: enum  
**Role**: Enumeration

Supported tool call formats for different language models.

## Declaration

```swift
enum ToolCallFormat
```

#### Overview

This enum defines the various tool call formats used by different LLM families. Each format has its own syntax for encoding function names and arguments.

The raw string values can be used for JSON serialization or CLI parameters.

Reference: https://github.com/ml-explore/mlx-lm/tree/main/mlx_lm/tool_parsers

## Topics

### Enumeration Cases
- [ToolCallFormat.atem](./toolcallformat/atem.md)
  Muse Glimmer’s Onyx ATEM invoke/parameter format. Example: `<atem:function_calls><atem:invoke name="f">...</atem:invoke></atem:function_calls>`
- [ToolCallFormat.gemma](./toolcallformat/gemma.md)
  Gemma function call format. Example: `<start_function_call>call:name{key:value,k:<escape>str<escape>}<end_function_call>`
- [ToolCallFormat.gemma4](./toolcallformat/gemma4.md)
  Gemma4 function call format. Example: `<|tool_call>call:name{key:<|"|>value<|"|>}<tool_call|>`
- [ToolCallFormat.glm4](./toolcallformat/glm4.md)
  GLM4 format with arg_key/arg_value tags, plus GLM-4-0414’s markerless function-name-then-JSON dialect. Examples: `<tool_call>func<arg_key>k</arg_key><arg_value>v</arg_value></tool_call>` and `func\n{"k": "v"}` (detected only for a declared tool).
- [ToolCallFormat.gptOSS](./toolcallformat/gptoss.md)
  GPT-OSS full Harmony response protocol.
- [ToolCallFormat.json](./toolcallformat/json.md)
  Default JSON format used by Llama, Qwen, and most models. Example: `<tool_call>{"name": "func", "arguments": {...}}</tool_call>`
- [ToolCallFormat.kimiK2](./toolcallformat/kimik2.md)
  Kimi K2 format with functions prefix. Example: `functions.name:0<|tool_call_argument_begin|>{"key": "value"}`
- [ToolCallFormat.lfm2](./toolcallformat/lfm2.md)
  LFM2/LFM2.5 Pythonic format with model-specific tags. Example: `<|tool_call_start|>[func(arg='value')]<|tool_call_end|>`
- [ToolCallFormat.llama3](./toolcallformat/llama3.md)
  Llama 3 inline JSON format. Example: `<|python_tag|>{ "name": "func", "parameters": {...} }`
- [ToolCallFormat.minimaxM2](./toolcallformat/minimaxm2.md)
  MiniMax M2 format with invoke/parameter tags. Example: `<invoke name="f"><parameter name="k">v</parameter></invoke>`
- [ToolCallFormat.mistral](./toolcallformat/mistral.md)
  Mistral V11+ format with [TOOL_CALLS] and [ARGS] delimiters. Example: `[TOOL_CALLS]get_weather [ARGS]{"location": "Tokyo"}`
- [ToolCallFormat.qwen35](./toolcallformat/qwen35.md)
  Qwen 3.5’s XML function format with a framed Hermes-JSON compatibility dialect.
- [ToolCallFormat.xmlFunction](./toolcallformat/xmlfunction.md)
  XML function format used by Nemotron, Qwen3 Coder, Qwen3 Next, and similar models. Example: `<tool_call><function=name><parameter=key>value</parameter></function></tool_call>`
### Initializers
- [init?(rawValue: String)](./toolcallformat/init%28rawvalue%29.md)
- [init?(toolParserType: String)](./toolcallformat/init%28toolparsertype%29.md)
  The format named by a `tool_parser_type` entry, using the parser names mlx-lm publishes so a checkpoint carrying one is honored as written.
### Instance Methods
- [func createParser() -> any ToolCallParser](./toolcallformat/createparser%28%29.md)
  Create the appropriate parser for this format.
### Type Methods
- [static func inferred(fromChatTemplate: String) -> ToolCallFormat?](./toolcallformat/inferred%28fromchattemplate%29.md)
  The dialect a chat template renders, or `nil` when it renders none that is recognized.
### Default Implementations
- [Encodable Implementations](./toolcallformat/encodable-implementations.md)
- [Equatable Implementations](./toolcallformat/equatable-implementations.md)
- [RawRepresentable Implementations](./toolcallformat/rawrepresentable-implementations.md)

## Relationships

### Conforms To
- Swift.CaseIterable
- Swift.Decodable
- Swift.Encodable
- Swift.Equatable
- Swift.Hashable
- Swift.RawRepresentable
- Swift.Sendable
- Swift.SendableMetatype


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/toolcallformat)*