---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/reasoningconfig/implicitenddelimiters"
framework: "mlx-swift-lm/MLXLMCommon"
---

# implicitEndDelimiters

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: property  
**Role**: Instance Property

Markers that implicitly leave reasoning without emitting [`endDelimiter`](./enddelimiter.md).

## Declaration

```swift
var implicitEndDelimiters: [String]
```

## Discussion

These markers remain part of the generated stream. They are boundaries, not replacements for the canonical closing delimiter. For example, Qwen3.5 may begin `<tool_call>` directly from its thinking block.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/reasoningconfig/implicitenddelimiters)*