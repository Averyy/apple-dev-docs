---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/toolcallprocessor/init(format:tools:toolcallpolicy:)"
framework: "mlx-swift-lm/MLXLMCommon"
---

# init(format:tools:toolCallPolicy:)

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: init  
**Role**: Initializer

Initialize with a specific tool call format.

## Declaration

```swift
init(format: ToolCallFormat = .json, tools: [[String : any Sendable]]? = nil, toolCallPolicy: ToolCallPolicy = .init())
```

## Parameters

- `format`: The tool call format to use (defaults to `.json` for standard JSON format)
- `tools`: Optional tool schemas for type-aware parsing and authorization. `nil` accepts any parsed function name; a supplied array, including an empty one, authorizes only the names it declares. A nonempty declaration also enables bounded cross-dialect recovery; only an exactly declared function name can be promoted by recovery.
- `toolCallPolicy`: Recovery and validation rules. Defaults to conservative recovery and permissive schema validation; tool-name authorization always applies.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/toolcallprocessor/init(format:tools:toolcallpolicy:))*