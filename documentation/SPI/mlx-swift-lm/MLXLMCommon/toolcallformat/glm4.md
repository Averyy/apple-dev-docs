---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/toolcallformat/glm4"
framework: "mlx-swift-lm/MLXLMCommon"
---

# ToolCallFormat.glm4

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: case  
**Role**: Case

GLM4 format with arg_key/arg_value tags, plus GLM-4-0414’s markerless function-name-then-JSON dialect. Examples: `<tool_call>func<arg_key>k</arg_key><arg_value>v</arg_value></tool_call>` and `func\n{"k": "v"}` (detected only for a declared tool).

## Declaration

```swift
case glm4
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/toolcallformat/glm4)*