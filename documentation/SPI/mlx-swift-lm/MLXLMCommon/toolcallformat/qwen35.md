---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/toolcallformat/qwen35"
framework: "mlx-swift-lm/MLXLMCommon"
---

# ToolCallFormat.qwen35

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: case  
**Role**: Case

Qwen 3.5’s XML function format with a framed Hermes-JSON compatibility dialect.

## Declaration

```swift
case qwen35
```

## Discussion

Qwen 3.5 is prompted to emit `xmlFunction`, but can sporadically emit the Qwen/Hermes JSON dialect used by earlier Qwen models instead. Both dialects use the same `<tool_call>` frame; this format accepts either payload without enabling bare JSON recovery.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/toolcallformat/qwen35)*